import os
import json
import clipboard

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QPropertyAnimation, QEasingCurve,QEvent, QTimer)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient, QFontDatabase)
from PySide2.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PySide2.QtWidgets import *

from main import *

# from app_functions import *

# GLOBAL STATE varibale
GLOBAL_STATE = 0
GLOBAL_TITLE_BAR = True

# COUNT INITAL MENU
count = 1

class UIFunctions(MainWindow):

    # GLOBAL STATE varibale
    # 0 : restored
    # 1 : maximized

    GLOBAL_STATE = 0
    GLOBAL_TITLE_BAR = True

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
        button.clicked.connect(self.Button_menu)

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

    # 위젯이 눌려있게 만듦
    def selectStandardMenu(self, widget):
        for w in self.ui.frame_left_menu.findChildren(QPushButton):
            if w.objectName() == widget:
                w.setStyleSheet(UIFunctions.selectMenu(w.styleSheet()))

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



class APPFunctions(MainWindow):
    
    def __init__(self):
        self.GLOBAL_SELECTED_PASSWORD = "hi"

    def returnPassword(self):
        return self.GLOBAL_SELECTED_PASSWORD
    ####################################################################################################################################### 
    # GET/SET ACCOUNT DATA
    #######################################################################################################################################
    
    def get_account_data_loc():
        cwd = os.getcwd()

        #############################################
        # load config file

        # check if there is config file | if not, make new one
        if not os.path.exists(cwd+"\\config.json"):
            with open("config.json", "w") as json_file:
                default_loc = cwd+"\\account_data.json"
                json.dump({"AccountFileLoc": {"LOC": default_loc}}, json_file)
            file_loc = default_loc
        else:
            # load config
            with open(cwd+'\\config.json', 'r') as json_file:
                config = json.loads(json_file.read())
            file_loc = config['AccountFileLoc']['LOC']

        return file_loc

    # return json file
    def get_account_data(self):

        # load account data
        file_loc = APPFunctions.get_account_data_loc()
        
        # if file_loc is wrong or account_data file has been removed
        # and edit config file as default
        if not os.path.exists(file_loc):
            self.ui.label_current.setText("Account file is disappeared. Please reassign account file or restore")
            return {}
        try:
            with open(file_loc, "r") as json_file:
                account_data = json.loads(json_file.read())
            return account_data
        # selected file is not account file(json file)
        except:
            self.ui.label_current.setText("Selected file is not an account file. Please reassign account file or restore")
            return {}

    def restore_account_data(self):
        cwd = os.getcwd()

        # set account_data as default(create empty data)
        default_loc = cwd+"\\account_data.json"
        with open(default_loc, "w") as json_file:
            json.dump({}, json_file)

        # set config file as default
        with open("config.json", "w") as json_file:
            default_loc = cwd+"\\account_data.json"
            json.dump({"AccountFileLoc": {"LOC": default_loc}}, json_file)

        self.ui.label_current.setText("Current : "+default_loc)
        

    ####################################################################################################################################### 
    #SCROLL AREA
    #######################################################################################################################################
    def restoreScrollArea(self, account_data, is_initial = False):
        
        if is_initial:
            pass
        else:
            # while self.ui.verticalLayout_9.count():
            #     child = self.ui.verticalLayout_9.takeAt(0)
            #     #remove existing scroll area
            #     if child.widget().objectName() == u"scrollArea":
            #         child.widget().deleteLater()
            #print(self.ui.verticalLayout_9.takeAt(0))
            self.ui.verticalLayout_9.takeAt(1).widget().deleteLater()
                    
        # scroll area
        scrollArea = QScrollArea(self.ui.frame_list)
        scrollArea.setObjectName(u"scrollArea")
        scrollArea.setMinimumSize(QSize(400, 0))
        scrollArea.setMaximumSize(QSize(400, 16777215))
        scrollArea.setStyleSheet(Style.style_scroll_area)
        scrollArea.setWidgetResizable(True)
        scrollAreaWidgetContents = QWidget()
        scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        scrollAreaWidgetContents.setGeometry(QRect(0, 0, 384, 542))

        # vertical layout : content of scroll area
        self.ui.verticalLayout_scrollable = QVBoxLayout(scrollAreaWidgetContents)
        self.ui.verticalLayout_scrollable.setSpacing(10)
        self.ui.verticalLayout_scrollable.setObjectName(u"verticalLayout_scrollable")
        self.ui.verticalLayout_scrollable.setContentsMargins(9, 9, 9, 9)
        
        for name in account_data.keys():
            APPFunctions.add_service_button(self, name)

        scrollArea.setWidget(scrollAreaWidgetContents)
        self.ui.verticalLayout_9.addWidget(scrollArea)
        
        #############################################################################################

    def Button_service(self, selected_service):
        account = APPFunctions.get_account_data(self)[selected_service]

        self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_specific)
        self.ui.label_service_name.setText(selected_service)

        ID = account['ID']
        PASSWORD = account['PASSWORD']

        self.GLOBAL_SELECTED_PASSWORD = PASSWORD
        
        encoded = "*"*len(PASSWORD)

        self.ui.label_id_2.setText(QCoreApplication.translate("MainWindow", ID, None))
        self.ui.label_password_2.setText(QCoreApplication.translate("MainWindow", encoded, None))

        self.ui.label_clipboard_id.setText("")
        self.ui.label_clipboard_password.setText("")

    def add_service_button(self, name):

        # set font
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)

        # parent = scrollAreaWidgetContents
        button = QPushButton(name, self)
        # button.setObjectName("btn_"+list(account_data.keys())[idx])
        button.setMinimumSize(QSize(0, 70))
        button.setMaximumSize(QSize(16777215, 70))
        button.setFont(font)
        button.setStyleSheet(Style.style_scroll_area_button)
        button.clicked.connect(lambda: APPFunctions.Button_service(self, name))
        button.setText(QCoreApplication.translate("MainWindow", name, None))
        self.ui.verticalLayout_scrollable.addWidget(button)

    #######################################################################################################################################
    #SCROLL AREA - END
    #######################################################################################################################################
    # be used at add_page, edit 
    
    def delete_button(self):
        service_name = self.ui.label_service_name.text()
        account_data = APPFunctions.get_account_data(self)
        account_data.pop(service_name, None)

        with open(APPFunctions.get_account_data_loc(), "w") as json_file:
            json.dump(account_data, json_file)

        # go back to guide_pages
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_guide)
        # restore scroll_area
        APPFunctions.restoreScrollArea(self, account_data, False)

        self.ui.label_clipboard_id.setText("")
        self.ui.label_clipboard_password.setText("")

    def add_save_button(self, is_add):
        if is_add == True:
            service_name = self.ui.lineEdit_add_name.text()
            ID = self.ui.lineEdit_add_id.text()
            PASSWORD = self.ui.lineEdit_add_password.text()

            # remove what user wrote after save
            self.ui.lineEdit_add_name.setText("")
            self.ui.lineEdit_add_id.setText("")
            self.ui.lineEdit_add_password.setText("")
        else:
            # edit_save
            service_name = self.ui.label_service_name.text()
            ID = self.ui.lineEdit_edit_id.text()
            PASSWORD = self.ui.lineEdit_edit_password.text()

            # remove what user wrote after save
            self.ui.lineEdit_edit_id.setText("")
            self.ui.lineEdit_edit_password.setText("")

        
        account_data = APPFunctions.get_account_data(self)
        account_data[service_name] = {'ID': ID, 'PASSWORD': PASSWORD}
        
        with open(APPFunctions.get_account_data_loc(), "w") as json_file:
            json.dump(account_data, json_file)

    # set location of account_data
    def OpenFolder(self):
        fname = QFileDialog.getOpenFileName(self)[0]
        
        # user didn't select anything
        if fname == "":
            return

        self.ui.label_current.setText("Current : "+fname)

        with open("config.json", "w") as json_file:
            json.dump({"AccountFileLoc": {"LOC": fname}}, json_file)

    # copy ID or Password to clipboard
    def clipboard(self, objectname):
        if objectname == "pushButton_clipboard_id":
            clipboard.copy(self.ui.label_id_2.text())
            self.ui.label_clipboard_id.setText("Copied")

        elif objectname == "pushButton_clipboard_password":
            clipboard.copy(self.GLOBAL_SELECTED_PASSWORD)
            self.ui.label_clipboard_password.setText("Copied")

    # show what user searched( restore scroll area )
    def search(self):
        account_data = APPFunctions.get_account_data(self)

        keyword = self.ui.lineEdit_search.text()
        
        service_names = list(account_data.keys())
        for service_name in service_names:
            if not (keyword.lower() in service_name.lower()):
                account_data.pop(service_name, None)
        APPFunctions.restoreScrollArea(self, account_data, is_initial = False)

    def appDefinitions(self):
        ################################################################################
        # PASSWORD
        ################################################################################
        self.ui.lineEdit_add_password.setEchoMode(QLineEdit.Password)
        self.ui.lineEdit_edit_password.setEchoMode(QLineEdit.Password)


        ################################################################################
        # BUTTONS
        ################################################################################
        self.ui.pushButton_search.clicked.connect(lambda: APPFunctions.search(self))
        # user also can press enter key to search
        self.ui.lineEdit_search.returnPressed.connect(lambda: APPFunctions.search(self))
        
        self.ui.pushButton_delete.clicked.connect(lambda: APPFunctions.delete_button(self))

        self.ui.pushButton_clipboard_id.clicked.connect(lambda: APPFunctions.clipboard(self, "pushButton_clipboard_id"))
        self.ui.pushButton_clipboard_password.clicked.connect(lambda: APPFunctions.clipboard(self, "pushButton_clipboard_password"))

        self.ui.pushButton_add.clicked.connect(lambda: APPFunctions.add_save_button(self, True))
        self.ui.pushButton_edit_save.clicked.connect(lambda: APPFunctions.add_save_button(self, False))

        self.ui.pushButton_open_folder.clicked.connect(lambda: APPFunctions.OpenFolder(self))

        self.ui.pushButton_restore.clicked.connect(lambda: APPFunctions.restore_account_data(self))
        
        # ################################################################################
        # # CHECKBOX
        # ################################################################################
        self.ui.checkBox_retrieve_show.stateChanged.connect(self.show_password)

        self.ui.checkBox_add_show.stateChanged.connect(self.show_password)

        self.ui.checkBox_edit_show.stateChanged.connect(self.show_password)

        ################################################################################
        # SHORTCUTS
        ################################################################################
        # exit
        self.shortcut_exit = QShortcut(QKeySequence("Ctrl+W"), self)
        self.shortcut_exit.activated.connect(lambda: self.close())

        ####################################################################################
        # scroll area
        APPFunctions.restoreScrollArea(self, APPFunctions.get_account_data(self), True)
        
    ###############################################################################################