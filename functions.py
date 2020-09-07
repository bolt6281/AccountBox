import base64
import os
import json
import hashlib
import sys

import clipboard
from Crypto import Random
from Crypto.Cipher import AES

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QPropertyAnimation, QEasingCurve,QEvent, QTimer)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient, QFontDatabase)
from PySide2.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PySide2.QtWidgets import *

from main import *

# GLOBAL STATE varibale
# 0 : restored
# 1 : maximized
GLOBAL_STATE = 0
GLOBAL_TITLE_BAR = True
# GLOBAL TAG page variable
globalSlotCount = 0
globalSlotNumber = 0
globalFilterList = []

# GLOBAL key variable
GLOBAL_KEY = ""

# others
dictValue = {}

# COUNT INITAL MENU
count = 1

# AES Algorithm setting
BS = 16
pad = lambda s: s + (BS - len(s.encode('utf-8')) % BS) * chr(BS - len(s.encode('utf-8')) % BS)
unpad = lambda s : s[:-ord(s[len(s)-1:])]

class UIFunctions(MainWindow):
    ##################################################################################
    # START - GUI FUNCTIONS
    ##################################################################################
    # MAXIMIZE&RESTORE
    def maximize_restore(self):
        global GLOBAL_STATE
        status = GLOBAL_STATE
        if status == 0:
            # maximize
            self.showMaximized()
            GLOBAL_STATE = 1
            # remove spaces of each side
            self.ui.horizontalLayout.setContentsMargins(0, 0, 0, 0)
            # change tooltip and icon
            self.ui.btn_maximize_restore.setToolTip("Restore")
            self.ui.btn_maximize_restore.setIcon(QIcon(u":/icons/icons/16x16/cil-window-restore.png"))
            self.ui.frame_info1.setStyleSheet("background-color: rgb(27, 29, 35)")
            # hide size grip
            self.ui.frame_size_grip.hide()
        else:
            GLOBAL_STATE = 0
            # restore(normalize)
            self.showNormal()
            self.resize(self.width() + 1, self.height() + 1)
            # if there is no margin, it's maximized
            # self.ui.horizontalLayout.setContentsMargins(10, 10, 10, 10)
            self.ui.horizontalLayout.setContentsMargins(0, 0, 0, 0)
            self.ui.btn_maximize_restore.setToolTip("Maximize")
            self.ui.btn_maximize_restore.setIcon(QIcon(u":/icons/icons/16x16/cil-window-maximize.png"))
            self.ui.frame_info1.setStyleSheet("background-color: rgba(27, 29, 35, 200)")
            self.ui.frame_size_grip.show()

    ##################################################################################
    # return status
    def returnStatus():
        return GLOBAL_STATE

    ##################################################################################
    # set status
    def setStatus(status):
        global GLOBAL_STATE
        GLOBAL_STATE = status

    ##################################################################################
    # enable maximun size
    def enableMaximumSize(self, width, height):
        #이게 무슨 뜻
        if width != '' and height != '':
            self.setMaximunSize(QSize(width, height))
            self.ui.frame_size_grip.hide()
            self.ui.btn_maximize_restore.hide()

    ##################################################################################
    # when toggle button is pressed
    def toggleMenu(self, maxWidth, enable):
        if enable:
            # get current width
            current_width = self.ui.frame_left_menu.width()
            maxExtend = maxWidth
            standard = 70

            # set max width
            # if it's not extented now
            if current_width == 70:
                widthExtended = maxExtend
            # if it's extendted now
            else:
                widthExtended = standard

            # animation
            self.animation = QPropertyAnimation(self.ui.frame_left_menu, b"minimumWidth")
            # animate for 300ms
            self.animation.setDuration(300)
            self.animation.setStartValue(current_width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QEasingCurve.InOutQuart)
            self.animation.start()

    ##################################################################################
    # set title bar status
    def removeTitleBar(status):
        global GLOBAL_TITLE_BAR
        GLOBAL_TITLE_BAR = status

    ##################################################################################
    # set title bar text
    def labelTitle(self, text):
        self.ui.label_title_bar_top.setText(text)

    ##################################################################################
    # set text
    def labelDescription(self, text):
        self.ui.label_fileloc.setText(text)

    ##################################################################################
    # define add function
    def addNewMenu(self, name, objName, icon, isTopMenu):
        # set font
        font = QFont()
        font.setFamily(u"Segoe UI")
        # make button
        button = QPushButton(str(count), self)
        # set object name
        button.setObjectName(objName)
        # 무슨 뜻
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(button.sizePolicy().hasHeightForWidth())
        button.setSizePolicy(sizePolicy3)
        # set minimum size
        button.setMinimumSize(QSize(0, 70))
        # set layout direction
        button.setLayoutDirection(Qt.LeftToRight)
        # set button's font
        button.setFont(font)

        # ui_styles : set icon
        button.setStyleSheet(Style.style_bt_standard.replace('ICON_REPLACE', icon))
        
        # set name of button, tooltip
        button.setText(name)
        button.setToolTip(name)
        # set function of the button
        button.clicked.connect(self.buttonMenu)
        #add button from top
        if isTopMenu:
            self.ui.layout_menus.addWidget(button)
        #add button from bottom
        else:
            self.ui.layout_menu_bottom.addWidget(button)
    

    ##################################################################################
    # set menu button style when menu(button) is selected(pressed)
    # selected
    def selectMenu(getStyle):
        select = getStyle + ("QPushButton { border-right: 7px solid rgb(44, 49, 60); }")
        return select

    # deselected
    def deselectMenu(getStyle):
        deselect = getStyle.replace("QPushButton { border-right: 7px solid rgb(44, 49, 60); }", "")
        return deselect

    # def selectStandardMenu(self, widget):
    #     for w in self.ui.frame_left_menu.findChildren(QPushButton):
    #         if w.objectName() == widget:
    #             w.setStyleSheet(UIFunctions.selectMenu(w.styleSheet()))

    # reset select
    def resetStyle(self, widget):
        for w in self.ui.frame_left_menu.findChildren(QPushButton):
            if w.objectName() != widget:
                w.setStyleSheet(UIFunctions.deselectMenu(w.styleSheet()))

    # change label page that let user know where he is
    def labelPage(self, text):
        newText = '| ' + text.upper()
        self.ui.label_where.setText(newText)
    
    ##################################################################################
    # set user icon above the bottom-side menus
    # but I won't use this at this project
    def userIcon(self, initialsTooltip, icon, showHide):
        if showHide:
            # set text
            self.ui.label_user_icon.setText(initialsTooltip)

            # set icon
            if icon:
                style = self.ui.label_user_icon.styleSheet()
                setIcon = "QLabel { background-image: " + icon + "; }"
                self.ui.label_user_icon.setStyleSheet(style + setIcon)
                self.ui.label_user_icon.setText('')
                self.ui.label_user_icon.setToolTip(initialsTooltip)
        else:
            self.ui.label_user_icon.hide()
    ##################################################################################
    # END - GUI FUNCTIONS
    # START - UI DEFINITIONS 사실상 이게 메인
    ##################################################################################

    def uiDefinitions(self):
        # if user clicked title bar twice, restore or maximize
        def doubleClickMaximizeRestore(event):
            if event.type() == QEvent.MouseButtonDblClick:
                QTimer.singleShot(250, lambda: UIFunctions.maximize_restore(self))

        # title bar processing
        # remove
        if GLOBAL_TITLE_BAR:
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)
            self.ui.frame_label_top_btns.mouseDoubleClickEvent = doubleClickMaximizeRestore
        # not remove
        else:
            self.ui.horizontalLayout.setContentsMargins(0, 0, 0, 0)
            # add margin for make defalut title bar space
            self.ui.frame_label_top_btns.setContentsMargins(8, 0, 0, 5)
            # increase minimum height for make defalut title bar space
            self.ui.frame_label_top_btns.setMinimumHeight(42)
            # remove all buttons I made instead of default buttons
            self.ui.frame_icon_top_bar.hide()
            self.ui.frame_btns_right.hide()
            self.ui.frame_size_grip.hide()

        # drop shadow - 인싸 프로그램의 필수 조건
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(17)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 150))
        self.ui.frame_main.setGraphicsEffect(self.shadow)

        # make resize grip
        self.sizegrip = QSizeGrip(self.ui.frame_size_grip)
        self.sizegrip.setStyleSheet("width: 20px; height: 20px; margin 0px; padding: 0px;")



        # define functions of title bar buttons
        # minimize button
        self.ui.btn_minimize.clicked.connect(lambda: self.showMinimized())

        # maximize/restore button
        self.ui.btn_maximize_restore.clicked.connect(lambda: UIFunctions.maximize_restore(self))

        # close button
        self.ui.btn_close.clicked.connect(lambda: self.close())



