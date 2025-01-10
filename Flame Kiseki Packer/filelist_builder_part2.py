from functools import partial
from itertools import chain
import os
import struct
import ISO_extract
import pdb

DATA_START = 0x400
BASEPATH = 'USRDIR'
target = 'output.iso'

print('Reading path table.')
with open(target, 'rb') as f:
    pathtbl = ISO_extract.getpathtbl(f)
print('Updating data.lst with file locations (LBA).')
datalst_size = os.path.getsize('data.lst')
with open('data.lst', 'rb+') as f:
    ext_list = []
    f.seek(4)
    for ext in iter(partial(f.read, 4), b'\x00' * 4):
        ext_list.append('.' + ext.rstrip(b'\x00').decode('ascii'))
    path_list = []
    path_count = []
    f.seek(DATA_START)
    while f.tell() < datalst_size:
        name = f.read(8).rstrip(b'\x00').decode('cp932')
        size = struct.unpack('<I', f.read(4))[0]
        LBA = f.read(3)
        ext = f.read(1)[0]
        path_count = [x - 1 for x in path_count]
        if ext == 0:
            path_list.append(name)
            path_count.append(size)
        else:
            path = 'USRDIR' + '\\'.join(chain(path_list, (name + ext_list[ext - 1],)))
            LBA = ISO_extract.get_dir_rec(path, pathtbl).LBA
            f.seek(-4, 1)
            f.write(struct.pack('<I', LBA)[:3])
            f.seek(1, 1)
        while path_count[-1] == 0:
            del path_count[-1]
            del path_list[-1]
            if len(path_count) == 0:
                break
print('Inserting modified data.lst file overtop of the template.')
with open(target, 'rb+') as f:
    ISO_extract.replace(f, r'USRDIR\data.lst', 'data.lst', pathtbl)
print('Operation finished. Time to test it!')
