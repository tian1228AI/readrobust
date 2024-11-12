# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import image_rc
import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.main_window = MainWindow  # 存储MainWindow的引用
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(797, 595)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("""
                QMainWindow {
                    background-image: url(:/ziyuan/back01.png);
                    background-repeat: no-repeat;
                    background-position: center;
                }
                """)  # 移除了background-size
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(160, 110, 121, 41))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 110, 81, 51))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(380, 130, 72, 15))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(480, 110, 121, 41))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 190, 91, 71))
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(160, 200, 121, 41))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(380, 220, 72, 15))
        self.label_4.setObjectName("label_4")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(480, 200, 121, 41))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(50, 320, 72, 15))
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(590, 360, 171, 71))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(592, 447, 171, 71))
        self.pushButton_2.setObjectName("pushButton_2")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(170, 310, 101, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(50, 430, 72, 15))
        self.label_6.setObjectName("label_6")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(170, 420, 101, 31))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 797, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton_2.clicked.connect(self.close_application)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "书名"))
        self.label_2.setText(_translate("MainWindow", "起始页数"))
        self.label_3.setText(_translate("MainWindow", "结束页数"))
        self.label_4.setText(_translate("MainWindow", "总页数"))
        self.label_5.setText(_translate("MainWindow", "书的大小"))
        self.pushButton.setText(_translate("MainWindow", "进入"))
        self.pushButton_2.setText(_translate("MainWindow", "退出"))
        self.comboBox.setItemText(0, _translate("MainWindow", "16k"))
        self.comboBox.setItemText(1, _translate("MainWindow", "32k"))
        self.comboBox.setItemText(2, _translate("MainWindow", "1M"))
        self.comboBox.setItemText(3, _translate("MainWindow", "2M"))
        self.label_6.setText(_translate("MainWindow", "串口号"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "COM5"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "COM7"))


    def close_application(self):
        QtWidgets.QApplication.quit()

    def show_main_window(self):
        self.main_window.show()  # 重新显示主窗口
def main():
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(main_window)
    main_window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()