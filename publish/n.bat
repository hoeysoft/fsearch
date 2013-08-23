 @echo off

::URL to query
SET HOEY_LCHR_QUERY="search.naver.com/search.naver?ie=utf8&query="
SET HOEY_LCHR_QUERY=%HOEY_LCHR_QUERY%%1
SHIFT

::Extract default browser path(Windows7 Based)
FOR /F "tokens=2* delims=	 " %%A IN ('REG QUERY "HKEY_CLASSES_ROOT\http\shell\open\command" /ve') DO SET HOEY_LCHR_BROWSER=%%B

:Loop
IF "%1"=="" GOTO Continue

SET HOEY_LCHR_QUERY=%HOEY_LCHR_QUERY%%%20%1

SHIFT
GOTO Loop
:Continue

%HOEY_LCHR_BROWSER% %HOEY_LCHR_QUERY%

SET HOEY_LCHR_BROWSER=
SET HOEY_LCHR_QUERY=
