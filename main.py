import os
import sys

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

from functions import *

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        
        # apply UI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

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

        # alignment setting
        self.ui.layout_menus.setAlignment(Qt.AlignTop)
        self.ui.layout_menu_bottom.setAlignment(Qt.AlignBottom)
        self.ui.verticalLayout_register.setAlignment(self.ui.pushButton_register, Qt.AlignCenter)
        self.ui.verticalLayout_home.setAlignment(self.ui.pushButton_home_button, Qt.AlignCenter)
        self.ui.gridLayout_password.setAlignment(self.ui.pushButton_chkey, Qt.AlignCenter)
        self.ui.verticalLayout_add_tag.setAlignment(self.ui.comboBox_add_tag, Qt.AlignCenter)
        self.ui.verticalLayout_add_tag.setAlignment(self.ui.pushButton_add_tag, Qt.AlignCenter)
        self.ui.verticalLayout_add_detail.setAlignment(self.ui.pushButton_add_detail, Qt.AlignHCenter)
        self.ui.verticalLayout_add_detail.setAlignment(self.ui.pushButton_btn_add, Qt.AlignHCenter)
        self.ui.verticalLayout_login.setAlignment(self.ui.pushButton_login, Qt.AlignCenter)
        self.ui.pushButton_home_button.setStyleSheet("color:#c8c8c8;margin-right:30")
        
        UIFunctions.addNewMenu(self, "Home Page", "btn_home", "url(:icons/icons/16x16/cil-home.png)", True)
        UIFunctions.addNewMenu(self, "Add", "btn_add", "url(:icons/icons/16x16/cil-pencil.png)", True)
        UIFunctions.addNewMenu(self, "Retrieve & Manage", "btn_retrieve", "url(:icons/icons/16x16/cil-magnifying-glass.png)", True)
        
        UIFunctions.addNewMenu(self, "Tag Management", "btn_tag", "url(:/icons/icons/16x16/cil-tags.png)", False)
        UIFunctions.addNewMenu(self, "Setting", "btn_setting", "url(:/icons/icons/16x16/cil-settings.png)", False)


        # if this is first execution, show register page
        if AppFunctions.getConfig()["is_first"] == 1:
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_register)
            UIFunctions.labelPage(self, "Register")
        # if not, show login? page
        else:
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_login)
            UIFunctions.labelPage(self, "Login")
        

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
        AppFunctions.appDefinitions(self)

        # show main window - end
        self.show()

    ########################################################################
    # menu button

    def buttonMenu(self):
        # GET BT CLICKEDX
        btnWidget = self.sender()

        # not login yet.
        if self.ui.stackedWidget.currentWidget() == self.ui.page_login or self.ui.stackedWidget.currentWidget() == self.ui.page_register:
            QMessageBox().information(self, 'PySide2', "Please type key first", QMessageBox.Ok)
            return

        # PAGE HOME
        if btnWidget.objectName() == "btn_home":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
            UIFunctions.resetStyle(self, "btn_home")
            UIFunctions.labelPage(self, "Home")

        # PAGE ADD
        if btnWidget.objectName() == "btn_add" or btnWidget.objectName() == "pushButton_btn_add":
            AppFunctions.page_add_tagSetting(self)

            self.ui.stackedWidget_add.setCurrentWidget(self.ui.page_add_tag)
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_add)
            UIFunctions.resetStyle(self, "btn_add")
            UIFunctions.labelPage(self, "Add")

        # PAGE retrieve
        if btnWidget.objectName() == "btn_retrieve":
            self.ui.lineEdit_search.setText("")
            AppFunctions.restoreScrollArea(self, AppFunctions.getAccountData(self), False)
            
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_retrieve)
            UIFunctions.resetStyle(self, "btn_retrieve")
            UIFunctions.labelPage(self, "Retrieve")

            # restore comboBox
            self.ui.comboBox_search.clear()

            self.ui.comboBox_search.addItem("All")
            for tag in AppFunctions.getAccountData(self)['TAG'].keys():
                self.ui.comboBox_search.addItem(tag)
            

            self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_guide)
            #page_specific

        # PAGE setting
        if btnWidget.objectName() == "btn_setting":
            self.ui.lineEdit_chkey_old.setText("")
            self.ui.lineEdit_chkey_new.setText("")

            self.ui.stackedWidget.setCurrentWidget(self.ui.page_setting)
            UIFunctions.resetStyle(self, "btn_setting")
            UIFunctions.labelPage(self, "Setting")
        
        # PAGE tag management
        if btnWidget.objectName() == "btn_tag":
            # self.ui.lineEdit_tag_name.setText("")
            # self.ui.lineEdit_slot.setText("")

            self.ui.stackedWidget.setCurrentWidget(self.ui.page_tag_management)
            UIFunctions.resetStyle(self, "btn_tag")
            UIFunctions.labelPage(self, "Tag Management")

            AppFunctions.restore_tag_slot(self)
            AppFunctions.restoreScrollArea2(self, AppFunctions.getAccountData(self), False)
        
        # PAGE setting
        if btnWidget.objectName() == "btn_login":

            self.ui.stackedWidget.setCurrentWidget(self.ui.page_login)
            UIFunctions.resetStyle(self, "btn_login")
            UIFunctions.labelPage(self, "Login")

        btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))
        
    ##########################################################
    # checkbox
    ##########################################################
    def showPassword(self):
        chbox = self.sender()
        number = chbox.objectName()[-1]

        if "checkBox_retrieve_show" in chbox.objectName():
            value =  dictValue[number]
            if chbox.isChecked():
                self.ui.frame_retrieve.findChild(QLabel, "label_value" + number).setText(value)
            else:
                self.ui.frame_retrieve.findChild(QLabel, "label_value" + number).setText("*" * len(value))

        elif "checkBox_add_detail" in chbox.objectName():
            if chbox.isChecked():
                self.ui.gridFrame_add_detail.findChild(QLineEdit, "lineEdit_add_detail" + number).setEchoMode(QLineEdit.Normal)
            else:
                self.ui.gridFrame_add_detail.findChild(QLineEdit, "lineEdit_add_detail" + number).setEchoMode(QLineEdit.Password)
        
        elif "checkBox_edit_show" in chbox.objectName():
            if chbox.isChecked():
                self.ui.frame_retrieve.findChild(QLineEdit, 'lineEdit_edit' + number).setEchoMode(QLineEdit.Normal)
            else:
                self.ui.frame_retrieve.findChild(QLineEdit, 'lineEdit_edit' + number).setEchoMode(QLineEdit.Password)

        elif "checkBox_login" in chbox.objectName():
            if chbox.isChecked():
                self.ui.horizontalFrame_login.findChild(QLineEdit, "lineEdit_login").setEchoMode(QLineEdit.Normal)
            else:
                self.ui.horizontalFrame_login.findChild(QLineEdit, "lineEdit_login").setEchoMode(QLineEdit.Password)

        elif "checkBox_register" in chbox.objectName():
            if chbox.isChecked():
                self.ui.horizontalFrame_register_password.findChild(QLineEdit, "lineEdit_register").setEchoMode(QLineEdit.Normal)
            else:
                self.ui.horizontalFrame_register_password.findChild(QLineEdit, "lineEdit_register").setEchoMode(QLineEdit.Password)



    ## EVENT ==> RESIZE EVENT
    ########################################################################
    def resizeEvent(self, event):
        self.resizeFunction()
        return super(MainWindow, self).resizeEvent(event)

    def resizeFunction(self):
        print('Height: ' + str(self.height()) + ' | Width: ' + str(self.width()))

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    ########################################################################
    ## END ==> APP EVENTS
    ############################## ---/--/--- ##############################

if __name__ == "__main__":
    app = QApplication(sys.argv)
    QFontDatabase.addApplicationFont('fonts/segoeui.ttf')
    QFontDatabase.addApplicationFont('fonts/segoeuib.ttf')
    window = MainWindow()
    sys.exit(app.exec_())