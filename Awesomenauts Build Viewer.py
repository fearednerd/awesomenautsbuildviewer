#!/usr/bin/env python
#Paul Yi

import sys
from PySide import QtGui
from PySide import QtCore

class CharButtons(QtGui.QWidget):
    def __init__(self):
        super(CharButtons, self).__init__()
        
        self.initUI()
        
    def initUI(self):
        self.resize(250, 150)
        #set grid layout
        grid = QtGui.QGridLayout()
        
        
        #Button setup for Clunk
        clunkbtn = QtGui.QPushButton(self)
        clunkimg = QtGui.QPixmap("Images/Icon_Clunk.png")
        clunkbtn.setIcon(QtGui.QIcon(clunkimg))
        clunkbtn.setIconSize(QtCore.QSize(100,100))
        clunkbtn.setObjectName("clunkbtn")
        clunkbtn.clicked.connect(self.buttonClicked) 
        grid.addWidget(clunkbtn,0,0)
        
        #Button setup for Coco
        cocobtn = QtGui.QPushButton(self)
        cocoimg = QtGui.QPixmap("Images/Icon_Coco.png")
        cocobtn.setIcon(QtGui.QIcon(cocoimg))
        cocobtn.setIconSize(QtCore.QSize(100,100))
        grid.addWidget(cocobtn,0,1)
        
        #Button setup for Derpl
        derplbtn = QtGui.QPushButton(self)
        derplimg = QtGui.QPixmap("Images/Icon_Derpl.png")
        derplbtn.setIcon(QtGui.QIcon(derplimg))
        derplbtn.setIconSize(QtCore.QSize(100,100))
        grid.addWidget(derplbtn,0,2)
        
        #Button setup for Froggy
        frogbtn = QtGui.QPushButton(self)
        frogimg = QtGui.QPixmap("Images/Icon_Froggy.png")
        frogbtn.setIcon(QtGui.QIcon(frogimg))
        frogbtn.setIconSize(QtCore.QSize(100,100))
        grid.addWidget(frogbtn,0,3)
        
        #Button setup for Genji
        genjibtn = QtGui.QPushButton(self)
        genjiimg = QtGui.QPixmap("Images/Icon_Genji.png")
        genjibtn.setIcon(QtGui.QIcon(genjiimg))
        genjibtn.setIconSize(QtCore.QSize(100,100))
        grid.addWidget(genjibtn,1,0)
        
        #Button setup for Gnaw
        gnawbtn = QtGui.QPushButton(self)
        gnawimg = QtGui.QPixmap("Images/Icon_Gnaw.png")
        gnawbtn.setIcon(QtGui.QIcon(gnawimg))
        gnawbtn.setIconSize(QtCore.QSize(100,100))
        grid.addWidget(gnawbtn,1,1)
        
        #Button setup for Leon
        leonbtn = QtGui.QPushButton(self)
        leonimg = QtGui.QPixmap("Images/Icon_Leon.png")
        leonbtn.setIcon(QtGui.QIcon(leonimg))
        leonbtn.setIconSize(QtCore.QSize(100,100))
        grid.addWidget(leonbtn,1,2)
        
        #Button setup for Lonestar
        lonebtn = QtGui.QPushButton(self)
        loneimg = QtGui.QPixmap("Images/Icon_Lonestar.png")
        lonebtn.setIcon(QtGui.QIcon(loneimg))
        lonebtn.setIconSize(QtCore.QSize(100,100))
        grid.addWidget(lonebtn,1,3)
        
        #Button setup for Raeylnn
        raebtn = QtGui.QPushButton(self)
        raeimg = QtGui.QPixmap("Images/Icon_Rae.png")
        raebtn.setIcon(QtGui.QIcon(raeimg))
        raebtn.setIconSize(QtCore.QSize(100,100))
        grid.addWidget(raebtn,2,0)
        
        #Button setup for Skolldir
        skollbtn = QtGui.QPushButton(self)
        skollimg = QtGui.QPixmap("Images/Icon_Skolldir.png")
        skollbtn.setIcon(QtGui.QIcon(skollimg))
        skollbtn.setIconSize(QtCore.QSize(100,100))
        grid.addWidget(skollbtn,2,1)
        
        #Button setup for Vinnie
        vinbtn = QtGui.QPushButton(self)
        vinimg = QtGui.QPixmap("Images/Icon_Vinnie.png")
        vinbtn.setIcon(QtGui.QIcon(vinimg))
        vinbtn.setIconSize(QtCore.QSize(100,100))
        grid.addWidget(vinbtn,2,2)
        
        #Button setup for Voltar
        volbtn = QtGui.QPushButton(self)
        volimg = QtGui.QPixmap("Images/Icon_Voltar.png")
        volbtn.setIcon(QtGui.QIcon(volimg))
        volbtn.setIconSize(QtCore.QSize(100,100))
        grid.addWidget(volbtn,2,3)
        
        #Button setup for Yuri
        yuribtn = QtGui.QPushButton(self)
        yuriimg = QtGui.QPixmap("Images/Icon_Yuri.png")
        yuribtn.setIcon(QtGui.QIcon(yuriimg))
        yuribtn.setIconSize(QtCore.QSize(100,100))
        grid.addWidget(yuribtn,3,0)
        
        self.setLayout(grid)
        self.show()
        
        
    def buttonClicked(self):
        sender = self.sender()
        print sender.objectName()

class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        self.initUI()
        
    def initUI(self):               
        
        exitAction = QtGui.QAction(QtGui.QIcon('exit.png'), '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)
        
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Awesomenauts Build Viewer')
        characterbuttons = CharButtons()
        self.setCentralWidget(characterbuttons)
        self.show()
    
    
def main():
    app = QtGui.QApplication(sys.argv)
    mainWindow = MainWindow()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()