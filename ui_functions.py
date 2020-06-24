# made by bolt6281

# load  GUI FILE
from main import *

# import APP FUNCTIONS
from app_functions import *

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
            self.ui.frame_top_btns.setStyleSheet("background-color: rgb(27, 29, 35)")
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
            self.ui.frame_top_btns.setStyleSheet("background-color: rgba(27, 29, 35, 200)")
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

    def setAccountList(self, account_data):
        # set font
        font = QFont()
        font.setFamily(u"Segoe UI")
        # 무슨 뜻
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(button.sizePolicy().hasHeightForWidth())
        
        for each in account_data.keys():
            # make button
            button = QPushButton(each, self)
            # set object name
            button.setObjectName(each)

            # set minimum size
            button.setMinimumSize(QSize(0, 70))
            # set layout direction
            button.setLayoutDirection(Qt.LeftToRight)
            # set button's font
            button.setFont(font)
            button.setSizePolicy(sizePolicy4)
            # ui_styles - set stylesheet
            button.setStyleSheet(Style.style_bt_retrieve)
            # set name of button
            button.setText(each)
            # set function of the button
            button.clicked.connect(self.Button_service)

            #add button
            self.ui.layout_menus.addWidget(button)
        
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


        #############################################################################################

        # define functions of title bar buttons
        # minimize button
        self.ui.btn_minimize.clicked.connect(lambda: self.showMinimized())

        # maximize/restore button
        self.ui.btn_maximize_restore.clicked.connect(lambda: UIFunctions.maximize_restore(self))

        # close button
        self.ui.btn_close.clicked.connect(lambda: self.close())
        
        #############################################################################################
        # app buttons

        # self.ui.pushButton_search.clicked.connect(lambda: UIFunctions.maximize_restore(self))
        # self.ui.pushButton_delete.clicked.connect(lambda: UIFunctions.maximize_restore(self))
        # self.ui.pushButton_clipboard_id.clicked.connect(lambda: UIFunctions.maximize_restore(self))
        # self.ui.pushButton_clipboard_password.clicked.connect(lambda: UIFunctions.maximize_restore(self))
        # self.ui.pushButton_edit_save.clicked.connect(lambda: UIFunctions.maximize_restore(self))
        self.ui.pushButton_open_folder.clicked.connect(lambda: Functions.OpenFolder(self))
        # pushButton_add
        # checkBox_add_show
        # checkBox_retrieve_show
        # checkBox_edit_show



    ########################################################################
    ## END - GUI DEFINITIONS
    ########################################################################