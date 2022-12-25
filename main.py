import os
import threading
from pStart import PStart
import time

# <TODO> Сделать логер.
# <TODO> хранить бд в файах.
# <TODO> сделать отдельную функцию для запуска потоков.


def main():
    if PStart():
        threading.Thread(target=thInitProject, name="startProgram").start()
        # <TODO> - запускать gui в другом треде


def thInitProject():
    ps = PStart
    while (True):
        print('ok')
        time.sleep(900)
        ps.thUppdate(ps)


if __name__ == "__main__":
    main()
