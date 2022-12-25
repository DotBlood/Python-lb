import os
import threading
from pStart import PStart
import time


##############################################################
#                       todo dlya vas
# <TODO> Сделать логер.
# <TODO> - Сдлеать гуи
##############################################################
#  
# <TODO> сделать отдельную функцию для запуска тредов.
#
##############################################################

def main():
    if PStart():
        threading.Thread(target=thInitProject, name="startProgram").start()

        # <TODO> - запускать gui в другом треде
        # threading.Thread(target=gui, name="gui").start()
        # pyqt5 / tkinker =>


def thInitProject():
    ps = PStart
    while (True):
        print('ok')
        try:
            time.sleep(900)
            ps.thUppdate(ps)
        except TimeoutError as error:
            exit(0)  # logger


if __name__ == "__main__":
    main()
