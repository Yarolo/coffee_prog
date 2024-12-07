import sqlite3
import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem


class Coffee_viewing(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.connection = sqlite3.connect("coffee.sqlite")
        self.make_table()
        self.pushButton.clicked.connect(self.open_2form)

    def make_table(self):
        res = self.connection.cursor().execute('''select coffee.id, coffee.name_sort, degree_of_roasting.name, 
        crushing.name, coffee.taste, coffee.cost, coffee.volume
        from coffee
        join degree_of_roasting on degree_of_roasting.id = coffee.degree_of_roasting
        join crushing on crushing.id = coffee.crushing
        ''').fetchall()
        self.tableWidget.clear()
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

    def open_2form(self):
        self.f = AddEditCoffeeForm(self)
        self.f.show()


class AddEditCoffeeForm(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi('addEditCoffeeForm.ui', self)
        self.con = sqlite3.connect("coffee.sqlite")
        self.pushButton.clicked.connect(self.srav)
        res = self.con.cursor().execute('SELECT * FROM degree_of_roasting').fetchall()
        self.params1 = {}
        self.params2 = {}
        for i in res:
            self.params1[i[1]] = str(i[0])
        self.degree_of_roasting.addItems(self.params1.keys())
        res = self.con.cursor().execute('SELECT * FROM crushing').fetchall()
        for i in res:
            self.params2[i[1]] = str(i[0])
        self.crushing.addItems(self.params2.keys())

    def srav(self):
        try:
            m = []
            m.append(self.name_sort.text())
            m.append(self.params1[self.degree_of_roasting.currentText()])
            m.append(self.params2[self.crushing.currentText()])
            m.append(self.taste.toPlainText())
            m.append(self.cost.text())
            m.append(self.volume.text())
            m.append(self.id.text())
            if not (self.name_sort.text()):
                raise Exception
            if not (self.taste.toPlainText()):
                raise Exception
            if int(self.id.text()) in [i[0] for i in self.con.cursor().execute('''select id from coffee''').fetchall()]:
                self.con.cursor().execute('''DELETE from coffee where id = ?''', (m[-1],))
                self.con.commit()
            self.con.cursor().execute('''insert into coffee
                        (name_sort, degree_of_roasting, crushing, taste, cost, volume, id)
                        VALUES(?,?,?,?,?,?,?)''', (*m,))
            self.con.commit()
            self.parent().make_table()
            self.close()
        except Exception:
            self.statusBar().showMessage('Некорректный ввод')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Coffee_viewing()
    ex.show()
    sys.exit(app.exec())
