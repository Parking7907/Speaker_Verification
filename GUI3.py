import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLCDNumber, QDial, QPushButton, QVBoxLayout, QHBoxLayout, QDesktopWidget, QLabel, QProgressBar)
from PyQt5.QtGui import QImage, QPalette, QBrush, QPixmap,  QIcon, QMovie
from PyQt5.QtCore import QCoreApplication, Qt, QBasicTimer, QSize
from scipy.io.wavfile import write
from GUI4 import myGUI4
from GUI5 import myGUI5
from test import test
from verification_data_preprocess import save_spectrogram_tisv
import pdb
import soundfile as sf
import sounddevice as sd
from time import sleep

class myGUI3(QWidget):
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

        #image insert
        pixmap = QPixmap('Hi IIPHIS.PNG')
        pixmap2 = pixmap.scaled(200,120)
        lbl_img = QLabel()
        lbl_img.setPixmap(pixmap2)
        lbl_img.setAlignment(Qt.AlignRight)
        ##########################
        #hbox = QHBoxLayout()
        #hbox.addWidget(lbl_img)
        #vbox = QVBoxLayout()
        #vbox.addLayout(hbox) #image or two button
        #self.setLayout(vbox)

        #Label for Script
        label1 = QLabel('Read it for 2 seconds', self)
        label1.setStyleSheet("font-size:40px;")
        label1.resize(600, 60) #JY
        label1.move(745, 65)
        #label1.resize(450, 40) #WS
        #label1.move(400, 40)

        #Exit
        #btn = QPushButton('X', self)
        #btn.setStyleSheet("font-size:25px;")
        #btn.resize(40, 40) #JY
        #btn.move(1860, 10)
        #btn.resize(30, 30) #WS
        #btn.move(1240, 10)
        #btn.clicked.connect(QCoreApplication.instance().quit)

        #button(recording)
        btn1 = QPushButton('Record', self)
        btn1.setStyleSheet("font-size:30px;")
        btn1.resize(150, 30) #JY
        btn1.move(600, 920)
        #btn1.resize(120, 30) #WS
        #btn1.move(320, 600)
        btn1.clicked.connect(self.recordaudio)

        #Go to GUI4
        btn2 = QPushButton('Next', self)
        btn2.setStyleSheet("font-size:30px;")
        btn2.resize(150,30) #JY
        btn2.move(1150, 920) 
        #btn2.resize(100,30) #WS
        #btn2.move(900,600)
        btn2.clicked.connect(self.test)

        #Listen again
        btn3 = QPushButton('Listen again', self)
        btn3.setStyleSheet("font-size:30px;")
        btn3.resize(220,40) #JY
        btn3.move(1585, 650)
        #btn3.resize(100,30) #WS
        #btn3.move(700,600)
        btn3.clicked.connect(self.ListenAgain)
        self.resize(1920, 1080)
        self.center() 
        self.show()

    def center(self): 
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def test(self): #button 1 more -> end of discussion
        k = test('./model.model')
        print(k)
        if k>5:
            success_audio = './Success.wav'
            data, fs = sf.read(success_audio, dtype='float32')
            sd.play(data, fs)
            sd.wait()
            self.child3_win = myGUI4()
            self.child3_win.show()
        else:
            fail_audio = './Fail.wav'
            data, fs = sf.read(fail_audio, dtype='float32')
            sd.play(data, fs)
            sd.wait()
            #self.hide()
            self.child4_win = myGUI5()
            self.child4_win.show()
        
    def reshowGUI3(self):
        self.show()

    def recordaudio(self):
        fs = 16000
        seconds = 2	
        sleep(0.1)
        print("Recording Start!")
        myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
        print("Recording done!")
        sd.wait()
        for i in range(5):
            #write('Z:/github/myway/verification_audio/Verification_test_audio_%d.wav'%i, fs, myrecording)
            write('./verification_audio/Verification_test_audio_%d.wav'%i, fs, myrecording)
        print("wav done!")
        save_spectrogram_tisv()
        print("Speaker done!")

    def ListenAgain(self):
        #audio = './enrollment_audio/enrollment_test_audio_.wav'
        #data, samplerate = librosa.load(audio)
        #times = np.arange(len(data))/float(samplerate)
        #sd.play(data,samplerate)
        audio = './verification_audio/Verification_test_audio_0.wav'
        data, fs = sf.read(audio, dtype='float32')
        sd.play(data, fs)
        sd.wait()
        #os.system("./enrollment_audio/enrollment_test_audio_.wav")
        #playsound('./enrollment_audio/enrollment_test_audio_.wav')
        print('k')

        
# Don't touch me
if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = myGUI3()
   sys.exit(app.exec_())
