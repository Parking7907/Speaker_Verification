import sys
from PyQt5.QtCore import QSize, QCoreApplication, Qt, QBasicTimer
from PyQt5.QtGui import QImage, QPalette, QBrush, QPixmap,  QIcon, QMovie
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import (QApplication, QWidget, QLCDNumber, QDial, QPushButton, QVBoxLayout, QHBoxLayout, QDesktopWidget, QLabel, QProgressBar)
from scipy.io.wavfile import write
from GUI2 import myGUI2
import pdb
#import pyaudio
import sounddevice as sd
from time import sleep

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        QWidget.__init__(self)
        self.setGeometry(100,100,900,600)
        self.setWindowTitle('IIPHIS')
        self.setWindowIcon(QIcon('Icon.png'))
        
        #background
        oImage = QImage("background3.png")
        sImage = oImage.scaled(QSize(1920,1080))                   # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))                
        self.setPalette(palette)

        #Title Label
        label1 = QLabel('Speaker Authentication system', self)
        label1.setStyleSheet("color:#2ECCFA;" "font-size:90px;" "font: bold italic large")
        #label1.resize(600, 60) #jinyeong fit
        #label1.move(720, 65)
        label1.resize(1600,120) #wonsuk fit
        label1.move(150, 50)

        #Go to GUI2
        btn1 = QPushButton('User registration', self)
        btn1.setStyleSheet("color:white;" "font-size:35px;" "background-image:url(background3_button.png);" "font: bold italic large;")
        #btn1.resize(250,40) #jinyeong fit
        #btn1.move(860,920)
        btn1.resize(350,60) #wonsuk fit
        btn1.move(800,875)
        btn1.clicked.connect(self.showGUI2)

        ########################## 
        self.resize(1920, 1080)
        self.center() 
        self.show()

    def center(self): 
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def showGUI2(self):
        self.hide()
        self.child_win = myGUI2()
        self.child_win.show()

# Don't touch me
if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MyApp()
   sys.exit(app.exec_())
