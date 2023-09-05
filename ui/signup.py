from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Signup(object):
    def setupUi(self, Signup):
        Signup.setObjectName("Signup")
        Signup.resize(720, 580)
        Signup.setMinimumSize(QtCore.QSize(720, 580))
        Signup.setMaximumSize(QtCore.QSize(720, 580))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../img/lock.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Signup.setWindowIcon(icon)
        Signup.setStyleSheet("#centralwidget{\n"
"background-color: #1a1a1a;\n"
"}")
        Signup.setIconSize(QtCore.QSize(16, 16))
        self.centralwidget = QtWidgets.QWidget(Signup)
        self.centralwidget.setObjectName("centralwidget")
        self.password = QtWidgets.QLineEdit(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(191, 399, 440, 32))
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
        self.label_2.setGeometry(QtCore.QRect(91, 343, 87, 21))
        font = QtGui.QFont()
        font.setFamily("Source Code Pro")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: white;")
        self.label_2.setObjectName("label_2")
        self.username = QtWidgets.QLineEdit(self.centralwidget)
        self.username.setGeometry(QtCore.QRect(191, 338, 440, 32))
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
        self.firstName = QtWidgets.QLineEdit(self.centralwidget)
        self.firstName.setGeometry(QtCore.QRect(192, 157, 440, 32))
        font = QtGui.QFont()
        font.setFamily("Source Code Pro")
        font.setPointSize(12)
        self.firstName.setFont(font)
        self.firstName.setStyleSheet("background-color: white;\n"
"color: black;\n"
"border: 0.5px solid black;\n"
"border-radius: 5px;")
        self.firstName.setMaxLength(20)
        self.firstName.setObjectName("firstName")
        self.lastName = QtWidgets.QLineEdit(self.centralwidget)
        self.lastName.setGeometry(QtCore.QRect(193, 218, 440, 32))
        font = QtGui.QFont()
        font.setFamily("Source Code Pro")
        font.setPointSize(12)
        self.lastName.setFont(font)
        self.lastName.setStyleSheet("background-color: white;\n"
"color: black;\n"
"border: 0.5px solid black;\n"
"border-radius: 5px;")
        self.lastName.setMaxLength(20)
        self.lastName.setObjectName("lastName")
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
        self.label_3.setGeometry(QtCore.QRect(90, 404, 87, 21))
        font = QtGui.QFont()
        font.setFamily("Source Code Pro")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: white;")
        self.label_3.setObjectName("label_3")
        self.email = QtWidgets.QLineEdit(self.centralwidget)
        self.email.setGeometry(QtCore.QRect(191, 277, 440, 32))
        font = QtGui.QFont()
        font.setFamily("Source Code Pro")
        font.setPointSize(12)
        self.email.setFont(font)
        self.email.setStyleSheet("background-color: white;\n"
"color: black;\n"
"border: 0.5px solid black;\n"
"border-radius: 5px;")
        self.email.setMaxLength(128)
        self.email.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.email.setObjectName("email")
        self.signupBtn = QtWidgets.QPushButton(self.centralwidget)
        self.signupBtn.setGeometry(QtCore.QRect(197, 491, 350, 60))
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
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(76, 161, 106, 21))
        font = QtGui.QFont()
        font.setFamily("Source Code Pro")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: white;")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(85, 223, 96, 21))
        font = QtGui.QFont()
        font.setFamily("Source Code Pro")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: white;")
        self.label_5.setObjectName("label_5")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(121, 282, 58, 21))
        font = QtGui.QFont()
        font.setFamily("Source Code Pro")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("color: white;")
        self.label.setObjectName("label")
        Signup.setCentralWidget(self.centralwidget)

        self.retranslateUi(Signup)
        QtCore.QMetaObject.connectSlotsByName(Signup)

    def retranslateUi(self, Signup):
        _translate = QtCore.QCoreApplication.translate
        Signup.setWindowTitle(_translate("Signup", "Sign up"))
        self.label_2.setText(_translate("Signup", "Username:"))
        self.label_6.setText(_translate("Signup", "Sign up"))
        self.label_3.setText(_translate("Signup", "Password:"))
        self.signupBtn.setText(_translate("Signup", "Sign up"))
        self.label_4.setText(_translate("Signup", "First Name:"))
        self.label_5.setText(_translate("Signup", "Last Name:"))
        self.label.setText(_translate("Signup", "Email:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Signup = QtWidgets.QMainWindow()
    ui = Ui_Signup()
    ui.setupUi(Signup)
    Signup.show()
    sys.exit(app.exec_())
