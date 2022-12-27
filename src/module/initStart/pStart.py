import os
from pathlib import Path
import src.module.Config.config as config
from src.module.Database.dataBase import DataBase
import urllib.request
import urllib.error
import json
import time
import subprocess


class PStart:

    def __init__(self) -> None:
        self.main()

    def main(self):
        if self.validateFolder() and self.ChekConection():
            if self.validateData():
                print("[INFO] - все проверки успешно проейденны")
                return True

    def thUppdate(self):
        thr_name = "Uppdater"
        print(f"[{thr_name}] - начинаю обнавление бд")
        if self.ChekConection():
            if self.uppdateApiData():
                print(f"[{thr_name}] - Успешное обнавление")

    def validateData(self):
        DataBase()
        databaseData = None
        db = DataBase
        db.connect(db)
        databaseData = db.getAllValue(db).fetchall()

        if not databaseData:
            if self.setApiData():
                return True
        else:
            return True

    def connectToApi(self, APIKEY=config.getApiKey()):
        link = f"https://currate.ru/api/?get=rates&pairs=EURRUB,RUBEUR,USDRUB,RUBUSD&key={APIKEY}"

        try:
            exchange_rate = json.loads(
                urllib.request.urlopen(link).read().decode('utf-8'))
        except urllib.error as Error:
            return False  # Фатальная ошибка

        if exchange_rate['status'] != 200:
            return print({"Error": "Connection close!"})  # Пробрасывать ошибку

        return exchange_rate

    def setApiData(self):
        exchange_rate = self.connectToApi()

        RUBEUR = f"'RUBEUR', {exchange_rate['data']['RUBEUR']}"
        EURRUB = f"'EURRUB', {exchange_rate['data']['EURRUB']}"
        RUBUSD = f"'RUBUSD', {exchange_rate['data']['RUBUSD']}"
        USDRUB = f"'USDRUB', {exchange_rate['data']['USDRUB']}"

        db = DataBase
        db.connect(db)
        db.setValue(db, colums='"ename", "exchange"', cdata=f"{RUBEUR}")
        db.setValue(db, colums='"ename", "exchange"', cdata=f"{EURRUB}")
        db.setValue(db, colums='"ename", "exchange"', cdata=f"{RUBUSD}")
        db.setValue(db, colums='"ename", "exchange"', cdata=f"{USDRUB}")
        db.close(db)
        return True

    def uppdateApiData(self):
        exchange_rate = self.connectToApi()

        RUBEUR = exchange_rate['data']['RUBEUR']
        EURRUB = exchange_rate['data']['EURRUB']
        RUBUSD = exchange_rate['data']['RUBUSD']
        USDRUB = exchange_rate['data']['USDRUB']

        db = DataBase
        db.connect(db)
        db.uppdateValue(db, cdata=f"{RUBEUR}", colums='RUBEUR',)
        db.uppdateValue(db, cdata=f"{EURRUB}", colums='EURRUB',)
        db.uppdateValue(db, cdata=f"{RUBUSD}", colums='RUBUSD',)
        db.uppdateValue(db, cdata=f"{USDRUB}", colums='USDRUB',)
        db.close(db)

        return True

    def validateFolder(self):
        mainDir = str(Path.home())+'\\documents\\test\\'
        if not (os.path.exists(mainDir) and os.path.exists(mainDir+'Log')):
            try:
                os.makedirs(mainDir+'Log')
                return True
            except OSError as error:
                return False  # looger
        else:
            return True

    def ChekConection(self):
        CInternet = self.Ping()
        if not CInternet:
            while not CInternet:
                if CInternet:
                    break
                else:
                    time.sleep(5)
                    CInternet = self.Ping()
        else:
            return True

    def Ping(self):
        while True:
            try:
                subprocess.check_output(["ping", "www.ya.ru"])
                return True
            except subprocess.SubprocessError:
                return False
