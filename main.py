import os
import sys
import platform

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QPropertyAnimation, QEasingCurve,QEvent, QTimer)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient, QFontDatabase)
from PySide2.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PySide2.QtWidgets import *

# load gui
from ui_main import Ui_MainWindow

# IMPORT QSS CUSTOM
from ui_styles import Style

# IMPORT FUNCTIONS
#from app_functions import *

from functions import *


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        
        # apply UI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # print system information
        print('System: ' + platform.system())
        print('Version: ' +platform.release())

        ##################################################################################
        # Window Setting

        # remove title bar
        UIFunctions.removeTitleBar(True)

        # set window title text
        self.setWindowTitle('AccountBox')
        # set custom title text
        UIFunctions.labelTitle(self, 'AccountBox')
        # set labelDescription to location of this file
        UIFunctions.labelDescription(self, os.path.dirname(os.path.abspath(__file__)))

        # set initial size and minimum size
        startSize = QSize(1000, 720)
        self.resize(startSize)
        self.setMinimumSize(startSize)
        # UIFunctions.enableMaximumSize(self, 500, 720)
        

        # toggle menu setting
        self.ui.btn_toggle_menu.clicked.connect(lambda: UIFunctions.toggleMenu(self, 220, True))

        # add other menus
        self.ui.stackedWidget.setMinimumWidth(20)
        UIFunctions.addNewMenu(self, "Home Page", "btn_home", "url(:icons/icons/16x16/cil-home.png)", True)
        UIFunctions.addNewMenu(self, "Add Account", "btn_add", "url(:icons/icons/16x16/cil-pencil.png)", True)
        UIFunctions.addNewMenu(self, "Retrieve N Manage", "btn_retrieve", "url(:icons/icons/16x16/cil-magnifying-glass.png)", True)
        UIFunctions.addNewMenu(self, "Setting", "btn_setting", "url(:/icons/icons/16x16/cil-settings.png)", False)

        ##################################################################################
        # START MENU => SELECTION
        UIFunctions.selectStandardMenu(self, "btn_home")

        ## ==> START PAGE
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
        

        # USER ICON ==> SHOW HIDE
        #UIFunctions.userIcon(self, "WM", "url(:/16x16/icons/16x16/cil-user.png)", True)


        # MOVE WINDOW / MAXIMIZE / RESTORE
        def moveWindow(event):
        
            # IF MAXIMIZED CHANGE TO NORMAL
            if UIFunctions.returnStatus() == 1:
                UIFunctions.maximize_restore(self)

            # MOVE WINDOW
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        # WIDGET TO MOVE
        self.ui.frame_label_top_btns.mouseMoveEvent = moveWindow
    
        # LOAD DEFINITIONS
        UIFunctions.uiDefinitions(self)
        APPFunctions.appDefinitions(self)

        # show main window - end
        self.show()

    ########################################################################
    # menu button

    def Button_menu(self):
        # GET BT CLICKED
        btnWidget = self.sender()

        # PAGE HOME
        if btnWidget.objectName() == "btn_home":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
            UIFunctions.resetStyle(self, "btn_home")
            UIFunctions.labelPage(self, "Home")

        # PAGE ADD
        if btnWidget.objectName() == "btn_add":
             # remove what user wrote after save
            self.ui.lineEdit_add_name.setText("")
            self.ui.lineEdit_add_id.setText("")
            self.ui.lineEdit_add_password.setText("")

            self.ui.stackedWidget.setCurrentWidget(self.ui.page_add)
            UIFunctions.resetStyle(self, "btn_add")
            UIFunctions.labelPage(self, "Add")

        # PAGE WIDGETS
        if btnWidget.objectName() == "btn_retrieve":

            APPFunctions.restoreScrollArea(self, APPFunctions.get_account_data(self))
            
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_retrieve)
            UIFunctions.resetStyle(self, "btn_retrieve")
            UIFunctions.labelPage(self, "Retrieve N Manage")

            self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_guide)
            #page_specific

        # PAGE WIDGETS
        if btnWidget.objectName() == "btn_setting":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_setting)
            UIFunctions.resetStyle(self, "btn_setting")
            UIFunctions.labelPage(self, "Setting")

        btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))
        
    ##########################################################
    # checkbox
    ##########################################################
    def show_password(self):
        chbox = self.sender()
        if "retrieve" in chbox.objectName():
            if chbox.isChecked():
                self.ui.label_password_2.setText((APPFunctions.returnPassword(self)))
            else:
                self.ui.label_password_2.setText("*" * len(APPFunctions.returnPassword(self)))

        elif "add" in chbox.objectName():
            if chbox.isChecked():
                self.ui.lineEdit_add_password.setEchoMode(QLineEdit.Normal)
            else:
                self.ui.lineEdit_add_password.setEchoMode(QLineEdit.Password)
        
        elif "edit" in chbox.objectName():
            if chbox.isChecked():
                self.ui.lineEdit_edit_password.setEchoMode(QLineEdit.Normal)
            else:
                self.ui.lineEdit_edit_password.setEchoMode(QLineEdit.Password)

## START ==> APP EVENTS
    ########################################################################

    ## EVENT ==> MOUSE DOUBLE CLICK
    def eventFilter(self, watched, event):
        if watched == self.le and event.type() == QEvent.MouseButtonDblClick:
            print("pos: ", event.pos())


    ## EVENT ==> MOUSE CLICK
    ########################################################################
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()
        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')
        if event.buttons() == Qt.MidButton:
            print('Mouse click: MIDDLE BUTTON')


    ## EVENT ==> KEY PRESSED
    ########################################################################
    def keyPressEvent(self, event):
        print('Key: ' + str(event.key()) + ' | Text Press: ' + str(event.text()))


    ## EVENT ==> RESIZE EVENT
    ########################################################################
    def resizeEvent(self, event):
        self.resizeFunction()
        return super(MainWindow, self).resizeEvent(event)

    def resizeFunction(self):
        print('Height: ' + str(self.height()) + ' | Width: ' + str(self.width()))


    ########################################################################
    ## END ==> APP EVENTS
    ############################## ---/--/--- ##############################

if __name__ == "__main__":
    app = QApplication(sys.argv)
    QFontDatabase.addApplicationFont('fonts/segoeui.ttf')
    QFontDatabase.addApplicationFont('fonts/segoeuib.ttf')
    window = MainWindow()
    sys.exit(app.exec_())