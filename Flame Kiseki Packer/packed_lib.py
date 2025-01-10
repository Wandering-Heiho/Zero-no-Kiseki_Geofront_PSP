import os
import struct

class packed_file(object):
    def __init__(self, f):
        self.updated = False
        self.name = os.path.split(f.name)[1]
        self.num_files = struct.unpack('<I', f.read(4))[0]
        self.TOC = []
        f.seek(0x10)
        for x in range(self.num_files):
            self.TOC.append(sub_file(f.read(0x20)))
        for x in self.TOC:
            f.seek(x.offset)
            x.data = f.read(x.size)
##        while True:
##            for i, x in enumerate(self.TOC):
##                if x.name == '':
##                    self.remove(x.name)
##                    break
##            else:
##                break
    def __len__(self):
        return len(self.TOC)
    def remove(self, filename):
        for i, file in enumerate(self.TOC):
            if file.name == filename:
                break
        else:           #Not there
            print(self.name, 'not found')
            return
        self.updated = True
        self.num_files -= 1
        del self.TOC[i]
    def bin(self):
        offset = 0x10 + 0x20 * len(self.TOC)
        for x in self.TOC:
            x.offset = offset
            offset += len(x)
        b = struct.pack('<I', self.num_files) * 4
        b += b''.join(x.bin() for x in self.TOC)
        b += b''.join(x.data for x in self.TOC)
        return b
class sub_file(object):
    def __init__(self, TOC):
        self.name = TOC[:0x10].rstrip(b'\x00').decode('ascii')
        self.offset, self.size, self.decompressed_size = (
            struct.unpack('<III', TOC[0x10:0x1C]))
    def __len__(self):
        return self.size
    def bin(self):
        name = (self.name + '\x00' * (0x10 - len(self.name))).encode('ascii')
        return name + struct.pack(
            '<IIII', self.offset, self.size, self.decompressed_size, 0)
##with open(r'G:\Emu\PSP\ZnK Tool\ISO\PSP_GAME\USRDIR\data\cclm\map4\c1130_zz.mcz', 'rb') as f:
##    packed = packed_file(f)
##packed.remove('t_book05._dt')
##with open('c1130_zz.mcz', 'wb') as f:
##    f.write(packed.bin())
