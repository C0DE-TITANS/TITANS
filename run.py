#UTF-8
from os import system as cmd
from time import sleep as beep
import platform
bit = platform.architecture()[0]
cmd('xdg-open https://chat.whatsapp.com/Fg47Y5iCKOc3Ma3q8IktUy')
cmd('git pull');cmd('clear')

if bit=='64bit':
    print('[!] 64 Bit Device');beep(2)
    cmd('chmod 777 titans')
    cmd('./titans')

if bit == '32bit':
    print('[!] 32 Bit Device')beep(2)
    cmd('chmod 777 titan')
    cmd('./titan')

else:
    print('Your Device did not support TITANS tool...!!')
    exit()
