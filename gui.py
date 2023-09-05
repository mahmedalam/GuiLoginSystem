from ui.ui import Ui_MainWindow
from ui.login import Ui_Login
from ui.signup import Ui_Signup
from client import Client
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5 import QtGui
import sys


class Gui(QMainWindow):
    def __init__(self):
        super().__init__()

        self.UI = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.UI)
        self.UI.show()

        self.LOGIN = QMainWindow()
        self.loginUi = Ui_Login()
        self.loginUi.setupUi(self.LOGIN)

        self.SIGNUP = QMainWindow()
        self.signupUi = Ui_Signup()
        self.signupUi.setupUi(self.SIGNUP)

        self.ui.loginBtn.clicked.connect(lambda: self.LOGIN.show())
        self.ui.signupBtn.clicked.connect(lambda: self.SIGNUP.show())

        self.signupUi.signupBtn.clicked.connect(lambda: self.signupHandler())
        self.loginUi.loginBtn.clicked.connect(lambda: self.loginHandler())

    def signupHandler(self):
        self.signupUi.signupBtn.setEnabled(False)
        firstName = self.signupUi.firstName.text()
        lastName = self.signupUi.lastName.text()
        email = self.signupUi.email.text()
        username = self.signupUi.username.text()
        password = self.signupUi.password.text()

        self.signup = signup(firstName, lastName, email, username, password)
        self.signup.finished.connect(lambda: self.signupFinished())
        self.signup.start()

    def signupFinished(self):
        self.message(self.signup.msg, self.signup.color)
        self.signupUi.signupBtn.setEnabled(True)

    def loginHandler(self):
        self.loginUi.loginBtn.setEnabled(False)
        username = self.loginUi.username.text()
        password = self.loginUi.password.text()

        self.login = login(username, password)
        self.login.finished.connect(lambda: self.loginFinished())
        self.login.start()

    def loginFinished(self):
        self.message(self.login.msg, self.login.color)
        self.loginUi.loginBtn.setEnabled(True)

    def message(self, msg, color):
        self.msg = QMessageBox()
        self.msg.setWindowTitle(msg)
        self.msg.setText(msg)
        self.msg.setStyleSheet(f"color: {color}; padding: 10px 30px 10px 20px;")

        font = QtGui.QFont()
        font.setFamily("Source Code Pro")
        font.setPointSize(20)
        self.msg.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/lock.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)

        self.msg.show()
        self.msg.exec_()


class signup(QThread, Client):
    finished = pyqtSignal()

    def __init__(self, firstName, lastName, email, username, password):
        super().__init__()
        try:
            self.client()
            self.msg = ""
        except:
            self.msg = "Server Connection Failed"
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.username = username
        self.password = password

    def run(self):
        if self.msg == "":
            self.signup(self.firstName, self.lastName, self.email, self.username, self.password)
            if self.signupMsg == b"Signup Successful":
                self.msg = "Signup Successful"
            else:
                self.msg = "Username Already Taken!"

        if self.msg == "Signup Successful":
            self.color = "#00ff1c"
        else:
            self.color = "red"

        self.finished.emit()


class login(QThread, Client):
    finished = pyqtSignal()

    def __init__(self, username, password):
        super().__init__()
        try:
            self.client()
            self.msg = ""
        except:
            self.msg = "Server Connection Failed"
        self.username = username
        self.password = password

    def run(self):
        if self.msg == "":
            self.login(self.username, self.password)
            if self.loginMsg == b"Login Successful":
                self.msg = "Login Successful"
            else:
                self.msg = "Login Failed!"

        if self.msg == "Login Successful":
            self.color = "#00ff1c"
        else:
            self.color = "red"

        self.finished.emit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Gui()
    sys.exit(app.exec_())
