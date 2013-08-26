# fsgen.py - Search Launcher Generator
# Written by hoey @ hoeysoft.com

"""Usage : >>python fsgen.py [out.path] < list.txt
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

start "" %HOEY_LCHR_BROWSER% %HOEY_LCHR_QUERY%

:: Release env variable.
SET HOEY_LCHR_BROWSER=
SET HOEY_LCHR_QUERY=
"""

_OUT_EXTENSION = '.bat'


import sys
import os
import re


def get_args():
    """read args from <stdin> or <argv>
    """

    if argc == 1: # stdin mode
        return 
        
    else: # argv mode
        return sys.argv[1:]


if __name__ == '__main__':
    try:
        argc = len(sys.argv)
        if argc == 1: outpath = '.' 
        else:         outpath = sys.argv[1]
        
        while True:
            line = raw_input()
            args = re.split('\s*', line, 2)

            outname = 'out.bat'
            if len(args) > 1: 
                outname = args[0]
                if outname[-4:] != _OUT_EXTENSION:
                    outname = outname + _OUT_EXTENSION 

            query_url = args[1]
            assert(query_url != '')
    
            outfile = os.path.join(outpath, outname)
            f = open(outfile, 'w')
            f.write(_TEMPLATE.format(query_url))
            f.close()
            
            print(outfile + ' ==> ' + query_url)

    except EOFError:
        pass

    except:
        sys.stderr.write('error occurred.\n')

else:
    print("Can't use 'fsgen.py' as a module")
