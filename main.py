import sqlite3
import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem


class DBSample(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.connection = sqlite3.connect("coffee.sqlite")
        self.select_data()

    def select_data(self):

        res = self.connection.cursor().execute('''select coffee.id, coffee.name_sort, degree_of_roasting.name, 
        crushing.name, coffee.taste, coffee.cost, coffee.volume
        from coffee
        join degree_of_roasting on degree_of_roasting.id = coffee.degree_of_roasting
        join crushing on crushing.id = coffee.crushing
        ''').fetchall()

        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setHorizontalHeaderLabels(
            ['ID', 'название сорта', 'степень обжарки', 'помолка', 'описание вкуса', 'цена',
             'объем упаковки (в литрах)'])

        for i, row in enumerate(res):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(str(elem)))

    def closeEvent(self, event):
        self.connection.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DBSample()
    ex.show()
    sys.exit(app.exec())
