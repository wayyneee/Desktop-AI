import os, sys
import random
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtGui
class DesktopPet(QWidget):
    def __init__(self, parent= None,**kwargs):
        super(DesktopPet,self).__init__(parent)
        self.init()
        self.initPall()
        self.initPetImage()
        # self.PetNormalAction()
    
    def init(self):
        #無邊匡 ｜ 總是在最上層 ｜ “子視窗 (Qt.SubWindow)使用的話會沒畫面”！！
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        #背景透明
        self.setAutoFillBackground(False)
        #窗口透明,物體不透明
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.repaint()

    def initPall(self):
        #設定icons
        iconsPath = '/Applications/DesktopAI/source/'
        icons = os.path.join(iconsPath+'/icon2.jpeg')
        QuitAction = QAction('退出',self,triggered =self.quit)
        QuitAction.setIcon(QIcon(icons))
        ShowingAction = QAction('顯示',self,triggered =self.showwin)
        HindAction = QAction('隱藏',self,triggered =self.hindwin)
        #創menu 並賦予menu Action
        self.TrayIconMenu = QMenu(self)
        self.TrayIconMenu.addAction(QuitAction)
        self.TrayIconMenu.addAction(ShowingAction)
        self.TrayIconMenu.addAction(HindAction)
        #創icon並賦予icon圖示, menu
        self.TrayIcon=  QSystemTrayIcon(self)
        self.TrayIcon.setIcon(QIcon(icons))
        self.TrayIcon.setContextMenu(self.TrayIconMenu)
        self.TrayIcon.show()
    
    def initPetImage(self):
        #設定交談匡
        self.TalkLabel = QLabel(self)
        self.TalkLabel.setText('Hi')
        self.TalkLabel.setStyleSheet("font:40pt;border-width: 1px; color:black;")
        #宣告一個label用來show gif檔
        self.PetImageLabel = QLabel(self)
        #宣告一個Qmovie等於要show的gif檔
        MoviePath = "/Applications/DesktopAI/source/normal"
        self.PetMovie = QMovie(MoviePath+"/normal4.gif")
        self.PetMovie.setScaledSize(QSize(200,200))
        self.PetImageLabel.setMovie(self.PetMovie)
        self.PetMovie.start()
        self.resize(200,200)
        self.RandomPosition()
        self.show()

    def quit(self):
        self.close()
        sys.exit()
    def showwin(self):
        #設定窗體透明度
        self.setWindowOpacity(1)
    def hindwin(self):
         #設定窗體透明度
        self.setWindowOpacity(0)
    def RandomPosition(self):
        ScreenGeometry = QDesktopWidget().screenGeometry()
        PetGeometry = self.geometry()
        width = int((ScreenGeometry.width()-PetGeometry.width())*random.random())
        Height = int((ScreenGeometry.height()- PetGeometry.height())*random.random())
        self.move(width,Height)

    #__________mouse Event__________________________________#
    def mousePressEvent(self, event: QtGui.QMouseEvent):
        self.condition = 1
        if event.button() ==Qt.LeftButton:
            self.is_follow_mouse = True
        self.mouse_drag_pos = event.globalPos() - self.pos()
        event.accept()
        self.setCursor(QCursor(Qt.OpenHandCursor))
        return super().mousePressEvent(event)

    def mouseMoveEvent(self, event: QtGui.QMouseEvent):
        if Qt.LeftButton and self.is_follow_mouse:
            self.move(event.globalPos()-self.mouse_drag_pos)
        event.accept()
        return super().mouseMoveEvent(event)
    def mouseReleaseEvent(self, event: QtGui.QMouseEvent):
        self.is_follow_mouse==False
        self.setCursor(QCursor(Qt.ArrowCursor))
        return super().mouseReleaseEvent(event)
    #________________end mouse event__________________________#





if __name__ ==  '__main__':
    app = QApplication(sys.argv)
    pet = DesktopPet()
    sys.exit(app.exec_())


