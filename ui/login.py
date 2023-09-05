from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(720, 450)
        Login.setMinimumSize(QtCore.QSize(720, 450))
        Login.setMaximumSize(QtCore.QSize(720, 450))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../img/lock.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Login.setWindowIcon(icon)
        Login.setStyleSheet("#centralwidget{\n"
"background-color: #1a1a1a;\n"
"}")
        Login.setIconSize(QtCore.QSize(16, 16))
        self.centralwidget = QtWidgets.QWidget(Login)
        self.centralwidget.setObjectName("centralwidget")
        self.password = QtWidgets.QLineEdit(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(191, 235, 440, 32))
        font = QtGui.QFont()
        font.setFamily("Source Code Pro")
        font.setPointSize(12)
        self.password.setFont(font)
        self.password.setStyleSheet("background-color: white;\n"
"color: black;\n"
"border: 0.5px solid black;\n"
"border-radius: 5px;")
        self.password.setMaxLength(20)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(91, 179, 87, 21))
        font = QtGui.QFont()
        font.setFamily("Source Code Pro")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: white;")
        self.label_2.setObjectName("label_2")
        self.username = QtWidgets.QLineEdit(self.centralwidget)
        self.username.setGeometry(QtCore.QRect(191, 174, 440, 32))
        font = QtGui.QFont()
        font.setFamily("Source Code Pro")
        font.setPointSize(12)
        self.username.setFont(font)
        self.username.setStyleSheet("background-color: white;\n"
"color: black;\n"
"border: 0.5px solid black;\n"
"border-radius: 5px;")
        self.username.setMaxLength(20)
        self.username.setObjectName("username")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(0, 0, 720, 100))
        font = QtGui.QFont()
        font.setFamily("Source Code Pro")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgba(0, 255, 234, 255), stop:0.5 rgba(90, 214, 255, 255), stop:1 rgba(0, 255, 237, 255));\n"
"color: black;")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(90, 240, 87, 21))
        font = QtGui.QFont()
        font.setFamily("Source Code Pro")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: white;")
        self.label_3.setObjectName("label_3")
        self.loginBtn = QtWidgets.QPushButton(self.centralwidget)
        self.loginBtn.setGeometry(QtCore.QRect(197, 340, 350, 60))
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
        Login.setCentralWidget(self.centralwidget)

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Login"))
        self.label_2.setText(_translate("Login", "Username:"))
        self.label_6.setText(_translate("Login", "Login"))
        self.label_3.setText(_translate("Login", "Password:"))
        self.loginBtn.setText(_translate("Login", "Login"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Login = QtWidgets.QMainWindow()
    ui = Ui_Login()
    ui.setupUi(Login)
    Login.show()
    sys.exit(app.exec_())
