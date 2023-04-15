"""
Задание 5.

Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.

Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!
"""
import os
import subprocess
import chardet
from concurrent.futures import ThreadPoolExecutor

websites = ['yandex.ru', 'youtube.com']
print(os.name)


def ping_website(website):
    ARGS = ['ping', website]
    WS_PING = subprocess.Popen(ARGS, stdout=subprocess.PIPE)
    for line in WS_PING.stdout:
        result = chardet.detect(line)
        print(line.decode(encoding=result['encoding']))


if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers=len(websites)) as executor:
        results = executor.map(ping_website, websites)

