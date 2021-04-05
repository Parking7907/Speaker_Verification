import sys
from PyQt5.QtCore import QSize, QCoreApplication, Qt, QBasicTimer
from PyQt5.QtGui import QImage, QPalette, QBrush, QPixmap,  QIcon, QMovie
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import (QApplication, QWidget, QLCDNumber, QDial, QPushButton, QVBoxLayout, QHBoxLayout, QDesktopWidget, QLabel, QProgressBar)
from scipy.io.wavfile import write
#from GUI import MyApp
import pdb
#import pyaudio
import sounddevice as sd
from time import sleep
#from GUI3 import reshowGUI3
import subprocess
class myGUI4(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        QWidget.__init__(self)
        self.setGeometry(100,100,900,600)
        self.setWindowTitle('IIPHIS')
        self.setWindowIcon(QIcon('Icon.png'))
        
        #background
        oImage = QImage("success.jpg")
        sImage = oImage.scaled(QSize(1920,1080))                   # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))                
        self.setPalette(palette)

        #image insert
        #pixmap = QPixmap('Hi IIPHIS.PNG')
        #pixmap2 = pixmap.scaled(800,440)
        #lbl_img = QLabel()
        #lbl_img.setPixmap(pixmap2)
        #lbl_img.setAlignment(Qt.AlignCenter)
        ##########################
        #hbox = QHBoxLayout()
        #hbox.addWidget(lbl_img)
        #vbox = QVBoxLayout()
        #vbox.addLayout(hbox) #image or two button
        #self.setLayout(vbox)

        #Label for Script
        #label1 = QLabel('SUCCESS!', self)
        #label1.setStyleSheet("font-size:300px;")
        #label1.resize(1500, 800)
        #label1.move(300, 300)

        #Go back to GUI
        btn2 = QPushButton('Revalidation', self)
        btn2.setStyleSheet("font-size:60px;" "font: bold italic large;")
        btn2.resize(440,60)
        btn2.move(760, 900)
        btn2.clicked.connect(self.run_py)

        self.resize(1920, 1080)
        self.center() 
        self.show()
        
        #button = QPushButton('run_GUI', self)# print output on command
        #button.move(10,30)

        #button.clicked.connect(self.run_py)
        #self.show()
    def center(self): 
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    #def showGUI(self):
        #self.hide()
        #self.child5_win = MyApp()
        #self.child5_win.show()
        
    def run_py(self):
       self.hide()
       #command = ('python GUI3.py') 
       #output = subprocess.call(command, shell=True, stdout=None)
       
# Don't touch me
if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex =myGUI4()
   sys.exit(app.exec_())