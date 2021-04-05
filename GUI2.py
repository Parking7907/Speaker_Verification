import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLCDNumber, QDial, QPushButton, QVBoxLayout, QHBoxLayout, QDesktopWidget, QLabel, QProgressBar)
from PyQt5.QtGui import QImage, QPalette, QBrush, QPixmap,  QIcon, QMovie
from PyQt5.QtCore import QCoreApplication, Qt, QBasicTimer, QSize
from scipy.io.wavfile import write
from GUI3 import myGUI3
from enrollment_data_preprocess import save_spectrogram_tisv
import pdb
#import pyaudio
import soundfile as sf
import sounddevice as sd
from time import sleep

class myGUI2(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        QWidget.__init__(self)
        self.setWindowTitle('IIPHIS')
        self.setWindowIcon(QIcon('Icon.png'))
        
        #background
        oImage = QImage("background3.png")
        sImage = oImage.scaled(QSize(1920,1080))                   # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))                
        self.setPalette(palette)
        
        #image insert
        #pixmap = QPixmap('script.PNG')
        #pixmap2 = pixmap.scaled(1200,660) #JY
        #pixmap2 = pixmap.scaled(800,440) #WS
        #lbl_img = QLabel()
        #lbl_img.setPixmap(pixmap2)
        #lbl_img.setAlignment(Qt.AlignCenter)
        ##########################
        #hbox = QHBoxLayout()
        #hbox.addWidget(lbl_img)
        #vbox = QVBoxLayout()
        #vbox.addLayout(hbox) #image or two button
        #self.setLayout(vbox)
        
        #Label for script
        label1 = QLabel('Say "Hi IIPHIS" 5Times\n in 10 seconds', self)
        label1.setStyleSheet("font-size:60px;" "font: bold italic large")
        #label1.resize(600, 60) #jinyeong fit
        #label1.move(720, 65)
        label1.resize(1100,160) #wonsuk fit
        label1.move(600, 100)

        #button(recording)
        self.btn1 = QPushButton('Record', self)
        self.btn1.setStyleSheet("font-size:30px;")
        self.btn1.resize(150, 40) #JY
        self.btn1.move(450, 920)
        #self.btn1.resize(120, 30) #WS
        #self.btn1.move(300, 600)
        self.btn1.clicked.connect(self.recordaudio)
        
        #Go to GUI3
        btn2 = QPushButton('Next', self)
        btn2.setStyleSheet("font-size:30px;")
        btn2.resize(150,40) #JY
        btn2.move(1320, 920)
        #btn2.resize(100,30) #WS
        #btn2.move(920,600)
        btn2.clicked.connect(self.showGUI3)

        #Listen again
        btn3 = QPushButton('Listen again', self)
        btn3.setStyleSheet("font-size:30px;")
        btn3.resize(220,40) #JY
        btn3.move(1585, 650)
        #btn3.resize(100,30) #WS
        #btn3.move(700,600)
        btn3.clicked.connect(self.ListenAgain)
        
        #timer
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

    def showGUI3(self):
        self.hide()
        self.child2_win = myGUI3()
        self.child2_win.show()
        
    #def TimerEvent(self, e):
        #if self.step >= 100:
            #self.timer.stop()
            #self.btn1.setText('Finished')
            #return
        #self.step = self.step + 1
        #self.pbar.setValue(self.step)
        
    #def doAction(self):
        #if self.timer.isActive():
            #self.timer.stop()
            #self.btn1.setText('Recording..')
        #else:
            #self.timer.start(250, self)
            #self.btn1.setText('Stop')
    def recordaudio(self):
        #self.doAction()
        fs = 16000
        seconds = 10

        #sleep(0.1)
        new_sec = int(seconds * fs / 5)
        new_record = [[0]*new_sec for i in range(5)]
        print("Recording Start!")
        myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels = 1)
        #self.btn1.setText('Say IIPHIS : 5')
        print(myrecording.shape)
        print("Recording End!")
        sd.wait()
        write('./enrollment_test_audio.wav', fs, myrecording)
        for i in range(5):
            new_record[i] = myrecording[i*new_sec:(i+1)*new_sec-1]
            print(new_record[i].shape)
            #write('Z:/github/myway/enrollment_audio/enrollment_test_audio_%d.wav'%i, fs, new_record[i])
            write('./enrollment_audio/enrollment_test_audio_%d.wav'%i, fs, new_record[i])
            #self.btn1.setText('Say IIPHIS : %d'%i)
            #print('Say IIPHIS : %d'%i)
        #self.btn1.setText('unfinished')
        print("wav done!")
        save_spectrogram_tisv()
        print("speaker done!")
        #for j in range(5):
        #    sd.play('./enrollment_audio/enrollment_test_audio_%d.wav'%i, fs, new_record[i]
        #self.btn1.setText('Finished')

    def ListenAgain(self):
        #audio = './enrollment_audio/enrollment_test_audio_.wav'
        #data, samplerate = librosa.load(audio)
        #times = np.arange(len(data))/float(samplerate)
        #sd.play(data,samplerate)
        for k in range(5):
            audio = './enrollment_audio/enrollment_test_audio_%d.wav'%k
            print(audio)
            data, fs = sf.read(audio, dtype='float32')
            sd.play(data, fs)
            sd.wait()
            sleep(1)
        #os.system("./enrollment_audio/enrollment_test_audio_.wav")
        #playsound('./enrollment_audio/enrollment_test_audio_.wav')
        
        print('listen again done')

# Don't touch me
if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = myGUI2()
   sys.exit(app.exec_())
