@echo off
python "%USERPROFILE%\Documents\clean_dl.py" --dir "%USERPROFILE%\Downloads" --ext ifc ifczip bcf bcfzip zip pdf smc xlsx dwg ics msi exe --path "temp*"
:: python "%USERPROFILE%\Documents\clean_dl.py" --dir "%USERPROFILE%\Desktop" --ext ifc zip pdf smc xlsx log bak dwg
pause