import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication, QDesktopWidget
import cv2
'''
功能：
    1.连接相机
    2.定位试管
    3.抓取，震荡
'''


class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.timer_camera = QtCore.QTimer()
        self.cap = cv2.VideoCapture()
        self.initUI()

    def initUI(self):
        self.resize(1200, 800)
        self.center()

        btn1 = QPushButton("链接相机", self)
        btn1.move(30, 50)

        btn2 = QPushButton("定位试管", self)
        btn2.move(150, 50)

        btn3 = QPushButton("抓取震荡", self)
        btn3.move(270, 50)

        btn1.clicked.connect(self.connect_cammera)
        btn2.clicked.connect(self.detect_tube)
        btn3.clicked.connect(self.shake)

        self.statusBar()
        self.setWindowTitle('智能检测')
        self.show()

    def connect_cammera(self):
        pass

    def detect_tube(self):
        pass

    def shake(self):


        pass



    def center(self):
        # 获得窗口
        qr = self.frameGeometry()
        # 获得屏幕中心点
        cp = QDesktopWidget().availableGeometry().center()
        # 显示到屏幕中心
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
