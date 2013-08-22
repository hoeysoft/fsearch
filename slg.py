# slg.py - Search Launcher Generator
# Written by hoey.

"""Usage : >>python slg.py QUERY_URL [, OUTNAME]
"""

_TEMPLATE = \
""" @echo off

::URL to query
SET HOEY_LCHR_QUERY={0}
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
"""


_OUT_EXTENSION = '.bat'

import sys
if __name__ == '__main__':
    argc = len(sys.argv)
    assert argc > 1, 'Should be specified QUERY_URL at least.'
    assert argc < 4, 'Should be specified QUERY_URL, OUTFILE at most.'

    query_url = sys.argv[1]
    outfile = 'out.bat'
    if argc == 3:
        outfile = sys.argv[2]
        if outfile[-4:] != _OUT_EXTENSION:
            outfile = outfile + _OUT_EXTENSION 
    
    try:
        f = open(outfile, 'w')
        f.write(_TEMPLATE.format(query_url))
        f.close()
    except:
        print('File error occured.')

else:
    print("Can't use 'slg.py' as a module")

    
    


