@echo off

setlocal
set BASE_PATH=%~1
if not defined BASE_PATH set BASE_PATH=%cd%

echo %BASE_PATH%

set FSEARCH_PATH="%HOMEDRIVE%%HOMEPATH%\fsearch"
mkdir %FSEARCH_PATH%
copy /Y "%BASE_PATH%\batch\??.bat" %FSEARCH_PATH%

call "%BASE_PATH%\config\addpath.bat" %FSEARCH_PATH%
endlocal
pause
