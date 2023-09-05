from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/lock.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("#centralwidget{\n"
"background-color: #1a1a1a;\n"
"}")
        MainWindow.setIconSize(QtCore.QSize(16, 16))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.header = QtWidgets.QWidget(self.centralwidget)
        self.header.setMaximumSize(QtCore.QSize(16777215, 100))
        self.header.setObjectName("header")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.header)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.header)
        self.label.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setFamily("Source Code Pro")
        font.setPointSize(25)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgba(0, 255, 234, 255), stop:0.5 rgba(90, 214, 255, 255), stop:1 rgba(0, 255, 237, 255));\n"
"color: black;")
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.verticalLayout.addWidget(self.header)
        self.center = QtWidgets.QWidget(self.centralwidget)
        self.center.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.center.setObjectName("center")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.center)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.center)
        self.label_2.setMinimumSize(QtCore.QSize(256, 256))
        self.label_2.setMaximumSize(QtCore.QSize(256, 256))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("img/lock.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.verticalLayout.addWidget(self.center)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setMinimumSize(QtCore.QSize(775, 0))
        self.widget.setMaximumSize(QtCore.QSize(16777215, 150))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(30, 0, 30, 30)
        self.horizontalLayout.setSpacing(30)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.loginBtn = QtWidgets.QPushButton(self.widget)
        self.loginBtn.setMinimumSize(QtCore.QSize(350, 60))
        self.loginBtn.setMaximumSize(QtCore.QSize(350, 60))
        font = QtGui.QFont()
        font.setFamily("Source Code Pro")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.loginBtn.setFont(font)
        self.loginBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.loginBtn.setStyleSheet("QPushButton{\n"
"background-color: #00e31a;\n"
"color: black;\n"
"border: 5px solid green;\n"
"border-radius: 30px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #00ff1c;\n"
"}")
        self.loginBtn.setObjectName("loginBtn")
        self.horizontalLayout.addWidget(self.loginBtn)
        self.signupBtn = QtWidgets.QPushButton(self.widget)
        self.signupBtn.setMinimumSize(QtCore.QSize(350, 60))
        self.signupBtn.setMaximumSize(QtCore.QSize(350, 60))
        font = QtGui.QFont()
        font.setFamily("Source Code Pro")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.signupBtn.setFont(font)
        self.signupBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.signupBtn.setStyleSheet("QPushButton{\n"
"background-color: #00e31a;\n"
"color: black;\n"
"border: 5px solid green;\n"
"border-radius: 30px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #00ff1c;\n"
"}")
        self.signupBtn.setObjectName("signupBtn")
        self.horizontalLayout.addWidget(self.signupBtn)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addWidget(self.widget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Gui Login System"))
        self.label.setText(_translate("MainWindow", "Gui Login System"))
        self.loginBtn.setText(_translate("MainWindow", "Login"))
        self.signupBtn.setText(_translate("MainWindow", "Sign up"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
