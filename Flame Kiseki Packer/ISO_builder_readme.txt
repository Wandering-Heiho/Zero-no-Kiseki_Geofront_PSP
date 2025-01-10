ISO_build by flamethrower
Extract and rebuild PSP UMD Image (.iso) that use Falcom data.lst allocation
table.

v2.1 02Oct16
-Part 1 builds data.lst in the current folder (of filelist_builder_part1.py)
 instead of hard coded.

v2 02Oct16
-Added python unpack of ISO.
-As a pre-processing step, will discard files with non-ASCII characters in the
 filename
v1 01Oct16
-Initial version

1A. Extract your game by drag & dropping the ISO overtop of _extract.bat
1B. The alternate is _extract_new.bat which uses Python to extract and is
device independent (will produce correct SJIS filename characters).
2. Modify, add and/or delete files as needed. 
Files must conform to 8.3 specification and there isn't automated checking for
this. Non-ASCII characters in filenames are not allowed.
3. Build by running _build.bat
Alternatively you could run _part1, then _mkisofs, then _part2.

The objective of part 1 is to build a data.lst template based on target ISO
file structure and file system data such as file name, extension and size.
We can't finish off data.lst at part 1 because file locations (LBA) aren't
known yet.

The objective of the mkisofs part is to build an ISO image using the target
ISO file structure.

The objective of part 2 is to update the data.lst template created in part 1
with the file locations, which have been finalized at this point. After that,
the new data.lst is inserted into the image overtop of the template.