# Form implementation generated from reading ui file 'addEditCoffeeForm.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow2(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(528, 579)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.taste = QtWidgets.QPlainTextEdit(parent=self.centralwidget)
        self.taste.setGeometry(QtCore.QRect(160, 180, 341, 141))
        self.taste.setObjectName("taste")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 20, 21, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 60, 91, 21))
        self.label_2.setObjectName("label_2")
        self.name_sort = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.name_sort.setGeometry(QtCore.QRect(160, 60, 341, 20))
        self.name_sort.setObjectName("name_sort")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 100, 101, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(100, 140, 51, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(60, 180, 91, 21))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(120, 340, 31, 21))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 380, 151, 21))
        self.label_7.setObjectName("label_7")
        self.degree_of_roasting = QtWidgets.QComboBox(parent=self.centralwidget)
        self.degree_of_roasting.setGeometry(QtCore.QRect(160, 100, 341, 22))
        self.degree_of_roasting.setObjectName("degree_of_roasting")
        self.crushing = QtWidgets.QComboBox(parent=self.centralwidget)
        self.crushing.setGeometry(QtCore.QRect(160, 140, 341, 22))
        self.crushing.setObjectName("crushing")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(110, 450, 311, 51))
        self.pushButton.setObjectName("pushButton")
        self.volume = QtWidgets.QSpinBox(parent=self.centralwidget)
        self.volume.setGeometry(QtCore.QRect(160, 380, 341, 22))
        self.volume.setMinimum(1)
        self.volume.setMaximum(10000)
        self.volume.setObjectName("volume")
        self.id = QtWidgets.QSpinBox(parent=self.centralwidget)
        self.id.setGeometry(QtCore.QRect(160, 20, 341, 22))
        self.id.setMinimum(1)
        self.id.setObjectName("id")
        self.cost = QtWidgets.QSpinBox(parent=self.centralwidget)
        self.cost.setGeometry(QtCore.QRect(160, 340, 341, 22))
        self.cost.setMinimum(1)
        self.cost.setMaximum(10000)
        self.cost.setSingleStep(1)
        self.cost.setObjectName("cost")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 528, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Редактирование"))
        self.label.setText(_translate("MainWindow", "ID:"))
        self.label_2.setText(_translate("MainWindow", "название сорта:"))
        self.label_3.setText(_translate("MainWindow", "степень обжарки:"))
        self.label_4.setText(_translate("MainWindow", "помолка:"))
        self.label_5.setText(_translate("MainWindow", "описание вкуса:"))
        self.label_6.setText(_translate("MainWindow", "цена:"))
        self.label_7.setText(_translate("MainWindow", "объем упаковки (в литрах):"))
        self.pushButton.setText(_translate("MainWindow", "Применить"))