import logging
import threading
from time import sleep
from typing import Callable, Final

LOG_PATH: Final[str] = './logger_v1.log'


logging.basicConfig(filename=LOG_PATH,
                    datefmt='%H:%M:%S %d:%m:%Y',
                    level=logging.DEBUG,
                    #format='%(levelname)s (%(asctime)s) %(message)s (Line: %(lineno)s [%(filename)s])'
                    format='%(levelname)s (%(asctime)s) %(message)s'
)

debug: Final[Callable] = logging.debug
info: Final[Callable] = logging.info
warn: Final[Callable] = logging.warning
crit: Final[Callable] = logging.critical

exit_var: bool = False
list_of_lines: list[str] = []
old_list_of_lines: list[str]

def exiting() -> None:
    info('"Exiting program..."\n')
    global exit_var
    exit_var = True
    exit()

def read() -> None:
    with open('C:/Users/user/AppData/LocalLow/TheFarmerWasReplaced/TheFarmerWasReplaced/output.txt') as output:
        global old_list_of_lines
        global list_of_lines
        old_list_of_lines = list_of_lines
        list_of_lines = [line.rstrip('\n') for line in output.readlines()]

def start_thread(func: Callable, *args) -> None:
    thread = threading.Thread(target=func, args=args)
    thread.start()

def main() -> None:
    start_thread(reader)
    input('exit? ')

def reader():
    while not exit_var:
        read()
        _list_of_lines = list_of_lines.copy()
        for line in old_list_of_lines:
            _list_of_lines.remove(line)
        for line in _list_of_lines:
            match line[:3].lower():
                case 'd: ':
                    debug(line[3:])
                case 'i: ':
                    info(line[3:])
                case 'w: ':
                    warn(line[3:])
                case 'c: ':
                    crit(line[3:])
                case _:
                    warn(line)
        sleep(2)
        
try:
    if __name__ == '__main__':
        info('"Starting..."')
        main()
except Exception as e:
    logging.critical('%s: %s', type(e), e)
finally:
    exiting()