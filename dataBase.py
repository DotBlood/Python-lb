import sqlite3
import json


class DataBase:
    conn = None

    def __init__(self) -> None:
        self.connect()
        self.chekpoint()
        self.close()

    def connect(self):
        try:
            self.conn = sqlite3.connect('data.db')
        except sqlite3.Error as error:
            print("Ошибка при работе с SQLite", error)
            exit(0)

    def close(self):
        try:
            if self.conn:
                self.conn.close()
        except sqlite3.Error as error:
            print("Ошибка при работе с SQLite", error)
            exit(0)

    def chekpoint(self):
        if not self.conn:
            self.connect()
        try:
            cur = self.conn.cursor()
            cur.execute(
                """CREATE TABLE IF NOT EXISTS exchanges ("ename" VARCHAR(20) NOT NULL UNIQUE, "exchange" FLOAT NOT NULL)""")
            self.conn.commit()
            return True
        except sqlite3.Error as error:
            print("Ошибка при работе с SQLite", error)
            exit(0)

    def setValue(self, colums, cdata):
        if not self.conn:
            self.connect()
        try:
            cur = self.conn.cursor()
            sql = f"INSERT INTO exchanges ({colums}) VALUES ({cdata})"
            cur.execute(sql)
            self.conn.commit()
        except sqlite3.Error as error:
            print("Ошибка при работе с SQLite", error)
            exit(0)

    def uppdateValue(self, colums, cdata):
        if not self.conn:
            self.connect()

        try:
            cur = self.conn.cursor()
            sql = f'UPDATE exchanges SET exchange={cdata} WHERE ename="{colums}"'
            print(sql)
            cur.execute(sql)
            self.conn.commit()
        except sqlite3.Error as error:
            print("Ошибка при работе с SQLite", error)
            exit(0)

    def getValue(self, index, ename):
        if not self.conn:
            self.connect()
        try:
            cur = self.conn.cursor()
            return cur.execute(f'SELECT {index} FROM exchanges WHEAR "ename={ename}"')
        except sqlite3.Error as error:
            print("Ошибка при работе с SQLite", error)
            exit(0)

    def getAllValue(self):
        if not self.conn:
            self.connect()

        try:
            cur = self.conn.cursor()
            data = cur.execute(f"""SELECT * FROM exchanges""")
            return data
        except sqlite3.Error as error:
            print("Ошибка при работе с SQLite", error)
            exit(0)
