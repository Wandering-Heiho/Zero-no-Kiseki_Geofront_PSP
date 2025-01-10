import os
import packed_lib
import shutil

src_path = 'img'

#manual images
filelist = tuple(os.path.join(src_path, x) for x in filter(
    lambda x: 'h_' in x and '.itp' in x, os.listdir(src_path)))
for filename in filelist:
    shutil.copy(filename, r'ISO\PSP_GAME\USRDIR\visual\help')

#save file images
for filename in (os.path.join(src_path, x) for x in (
    'icon_new.png', 'icon0.png', 'pic1.png')):
    shutil.copy(filename, r'ISO\PSP_GAME\USRDIR\savefile')
shutil.copy(r'{}\icon0.png'.format(src_path), r'ISO\PSP_GAME\ICON0.PNG')
shutil.copy(r'{}\pic1.png'.format(src_path), r'ISO\PSP_GAME\PIC1.PNG')

#"system" images
filelist = (
    'm_field0.itp', 'm_field2.itp', 'm_field3.itp', 'm_main.itp',
    'm_mons.itp', 'm_quest.itp', 'title0.it3', 'title1.it3', 'title2.it3')
for filename in filelist:
    shutil.copy(os.path.join(src_path, filename),
                r'ISO\PSP_GAME\USRDIR\system')

packed_list = (r'ISO\PSP_GAME\USRDIR\pack\global\first.dat',
               r'ISO\PSP_GAME\USRDIR\pack\global\global.dat')

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
