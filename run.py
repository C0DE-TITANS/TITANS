#UTF-8
from os import system as cmd
import platform
bit = platform.architecture()[0]
cmd('git pull');cmd('clear')

if bit=='64bit':
    print('[!] 64 Bit Device')
    cmd('chmod 777 titans')
    cmd('./titans')

if bit == '32bit':
    print('[!] 32 Bit Device')
    cmd('chmod 777 titan')
    cmd('./titan')

else:
    print('Your Device did not support TITANS tool...!!')
    exit()