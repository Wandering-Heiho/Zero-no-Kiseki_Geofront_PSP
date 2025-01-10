IF EXIST "output.iso" (
del output.iso
)
.\bin\mkisofs -iso-level 4 -xa -A "PSP GAME" -V "Whatever" -sysid "PSP GAME" -volset "Whatever" -p "" -publisher "" -o "output.iso" ISO
pause