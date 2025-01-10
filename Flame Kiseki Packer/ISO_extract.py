import pdb
import os
import struct
from collections import namedtuple

def ensure_dir(dirname):
    if not os.path.exists(dirname):
        os.makedirs(dirname)
        
def split_path(path):
    path = path.rstrip('\\')
    folders = []
    while True:
        path, folder = os.path.split(path)
        if folder == '':
            if path not in ('', '\\'):
                folders.append(path)
            break
        else:
            folders.append(folder)
    return folders

dir_record = namedtuple('dir_record', ['name', 'full_path', 'LBA', 'flags', 'size', 'dir_rec_pos'])
def read_dir_record(f, folder_path, codec='cp932'):
    #Advances the file position to the next directory record also.
    try:
        pos = f.tell()
        (rec_len, dummy1, LBA, dummy2, size, dummy3, dummy4, dummy5, dummy6, flags,
         dummy7, dummy8, dummy9, name_len) = (
            struct.unpack('<BBIIIIIHBBBBIB', f.read(33)))
        name = f.read(name_len)
        f.seek(pos + rec_len)
        return dir_record(name.decode(codec), folder_path + '\\' + name.decode(codec),
                          LBA, flags, size, pos)
    except Exception as err:
        print(hex(pos))
        print(name)
        raise err

def getpathtbl(f, codec='cp932'):
    pathtabledata = [None]                  #Shove indexes + 1
    f.seek(16 * 0x800 + 140)                #Path table LBA
    f.seek(struct.unpack('<I', f.read(4))[0] * 0x800)
    path_record = namedtuple('path_record', ['name', 'full_path', 'LBA', 'parent_ID', 'dir_tbl'])
    while True:
        name_len, addl_len, LBA, parent_ID = struct.unpack('<BBIH', f.read(8))
        name = f.read(name_len)
        if name == b'\x00':
            name = b''
        if f.tell() % 2 != 0:
            f.read(1)
        if LBA == 0:
            break
        else:
            name_temp = name
            parent_ID_temp = parent_ID
            full_path = []
            while name_temp != b'':
                full_path.append(name_temp)
                record = pathtabledata[parent_ID_temp]
                name_temp = record.name
                parent_ID_temp = record.parent_ID
            full_path.append(b'')
            full_path = b'\\'.join(reversed(full_path)).decode('ascii')
            dir_tbl = getdirtbl(f, LBA, full_path, codec)
            pathtabledata.append(path_record(name, full_path, LBA, parent_ID, dir_tbl))
    return pathtabledata

