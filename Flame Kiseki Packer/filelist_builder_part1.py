import binascii
import shutil
import struct
import os

DATA_START = 0x400
buildpath = os.getcwd() + '\\ISO'

def ensure_dir(dirname):
    if not os.path.exists(dirname):
        os.makedirs(dirname)
def walk_len(foldername):
    count = 0
    for dirname, dirlist, filelist in os.walk(foldername):
        count += sum(1 if len(d) < 9 else 0 for d in dirlist) + len(filelist)
    return count

print('Operation part 1: Build data.lst template file.')
ext_lst = ['']
datalst = bytearray()
for dirpath, dirlist, filelist in os.walk(buildpath):
    for filename in filelist:
        try:
            filename.encode('ascii')
        except UnicodeEncodeError:
            ensure_dir('trashed')
            shutil.copy(dirpath + '\\' + filename, 'trashed')
            os.remove(dirpath + '\\' + filename)
            print('{}: Moved to trashed folder, non-ascii characters '
                  'found.'.format(dirpath + '\\' + filename))
            continue
        if len(os.path.splitext(filename)[0]) > 8:
            ensure_dir('trashed')
            shutil.copy(dirpath + '\\' + filename, 'trashed')
            os.remove(dirpath + '\\' + filename)
            print('{}: Moved to trashed folder, filename is over 8 letters'
                  .format(dirpath + '\\' + filename))
for dirpath, dirlist, filelist in os.walk(buildpath):
    basepath = os.path.relpath(dirpath, start=buildpath)
    #data.lst directory entry
    if 'USRDIR' in basepath:
        if len(os.path.basename(basepath)) < 9:
            if basepath == r'PSP_GAME\USRDIR':
                datalst += b'\x00' * 8
            else:
                s = os.path.basename(basepath).encode('ascii')
                datalst += s + b'\x00' * (8 - len(s))
            datalst += struct.pack('<II', walk_len(dirpath), 0)
#Some illegal names in there. Uncomment if you want to see them.
#They are illegal (unsupported by data.lst format) so they are skipped.
##        else:
##            print(basepath)
    for filename in filelist:
        try:
            filename.encode('cp932')
        except Exception as err:
            print(filename)
            print(binascii.hexlify(filename))
            raise err
        #data.lst file entry
        if 'USRDIR' in basepath:
            file, ext = os.path.splitext(filename)
            file = file.encode('cp932')
            datalst += (file + b'\x00' * (8 - len(file)))[:8]
            ext = ext[1:]
            filesize = os.path.getsize(dirpath + '\\' + filename)
            datalst += struct.pack('<I', filesize)
            datalst += b'\x00' * 3                  #Blank LBA entry
            if ext in ext_lst:
                datalst.append(ext_lst.index(ext))
            else:
                datalst.append(len(ext_lst))
                ext_lst.append(ext)
datalst[0x18:0x1C] = struct.pack('<I', len(datalst) + DATA_START)
with open('data.lst', 'wb') as f:
    f.write(struct.pack('<I', DATA_START + len(datalst)))
    for ext in ext_lst[1:]:
        f.write(ext.encode('ascii') + b'\x00' * (4 - len(ext)))
    f.write(b'\x00' * (DATA_START - f.tell()))
    f.write(datalst)
print('Finished building template file.',
      'Copying template into ISO folder structure.')
shutil.copy('data.lst', buildpath + r'\PSP_GAME\USRDIR\data.lst')
print('Operation part 1 finished.')
