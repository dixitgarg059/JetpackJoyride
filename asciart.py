import sys
import os
from colorama import init
init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
from termcolor import cprint 
from pyfiglet import figlet_format
os.system('clear')
print('\033[20;1H',end='')
cprint(figlet_format('coins',font="bubble"),
       'yellow', attrs=['bold'])	