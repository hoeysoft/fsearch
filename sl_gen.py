# sl_gen.py - Search Launcher Generator
# Written by hoey @ hoeysoft.com

"""Usage : >>python sl_gen.py 
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


def get_args():
    """read args from <stdin> or <argv>
    """

    argc = len(sys.argv)
    if argc == 1: # stdin mode
        line = raw_input()
        return re.split('\s*', line, 2)
        
    else: # argv mode
        return sys.argv[1:]


if __name__ == '__main__':
    try:
        while True:
            template = _TEMPLATE[:]
            args = get_args()

            query_url = args[0]
            assert(query_url != '')

            outfile = 'out.bat'
            if len(args) > 1: 
                outfile = args[1]
                if outfile[-4:] != _OUT_EXTENSION:
                    outfile = outfile + _OUT_EXTENSION 
    
            f = open(outfile, 'w')
            f.write(template.format(query_url))
            f.close()
            
            print(query_url + ' ==> ' + outfile)

            # don't repeat when argv mode.
            if len(sys.argv) > 1:
                break;

    except EOFError:
        pass

    except:
        sys.stderr.write('error occurred.\n')

else:
    print("Can't use 'sl_gen.py' as a module")
