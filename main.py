import sys

from PyQt6.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QHeaderView
from PyQt6 import uic

import sqlite3


class Coffee(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)

        self.initUI()

    def initUI(self):
        self.search.editingFinished.connect(self.searching)

        con = sqlite3.connect('coffee.sqlite')
        cur = con.cursor()
        result = cur.execute("""
        SELECT id, (
            SELECT name FROM varieties
            WHERE id = varietie
            ), (
            SELECT name FROM roasted
            WHERE id = roasted
            ), mill, description, price, volume FROM coffee""").fetchall()

        title = ['ID', 'Название сорта', 'Степень обжарки', 'Молотый', 'Описание вкуса', 'Цена', 'Объём упаковки']

        self.tableWidget.setColumnCount(len(title))
        self.tableWidget.setHorizontalHeaderLabels(title)
        self.tableWidget.setRowCount(0)
        for i, row in enumerate(result):
            self.tableWidget.setRowCount(i + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(i, j, QTableWidgetItem(elem))

        self.tableWidget.resizeColumnsToContents()

    def searching(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    coffee = Coffee()
    coffee.show()
    sys.exit(app.exec())