import sys
from chat_cli import ChatClient
import sys
import logging
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

cc = None

class LoginView(QWidget):

    def __init__(self, parent=None):
        super(LoginView, self).__init__(parent)
        self.view = parent
        self.initUI()
        
    def initUI(self):
        self.titleLabel = QLabel("Login", self)
        self.titleLabel.setFont(QFont("Arial", 28))
        self.titleLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # self.setStyleSheet("QLabel {background-color:red;}")
        self.titleLabel.move(300-int(self.titleLabel.width()/2), 100)

        userlabel = QLabel("Username", self)
        userlabel.setFont(QFont("Arial", 14))
        userlabel.move(300-int(userlabel.width()/2)-60, 200)

        passlabel = QLabel("Password", self)
        passlabel.setFont(QFont("Arial", 14))
        passlabel.move(300-int(passlabel.width()/2)-60, 250)

        # Create textbox
        self.userbox = QLineEdit(self)
        self.userbox.setFont(QFont("Arial", 14))
        self.userbox.resize(150,30)
        self.userbox.move(300-int(self.userbox.width()/2)+60, 200)

        # Create textbox
        self.passbox = QLineEdit(self)
        self.passbox.setFont(QFont("Arial", 14))
        self.passbox.resize(150,30)
        self.passbox.move(300-int(self.passbox.width()/2)+60, 250)

        # Create a button in the window
        self.button = QPushButton('Login', self)
        self.button.setFont(QFont("Arial", 20))
        self.button.resize(100,50)
        self.button.move(300-int(self.button.width()/2), 330)

        
        # # connect button to function on_click
        self.button.clicked.connect(self.login)

    def login(self):
        username = self.userbox.text()
        password = self.passbox.text()
        self.userbox.setText("")
        self.passbox.setText("")
        global cc
        response = cc.proses(f'auth {username} {password}')
        if(response['status'] == 'ERROR'):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Login failed")
            msg.setInformativeText(response['message'])
            msg.setWindowTitle("Login Failed")
            msg.exec_()
        else :
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Login Successful")
            msg.setWindowTitle("Login Successful")
            msg.exec_()
            self.view.showChatView()


class ChatView(QWidget):

    def __init__(self, parent=None):
        super(ChatView, self).__init__(parent)
        self.view = parent
        self.initUI()
        
    def initUI(self):
        self.titleLabel = QLabel("Chat", self)
        self.titleLabel.setFont(QFont("Arial", 28))
        self.titleLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # self.setStyleSheet("QLabel {background-color:red;}")
        self.titleLabel.move(300-int(self.titleLabel.width()/2), 100)


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setWindowTitle("Chat Client")
        self.setGeometry(0, 0, 600, 500)
        self.setFixedSize(600, 500)
        self.setContentsMargins(-10,-10,-10,-10)
        
        self.LoginView = LoginView(self)
        self.ChatView = ChatView(self)
        
        self.showLoginView()
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("No server found")
        msg.setInformativeText("Closing program")
        msg.setWindowTitle("Error")
        global cc
        try:
            cc = ChatClient()
        except ConnectionError:
            msg.exec_()
            exit()

    def showLoginView(self):
        self.setCentralWidget(self.LoginView)
        self.show()

    def showChatView(self):
        self.setCentralWidget(self.ChatView)
        self.show()

if __name__=="__main__":
    app = QApplication(sys.argv)
    ex = MainWindow()        
    sys.exit(app.exec_())
    

