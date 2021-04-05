import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLCDNumber, QDial, QPushButton, QVBoxLayout, QHBoxLayout, QDesktopWidget, QLabel, QProgressBar)
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QImage, QPalette, QBrush, QIcon, QPixmap
from PyQt5.QtCore import QCoreApplication, Qt, QBasicTimer, QSize
from scipy.io.wavfile import write
from GUI3 import myGUI3
from enrollment_data_preprocess import save_spectrogram_tisv
import pdb
import os
#import pyaudio as pa
import librosa
import sounddevice as sd
import soundfile as sf
from playsound import playsound #download this
import numpy as np
from time import sleep

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('IIPHIS')
        self.setWindowIcon(QIcon('Icon.png'))
        
        #background
        #oImage = QImage('background.png')
        #sImage = oImage.scaled(QSize(1260, 800)
        #palette = QPalette()
        #palette.setBruch(QPalette.Window, QBrush(sImage))
        #self.setPalette(palette)
        
        #image insert
        pixmap = QPixmap('script.PNG')
        #pixmap2 = pixmap.scaled(1200,660) #JY
        pixmap2 = pixmap.scaled(600,330) #WS
        lbl_img = QLabel()
        lbl_img.setPixmap(pixmap2)
        lbl_img.setAlignment(Qt.AlignCenter)
        ##########################
        hbox = QHBoxLayout()
        hbox.addWidget(lbl_img)
        vbox = QVBoxLayout()
        vbox.addLayout(hbox) #image or two button
        self.setLayout(vbox)
        
        #Exit
        btn = QPushButton('X', self)
        btn.setStyleSheet("font-size:25px;")
        #btn.resize(40, 40) #JY
        #btn.move(1860, 10)
        btn.resize(30, 30) #WS
        btn.move(1240, 10)
        btn.clicked.connect(QCoreApplication.instance().quit)

        self.btn1 = QPushButton('Record', self)
        self.btn1.move(40, 80)
        self.btn1.clicked.connect(self.recordaudio)
        
        #Go to GUI3
        btn2 = QPushButton('Next', self)
        btn2.setStyleSheet("font-size:30px;")
        #btn2.resize(150,30) #JY
        #btn2.move(1320, 920)
        btn2.resize(100,30) #WS
        btn2.move(920,600)
        btn2.clicked.connect(self.showGUI3)
        
        #...
        btn3 = QPushButton('Listen again', self)
        btn3.setStyleSheet("font-size:30px;")
        #btn3.resize(150,30) #JY
        #btn3.move(1320, 920)
        btn3.resize(100,30) #WS
        btn3.move(700,600)
        btn3.clicked.connect(self.ListenAgain)

        #self.pbar = QProgressBar(self)
        #self.pbar.move(100, 100)
        #self.pbar.resize(150, 30)
        #self.timer = QBasicTimer()
        #self.step = 0

        self.resize(1920, 1080)
        self.center() 
        self.show()
        
    def center(self): 
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        
    def ListenAgain(self):
        #audio = './enrollment_audio/enrollment_test_audio_.wav'
        #data, samplerate = librosa.load(audio)
        #times = np.arange(len(data))/float(samplerate)
        #sd.play(data,samplerate)
        audio = './enrollment_audio/enrollment_test_audio_.wav'
        data, fs = sf.read(audio, dtype='float32')
        sd.play(data, fs)
        sd.wait()
        #os.system("./enrollment_audio/enrollment_test_audio_.wav")
        #playsound('./enrollment_audio/enrollment_test_audio_.wav')
        print('k')

    #def timerEvent(self, e):
    #    if self.step >= 100:
    #        self.timer.stop()
    #        self.btn1.setText('Finished')
    #        return

    #   self.step = self.step + 1
    #   self.pbar.setValue(self.step)

    #def doAction(self):
    #    self.timer.start(250, self)
    #    self.btn1.setText('Recording..')
            
    def showGUI3(self):
        self.hide()
        self.child2_win = myGUI3()
        self.child2_win.show()
            
    def recordaudio(self):
        self.btn1.setText('Recording..')
        fs = 16000
        seconds = 5
        sleep(0.1)
        new_sec = int(seconds * fs / 5)
        new_record = [[0]*new_sec for i in range(5)]
        print("Recording Start!")
        myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
        print(myrecording.shape)
        print("Recording End!")
        sd.wait()
        for i in range(5):
            new_record[i] = myrecording[i*new_sec:(i+1)*new_sec-1]
            print(new_record[i].shape)
            #write('Z:/github/myway/enrollment_audio/enrollment_test_audio_%d.wav'%i, fs, new_record[i])
            write('./enrollment_audio/enrollment_test_audio_%d.wav'%i, fs, new_record[i])
        print("wav done!")
        save_spectrogram_tisv()
        print("speaker done!")
        self.btn1.setText('Finished')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())