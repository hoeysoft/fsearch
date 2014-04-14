@echo off
setlocal
set hour=%time:~0,2%
if "%hour:~0,1%" == " " set hour=0%hour:~1,1%

set min=%time:~3,2%
if "%min:~0,1%" == " " set min=0%min:~1,1%

set sec=%time:~6,2%
if "%sec:~0,1%" == " " set sec=0%sec:~1,1%

echo %hour%:%min%:%sec%
