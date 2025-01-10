import glob
import os
import subprocess
import shutil

import falcom_decompress

basepath = os.path.join('ISO', 'PSP_GAME', 'USRDIR')
r'ISO\PSP_GAME\USRDIR'

class cd:
    """Context manager for changing the current working directory"""
    def __init__(self, newPath):
        self.newPath = os.path.expanduser(newPath)

    def __enter__(self):
        self.savedPath = os.getcwd()
        os.chdir(self.newPath)

    def __exit__(self, etype, value, traceback):
        os.chdir(self.savedPath)

def ensure_dir(dirname):
    if not os.path.exists(dirname):
        os.makedirs(dirname)

#Text
#filename, compression offset
filelist = (
    ('fldlist0.tbb',    0x1F),
    ('fldlist1.tbb',    0x1F),
    ('fldlist2.tbb',    0x1F),
    ('fldlist3.tbb',    0x1F),
    ('foodarea.tbb',    0x1F),
    ('helplib.tbb',     0x1F),
    ('item.tbl',        -0x1),
    ('monslib.tbb',     0x1F),
    ('pc.tbb',          0x23),
    ('questlib.tbb',    0x1F))

target = r'text\orig'
ensure_dir(r'text\orig')

for filename in (x[0] for x in filelist):
    if os.path.isfile(os.path.join(target, filename)):
        pass
    else:
        shutil.copy(os.path.join(r'ISO\PSP_GAME\USRDIR\text', filename),
                    target)

with cd(r'text\orig'):
    for filename, compression_offset in filelist:
        if compression_offset < 0:
            continue
        output_filename = os.path.splitext(filename)[0] + '.tbl'
        with open(filename, 'rb') as f:
            f.seek(compression_offset)
            with open(output_filename, 'wb') as g:
                g.write(falcom_decompress.decompress_FALCOM3(f.read()))

#EBOOT
if os.path.isfile(r'EBOOT\NPJH50311.BIN'):
    pass
else:
    ensure_dir('EBOOT')
    shutil.copy(r'ISO\PSP_GAME\SYSDIR\EBOOT.BIN',
                r'EBOOT\TEMP.BIN')
    subprocess.run([r'bin\deceboot.exe',
                    r'EBOOT\TEMP.BIN',
                    r'EBOOT\NPJH50625.BIN'])
    os.remove(os.path.join('EBOOT', 'TEMP.BIN'))
    shutil.copy(r'EBOOT\NPJH50625.BIN', r'EBOOT\EBOOT.BIN')

        
#.arb (YS7_ARG files)
target = r'arg\orig'
ensure_dir(r'arg\orig')
for root, dirs, files in os.walk(r'ISO\PSP_GAME\USRDIR\map'):
    for filename in filter(lambda x: '.arb' in x, files):
        if os.path.isfile(os.path.join(target, filename)):
            pass
        else:
            shutil.copy(os.path.join(root, filename),
                        os.path.join(target, filename))

#.bin (YS7_SCP script files)
ensure_dir(r'script\orig')
for filename in os.listdir(r'ISO\PSP_GAME\USRDIR\script'):
    if 'mp_' in filename or 'noi' in filename or 'system' in filename:
        shutil.copy(os.path.join(r'ISO\PSP_GAME\USRDIR\script', filename),
                    r'script\orig')

#misc files
ensure_dir('misc')
shutil.copy(r'ISO\PSP_GAME\PARAM.SFO', r'misc\PARAM.SFO')
shutil.copy(r'ISO\PSP_GAME\PARAM.SFO', r'misc\PARAM.SFO.orig')
for filename in ('detail.txt', 'dtitle.txt', 'title.txt'):
    shutil.copy(os.path.join(basepath, 'savefile', filename),
                'misc')
