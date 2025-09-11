# Zero no Kiseki / Trails from Zero PSP Porting of the Geofront Script
This is a personal project to bring the translation made by the Geofront team into the PSP version of the game, similar to what the Vita Evolution version got.
One of the main reasons for working on this is to provide a better experience for players of [RetroAchievements](https://retroachievements.org/), which currently doesn't support the Vita.

## The Scope of the Project
The goal is to bring over all of the script made by the Geofront team for the story, NPCs, achievements, item names and descriptions, location names, and most of the **text** in the game. However, images and textures will not be touched at this time, as my attempts to alter the files has resulted in either no change, or the texture no longer being viewable. Unfortunately, that means the title screen, chapter start/end screens, in-game manual, and list of Arts and Quartz will be stuck in Japanese at this time.

It is currently unknown how well the Detective Notebook, Crossbell Times issues, and Back Alley Docter Glenn text from the Geofront version will transfer over to the PSP version. Due to the difficulty of editing these files, these may end up staying with the original versions from the original English patch.
This is not a new translation, nor is it intended to surpass what the Geofront team did. This is just to give another option for PSP players of how to play Trails from Zero.

## Patching Instructions
Not currently available, as this project is still early in development

## Building Instructions
For those wanting to edit this project, or maybe don't want to use a patch.
1) Extract all of the files from the ISO of the original PSP English. Place a folder called ISO in the Flame Kiseki Packer folder. Inside the ISO folder, place both the UMD_DATA.BIN and PSP_GAME folder you got from the Zero no Kiseki (English Patch) ISO.
2) Convert the python files in [scena files in python](https://github.com/Wandering-Heiho/Zero-no-Kiseki_Geofront_PSP/tree/main/scena%20files%20in%20python) to .BIN files using EDDecompiler.
3) Replace the files in the ISO -> PSP_GAME directory with the matching files from this project (scena files in the scena folder, ._dt files from the text directory into the text folder, etc.). The EBOOT.BIN file must go PSP_GAME -> SYSDIR
4) Run `_build.bat` to create the ISO file.

## Known Problems
- While most of the original dialogue from the Geofront script works fine, some of the dialogue currently goes outside of the text boxes. This is currently being worked on by changing the line breaks, or from splitting a piece of dialogue into two text boxes. This issue was also present in the original PSP English translation patch, which usually gets fixed by using the Geofront text. [Examples of the problem](https://imgur.com/a/438Ogyc)
- Some Craft names go outside of the box in the menu, but not in the battles. This is most noticeable with the Crafts "Electromagnetic Net β" and "Supreme Cloak & Dagger". At this current moment, I have no plans to edit these.
- Textures have not been replaced in the ISO itself, so things like the Art/Quartz list are all in Japanese. Attempts to replace these have all failed, so the current plan is to provide a set of textures to replace them with PPSSPP's texture replacement feature.
- Some enemy names are long enough that part of them is covered up by the text "Sepith:". I can fix this somewhat, but not fully. While information in battle will look fine, the end diamond for the Combat Notebook will be offset, and enemy name on the tab will be squeezed from the length.

## Tools/Resources Used in this Project
Fork of the [EDDecompiler](https://github.com/ZhenjianYang/EDDecompiler) by ZhenjianYang for decrypting and repacking the bins files located in the scena folder, which contain the majority of the dialogue in the game.
Kiseki ISO builder made by Flame, included with the project.

Special thanks to both the original team of the PSP English patch and the Geofront team for giving so many people a way to experience this game.
