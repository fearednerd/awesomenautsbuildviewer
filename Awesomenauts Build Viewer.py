#!/usr/bin/env python
#Paul Yi
#I know that here are multiple levels of certain upgrades
#This build viewer makes the assumption of maxing out a skill when selected


import sys
from PySide import QtGui
from PySide import QtCore



mainWindow = 0
#test comment
class CharWindow(QtGui.QWidget):
    global mainWindow
    hp = 0
    attack = 0
    atkspeed = 0
    startsolar = 0#remember to incorporate skill1 and skill2 costs
    solarpermin = 0
    solarneeded = 0
    movespeed = 0
    skill1dmg = 0
    skill2dmg = 0
    
    def __init__(self):
        super(CharWindow, self).__init__()
        
        self.initUI()
        
    def initUI(self):
        self.resize(250, 150)
    def setupChar(self, charname):
        print "window setup for" ,charname
        mainWindow.resize(800, 150)
        overHBox = QtGui.QHBoxLayout()
        skillGrid = QtGui.QGridLayout()
        
        #Sets up the Clunk Screen
        if charname == "Clunk":
            
            #setup default Clunk data
            hp = 255
            attack = 14
            atkspeed = 60
            startsolar = 0
            solarpermin = 0
            solarneeded = 0#remember to incorporate skill1 and skill2 costs
            movespeed = 7.2
            skill1dmg = 30
            skill2dmg = 60
            
            biteimg = QtGui.QPixmap("Images/Clunk/Bite-Clunk.png")
            clunkbite = QtGui.QLabel()
            clunkbite.setPixmap(biteimg)
            skillGrid.addWidget(clunkbite,0,0)
            overHBox.addLayout(skillGrid)
            print skillGrid.originCorner()
            
            bite1btn = QtGui.QPushButton()
            bite1btn.setCheckable(True)
            b1img = QtGui.QPixmap("Images/Clunk/Bite1-Clunk.png")
            bite1btn.setIconSize(QtCore.QSize(100,100))
            bite1btn.setObjectName("bite1")
            bite1btn.setIcon(QtGui.QIcon(b1img))
            bite1btn.clicked[bool].connect(self.biteclicked)
            skillGrid.addWidget(bite1btn,0,1)
            
            bite2btn = QtGui.QPushButton()
            bite2btn.setCheckable(True)
            b2img = QtGui.QPixmap("Images/Clunk/Bite2-Clunk.png")
            bite2btn.setIconSize(QtCore.QSize(100,100))
            bite2btn.setObjectName("bite2")
            bite2btn.setIcon(QtGui.QIcon(b2img))
            bite2btn.clicked[bool].connect(self.biteclicked)
            skillGrid.addWidget(bite2btn,0,2)
            
            bite3btn = QtGui.QPushButton()
            bite3btn.setCheckable(True)
            b3img = QtGui.QPixmap("Images/Clunk/Bite3-Clunk.png")
            bite3btn.setIconSize(QtCore.QSize(100,100))
            bite3btn.setObjectName("bite1")
            bite3btn.setIcon(QtGui.QIcon(b3img))
            bite3btn.clicked[bool].connect(self.biteclicked)
            skillGrid.addWidget(bite3btn,0,3)
            
            bite4btn = QtGui.QPushButton()
            bite4btn.setCheckable(True)
            b4img = QtGui.QPixmap("Images/Clunk/Bite4-Clunk.png")
            bite4btn.setIconSize(QtCore.QSize(100,100))
            bite4btn.setObjectName("bite4")
            bite4btn.setIcon(QtGui.QIcon(b4img))
            bite4btn.clicked[bool].connect(self.biteclicked)
            skillGrid.addWidget(bite4btn,0,4)
            
            bite5btn = QtGui.QPushButton()
            bite5btn.setCheckable(True)
            b5img = QtGui.QPixmap("Images/Clunk/Bite5-Clunk.png")
            bite5btn.setIconSize(QtCore.QSize(100,100))
            bite5btn.setObjectName("bite5")
            bite5btn.setIcon(QtGui.QIcon(b5img))
            bite5btn.clicked[bool].connect(self.biteclicked)
            skillGrid.addWidget(bite5btn,0,5)
            
            bite6btn = QtGui.QPushButton()
            bite6btn.setCheckable(True)
            b6img = QtGui.QPixmap("Images/Clunk/Bite6-Clunk.png")
            bite6btn.setIconSize(QtCore.QSize(100,100))
            bite6btn.setObjectName("bite6")
            bite6btn.setIcon(QtGui.QIcon(b6img))
            bite6btn.clicked[bool].connect(self.biteclicked)
            skillGrid.addWidget(bite6btn,0,6)
            
            #Explode Row for Clunk Screen
            eximg = QtGui.QPixmap("Images/Clunk/Ex-Clunk.png")
            clunkex = QtGui.QLabel()
            clunkex.setPixmap(eximg)
            skillGrid.addWidget(clunkex,1,0)
            
            ex1btn = QtGui.QPushButton()
            ex1btn.setCheckable(True)
            ex1img = QtGui.QPixmap("Images/Clunk/Ex1-Clunk.png")
            ex1btn.setIconSize(QtCore.QSize(100,100))
            ex1btn.setObjectName("ex1")
            ex1btn.setIcon(QtGui.QIcon(b1img))
            ex1btn.clicked[bool].connect(self.exclicked)
            skillGrid.addWidget(ex1btn,1,1)
            
            ex2btn = QtGui.QPushButton()
            ex2btn.setCheckable(True)
            ex2img = QtGui.QPixmap("Images/Clunk/Ex2-Clunk.png")
            ex2btn.setIconSize(QtCore.QSize(100,100))
            ex2btn.setObjectName("ex2")
            ex2btn.setIcon(QtGui.QIcon(b2img))
            ex2btn.clicked[bool].connect(self.exclicked)
            skillGrid.addWidget(ex2btn,1,2)
            
            ex3btn = QtGui.QPushButton()
            ex3btn.setCheckable(True)
            ex3img = QtGui.QPixmap("Images/Clunk/Ex3-Clunk.png")
            ex3btn.setIconSize(QtCore.QSize(100,100))
            ex3btn.setObjectName("ex1")
            ex3btn.setIcon(QtGui.QIcon(b3img))
            ex3btn.clicked[bool].connect(self.exclicked)
            skillGrid.addWidget(ex3btn,1,3)
            
            ex4btn = QtGui.QPushButton()
            ex4btn.setCheckable(True)
            ex4img = QtGui.QPixmap("Images/Clunk/Ex4-Clunk.png")
            ex4btn.setIconSize(QtCore.QSize(100,100))
            ex4btn.setObjectName("ex4")
            ex4btn.setIcon(QtGui.QIcon(b4img))
            ex4btn.clicked[bool].connect(self.exclicked)
            skillGrid.addWidget(ex4btn,1,4)
            
            ex5btn = QtGui.QPushButton()
            ex5btn.setCheckable(True)
            ex5img = QtGui.QPixmap("Images/Clunk/Ex5-Clunk.png")
            ex5btn.setIconSize(QtCore.QSize(100,100))
            ex5btn.setObjectName("ex5")
            ex5btn.setIcon(QtGui.QIcon(b5img))
            ex5btn.clicked[bool].connect(self.exclicked)
            skillGrid.addWidget(ex5btn,1,5)
            
            ex6btn = QtGui.QPushButton()
            ex6btn.setCheckable(True)
            ex6img = QtGui.QPixmap("Images/Clunk/Ex6-Clunk.png")
            ex6btn.setIconSize(QtCore.QSize(100,100))
            ex6btn.setObjectName("ex6")
            ex6btn.setIcon(QtGui.QIcon(b6img))
            ex6btn.clicked[bool].connect(self.exclicked)
            skillGrid.addWidget(ex6btn,1,6)
            
            melee1btn = QtGui.QPushButton()
            melee1btn.setCheckable(True)
            melee1img = QtGui.QPixmap("Images/Clunk/M1-Clunk.png")
            melee1btn.setIconSize(QtCore.QSize(100,100))
            melee1btn.setObjectName("melee1")
            melee1btn.setIcon(QtGui.QIcon(b1img))
            melee1btn.clicked[bool].connect(self.meleeclicked)
            skillGrid.addWidget(melee1btn,2,1)
            
            melee2btn = QtGui.QPushButton()
            melee2btn.setCheckable(True)
            melee2img = QtGui.QPixmap("Images/Clunk/M2-Clunk.png")
            melee2btn.setIconSize(QtCore.QSize(100,100))
            melee2btn.setObjectName("melee2")
            melee2btn.setIcon(QtGui.QIcon(b2img))
            melee2btn.clicked[bool].connect(self.meleeclicked)
            skillGrid.addWidget(melee2btn,2,2)
            
            melee3btn = QtGui.QPushButton()
            melee3btn.setCheckable(True)
            melee3img = QtGui.QPixmap("Images/Clunk/M3-Clunk.png")
            melee3btn.setIconSize(QtCore.QSize(100,100))
            melee3btn.setObjectName("melee1")
            melee3btn.setIcon(QtGui.QIcon(b3img))
            melee3btn.clicked[bool].connect(self.meleeclicked)
            skillGrid.addWidget(melee3btn,2,3)
            
            melee4btn = QtGui.QPushButton()
            melee4btn.setCheckable(True)
            melee4img = QtGui.QPixmap("Images/Clunk/M4-Clunk.png")
            melee4btn.setIconSize(QtCore.QSize(100,100))
            melee4btn.setObjectName("melee4")
            melee4btn.setIcon(QtGui.QIcon(b4img))
            melee4btn.clicked[bool].connect(self.meleeclicked)
            skillGrid.addWidget(melee4btn,2,4)
            
            melee5btn = QtGui.QPushButton()
            melee5btn.setCheckable(True)
            melee5img = QtGui.QPixmap("Images/Clunk/M5-Clunk.png")
            melee5btn.setIconSize(QtCore.QSize(100,100))
            melee5btn.setObjectName("melee5")
            melee5btn.setIcon(QtGui.QIcon(b5img))
            melee5btn.clicked[bool].connect(self.meleeclicked)
            skillGrid.addWidget(melee5btn,2,5)
            
            melee6btn = QtGui.QPushButton()
            melee6btn.setCheckable(True)
            melee6img = QtGui.QPixmap("Images/Clunk/M6-Clunk.png")
            melee6btn.setIconSize(QtCore.QSize(100,100))
            melee6btn.setObjectName("melee6")
            melee6btn.setIcon(QtGui.QIcon(b6img))
            melee6btn.clicked[bool].connect(self.meleeclicked)
            skillGrid.addWidget(melee6btn,2,6)
            
            #need to change image for this row
            misc1btn = QtGui.QPushButton()
            misc1btn.setCheckable(True)
            misc1img = QtGui.QPixmap("Images/Clunk/M1-Clunk.png")
            misc1btn.setIconSize(QtCore.QSize(100,100))
            misc1btn.setObjectName("misc1")
            misc1btn.setIcon(QtGui.QIcon(b1img))
            misc1btn.clicked[bool].connect(self.miscclicked)
            skillGrid.addWidget(misc1btn,3,1)
            
            misc2btn = QtGui.QPushButton()
            misc2btn.setCheckable(True)
            misc2img = QtGui.QPixmap("Images/Clunk/M2-Clunk.png")
            misc2btn.setIconSize(QtCore.QSize(100,100))
            misc2btn.setObjectName("misc2")
            misc2btn.setIcon(QtGui.QIcon(b2img))
            misc2btn.clicked[bool].connect(self.miscclicked)
            skillGrid.addWidget(misc2btn,3,2)
            
            misc3btn = QtGui.QPushButton()
            misc3btn.setCheckable(True)
            misc3img = QtGui.QPixmap("Images/Clunk/M3-Clunk.png")
            misc3btn.setIconSize(QtCore.QSize(100,100))
            misc3btn.setObjectName("misc1")
            misc3btn.setIcon(QtGui.QIcon(b3img))
            misc3btn.clicked[bool].connect(self.miscclicked)
            skillGrid.addWidget(misc3btn,3,3)
            
            misc4btn = QtGui.QPushButton()
            misc4btn.setCheckable(True)
            misc4img = QtGui.QPixmap("Images/Clunk/M4-Clunk.png")
            misc4btn.setIconSize(QtCore.QSize(100,100))
            misc4btn.setObjectName("misc4")
            misc4btn.setIcon(QtGui.QIcon(b4img))
            misc4btn.clicked[bool].connect(self.miscclicked)
            skillGrid.addWidget(misc4btn,3,4)
            
            misc5btn = QtGui.QPushButton()
            misc5btn.setCheckable(True)
            misc5img = QtGui.QPixmap("Images/Clunk/M5-Clunk.png")
            misc5btn.setIconSize(QtCore.QSize(100,100))
            misc5btn.setObjectName("misc5")
            misc5btn.setIcon(QtGui.QIcon(b5img))
            misc5btn.clicked[bool].connect(self.miscclicked)
            skillGrid.addWidget(misc5btn,3,5)
            
            misc6btn = QtGui.QPushButton()
            misc6btn.setCheckable(True)
            misc6img = QtGui.QPixmap("Images/Clunk/M6-Clunk.png")
            misc6btn.setIconSize(QtCore.QSize(100,100))
            misc6btn.setObjectName("misc6")
            misc6btn.setIcon(QtGui.QIcon(b6img))
            misc6btn.clicked[bool].connect(self.miscclicked)
            skillGrid.addWidget(misc6btn,3,6)
            
            self.setLayout(overHBox)
            self.show()
            
    def biteclicked(self, pressed):
        sender = self.sender()
        if pressed:
            on = 1
        else:
            on = 0
        if sender.objectName() == "bite1":
            sender.setFlat(on)
            if on == 1:
                skill1dmg = skill1dmg + 12
            else:
                skill1dmg = skill1dmg - 12
        if sender.objectName() == "bite2":
            sender.setFlat(on)
            if on == 1:
                hp = hp + 12
            else:
                hp = hp - 12
        if sender.objectName() == "bite3":
            sender.setFlat(on)
            skill1dmg = 42
        if sender.objectName() == "bite4":
            sender.setFlat(on)
            skill1dmg = 42
        if sender.objectName() == "bite5":
            sender.setFlat(on)
            skill1dmg = 42
        if sender.objectName() == "bite6":
            sender.setFlat(on)
            skill1dmg = 42    
    def exclicked(self, pressed):
        sender = self.sender()
        if pressed:
            on = 1
        else:
            on = 0
        if sender.objectName() == "bite1":
            sender.setFlat(on)
            
    def meleeclicked(self, pressed):
        sender = self.sender()
        if pressed:
            on = 1
        else:
            on = 0
        if sender.objectName() == "bite1":
            sender.setFlat(on)
            
    def miscclicked(self, pressed):
        sender = self.sender()
        if pressed:
            on = 1
        else:
            on = 0
        if sender.objectName() == "bite1":
            sender.setFlat(on)
            
# the widget that sets up the character buttons in grid mode
#This is the character selection screen
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
        
    # the button click listener; this listener will figure out which character
    # signal was sent and will open the according character window
    def buttonClicked(self):
        sender = self.sender()
        #If clunk is clicked it will do the setupchar method for Clunk
        #Then it will switch the central widget to the Clunk Character Window
        if sender.objectName() == "clunkbtn":
            charwindow = CharWindow()
            charwindow.setupChar("Clunk")
            mainWindow.setCentralWidget(charwindow)
            mainWindow.show()
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
    global mainWindow
    app = QtGui.QApplication(sys.argv)
    mainWindow = MainWindow()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()
