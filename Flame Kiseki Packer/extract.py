import ISO_extract
import sys

with open(sys.argv[1], 'rb') as f:
    pathtbl = ISO_extract.getpathtbl(f)
    ISO_extract.extract_all(f, sys.argv[2], 'cp932', pathtbl)
 
