

import threading
import time
from src.module.initStart.pStart import PStart
from src.module.sLoger.logger import Logger

# <TODO> - запускать gui в другом треде
# <TODO> - Связать gui с бд

class mainApp():
    def __init__(self) -> None:
        self.main()

    def main(self):
        if PStart():
            self.initTrhed()
            print('ok')

    def initTrhed(self):
        threading.Thread(target=self.thInitProject,
                         name="startProgram").start()
        return ('ok')

    def thInitProject(self):
        while (True):
            print('ok')
            try:
                time.sleep(5)
                print(['Все ок', 'я работаю'])
                # PStart().thUppdate()
                Logger().logInfo(['Все ок', 'я работаю'])
            except TimeoutError as error:
                Logger().logFatal(['Uppdater Fatal Error', error])
