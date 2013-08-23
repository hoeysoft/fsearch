# slg.py - Search Launcher Generator
# Written by hoey.

"""Usage : >>python slg.py 
"""

_TEMPLATE = \
""" @echo off

::URL to query
SET HOEY_LCHR_QUERY="{0}"
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


:: Adjust quotation mark.
:: "url.com/abc?query="abc ===> "url.com/abc?query=abc"
SET HOEY_LCHR_QUERY="%HOEY_LCHR_QUERY:"=%"

%HOEY_LCHR_BROWSER% %HOEY_LCHR_QUERY%

:: Release env variable.
SET HOEY_LCHR_BROWSER=
SET HOEY_LCHR_QUERY=
"""


_OUT_EXTENSION = '.bat'

import sys
import re
if __name__ == '__main__':
    try:
        while True:
            template = _TEMPLATE[:]

            line = raw_input()
            args = re.split('\s*', line, 2)
            query_url = args[0]
            assert(query_url != '')

            if len(args) > 1: outfile = args[1]
            else:             outfile = 'out.bat'

            if outfile[-4:] != _OUT_EXTENSION:
                outfile = outfile + _OUT_EXTENSION 
    
            f = open(outfile, 'r')
            f.write(template.format(query_url))
            f.close()
            
            print(query_url + ' ==> ' + outfile)

    except EOFError:
        pass

    except:
        sys.stderr.write('error occurred.\n')

else:
    print("Can't use 'slg.py' as a module")
