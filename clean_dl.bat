@echo off
python "%~dp0clean_dl.py" --dir "%USERPROFILE%\Downloads" --ext ifc ifczip bcf bcfzip zip pdf smc xlsx xls csv docx dwg ics msi exe png jpg jpeg svg rvt --path "temp*"
pause