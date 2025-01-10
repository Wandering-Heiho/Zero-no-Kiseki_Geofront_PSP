import os
import packed_lib
import shutil
import struct
from contextlib import suppress

src_path = r'text\output'
filelist = tuple(filter(lambda x: '.tbl' in x or '.tbb' in x,
                        os.listdir(src_path)))
packed_path = r'ISO\PSP_GAME\USRDIR\pack\map'
packed_list = tuple(filter(lambda x: '.mpp' in x, os.listdir(packed_path)))
packed_list = tuple(os.path.join(packed_path, x) for x in packed_list)
packed_list += r'ISO\PSP_GAME\USRDIR\pack\global\first.dat',
tgt_path = r'ISO\PSP_GAME\USRDIR\text'

for packed_file in packed_list:
    with open(packed_file, 'rb') as f:
        packed = packed_lib.packed_file(f)
    while True:
        for file in packed.TOC:
            if file.name in filelist:
                packed.remove(file.name)
                break
        else:
            break
    if packed.updated:
        with open(packed_file, 'wb') as f:
            f.write(packed.bin())

for filename in filelist:
    shutil.copy(
        os.path.join(src_path, filename),
        os.path.join(tgt_path, filename))

#questlib.tbb and m_quest.itp are in these
#that's all that's there so we're just going to delete them
with suppress(FileNotFoundError):
    os.remove(r'ISO\PSP_GAME\USRDIR\pack\script\mp_0004.2pp')
    os.remove(r'ISO\PSP_GAME\USRDIR\pack\script\mp_0004c.2pp')
    os.remove(r'ISO\PSP_GAME\USRDIR\pack\script\mp_0004d.2pp')
