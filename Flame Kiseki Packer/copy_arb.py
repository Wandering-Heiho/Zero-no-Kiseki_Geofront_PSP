import os
import packed_lib
import shutil
import struct

src_path = r'arg\output'
filelist = tuple(filter(lambda x: '.arb' in x, os.listdir(src_path)))
packed_path = r'ISO\PSP_GAME\USRDIR\pack\map'
packed_list = tuple(filter(lambda x: '.mpp' in x, os.listdir(packed_path)))
tgt_path = r'ISO\PSP_GAME\USRDIR\map'

for packed_file in packed_list:
    with open(os.path.join(packed_path, packed_file), 'rb') as f:
        packed = packed_lib.packed_file(f)
    while True:
        for file in packed.TOC:
            if file.name in filelist:
                packed.remove(file.name)
                break
        else:
            break
    if packed.updated:
        with open(os.path.join(packed_path, packed_file), 'wb') as f:
            f.write(packed.bin())

for filename in filelist:
    basename = os.path.splitext(filename)[0]
    shutil.copy(
        os.path.join(src_path, filename),
        os.path.join(tgt_path, basename, filename))