class AppFunctions(MainWindow):
    
    ####################################################################################################################################### 
    # GET/SET ACCOUNT DATA
    #######################################################################################################################################

    def getConfig():
        cwd = os.getcwd()

        #############################################
        # load config file
        # check if there is config file | if not, make new one
        if not os.path.exists(cwd+"\\config.json"):
            with open("config.json", "w") as json_file:
                defaultLoc = cwd+"\\account_data.json"
                defaultConfig = {"AccountFileLoc": defaultLoc, "is_first": 1}
                json.dump(defaultConfig, json_file)
            return defaultConfig
        else:
            # load config
            with open(cwd+'\\config.json', 'r') as json_file:
                config = json.loads(json_file.read())
            return config

    def getAccountDataLoc():
        file_loc = AppFunctions.getConfig()['AccountFileLoc']
        return file_loc

    # return json file
    def getAccountData(self):

        # load account data
        file_loc = AppFunctions.getAccountDataLoc()
        
        # if file_loc is wrong or accountData file has been removed
        # and edit config file as default
        if not os.path.exists(file_loc):
            # don't show messagebox
            if self.ui.stackedWidget.currentWidget() == self.ui.page_register:
                pass
            else:
                self.ui.label_current.setText("Account file is disappeared. Please reassign account file or restore")
                QMessageBox().warning(self, 'PySide2', "Account file is disappeared. Please reassign account file or restore", QMessageBox.Ok)

        try:
            with open(file_loc, "r") as json_file:
                accountData = json.loads(json_file.read())
                
            # decrypt
            for service in accountData['DATA'].keys():
                for key in accountData['DATA'][service].keys():
                    if key == 'tag':
                        continue
                    if AppFunctions.isInvisible(self, service, key, accountData):
                        # decrypt this data
                        encrypted_data = accountData['DATA'][service][key]
                        decrypted_data = AppFunctions.decrypt(encrypted_data)
                        accountData['DATA'][service][key] = decrypted_data.decode('utf-8')
            return accountData
        # selected file is not account file(json file)
        except ValueError:
            self.ui.label_current.setText("Selected file is not an account file. Please reassign account file or restore")
            QMessageBox().warning(self, 'PySide2', "Account file is disappeared. Please reassign account file or restore", QMessageBox.Ok)
            return {}
        except Exception as e:
            print(e)
            return {}

    def restoreData(self):
        cwd = os.getcwd()

        # set accountData as default(create empty data)
        defaultLoc = cwd+"\\account_data.json"
        with open(defaultLoc, "w") as json_file:
            json.dump({ "TAG" : {"common" : {"ID" : "visible", "Password" : "invisible"}}, "DATA" : {}}, json_file)

        # set config file as default
        with open("config.json", "w") as json_file:
            defaultLoc = cwd+"\\account_data.json"
            json.dump({"AccountFileLoc": defaultLoc, "is_first": 0}, json_file)

        self.ui.label_current.setText("Current : "+defaultLoc)
    
    def isInvisible(self, selectedService, key, accountData):
        selectedTag = accountData['DATA'][selectedService]['tag']
        return accountData['TAG'][selectedTag][key] == "invisible"

    def buttonResetKey(self):
        old = self.ui.lineEdit_chkey_old.text()
        new = self.ui.lineEdit_chkey_new.text()
        print(old, new)
        if old.strip() == "" or new.strip() == "":
            QMessageBox().information(self, 'PySide2', "Please type key", QMessageBox.Ok)
            return

        # ask again
        reply = QMessageBox
        reply.setText("If you typed wrong key, It'd be hard to recover your data.\nCheck old/new keys one more time")
        reply.addButton(QtGui.QPushButton('No thanks'), QMessageBox.NoRole)
        reply.addButton(QtGui.QPushButton("I'll check"), QMessageBox.OkRole)
        
        if reply == QMessageBox.Ok:
            return
        else:
            # change key
            global GLOBAL_KEY
            GLOBAL_KEY = old
            # decrypt data with old key
            accountData = AppFunctions.getAccountData(self)

            # change key
            GLOBAL_KEY  = new

            # encrypt data with new key
            for service in accountData['DATA'].keys():
                for key in accountData['DATA'][service].keys():
                    if key == 'tag':
                        continue
                    if AppFunctions.isInvisible(self, service, key, accountData):
                        # encrypt this data
                        decrypted_data = accountData['DATA'][service][key]
                        # decode it for save data with json
                        accountData['DATA'][service][key] = AppFunctions.encrypt(decrypted_data).decode('utf-8')

            with open(AppFunctions.getAccountDataLoc(), "w") as json_file:
                        json.dump(accountData, json_file)

            QMessageBox().information(self, 'PySide2', "Key is changed successfully", QMessageBox.Ok)
    ####################################################################################################################################### 
    # Page - register & login & home
    #######################################################################################################################################

    def buttonRegister(self):
        key = self.ui.lineEdit_register.text()
        if key.strip() == "":
            QMessageBox().information(self, 'PySide2', "Please type key", QMessageBox.Ok)
            return

        global GLOBAL_KEY
        GLOBAL_KEY = key
        AppFunctions.restoreData(self)

        UIFunctions.labelPage(self, "Home")
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
    
    def buttonNotFirst(self):
        # ask again
        QMessageBox().information(self, 'PySide2', "Select your data", QMessageBox.Ok)

        isSuccess = AppFunctions.openFolder(self, isNotLoginYet=True)
        if isSuccess == False:
            return
        self.ui.lineEdit_register.setText("")

        UIFunctions.labelPage(self, "Login")
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_login)

    def buttonChangeKey(self):
        self.ui.lineEdit_login.setText("")
        UIFunctions.labelPage(self, "Login")
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_login)

    def buttonLogin(self):
        key = self.ui.lineEdit_login.text()
        if key.strip() == "":
            QMessageBox().information(self, 'PySide2', "Please type key.\nIt's necessary for you", QMessageBox.Ok)
            return

        global GLOBAL_KEY
        GLOBAL_KEY = key

        UIFunctions.labelPage(self, "Home")
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)

    ####################################################################################################################################### 
    #SCROLL AREA - services
    #######################################################################################################################################
    def restoreScrollArea(self, accountData, is_initial = False):
        
        if is_initial:
            self.ui.scrollArea.setStyleSheet(Style.style_scroll_area)
        else:
            # restore scroll area
            for i in reversed(range(self.ui.verticalLayout_search.count())): 
                self.ui.verticalLayout_search.itemAt(i).widget().setParent(None)

        try:
            for name in accountData['DATA'].keys():
                AppFunctions.buttonAddService(self, name)
        # something is wrong with account data
        except KeyError:
            pass
            
    def buttonAddService(self, name):

        # set font
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)

        # parent = scrollAreaWidgetContents
        button = QPushButton(name, self)
        # button.setObjectName("btn_"+list(accountData.keys())[idx])
        button.setMinimumSize(QSize(365, 70))
        button.setMaximumSize(QSize(365, 70))
        button.setFont(font)
        button.setStyleSheet(Style.style_scroll_area_button)
        button.clicked.connect(lambda: AppFunctions.buttonService(self, name))
        button.setText(QCoreApplication.translate("MainWindow", name, None))
        self.ui.verticalLayout_search.addWidget(button)

    ####################################################################################################################################### 
    #SCROLL AREA - tags
    #######################################################################################################################################
    def restoreScrollArea2(self, accountData, is_initial = False):
        
        if is_initial:
            self.ui.scrollArea_tag.setStyleSheet(Style.style_scroll_area)
        else:
            # restore scroll area
            for i in reversed(range(self.ui.verticalLayout_tag.count())): 
                self.ui.verticalLayout_tag.itemAt(i).widget().setParent(None)

        try:    
            for name in accountData['TAG'].keys():
                AppFunctions.addTag(self, name)
        # something is wrong with account data
        except KeyError:
            pass

    def addTag(self, name):
        # set font
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(15)
        font.setWeight(75)

        horizontalWidget = QWidget(self)
        horizontalWidget.setMaximumSize(QSize(16777215, 70))
        horizontalWidget.setStyleSheet(u"border-radius : 7px;\n"
                                        "border: 3px solid rgb(34, 36, 43);\n"
                                        "")
        horizontalWidget_tag = QHBoxLayout(horizontalWidget)
        horizontalWidget_tag.setSpacing(0)
        label_tag = QLabel(horizontalWidget)
        label_tag.setFont(font)
        label_tag.setStyleSheet(u"border:0;")
        label_tag.setMargin(9)
        label_tag.setText(QCoreApplication.translate("MainWindow", name, None))

        horizontalWidget_tag.addWidget(label_tag)

        font.setPointSize(13)
        pushButton_tag = QPushButton(horizontalWidget)
        pushButton_tag.setMinimumSize(QSize(100, 40))
        pushButton_tag.setMaximumSize(QSize(100, 40))
        pushButton_tag.setFont(font)
        pushButton_tag.setStyleSheet(u"border:0;")

        pushButton_tag.clicked.connect(lambda: AppFunctions.buttonDeleteTag(self, name))
        pushButton_tag.setText(QCoreApplication.translate("MainWindow", "Delete", None))

        horizontalWidget_tag.addWidget(pushButton_tag)


        self.ui.verticalLayout_tag.addWidget(horizontalWidget)

    #######################################################################################################################################
    # Others(Button, ComboBox, etc.)
    #######################################################################################################################################

    ###############################################################################################
    # retrieve
    def buttonService(self, selectedService):
        # delete existing edit button and cancel button  
        for i in reversed(range(self.ui.horizontalLayout_retrieve.count())): 
            self.ui.horizontalLayout_retrieve.itemAt(i).widget().setParent(None)
        
        font = QFont()
        font.setPointSize(13)
        font.setFamily(u"Segoe UI")
        font.setWeight(75)

        # set Edit button
        pushButton_retrieve_edit = QPushButton(self)
        pushButton_retrieve_edit.setObjectName("pushButton_retrieve_edit")
        pushButton_retrieve_edit.setMinimumSize(QSize(150, 0))
        pushButton_retrieve_edit.setMaximumSize(QSize(150, 40))
        pushButton_retrieve_edit.setFont(font)
        pushButton_retrieve_edit.setText("Edit")
        pushButton_retrieve_edit.clicked.connect(lambda:AppFunctions.buttonEdit(self))
        self.ui.horizontalLayout_retrieve.addWidget(pushButton_retrieve_edit, alignment = Qt.AlignCenter)

        # clear layouts
        for i in reversed(range(self.ui.gridLayout_retrieve.count())): 
            self.ui.gridLayout_retrieve.itemAt(i).widget().setParent(None)

        accountData = AppFunctions.getAccountData(self)

        selectedTag = accountData['DATA'][selectedService]['tag']
        self.ui.label_retrieve_tag.setText("#"+selectedTag)
        self.ui.label_service_name.setText(selectedService)

        #----------------------------------------------------------
        # set frame_retrieve
        for number, key in enumerate(accountData["DATA"][selectedService].keys()):
            if key == 'tag':
                continue
            AppFunctions.buttonServiceHelper(self, accountData, selectedService, selectedTag, number-1, key, font)

        if number+1 == 1:
            self.ui.frame_retrieve.setMinimumSize(QSize(0, 200))
            self.ui.frame_retrieve.setMaximumSize(QSize(16777215, 200))
        else:
            self.ui.frame_retrieve.setMinimumSize(QSize(0, (number+1)*100))
            self.ui.frame_retrieve.setMaximumSize(QSize(16777215, (number+1)*100))

        self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_specific)

    def buttonServiceHelper(self, accountData, selectedService, selectedTag, number, key, font):
        global dictValue

        value = accountData['DATA'][selectedService][key]
        dictValue[str(number)] = value
        is_visible = (accountData['TAG'][selectedTag][key] == "visible")

        # label_key------------------------------------
        label_key = QLabel(self)
        label_key.setObjectName("label_key" + str(number))
        label_key.setMinimumSize(QSize(80, 0))
        label_key.setMaximumSize(QSize(80, 16777215))
        
        label_key.setFont(font)
        label_key.setStyleSheet("border:None;")
        label_key.setAlignment(Qt.AlignCenter)
        # long
        if len(key) >= 7 and " " in key:
            key = key.replace(" ", "\n")
        label_key.setText(key)
        self.ui.gridLayout_retrieve.addWidget(label_key, number, 0)

        # label_value------------------------------------
        label_value = QLabel(self)
        label_value.setObjectName("label_value" + str(number))
        label_value.setFont(font)
        label_value.setStyleSheet("border-radius : 0;")
        label_value.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        if is_visible:
            label_value.setText(value)
        else:
            label_value.setText("*" * len(value))
        self.ui.gridLayout_retrieve.addWidget(label_value, number, 1)

        # checkBox_edit_show------------------------------------

        font.setPointSize(11)
        font.setWeight(50)

        if not is_visible:
            checkBox_edit_show = QCheckBox(self)
            checkBox_edit_show.setObjectName("checkBox_retrieve_show" + str(number))
            checkBox_edit_show.setMaximumSize(QSize(70, 30))
            checkBox_edit_show.stateChanged.connect(self.showPassword)
            checkBox_edit_show.setFont(font)
            checkBox_edit_show.setText("Show")

            self.ui.gridLayout_retrieve.addWidget(checkBox_edit_show, number, 2)

        # pushButton_clipboard------------------------------------
        pushButton_clipboard = QPushButton(self)
        pushButton_clipboard.setObjectName("pushButton_clipboard" + str(number))
        pushButton_clipboard.setMinimumSize(QSize(0, 50))
        pushButton_clipboard.setMaximumSize(QSize(100, 16777215))
        pushButton_clipboard.setFont(font)
        pushButton_clipboard.setText("copy to\nclipboard")
        pushButton_clipboard.clicked.connect(lambda: AppFunctions.buttonClipboard(self, pushButton_clipboard.objectName(), value))
        self.ui.gridLayout_retrieve.addWidget(pushButton_clipboard, number, 3)
        font.setPointSize(13)
        font.setWeight(75)

    def buttonClipboard(self, objectName, value):
        clipboard.copy(value)
        self.ui.frame_retrieve.findChild(QPushButton, objectName).setText("copied")

    def buttonDeleteAccount(self):
        service_name = self.ui.label_service_name.text()
        accountData = AppFunctions.getAccountData(self)
        accountData['DATA'].pop(service_name, None)

        # encrypt
        for service in accountData['DATA'].keys():
            for key in accountData['DATA'][service].keys():
                if key == 'tag':
                    continue
                if AppFunctions.isInvisible(self, service, key, accountData):
                    # encrypt this data
                    decrypted_data = accountData['DATA'][service][key]
                    # decode it for save data with json
                    accountData['DATA'][service][key] = AppFunctions.encrypt(decrypted_data).decode('utf-8')
                    
        with open(AppFunctions.getAccountDataLoc(), "w") as json_file:
            json.dump(accountData, json_file)

        # go back to guide_pages
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_guide)
        # restore scroll_area
        AppFunctions.restoreScrollArea(self, accountData, False)

    # show what user searched( restore scroll area )
    def search(self):
        accountData = AppFunctions.getAccountData(self)
        keyword = self.ui.lineEdit_search.text()
        tag = self.ui.comboBox_search.currentText()

        service_names = list(accountData['DATA'].keys())
        for service_name in service_names:
            if not (keyword.lower() in service_name.lower()) or (accountData['DATA'][service_name]['tag'] != tag and tag != "All"):
                accountData['DATA'].pop(service_name, None)
        AppFunctions.restoreScrollArea(self, accountData)

    def buttonEdit(self):
        selectedService = self.ui.label_service_name.text()
        
        accountData = AppFunctions.getAccountData(self)

        font = QFont()
        font.setPointSize(13)
        font.setFamily(u"Segoe UI")
        font.setWeight(75)

        for number, key in enumerate(accountData["DATA"][selectedService].keys()):
            if key == 'tag':
                continue
            AppFunctions.buttonEditHelper(self, number-1)

        # remove edit button and add save button
        self.ui.horizontalFrame_retrieve.findChild(QPushButton, "pushButton_retrieve_edit").setParent(None)

        # add cancel button
        pushButton_retrieve_cancel = QPushButton(self)
        pushButton_retrieve_cancel.setObjectName("pushButton_retrieve_cancel")
        pushButton_retrieve_cancel.setMaximumSize(QSize(150, 40))
        pushButton_retrieve_cancel.setFont(font)
        pushButton_retrieve_cancel.setText("Cancel")
        pushButton_retrieve_cancel.clicked.connect(lambda:AppFunctions.buttonCancelEdit(self))

        self.ui.horizontalLayout_retrieve.addWidget(pushButton_retrieve_cancel)

        # add save button
        pushButton_edit_save = QPushButton(self)
        pushButton_edit_save.setObjectName("pushButton_edit_save")
        pushButton_edit_save.setMaximumSize(QSize(150, 40))
        pushButton_edit_save.setFont(font)
        pushButton_edit_save.setText("Save")
        pushButton_edit_save.clicked.connect(lambda:AppFunctions.buttonEditSave(self, selectedService))

        self.ui.horizontalLayout_retrieve.addWidget(pushButton_edit_save)
        # 이거 끝나고 암호화

        # change pushbutton's function to save button

    def buttonCancelEdit(self):
        # delete cancel button  
        self.ui.horizontalFrame_retrieve.findChild(QPushButton, "pushButton_retrieve_cancel").setParent(None)

        selectedService = self.ui.label_service_name.text()
        AppFunctions.buttonService(self, selectedService)

    def buttonEditHelper(self, number):
        font = QFont()
        font.setPointSize(13)
        font.setFamily(u"Segoe UI")
        font.setWeight(75)

        # change label to lineedit
        value = dictValue[str(number)]

        self.ui.frame_retrieve.findChild(QLabel, "label_value"+str(number)).deleteLater()

        lineEdit = QLineEdit(self)
        lineEdit.setObjectName('lineEdit_edit' + str(number))
        lineEdit.setMinimumSize(QSize(0, 40))
        lineEdit.setMaximumSize(QSize(16777215, 40))
        lineEdit.setFont(font)
        lineEdit.setStyleSheet(Style.style_line_edit)
        lineEdit.setText(value)
        self.ui.gridLayout_retrieve.addWidget(lineEdit, number, 1)

        # remove pushbutton(clipboard)
        self.ui.frame_retrieve.findChild(QPushButton, "pushButton_clipboard" + str(number)).deleteLater()

        # remove existing checkbox
        try: 
            self.ui.frame_retrieve.findChild(QCheckBox, "checkBox_retrieve_show" + str(number)).deleteLater()
        except:
            pass
        else:
            lineEdit.setEchoMode(QLineEdit.Password)

            font.setWeight(50)
            # add new one
            checkBox_edit_show = QCheckBox(self)
            checkBox_edit_show.setObjectName("checkBox_edit_show" + str(number))
            checkBox_edit_show.setMaximumSize(QSize(70, 30))
            checkBox_edit_show.stateChanged.connect(self.showPassword)
            checkBox_edit_show.setFont(font)
            checkBox_edit_show.setText("Show")
            self.ui.gridLayout_retrieve.addWidget(checkBox_edit_show, number, 2)
            font.setWeight(75)

    def buttonEditSave(self, selectedService):
        # accountData is tag-removed data
        accountData = AppFunctions.getAccountData(self)
        dictTemp = {'tag' : accountData["DATA"][selectedService]['tag']}
        for number, key in enumerate(accountData["DATA"][selectedService].keys()):
            if key == 'tag':
                continue
            txt = self.ui.frame_retrieve.findChild(QLineEdit, 'lineEdit_edit'+str(number-1)).text()
            if txt.strip() == "":
                QMessageBox().information(self, 'PySide2', "Please fill all blanks", QMessageBox.Ok)
                return
            dictTemp[key] = txt

        accountData['DATA'][selectedService] = dictTemp

        # encrypt
        for service in accountData['DATA'].keys():
            for key in accountData['DATA'][service].keys():
                if key == 'tag':
                    continue
                if AppFunctions.isInvisible(self, service, key, accountData):
                    # encrypt this data
                    decrypted_data = accountData['DATA'][service][key]
                    # decode it for save data with json
                    accountData['DATA'][service][key] = AppFunctions.encrypt(decrypted_data).decode('utf-8')

        # save it
        with open(AppFunctions.getAccountDataLoc(), "w") as json_file:
            json.dump(accountData, json_file)

        AppFunctions.buttonService(self, selectedService)

    ###############################################################################################
    # tag

    def buttonTag(self, selected_tag):
        tag_name = AppFunctions.getAccountData(self)["TAG"][selected_tag]

        self.ui.lineEdit_tag_name.setText("")

    def buttonDeleteTag(self, tag_name):

        accountData = AppFunctions.getAccountData(self)
        # if there is data using selected tag, cannot delete this tag before the data get removed
        for service_name in accountData['DATA'].keys():
            if accountData['DATA'][service_name]['tag'] == tag_name:
                QMessageBox().information(self, 'PySide2', "remove every data using '"+str(tag_name)+"' tag before delete tag", QMessageBox.Ok)
                return

        # ask again
        reply = QMessageBox.question(self, 'MessageBox', "Are you sure?", QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.No:
            return

        accountData['TAG'].pop(tag_name, None)

        # encrypt
        for service in accountData['DATA'].keys():
            for key in accountData['DATA'][service].keys():
                if key == 'tag':
                    continue
                if AppFunctions.isInvisible(self, service, key, accountData):
                    # encrypt this data
                    decrypted_data = accountData['DATA'][service][key]
                    # decode it for save data with json
                    accountData['DATA'][service][key] = AppFunctions.encrypt(decrypted_data).decode('utf-8')

        with open(AppFunctions.getAccountDataLoc(), "w") as json_file:
            json.dump(accountData, json_file)

        # restore scroll_area
        AppFunctions.restoreScrollArea2(self, accountData, False)

    def deleteTagSlot(self, current_count, slot_number, immune_list):
        # 먼저 생성된 위젯이 먼저 삭제되면 gridlayout_slot의 위젯 개수가 바뀌어서 삭제된 위젯보다 뒤에 생성된 위젯을 가리키는 인덱스가 잘못되게 되므로
        # 삭제되는 위젯보다 나중에 생성된 위젯의 인덱스를 한 칸 당겨서 계산해야 올바르게 작동한다.
        # 때문에 한 위젯이 삭제될 경우 그 위젯의 slot_number를 global filter에 저장하여 이 slot_number보다 큰 slot_number를 가지고 있는 위젯을 삭제할 때
        # 인덱스에 추가적인 값을 빼는 방법으로 해당 위젯을 지정하고, 신규 위젯은 이 필터에 영향을 받으면 안되므로 기존 filter에 영향을 받지 않도록 immune_filter를 만들어준다.

        global globalSlotCount
        global globalFilterList

        # cannot remove all slots
        if globalSlotCount == 1:
            QMessageBox().warining(self, 'PySide2', "You should left at least 1 slot", QMessageBox.Ok)
            return

        stack = 0

        # immune_list에도 있는 요소는 패스하고 immune_list에 없는 요소가 발견될 때마다 스택 추가
        for deleted_number in globalFilterList :
            if deleted_number in immune_list:
                continue
            if deleted_number < slot_number :
                stack+=1

        for i in range(3):
            # remove last 3 widgets
            self.ui.gridLayout_slot.itemAt( current_count - i - 1 - stack*3).widget().deleteLater()

        globalFilterList.append(slot_number)
        
        globalSlotCount-=1

    def addSlot(self):
        global globalSlotCount
        global globalFilterList
        global globalSlotNumber

        if globalSlotCount == 5:
            QMessageBox.warining(self, 'PySide2', "You don't need that much slots", QMessageBox.Ok)
            return

        current_count = self.ui.gridLayout_slot.count()

        # set font
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(12)

        # set lineEdit
        lineEdit_slot = QLineEdit(self.ui.gridFrame_slot)
        lineEdit_slot.setMinimumSize(QSize(0, 40))
        lineEdit_slot.setMaximumSize(QSize(16777215, 40))
        lineEdit_slot.setFont(font)
        lineEdit_slot.setStyleSheet(Style.style_line_edit)

        # set pushButton
        pushButton_slot = QPushButton(self.ui.gridFrame_slot)
        pushButton_slot.setMinimumSize(QSize(100, 40))
        pushButton_slot.setMaximumSize(QSize(100, 40))
        pushButton_slot.setFont(font)
        pushButton_slot.setStyleSheet(u"")
        pushButton_slot.setText("Delete")

        # 여태까지의 필터에 대해 면역
        immune_list = globalFilterList[:]
        slot_number = globalSlotNumber
        pushButton_slot.clicked.connect(lambda: AppFunctions.deleteTagSlot(self, current_count+3, slot_number, immune_list))
        
        # set checkbox
        checkBox_slot = QCheckBox(self.ui.gridFrame_slot)
        checkBox_slot.setMinimumSize(QSize(100, 40))
        checkBox_slot.setMaximumSize(QSize(100, 40))
        checkBox_slot.setFont(font)
        checkBox_slot.setText("Invisible")


        self.ui.gridLayout_slot.addWidget(pushButton_slot, globalSlotNumber, 3, 1, 1)
        self.ui.gridLayout_slot.addWidget(checkBox_slot, globalSlotNumber, 2, 1, 1)
        self.ui.gridLayout_slot.addWidget(lineEdit_slot, globalSlotNumber, 0, 1, 1)

        globalSlotCount+=1
        globalSlotNumber+=1

    def create_tag_button(self):
        tag_name = self.ui.lineEdit_tag_name.text()

        if tag_name.strip() == "":
            QMessageBox().information(self, 'PySide2', "Please fill the 'Tag name' blank", QMessageBox.Ok)
            return

        accountData = AppFunctions.getAccountData(self)
        
        # if the tag is already existing, cannot do this
        if tag_name in accountData['TAG'].keys():
            QMessageBox().information(self, 'PySide2', "There is same-named tag already.\nPlease delete existing one.", QMessageBox.Ok)
            return

        dict_tmp = {}
        for i in range(int(self.ui.gridLayout_slot.count()/3)):
            # QPushButton
            #self.ui.gridLayout_slot.itemAt(i*3).widget()
            # QCheckBox
            visiblity = "invisible" if self.ui.gridLayout_slot.itemAt(i*3 + 1).widget().isChecked() else "visible"
            # QLineEdit
            text = self.ui.gridLayout_slot.itemAt(i*3 + 2).widget().text()
            if text == "tag":
                QMessageBox().information(self, 'PySide2', "You can't use 'tag' word", QMessageBox.Ok)
                return

            if text.strip() == "":
                QMessageBox().information(self, 'PySide2', "Please fill all blanks", QMessageBox.Ok)
                return
            dict_tmp[text] = visiblity

        accountData['TAG'][tag_name] = dict_tmp

        # encrypt
        for service in accountData['DATA'].keys():
            for key in accountData['DATA'][service].keys():
                if key == 'tag':
                    continue
                if AppFunctions.isInvisible(self, service, key, accountData):
                    # encrypt this data
                    decrypted_data = accountData['DATA'][service][key]
                    # decode it for save data with json
                    accountData['DATA'][service][key] = AppFunctions.encrypt(decrypted_data).decode('utf-8')

        with open(AppFunctions.getAccountDataLoc(), "w") as json_file:
            json.dump(accountData, json_file)

        AppFunctions.restoreScrollArea2(self, accountData)
        AppFunctions.restore_tag_slot(self)

    def restore_tag_slot(self):
        global globalSlotCount
        global globalSlotNumber
        global globalFilterList

        globalSlotCount = 0
        globalSlotNumber = 0
        globalFilterList = []

        for i in reversed(range(self.ui.gridLayout_slot.count())): 
            self.ui.gridLayout_slot.itemAt(i).widget().setParent(None)

        self.ui.lineEdit_tag_name.setText("")

        AppFunctions.addSlot(self)

    ###############################################################################################
    # add

    def page_add_tagSetting(self):

        tags = AppFunctions.getAccountData(self)['TAG'].keys()
        self.ui.comboBox_add_tag.clear()
        for tag in tags:
            self.ui.comboBox_add_tag.addItem(tag)
        self.ui.stackedWidget_add.setCurrentWidget(self.ui.page_add_tag)

    def buttonSelectTag(self):
        selected_tag = self.ui.comboBox_add_tag.currentText()

        # clear layout
        for i in range(self.ui.gridLayout_add_detail.count()): 
            self.ui.gridLayout_add_detail.itemAt(i).widget().deleteLater()
            
        accountData = AppFunctions.getAccountData(self)

        # add service name slot
        # lineEdit_add_detail1
        AppFunctions.addAddSlot(self, 1, "Service Name")

        # add other slots
        # each : ID, Password, bank account, etc.
        for i, each in enumerate(accountData['TAG'][selected_tag].keys()):
            AppFunctions.addAddSlot(self, i+2, each, accountData['TAG'][selected_tag][each] == "invisible")
        
        self.ui.stackedWidget_add.setCurrentWidget(self.ui.page_add_detail)
            
    def addAddSlot(self, number, each, is_invisible = False):
        # set font
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(15)

        # set unique objectName
        label_add = QLabel(self)
        label_add.setMinimumSize(QSize(0, 50))
        label_add.setMaximumSize(QSize(16777215, 50))
        label_add.setFont(font)
        label_add.setStyleSheet(u'color:#c8c8c8;')
        label_add.setText(each)
        label_add.setAlignment(Qt.AlignCenter)

        # set lineEdit
        lineEdit_add_detail = QLineEdit(self)
        # set unique objectName
        lineEdit_add_detail.setObjectName("lineEdit_add_detail"+str(number))
        lineEdit_add_detail.setMinimumSize(QSize(0, 50))
        lineEdit_add_detail.setMaximumSize(QSize(16777215, 50))
        lineEdit_add_detail.setFont(font)
        lineEdit_add_detail.setStyleSheet(Style.style_line_edit)
        lineEdit_add_detail.setPlaceholderText("Type "+ each)
        
        # make password seems *
        if is_invisible == True:
            lineEdit_add_detail.setEchoMode(QLineEdit.Password)

        self.ui.gridLayout_add_detail.addWidget(label_add, number, 1, 1, 1)
        self.ui.gridLayout_add_detail.addWidget(lineEdit_add_detail, number, 2, 1, 1)

        if is_invisible == True:
            # set checkbox
            checkBox_add_detail = QCheckBox(self)
            # set unique objectName
            checkBox_add_detail.setObjectName("checkBox_add_detail"+str(number))
            checkBox_add_detail.setMinimumSize(QSize(100, 50))
            checkBox_add_detail.setMaximumSize(QSize(100, 50))
            checkBox_add_detail.setFont(font)
            checkBox_add_detail.setText("Show")
            checkBox_add_detail.setStyleSheet(u'color:#c8c8c8;')
            checkBox_add_detail.stateChanged.connect(self.showPassword)
            self.ui.gridLayout_add_detail.addWidget(checkBox_add_detail, number, 3, 1, 1)
    
    def buttonSave(self):

        selectedTag = self.ui.comboBox_add_tag.currentText()
        accountData = AppFunctions.getAccountData(self)
        tagData = accountData['TAG'][selectedTag]

        # get service name
        serviceName = self.ui.gridFrame_add_detail.findChild(QLineEdit, "lineEdit_add_detail1").text()
        if serviceName.strip() == "":
            QMessageBox().information(self, 'PySide2', "Please fill the 'Service Name' blank", QMessageBox.Ok)
            return

        dictTemp = {"tag" : selectedTag}

        # get others
        # tagData.keys() : "ID", "Password", etc.
        for i, each in enumerate(tagData.keys()):
            # get text from each lineEdit widgets
            lineEditInput = self.ui.gridFrame_add_detail.findChild(QLineEdit, "lineEdit_add_detail" + str(i+2)).text()

            if lineEditInput.strip() == "":
                QMessageBox().information(self, 'PySide2', "Please fill all blanks", QMessageBox.Ok)
                return

            dictTemp[each] = lineEditInput
        
        accountData = AppFunctions.getAccountData(self)
        accountData['DATA'][serviceName] = dictTemp

        # encrypt
        for service in accountData['DATA'].keys():
            for key in accountData['DATA'][service].keys():
                if key == 'tag':
                    continue
                if AppFunctions.isInvisible(self, service, key, accountData):
                    # encrypt this data
                    decrypted_data = accountData['DATA'][service][key]
                    # decode it for save data with json
                    accountData['DATA'][service][key] = AppFunctions.encrypt(decrypted_data).decode('utf-8')

        # save it
        with open(AppFunctions.getAccountDataLoc(), "w") as json_file:
            json.dump(accountData, json_file)

        self.ui.stackedWidget_add.setCurrentWidget(self.ui.page_add_tag)        

    ###############################################################################################
    # setting
    # set location of accountData
    def openFolder(self, isNotLoginYet = False):
        fname = QFileDialog.getOpenFileName(self)[0]
        
        # user didn't select anything
        if fname.strip() == "":

            if isNotLoginYet:
                return False
            return

        self.ui.label_current.setText("Current : "+fname)

        with open("config.json", "w") as json_file:
            json.dump({"AccountFileLoc": {"LOC": fname}, "is_first": 0}, json_file)

        if isNotLoginYet:
            return True

    ###############################################################################################

    def appDefinitions(self):

        ################################################################################
        # BUTTONS
        ################################################################################
        # register, login, home
        self.ui.pushButton_register.clicked.connect(lambda:AppFunctions.buttonRegister(self))
        self.ui.pushButton_register_existing.clicked.connect(lambda:AppFunctions.buttonNotFirst(self))
        self.ui.pushButton_login.clicked.connect(lambda:AppFunctions.buttonLogin(self))
        self.ui.pushButton_home_button.clicked.connect(lambda:AppFunctions.buttonChangeKey(self))


        # retrieve
        self.ui.pushButton_search.clicked.connect(lambda: AppFunctions.search(self))
        # user also can press enter key to search
        self.ui.lineEdit_search.returnPressed.connect(lambda: AppFunctions.search(self))

        self.ui.pushButton_delete.clicked.connect(lambda: AppFunctions.buttonDeleteAccount(self))
        #add
        self.ui.pushButton_add_tag.clicked.connect(lambda: AppFunctions.buttonSelectTag(self))
        self.ui.pushButton_add_detail.clicked.connect(lambda: AppFunctions.buttonSave(self))
        self.ui.pushButton_btn_add.clicked.connect(self.buttonMenu)

        # setting
        self.ui.pushButton_open_folder.clicked.connect(lambda: AppFunctions.openFolder(self))
        self.ui.pushButton_restore.clicked.connect(lambda: AppFunctions.restoreData(self))
        self.ui.pushButton_chkey.clicked.connect(lambda: AppFunctions.buttonResetKey(self))

        # tag
        self.ui.pushButton_tag_add.clicked.connect(lambda: AppFunctions.addSlot(self))
        self.ui.pushButton_create_tag.clicked.connect(lambda: AppFunctions.create_tag_button(self))

        ################################################################################
        # LINEEDITS
        ################################################################################
        self.ui.horizontalFrame_register_password.findChild(QLineEdit, "lineEdit_register").setEchoMode(QLineEdit.Password)
        self.ui.horizontalFrame_login.findChild(QLineEdit, "lineEdit_login").setEchoMode(QLineEdit.Password)
        ################################################################################
        # CHECKBOxES
        ################################################################################
        self.ui.checkBox_register.stateChanged.connect(self.showPassword)
        self.ui.checkBox_login.stateChanged.connect(self.showPassword)
        ################################################################################
        # SHORTCUTS
        ################################################################################
        # exit
        self.shortcut_exit = QShortcut(QKeySequence("Ctrl+W"), self)
        self.shortcut_exit.activated.connect(lambda: self.close())

        ####################################################################################
        # scroll area
        AppFunctions.restoreScrollArea(self, AppFunctions.getAccountData(self), True)
        AppFunctions.restoreScrollArea2(self, AppFunctions.getAccountData(self), True)

    ###############################################################################################
    # Security - AES Algorithm

    def encrypt(raw):
        raw = pad(raw)
        iv = Random.new().read( AES.block_size )
        cipher = AES.new( AppFunctions.getKey(), AES.MODE_CBC, iv )
        return base64.b64encode( iv + cipher.encrypt( raw.encode('utf-8') ) )

    def decrypt(enc):
        enc = base64.b64decode(enc)
        iv = enc[:16]
        cipher = AES.new(AppFunctions.getKey(), AES.MODE_CBC, iv )
        return unpad(cipher.decrypt( enc[16:] ))

    def getKey():
        global GLOBAL_KEY
        encoded = GLOBAL_KEY.encode('utf-8')
        salt1 = hashlib.sha256(encoded).digest()
        key = hashlib.sha256(salt1+encoded).digest()
        return bytes(key)
    ###############################################################################################