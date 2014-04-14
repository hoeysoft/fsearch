@echo off
setlocal
for /F "tokens=*" %%i in ('date /t') do set today=%%i
set today=%today: =%
set logpath=%HOMEDRIVE%%HOMEPATH%\fsearch_log\%today%.txt

for /f "tokens=*" %%i in ('mytime.bat') do set now=%%i
echo [%now%] %* >> %logpath%
endlocal
