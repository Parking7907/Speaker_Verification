import sys
from PyQt5.QtCore import QSize, QCoreApplication, Qt, QBasicTimer
from PyQt5.QtGui import QImage, QPalette, QBrush, QPixmap,  QIcon, QMovie
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import (QApplication, QWidget, QLCDNumber, QDial, QPushButton, QVBoxLayout, QHBoxLayout, QDesktopWidget, QLabel, QProgressBar)
from GUI3 import myGUI3

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        QWidget.__init__(self)
        self.setGeometry(100,100,900,600)
        
        self.setWindowTitle('IIPHIS')
        self.setWindowIcon(QIcon('Icon.png'))

        #image insert
        pixmap = QPixmap('script.PNG')
        pixmap2 = pixmap.scaled(1200,660) #JY
        pixmap2 = pixmap.scaled(600,330) #WS
        lbl_img = QLabel()
        lbl_img.setPixmap(pixmap2)
        lbl_img.setAlignment(Qt.AlignCenter)
        #########################
        hbox = QHBoxLayout()
        hbox.addWidget(lbl_img)
        vbox = QVBoxLayout()
        vbox.addLayout(hbox) #image or two button
        self.setLayout(vbox)
        
        #gif insert
        self.movie = QMovie("cat.gif")
        self.label.setMovie(self.movie)
        self.movie.start()

        oImage = QImage("background.png")
        sImage = oImage.scaled(QSize(1920,1080))                   # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))                
        self.setPalette(palette)

        #Exit
        btn = QPushButton('X', self)
        btn.setStyleSheet("color: red;" "font-size:25px;")
        #btn.resize(40, 40) #JY
        #btn.move(1860, 10)
        btn.resize(30, 30) #WS
        btn.move(1240, 10)
        btn.clicked.connect(QCoreApplication.instance().quit)

        btn1 = QPushButton('Record', self)
        btn1.setStyleSheet("color: red;" "font-size:10px;" "font: bold italic large")
        btn1.move(40, 80)
        btn1.clicked.connect(self.recordaudio)
        
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

        self.resize(1920,1080)
        self.center()
        self.show()
       
    def center(self): 
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        
    def ListenAgain(self):
        audio = './enrollment_audio/enrollment_test_audio_.wav'
        data, fs = sf.read(audio, dtype='float32')
        sd.play(data, fs)
        sd.wait()
        
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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    oMainwindow = MyApp()
    sys.exit(app.exec_())