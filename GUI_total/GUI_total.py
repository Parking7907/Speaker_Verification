import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLCDNumber, QDial, QPushButton, QVBoxLayout, QHBoxLayout, QDesktopWidget, QLabel)
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QCoreApplication, Qt
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
        self.setWindowTitle('IIPHIS')
        self.setWindowIcon(QIcon('Icon.png'))

        #Title Label
        label1 = QLabel('Speaker Authentication system', self)
        label1.setStyleSheet("font-size:40px;")
        #label1.resize(600, 60) #jinyeong fit
        #label1.move(720, 65)
        label1.resize(450, 40) #wonsuk fit
        label1.move(450, 20)

        #image insert
        pixmap = QPixmap('sound-856770.png')
        #pixmap2 = pixmap.scaled(1890,660) #jinyeong fit
        pixmap2 = pixmap.scaled(1260,440) #wonsuk fit
        lbl_img = QLabel()
        lbl_img.setPixmap(pixmap2)
        vbox = QVBoxLayout()
        vbox.addWidget(lbl_img)
        self.setLayout(vbox)

        #Exit
        btn = QPushButton('X', self)
        btn.setStyleSheet("font-size:25px;")
        #btn.resize(40, 40) #jinyeong fit
        #btn.move(1860, 10) 
        btn.resize(30, 30) #wonsuk fit
        btn.move(1240, 10)
        btn.clicked.connect(QCoreApplication.instance().quit)

        #Go to GUI2
        btn1 = QPushButton('User registration', self)
        btn1.setStyleSheet("font-size:25px;")
        #btn1.resize(250,40) #jinyeong fit
        #btn1.move(860,920)
        btn1.resize(200,40) #wonsuk fit
        btn1.move(560,600)
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

    def recordaudio(self):
        fs = 16000
        seconds = 1.6
        sleep(0.1)
        myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
        sd.wait()
        for i in range(5):
            #write('Z:/github/myway/Verification_test_audio_%d.wav'%i, fs, myrecording)
            write('./Verification_test_audio_%d.wav'%i, fs, myrecording)



# Don't touch me
if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MyApp()
   sys.exit(app.exec_())