def getdirtbl(f, LBA, full_path, codec):
    saved = f.tell()
    dir_pos = LBA * 0x800
    f.seek(dir_pos)
    dir_size = read_dir_record(f, full_path, codec).size
    dir_tbl = []
    while f.tell() < dir_pos + dir_size:
        dir_rec = read_dir_record(f, full_path, codec)
        test = f.read(1)
        f.seek(-1, 1)
        #If at end of current LBA, advance to the next one
        if test == b'\x00':
            f.seek(((f.tell() + 0x800 - 1) // 0x800) * 0x800)
        if dir_rec.flags == 0:
            dir_tbl.append(dir_rec)
    f.seek(saved)
    return dir_tbl
def get_dir_rec(pathname, pathtbl):
    folder, file = os.path.split(pathname)
    dirID = getdirID(folder, pathtbl)
    if not dirID:
        return
    for dir_rec in pathtbl[dirID].dir_tbl:
        if dir_rec.name.lower() == file.lower():
            return dir_rec
    raise Exception('File {} not found in the ISO'.format(pathname))
def getdirID(pathname, pathtbl):
    folders = split_path(pathname)
    for i, record in enumerate(pathtbl[1:], 1):
        for foldername in folders:
            if record.name.decode('ascii').lower() == foldername.lower():
                prev_record = record
                record = pathtbl[record.parent_ID]
            else:
                break
        else:
            return i    #Matched full path
    else:
        return          #Not found
def extract(f, filename, LBA, size):
    f.seek(LBA * 0x800)
    with open(filename, 'wb') as g:
        g.write(f.read(size))
def extract_all(f, target_path, codec='cp932', pathtbl=None):
    if pathtbl == None:
        pathtbl = getpathtbl(f, codec)
    for path_rec in pathtbl[1:]:
        ensure_dir(target_path + path_rec.full_path)
        for dir_rec in path_rec.dir_tbl:
            with open(target_path + dir_rec.full_path, 'wb') as g:
                f.seek(dir_rec.LBA * 0x800)
                g.write(f.read(dir_rec.size))
                
def replace(f, replace_path, replace_file, pathtbl = None, LBAlist = None):
    '''replace a file in ISO f

    f must be opened for updating.
    If replace_path is a file in the ISO and replace_file is a valid file,
    the file is replaced if there's enough space for it (otherwise no action
    is taken).
    
    If pathtbl and LBAlist are not specified, it will compute them.
    If you care calling this over and over, you might want to pass them in
    to save on computation time.
    '''
    if f.mode != 'rb+':
        raise IOError('Replace: file not opened for updating')
    if pathtbl == None:
        pathtbl = getpathtbl(f)
    dir_rec = get_dir_rec(replace_path, pathtbl)
    if not os.path.isfile(replace_file):
        raise Exception('Replace file {} not found'.format(replace_file))
    if LBAlist == None:
        LBAlist = [dir_rec.LBA for path_rec in pathtbl[1:] for
                   dir_rec in path_rec.dir_tbl]
        f.seek(16 * 0x800 + 0x50)
        LBAlist.append(struct.unpack('<I', f.read(4))[0])
        LBAlist.sort()
    nextLBA = LBAlist[LBAlist.index(dir_rec.LBA) + 1]
    avail_space = (nextLBA - dir_rec.LBA) * 0x800
    size = os.path.getsize(replace_file)
    if size > avail_space:
        raise Exception('Not enough space for {} (required: {} bytes, '
                        'available: {} bytes'.format(
                            replace_file, size, avail_space))
#Time to do the replace
    f.seek(dir_rec.LBA * 0x800)         #Zero out original file
    f.write(b'\x00' * avail_space)
    f.seek(dir_rec.LBA * 0x800)
    with open(replace_file, 'rb') as g: #Write new file
        f.write(g.read())
    f.seek(dir_rec.dir_rec_pos + 10)    #Update directory record with new filesize
    f.write(struct.pack('<I', size))    
    f.write(struct.pack('>I', size))
    
def ISO_extract(filename, pathname, filelist=None):
    """Extract files from an ISO

    Doesn't necessarily have to be from a PSP ISO, any ISO should work.

    If pathname is the path to a file, filelist must not be specified.
    It will look for the specified file and if found, will extract it.

    If path name is the path to a folder, filelist must be specified.
    It will look for the folder.
    If the folder is found, it will look for each file in filelist within
    that folder and will dump any and all of them it finds.

    Pathname doesn't have to be the full path but if ambiguous, might not work.
    Only the first folder that matches the entire path will be searched.
    """
    if filelist == None:
        pathname = pathname.rstrip('\\')
        pathname, targetfile = os.path.split(pathname)
        filelist = [targetfile]
    else:
        filelist = list(filelist)

    with open(filename, 'rb') as f:
        pathtbl = getpathtbl(f)
        i = getdirID(pathname, pathtbl)
        if not i:
            print('Path {} not found.'.format(pathname))
            return
        for dir_rec in pathtbl[i].dir_tbl:
            for name in filelist:
                if name.lower() == dir_rec.name.lower():
                    filelist.remove(name)
                    extract(f, dir_rec.name, dir_rec.LBA, dir_rec.size)
                    break
            if filelist == []:          #All files found
                break
    if filelist == []:                  #All files found
        pass
    else:
        print('Files not found:', ', '.join(filelist))
#Example 1:
#All of these will work for path definitions
#It does not have to be the full path
##targetfolder = r'GAMEDATA\FLD\MAP''\\'
##targetfolder = r'GAMEDATA\FLD\MAP'
##targetfolder = r'\GAMEDATA\FLD\MAP' + '\\'
##ISO_extract('LR.iso', targetfolder, ('MAP_T_KAN_01.BIN', 'MAP_T_KAN_00.BIN'))
#Example 2: Extract UMD_DATA.BIN from the root folder.
##ISO_extract('UMD_DATA.BIN')
#Example 3: Extract a specific pathname.
##ISO_extract(r'GAMEDATA\FLD\MAP\MAP_T_KAN_01.BIN')
##with open('LR.iso', 'rb') as f:
##    pathtbl = getpathtbl(f)
##    print(get_dir_rec(r'GAMEDATA\FLD\MAP\MAP_T_KAN_01.BIN', pathtbl))
##with open('output.iso', 'rb') as f:
##    pathtbl = getpathtbl(f)
