Nayuta Tools

Credits:
Most of this code is by flamethrower

Falcom ISO builder (part of this tool pack) is by flamethrower
mkisofs is part of CDRtools. 
See http://cdrtools.sourceforge.net/private/cdrecord.html for credits.
deceboot is by NoOnee, http://www.romhacking.net/utilities/1225/

Falcom Compression and Decompression Library is by me, but it's based on EsperKnight's 
code: http://www.romhacking.net/forum/index.php?topic=17666.msg256702#msg256702

The included images are edits of the original Falcom ones.
Images edited by SkyeWelse, http://www.retro-type.com/

OK, so how does this thing work?

1. Setup (only once)
Run extract by dragging your ISO overtop of _extract_new.bat
Run setup.py

2. Edit contents

2.1 Argument files (*.arb)
2.2 EBOOT and miscellaneous files (EBOOT.bin)
2.3 Images (*.itp, *.it3)
2.4 Script (*.bin)
2.5 Text (*.tbl, *.tbb)

Some content if you want it:
Nayuta Dumps v2: https://docs.google.com/spreadsheets/d/1arjwWsncNemLRyI0279mjiuT-fw08I9NXt4p2etMVSA
Nayuta Scripts v2 Blank: https://docs.google.com/spreadsheets/d/1uexPZ_TWpdjCNnkVppV3M3bFZRfz7sC2iY69VUtCbn0
Nayuta Scripts v2 Merged: https://docs.google.com/spreadsheets/d/1swS6jjiP2Ph7OHMFMJZIVTM92PwxY4xEmIWBT_a5bcU

All input files are tsv format with utf-8 encoding
If you are exporting spreadsheets to get your tsvs, keep in mind that tsv format does not
support linebreaks within cells.

2.1 Argument files (*.arb)

Has area names and character names. I do not know what the other arguments do.

There is a limit of 31 bytes for both area name and character name.

I am assuming arb is "machine-readable argument file", has YS7_ARG at the top

Dump by running arb_dump.py
Insert by running arb_insert.py

For insert, it is looking for in the arb folder:
area_names.tsv
chr_names.tsv

For the insert, lines with a blank in the translated column are ignored on the insert.

It might break if you edit what you're not supposed to. Only area names and character 
names within these files are user text.

About references:
References look like: mp_0000 0x122c
This is telling the inserter program to recall what what put in at this file and position
and put the same string in at this file and position.

This is a feature where you need to translate each string only once. Each other time the
same exact string appears, a reference to the earlier one is added for you in the
translation column. If you would like the string to appear the same as the earlier one you
need not do anything, and if you would like it to appear different, you need to delete the
reference and enter the desired string as normal.

2.2 EBOOT and miscellaneous files (EBOOT.bin)
The miscellaneous files are PARAM.SFO, detail.txt, dtitle.txt and title.txt.

Text in EBOOT could appear anywhere in the game, and even in save files.
PARAM.SFO governs the name of the game in the PPSSPP title bar, and in the PSP XMB 
interface.
detail.txt, dtitle.txt, title.txt I believe govern the text that appears when using the
save manager in the PSP XMB.

An EBOOT dumper is not included. See the dump in Nayuta Dumps v2.

Insert EBOOT by running nayuta_eboot_insert_v2.py
The inserter is looking for eboot.tsv in the same folder.

Insert miscellaneous files by running misc.py
There is no input file for this. Adjust the values to insert by editing the code.

2.3 Images (*.itp, *.it3)
Various images that require localization.

You can transform .itp format that the game can read to .bmp or .png using itpcnv by
Pokanchan. You can get that at his site: http://www.pokanchan.jp/dokuwiki/software/itxcnv

IT3 are more complicated. I believe CompileTools by M-bot has a function to decompile and
compile them. I'd start there if I were you.
Compile Tools by M-bot: https://github.com/M-bot/CompileTools

h_###_##.itp:	manual images
icon_new.png;	empty save slot icon
icon0.png:	Game's icon in XMB interface (or PPSSPP interface)
m_field0.itp:	Continent names, season changing
m_field2.itp:	Names of sectors underneath each continent
m_field3.itp:	Stellarium
m_mons.itp:	Season names, area names, page numbers
m_quest.itp:	Complete and failed markers for quest screen
pic1.png	Wallpaper when the game is selected in XMB or PPSSPP interface
title0[012].it3:Title screens

2.4 Script (*.bin)
Most of the game content.

Dump using scriptdump.py, files are placed in the "dumped" folder
You could also just use the blank dump (see "Nayuta Scripts v2 Blank" above)
Insert using scriptinsert.py, it's looking for files in a "merged" folder

It takes a very long time to run this tool compared to any of the others, about one 
minute. If it's too annoying you could try adding multi-threaded programming to it.

The maximum length for a line is 63 characters. More than that will crash the game.
It'll be up to you to figure out other limits beyond that (63 bytes in a line for
the most common 0x98 opcode won't display properly).

For 0x98, 0x40 opcode:	Use up to three lines.
For 0x41 opcode:	Use up to ten lines

To get the extra lines, insert lines after the last line of the opcode and before the
next opcode.

2.5 Text (*.tbl, *.tbb)
fldlist: 		Level names and missions. Also the description text that displays
			when moving between continents
item:			menu screen, field screen, dialogues

fldlist0, fldlist1:	I don't know what the difference between these are
			Data for the main world map (Terra)
fldlist2		Data for the below Terra map
fldlist3		Data for the Stellarium map
foodarea		Data for the cooking menu screen
helplib			Titles for help images (menu screen)
item			Used many places throughout the game
monslib			Data for the monster library (menu screen)
pc			Nayuta and Noi's names
questlib		Data for quest mailbox and the quest screen (menu screen)

Length limits for text files
fldlist[0123]:	name:	23
		desc:	63	Text for moving between continents on world map
item:		name:	23
		desc:	63
monslib:	name:	31
		line:	31
questlib:	name:	47
		client:	31
		line:	51
foodarea	name:	25
helplib		name:	31
pc		name:	15

3. Copy data
There are a bunch of "copiers" in the tool's root folder. They grab the right files from
wherever and move them into the ISO folder structure. The other thing they do is delete
the files from the packed/archive files in USRDIR/pack if necessary so your new versions
will actually be read.

4. Build
Double-click build.bat.
You can get more information on the build process in the readme for Falcom ISO builder.