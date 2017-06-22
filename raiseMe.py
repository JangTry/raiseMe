import os
import random
import sys

import time
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QWidget, QLabel, QApplication, QDesktopWidget

class Example(QWidget):
    size=100
    imgNum=0
    frameCount=4
    isXmin = False
    isXmax = False
    isYmin = False
    isYmax = False
    isLeft= True
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        sizeObject = QDesktopWidget().screenGeometry()
        # print(" Screen size : " + str(sizeObject.height()) + "x" + str(sizeObject.width()))
        self.xMax=sizeObject.width()-10
        self.yMax=sizeObject.height()-10
        print(self.xMax)
        print(self.yMax)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setStyleSheet("background-color:transparent;")
        self.setGeometry(100, 100, 100, 100)
        self.setWindowFlags(Qt.SplashScreen | Qt.WindowStaysOnTopHint)
        self.setAcceptDrops(True)
        self.label=QLabel(self)
        self.pixmaps=[QPixmap('left.png'),QPixmap('stand.png'),QPixmap('right.png'),QPixmap('stand.png'),QPixmap('leftR.png'),QPixmap('standR.png'),QPixmap('rightR.png'),QPixmap('standR.png')]
        for x in range(len(self.pixmaps)):
            self.pixmaps[x]=self.pixmaps[x].scaled(self.size,self.size,Qt.KeepAspectRatio)
        self.resize(self.pixmaps[2].width(),self.pixmaps[2].height())
        self.label.setPixmap(self.pixmaps[len(self.pixmaps)-1])
        self.changeTimer=QTimer(self)
        self.changeTimer.timeout.connect(self.changeFoot)
        self.moveTimer=QTimer(self)
        self.moveTimer.timeout.connect(self.moving)
        self.show()
        self.label.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        for url in event.mimeData().urls():
            path = url.toLocalFile().toLocal8Bit().data()
            # if os.path.isfile(path):
            print(path)
    def moving(self):
        if self.distance == 0:
            print(self.distance)
            print(self.x(),"x",self.y())
            self.label.setPixmap(self.pixmaps[1])
            self.moveTimer.stop()
            self.changeTimer.stop()
            time.sleep(3)
            self.setMovement()
            return 0
        else:
            self.move(self.x()+self.direct[0],self.y()+self.direct[1])
            self.distance-=1
        if self.x()<=-10 :
            self.distance=0
            print("xm")
            self.isXmin = True
        if self.y()<=-10 :
            self.distance=0
            print("ym")
            self.isYmin = True
        if self.x()>=self.xMax:
            self.distance=0
            print("xM")
            self.isXmax=True
        if self.y()>=self.yMax :
            self.distance=0
            print("yM")
            self.isYmax=True

    def setMovement(self):
        self.direct=[0,0]
        while(self.direct[0]==0 and self.direct[1]==0):
            self.direct=[random.randint(-1,1),random.randint(-1,1)]
        if self.isXmax:
            self.direct[0]=-1
        if self.isXmin:
            self.direct[0]=1
        if self.isYmin:
            self.direct[1]=1
        if self.isYmax:
            self.direct[1]=-1

        if self.direct[0]== -1:
            self.isLeft=True
            self.imgNum=0
        elif self.direct[0]== 1:
            self.isLeft=False
            self.imgNum=4
        self.isXmax = False
        self.isXmin = False
        self.isYmin = False
        self.isYmax = False
        # if direct[0]*direct[1]==0 : self.delta = QPoint(dX*direct[0],dY*direct[1])
        # else: self.delta=QPoint(direct[0]*(dX**(1/2)),direct[1]*(dY**1/2))
        self.distance=random.randint(200,400)
        self.changeTimer.start(300)
        self.moveTimer.start(30)

    def changeFoot(self):
        self.label.setPixmap(self.pixmaps[self.imgNum])
        if self.isLeft:
            if self.imgNum<self.frameCount-1:
                self.imgNum+=1
            else :
                self.imgNum=0
        else:
            if self.imgNum<2*self.frameCount-1:
                self.imgNum+=1
            else :
                self.imgNum=self.frameCount

    def mousePressEvent(self, QMouseEvent):
        self.setMovement()

    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key() == Qt.Key_Escape:
            sys.exit()
        # if QKeyEvent.key() == Qt.Key_G:
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
# 끝자락에선 발안움직이는거 개선 O
#속도에 따라 발속도 따라가기
#오른쪽으로갈때 사진뒤집기 O
#자연스럽게 움직이기
#행동하나끝나고 뭐할지 정하기
#클릭해서 드래그하면 ㅂㄷㅂㄷ하면서 끌려오기
#exe 추출어떻게하는거지 O
#exe 추출할때 파일수좀 줄이고 정리되서, 그리고 크기 줄이기
#폴더주면 좋아하기
#클릭하면 테미! 4번째엔 밥.
