:: assume python27 is installed.
@echo off
python fsgen.py "..\batch" < list.txt
call %cd%\..\setup.bat "%cd%\..\"
