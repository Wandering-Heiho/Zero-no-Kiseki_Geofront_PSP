import shutil

#EBOOT
shutil.copy(r'EBOOT\EBOOT.BIN', r'ISO\PSP_GAME\SYSDIR')

#PARAM.SFO
shutil.copy(r'misc\PARAM.SFO', r'ISO\PSP_GAME')

#misc files
shutil.copy(r'misc\detail.txt', r'ISO\PSP_GAME\USRDIR\savefile')
shutil.copy(r'misc\dtitle.txt', r'ISO\PSP_GAME\USRDIR\savefile')
shutil.copy(r'misc\title.txt', r'ISO\PSP_GAME\USRDIR\savefile')

#delete UPDATE folder (not needed)
shutil.rmtree(r'ISO\PSP_GAME\SYSDIR\UPDATE', ignore_errors = True)
