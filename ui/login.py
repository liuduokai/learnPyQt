import sys

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor, QPixmap


class loginUi(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(loginUi, self).__init__(parent)
        self.init_ui()

    def init_ui(self):
        self.setFixedSize(400, 300)
        self.main_widget = QtWidgets.QWidget()
        self.main_layout = QtWidgets.QGridLayout()
        self.main_widget.setLayout(self.main_layout)

        self.button_widget = QtWidgets.QWidget()
        self.button_widget.setObjectName("button_widget")
        self.button_layout = QtWidgets.QGridLayout()
        self.button_widget.setLayout(self.button_layout)

        self.top_widget = QtWidgets.QWidget()
        self.top_widget.setObjectName("top_widget")
        self.top_layout = QtWidgets.QGridLayout()
        self.top_widget.setLayout(self.top_layout)

        self.down_widget = QtWidgets.QWidget()
        self.down_widget.setObjectName("down_widget")
        self.down_layout = QtWidgets.QGridLayout()
        self.down_widget.setLayout(self.down_layout)

        self.main_layout.addWidget(self.button_widget, 0, 0, 1, 1)
        self.main_layout.addWidget(self.top_widget, 1, 0, 6, 10)
        self.main_layout.addWidget(self.down_widget, 7, 0, 2, 10)
        self.setCentralWidget(self.main_widget)

        self.button_close = QtWidgets.QPushButton("")  # 关闭按钮
        self.button_mini = QtWidgets.QPushButton("")  # 最小化按钮

        self.button_layout.addWidget(self.button_close, 0, 0, 1, 1)
        self.button_layout.addWidget(self.button_mini, 0, 1, 1, 1)

        self.button_close.setFixedSize(15, 15)  # 设置关闭按钮的大小
        self.button_mini.setFixedSize(15, 15)  # 设置最小化按钮大小

        self.button_close.setStyleSheet(
            '''
            QPushButton{
                background:#F76677;
                border-radius:5px;
            }
            QPushButton:hover{
                background:red;
            }
            ''')
        self.button_mini.setStyleSheet(
            '''
            QPushButton{
                background:#6DDF6D;
                border-radius:5px;
            }
            QPushButton:hover{
                background:green;
            }
            ''')

        self.button_close.clicked.connect(self.close_window)
        self.button_mini.clicked.connect(self.mini_window)

        self.main_widget.setStyleSheet("""
            background-color:#ffffff;
            border-radius:20px;
        """)
        self.setWindowOpacity(1)  # 设置窗口透明度
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 设置窗口背景透明
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setWindowIcon(QtGui.QIcon('../assets/login.svg'))

        self.user_pic = QPixmap("../assets/user.svg")
        self.pwd_pic = QPixmap("../assets/pwd.svg")
        self.user_icon = QtWidgets.QLabel("用户名")
        self.pwd_icon = QtWidgets.QLabel("密码")
        self.user_icon.setFixedSize(30, 30)
        self.pwd_icon.setFixedSize(30, 30)
        self.user_icon.setScaledContents(True)
        self.pwd_icon.setScaledContents(True)

        self.user_input = QtWidgets.QLineEdit()
        self.pwd_input = QtWidgets.QLineEdit()
        self.user_input.setPlaceholderText("请输入用户名")
        self.pwd_input.setPlaceholderText("请输入密码")
        self.user_input.setStyleSheet(
            """
                border-style:solid;
                border-width:1px;
                border-radius:10px;
                height:40px;
            """
        )

        self.pwd_input.setStyleSheet(
            """
                border-style:solid;
                border-width:1px;
                border-radius:10px;
                height:40px;
            """
        )

        self.top_layout.addWidget(self.user_icon, 0, 0, 1, 2)
        self.top_layout.addWidget(self.pwd_icon, 2, 0, 1, 2)
        self.top_layout.addWidget(self.user_input, 0, 3, 1, 12)
        self.top_layout.addWidget(self.pwd_input, 2, 3, 1, 12)

        self.submit_button = QtWidgets.QPushButton('提交')
        self.cancel_button = QtWidgets.QPushButton('取消')

        self.submit_button.setStyleSheet(
            """
            QPushButton{
                background-color:#249ddd; 
                height:40px;
                width:20px; 
                border-radius:15px; 
            }
            QPushButton:hover{
                background-color:#1a73a2
            }      
            """
        )
        self.cancel_button.setStyleSheet(
            """
            QPushButton{
                background-color:#cacaca;
                height:40px;
                width:20px;
                border-radius:15px;    
            }
            QPushButton:hover{
                background-color:#a2a2a2
            }       
            """
        )
        self.submit_button.setFixedSize(120, 50)
        self.cancel_button.setFixedSize(120, 50)
        self.down_layout.addWidget(self.submit_button, 0, 0, 1, 1)
        self.down_layout.addWidget(self.cancel_button, 0, 1, 1, 1)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))  # 更改鼠标图标

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)  # 更改窗口位置
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False
        self.setCursor(QCursor(Qt.ArrowCursor))

    def close_window(self):
        self.close()

    def mini_window(self):
        self.showMinimized()


def main():
    app = QtWidgets.QApplication(sys.argv)
    gui = loginUi()
    gui.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
