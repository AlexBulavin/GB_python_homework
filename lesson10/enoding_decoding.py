__author__ = 'Alex Bulavin'
import subprocess
import chardet
import os

ARGS = ['ping', 'yandex.ru']
YA_PING = subprocess.Popen(ARGS, stdout=subprocess.PIPE)
print(YA_PING.stdout)
for line in YA_PING.stdout:
    #print(line.decode('cp866'))
    res = chardet.detect(line)
    print(res)
    print(line.decode(encoding=res['encoding']))
    print(f'os.name: {os.name}')

