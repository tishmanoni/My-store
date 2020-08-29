#!c:\users\mide\documents\mystore\env\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'flower==1.0.1','console_scripts','flower'
__requires__ = 'flower==1.0.1'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('flower==1.0.1', 'console_scripts', 'flower')()
    )
