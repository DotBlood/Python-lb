import os
import time
from pathlib import Path


class Logger:
    pathTofile = None

    def __init__(self) -> None:
        self.path = str(Path.home()) + \
            f'\\documents\\test\\log\\'
        self.templateStart = "Hello User, if you are viewing this file, there is some problem with your program!\nPleace, send this file to `url`, not screan!\n---------\nBody Error:\n"
        self.templateEnd = "---------\nThank you for using our platform, we love our users, but everyone has problems!\nWE hope we don't lose you because of this mistake!"
        self.ChekFolderLog()

    def logFatal(self, args=[]) -> None:
        pathTofile = f"{self.path}{time.time_ns()}-FError.log"
        if type(pathTofile) != None:
            try:
                with open(f"{pathTofile}", 'w')as file:
                    file.write(self.templateStart)
                    for i in range(len(args)):
                        file.write(f">>> {args[i]}\n")
                    file.write(self.templateEnd)
            except OSError as e:
                return exit(0)
            finally:
                return True

    def logWarn(self, args=[]) -> None:
        pathTofile = f"{self.path}{time.time_ns()}-Warn.log"
        if type(pathTofile) != None:
            try:
                with open(f"{pathTofile}", 'w')as file:
                    file.write(self.templateStart)
                    for i in range(len(args)):
                        file.write(f"{args[i]}\n")
                    file.write(self.templateEnd)
            except OSError as e:
                return exit(0)
            finally:
                return True

    def logInfo(self, args=[]) -> None:
        pathTofile = f"{self.path}{time.time_ns()}-Info.log"
        if type(pathTofile) != None:
            try:
                with open(f"{pathTofile}", 'w')as file:
                    file.write(self.templateStart)
                    for i in range(len(args)):
                        file.write(f"{args[i]}\n")
                    file.write(self.templateEnd)
            except OSError as e:
                return exit(0)
            finally:
                return True

    def ChekFolderLog(self) -> None:
        if not os.path.exists(self.path):
            os.mkdir(self.path)
            return True
        return True


Logger().logFatal(['asd', 'asd'])
