@echo off

if "%1" == "" (echo "pass a path." & goto ERROR)

:: check whether valid dir path.
pushd "%~1" 2> nul
if errorlevel 1 (echo "%1 is not a path." & goto ERROR)
popd

if not defined hoeypath (set hoeypath=;)

:: check redundant and add to local path.
set NEW_HOEYPATH="%1"
call :addPath "NEW_HOEYPATH" /B
if not errorlevel 0 (echo "Path parsing failed." & goto ERROR)

:: keep it registry, as USER env variable.
setx hoeypath "%hoeypath%"
setx path "%hoeypath%"


exit /b 0


:ERROR
echo FAILED.
exit /b 1
	
	

:: Referred By dbenham.
:: http://stackoverflow.com/questions/141344/how-to-check-if-directory-exists-in-path/141385
:: slightly modified for applying USER ENV;
:addPath pathVar /B
::
::  Safely appends the path contained within variable pathVar to the end
::  of PATH if and only if the path does not already exist within PATH.
::
::  If the case insensitive /B option is specified, then the path is
::  inserted into the front (Beginning) of PATH instead.
::
::  If the pathVar path is fully qualified, then it is logically compared
::  to each fully qualified path within PATH. The path strings are
::  considered a match if they are logically equivalent.
::
::  If the pathVar path is relative, then it is strictly compared to each
::  relative path within PATH. Case differences and double quotes are
::  ignored, but otherwise the path strings must match exactly.
::
::  Before appending the pathVar path, all double quotes are stripped, and
::  then the path is enclosed in double quotes if and only if the path
::  contains at least one semicolon.
::
::  addPath aborts with ERRORLEVEL 2 if pathVar is missing or undefined
::  or if PATH is undefined.
::
::------------------------------------------------------------------------
::
:: Error checking
if "%~1"=="" exit /b 2
if not defined %~1 exit /b 2
if not defined hoeypath exit /b 2
::
:: Determine if function was called while delayed expansion was enabled
setlocal
set "NotDelayed=!"
::
:: Prepare to safely parse PATH into individual paths
setlocal DisableDelayedExpansion
set "var=%hoeypath:"=""%"
set "var=%var:^=^^%"
set "var=%var:&=^&%"
set "var=%var:|=^|%"
set "var=%var:<=^<%"
set "var=%var:>=^>%"
set "var=%var:;=^;^;%"
set var=%var:""="%
set "var=%var:"=""Q%"
set "var=%var:;;="S"S%"
set "var=%var:^;^;=;%"
set "var=%var:""="%"
setlocal EnableDelayedExpansion
set "var=!var:"Q=!"
set "var=!var:"S"S=";"!"
::
:: Remove quotes from pathVar and abort if it becomes empty
set "new=!%~1:"^=!"
if not defined new exit /b 2
::
:: Determine if pathVar is fully qualified
echo("!new!"|findstr /i /r /c:^"^^\"[a-zA-Z]:[\\/][^\\/]" ^
                           /c:^"^^\"[\\][\\]" >nul ^
  && set "abs=1" || set "abs=0"
::
:: For each path in PATH, check if path is fully qualified and then
:: do proper comparison with pathVar. Exit if a match is found.
:: Delayed expansion must be disabled when expanding FOR variables
:: just in case the value contains !
for %%A in ("!new!\") do for %%B in ("!var!") do (
  if "!!"=="" setlocal disableDelayedExpansion
  for %%C in ("%%~B\") do (
    echo(%%B|findstr /i /r /c:^"^^\"[a-zA-Z]:[\\/][^\\/]" ^
                           /c:^"^^\"[\\][\\]" >nul ^
      && (if %abs%==1 if /i "%%~sA"=="%%~sC" exit /b 0) ^
      || (if %abs%==0 if /i %%A==%%C exit /b 0)
  )
)
::
:: Build the modified PATH, enclosing the added path in quotes
:: only if it contains ;
setlocal enableDelayedExpansion
if "!new:;=!" neq "!new!" set new="!new!"
if /i "%~2"=="/B" (set "rtn=!new!;!hoeypath!") else set "rtn=!hoeypath!;!new!"
::
:: rtn now contains the modified PATH. We need to safely pass the
:: value accross the ENDLOCAL barrier
::
:: Make rtn safe for assignment using normal expansion by replacing
:: % and " with not yet defined FOR variables
set "rtn=!rtn:%%=%%A!"
set "rtn=!rtn:"=%%B!"
::
:: Escape ^ and ! if function was called while delayed expansion was enabled.
:: The trailing ! in the second assignment is critical and must not be removed.
if not defined NotDelayed set "rtn=!rtn:^=^^^^!"
if not defined NotDelayed set "rtn=%rtn:!=^^^!%" !
::
:: Pass the rtn value accross the ENDLOCAL barrier using FOR variables to
:: restore the % and " characters. Again the trailing ! is critical.
for /f "usebackq tokens=1,2" %%A in ('%%^ ^"') do (
  endlocal & endlocal & endlocal & endlocal & endlocal
  set "hoeypath=%rtn%" !
)
exit /b 0
