# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_gui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 725)
        MainWindow.setMinimumSize(QSize(1000, 720))
        palette = QPalette()
        brush = QBrush(QColor(210, 210, 210, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 0))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush2 = QBrush(QColor(210, 210, 210, 128))
        brush2.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush2)
#endif
        MainWindow.setPalette(palette)
        MainWindow.setStyleSheet(u"QMainWindow {background: transparent; }\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(27, 29, 35, 160);\n"
"	border: 1px solid rgb(40, 40, 40);\n"
"	border-radius: 2px;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush3 = QBrush(QColor(39, 44, 54, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush3)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush3)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush3)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush3)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush3)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush3)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush2)
#endif
        self.centralwidget.setPalette(palette1)
        self.centralwidget.setStyleSheet(u"QMainWindow {background: transparent; }\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgb(27, 29, 35, 160);\n"
"	border: 1px solid rgb(40, 40, 40);\n"
"	border-radius: 2px;\n"
"}")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, -1, 0, 0)
        self.frame_main = QFrame(self.centralwidget)
        self.frame_main.setObjectName(u"frame_main")
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush2)
#endif
        self.frame_main.setPalette(palette2)
        self.frame_main.setStyleSheet(u"/* LINE EDIT */\n"
"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* SCROLL BARS */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(85, 170, 255);\n"
"    min-width: 25px;\n"
"	border-radius: 7px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
""
                        "	border-top-left-radius: 7px;\n"
"    border-bottom-left-radius: 7px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(85, 170, 255);\n"
"    min-height: 25px;\n"
"	border-radius: 7px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63"
                        ", 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* CHECKBOX */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	background-image: url(:/icons/icons/16x16/cil-check-alt.png);\n"
"}\n"
"\n"
"\n"
"/* SLIDERS */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 9px;\n"
"    height: 18px;\n"
"	margin: 0px;\n"
"	background-color: rgb("
                        "52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(85, 170, 255);\n"
"    border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	border-radius: 9px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 9px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(85, 170, 255);\n"
"	border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	border-radius: 9px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSlider::handle:vertical:"
                        "pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}\n"
"\n"
"")
        self.verticalLayout = QVBoxLayout(self.frame_main)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_top = QFrame(self.frame_main)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setMinimumSize(QSize(0, 65))
        self.frame_top.setMaximumSize(QSize(16777215, 65))
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette3.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette3.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.frame_top.setPalette(palette3)
        self.frame_top.setStyleSheet(u"background-color: transparent;")
        self.horizontalLayout_3 = QHBoxLayout(self.frame_top)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_toggle = QFrame(self.frame_top)
        self.frame_toggle.setObjectName(u"frame_toggle")
        self.frame_toggle.setMinimumSize(QSize(0, 65))
        self.frame_toggle.setMaximumSize(QSize(70, 16777215))
        self.frame_toggle.setStyleSheet(u"background-color: rgb(27, 29, 35);")
        self.verticalLayout_5 = QVBoxLayout(self.frame_toggle)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.btn_toggle_menu = QPushButton(self.frame_toggle)
        self.btn_toggle_menu.setObjectName(u"btn_toggle_menu")
        self.btn_toggle_menu.setMinimumSize(QSize(65, 65))
        palette4 = QPalette()
        brush4 = QBrush(QColor(27, 29, 35, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette4.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette4.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette4.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette4.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette4.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette4.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette4.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette4.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette4.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        self.btn_toggle_menu.setPalette(palette4)
        self.btn_toggle_menu.setStyleSheet(u"QPushButton {\n"
"	background-image: url(:/icons/icons/24x24/cil-menu.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"	border: none;\n"
"	background-color: rgb(27, 29, 35);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.btn_toggle_menu.setAutoRepeatInterval(0)

        self.verticalLayout_5.addWidget(self.btn_toggle_menu)


        self.horizontalLayout_3.addWidget(self.frame_toggle)

        self.frame_other = QFrame(self.frame_top)
        self.frame_other.setObjectName(u"frame_other")
        self.frame_other.setStyleSheet(u"background-color: rgba(27, 29, 35, 200)")
        self.verticalLayout_3 = QVBoxLayout(self.frame_other)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_info1 = QFrame(self.frame_other)
        self.frame_info1.setObjectName(u"frame_info1")
        self.frame_info1.setMinimumSize(QSize(0, 42))
        self.frame_info1.setMaximumSize(QSize(16777215, 65))
        palette5 = QPalette()
        brush5 = QBrush(QColor(34, 36, 43, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette5.setBrush(QPalette.Active, QPalette.Button, brush5)
        palette5.setBrush(QPalette.Active, QPalette.Base, brush5)
        palette5.setBrush(QPalette.Active, QPalette.Window, brush5)
        palette5.setBrush(QPalette.Inactive, QPalette.Button, brush5)
        palette5.setBrush(QPalette.Inactive, QPalette.Base, brush5)
        palette5.setBrush(QPalette.Inactive, QPalette.Window, brush5)
        palette5.setBrush(QPalette.Disabled, QPalette.Button, brush5)
        palette5.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette5.setBrush(QPalette.Disabled, QPalette.Window, brush5)
        self.frame_info1.setPalette(palette5)
        self.frame_info1.setStyleSheet(u"background-color: rgba(34, 36, 43)")
        self.frame_info1.setLineWidth(0)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_info1)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_label_top_btns = QFrame(self.frame_info1)
        self.frame_label_top_btns.setObjectName(u"frame_label_top_btns")
        self.hboxLayout = QHBoxLayout(self.frame_label_top_btns)
        self.hboxLayout.setObjectName(u"hboxLayout")
        self.label_title_bar_top = QLabel(self.frame_label_top_btns)
        self.label_title_bar_top.setObjectName(u"label_title_bar_top")
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_title_bar_top.setFont(font)
        self.label_title_bar_top.setStyleSheet(u"color:#c8c8c8")

        self.hboxLayout.addWidget(self.label_title_bar_top)


        self.horizontalLayout_4.addWidget(self.frame_label_top_btns)

        self.frame_btns_right = QFrame(self.frame_info1)
        self.frame_btns_right.setObjectName(u"frame_btns_right")
        self.frame_btns_right.setMaximumSize(QSize(120, 16777215))
        self.frame_btns_right.setLayoutDirection(Qt.RightToLeft)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_btns_right)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.btn_close = QPushButton(self.frame_btns_right)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setMaximumSize(QSize(40, 40))
        self.btn_close.setAutoFillBackground(False)
        self.btn_close.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/icons/16x16/cil-x.png", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u":/icons/icons/16x16/cil-x.png", QSize(), QIcon.Normal, QIcon.On)
        icon.addFile(u":/icons/icons/16x16/cil-x.png", QSize(), QIcon.Disabled, QIcon.Off)
        icon.addFile(u":/icons/icons/16x16/cil-x.png", QSize(), QIcon.Disabled, QIcon.On)
        icon.addFile(u":/icons/icons/16x16/cil-x.png", QSize(), QIcon.Active, QIcon.Off)
        icon.addFile(u":/icons/icons/16x16/cil-x.png", QSize(), QIcon.Active, QIcon.On)
        icon.addFile(u":/icons/icons/16x16/cil-x.png", QSize(), QIcon.Selected, QIcon.Off)
        icon.addFile(u":/icons/icons/16x16/cil-x.png", QSize(), QIcon.Selected, QIcon.On)
        self.btn_close.setIcon(icon)

        self.horizontalLayout_7.addWidget(self.btn_close)

        self.btn_maximize_restore = QPushButton(self.frame_btns_right)
        self.btn_maximize_restore.setObjectName(u"btn_maximize_restore")
        self.btn_maximize_restore.setMaximumSize(QSize(40, 40))
        self.btn_maximize_restore.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/16x16/cil-window-maximize.png", QSize(), QIcon.Selected, QIcon.On)
        self.btn_maximize_restore.setIcon(icon1)

        self.horizontalLayout_7.addWidget(self.btn_maximize_restore)

        self.btn_minimize = QPushButton(self.frame_btns_right)
        self.btn_minimize.setObjectName(u"btn_minimize")
        self.btn_minimize.setMaximumSize(QSize(40, 40))
        self.btn_minimize.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/16x16/cil-window-minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_minimize.setIcon(icon2)

        self.horizontalLayout_7.addWidget(self.btn_minimize)


        self.horizontalLayout_4.addWidget(self.frame_btns_right)


        self.verticalLayout_3.addWidget(self.frame_info1)

        self.frame_info2 = QFrame(self.frame_other)
        self.frame_info2.setObjectName(u"frame_info2")
        self.frame_info2.setMinimumSize(QSize(0, 20))
        self.frame_info2.setMaximumSize(QSize(16777215, 20))
        self.frame_info2.setStyleSheet(u"background-color: rgb(39, 44, 54);")
        self.horizontalLayout_5 = QHBoxLayout(self.frame_info2)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_fileloc = QLabel(self.frame_info2)
        self.label_fileloc.setObjectName(u"label_fileloc")
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(9)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_fileloc.setFont(font1)
        self.label_fileloc.setStyleSheet(u"\n"
"QLabel{\n"
"color:#62676f;\n"
"marin-left:20px;\n"
"padding-left:5px;\n"
"}")
        self.label_fileloc.setLineWidth(0)
        self.label_fileloc.setMargin(0)

        self.horizontalLayout_5.addWidget(self.label_fileloc)

        self.label_where = QLabel(self.frame_info2)
        self.label_where.setObjectName(u"label_where")
        palette6 = QPalette()
        brush6 = QBrush(QColor(98, 103, 102, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette6.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette6.setBrush(QPalette.Active, QPalette.Button, brush3)
        palette6.setBrush(QPalette.Active, QPalette.Base, brush3)
        palette6.setBrush(QPalette.Active, QPalette.Window, brush3)
        palette6.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette6.setBrush(QPalette.Inactive, QPalette.Button, brush3)
        palette6.setBrush(QPalette.Inactive, QPalette.Base, brush3)
        palette6.setBrush(QPalette.Inactive, QPalette.Window, brush3)
        brush7 = QBrush(QColor(120, 120, 120, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette6.setBrush(QPalette.Disabled, QPalette.WindowText, brush7)
        palette6.setBrush(QPalette.Disabled, QPalette.Button, brush3)
        palette6.setBrush(QPalette.Disabled, QPalette.Base, brush3)
        palette6.setBrush(QPalette.Disabled, QPalette.Window, brush3)
        self.label_where.setPalette(palette6)
        self.label_where.setFont(font1)
        self.label_where.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_where.setMargin(20)

        self.horizontalLayout_5.addWidget(self.label_where)


        self.verticalLayout_3.addWidget(self.frame_info2)


        self.horizontalLayout_3.addWidget(self.frame_other)


        self.verticalLayout.addWidget(self.frame_top)

        self.frame_center = QFrame(self.frame_main)
        self.frame_center.setObjectName(u"frame_center")
        self.frame_center.setEnabled(True)
        palette7 = QPalette()
        brush8 = QBrush(QColor(44, 49, 60, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette7.setBrush(QPalette.Active, QPalette.Button, brush8)
        palette7.setBrush(QPalette.Active, QPalette.Base, brush8)
        palette7.setBrush(QPalette.Active, QPalette.Window, brush8)
        palette7.setBrush(QPalette.Inactive, QPalette.Button, brush8)
        palette7.setBrush(QPalette.Inactive, QPalette.Base, brush8)
        palette7.setBrush(QPalette.Inactive, QPalette.Window, brush8)
        palette7.setBrush(QPalette.Disabled, QPalette.Button, brush8)
        palette7.setBrush(QPalette.Disabled, QPalette.Base, brush8)
        palette7.setBrush(QPalette.Disabled, QPalette.Window, brush8)
        self.frame_center.setPalette(palette7)
        self.frame_center.setStyleSheet(u"background-color: #2c313c;")
        self.horizontalLayout = QHBoxLayout(self.frame_center)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_left_menu = QFrame(self.frame_center)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        self.frame_left_menu.setMinimumSize(QSize(70, 0))
        self.frame_left_menu.setMaximumSize(QSize(70, 16777215))
        self.frame_left_menu.setLayoutDirection(Qt.LeftToRight)
        self.frame_left_menu.setAutoFillBackground(False)
        self.frame_left_menu.setStyleSheet(u"background-color: rgb(27, 29, 35); padding-bottom:12;")
        self.verticalLayout_2 = QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_menus = QFrame(self.frame_left_menu)
        self.frame_menus.setObjectName(u"frame_menus")
        self.frame_menus.setMaximumSize(QSize(16777215, 1677148))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        self.frame_menus.setFont(font2)
        self.frame_menus.setStyleSheet(u"color:#c8c8c8")
        self.frame_menus.setLineWidth(0)
        self.layout_menus = QVBoxLayout(self.frame_menus)
        self.layout_menus.setSpacing(0)
        self.layout_menus.setObjectName(u"layout_menus")
        self.layout_menus.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_2.addWidget(self.frame_menus, 0, Qt.AlignTop)

        self.frame_extra_menus = QFrame(self.frame_left_menu)
        self.frame_extra_menus.setObjectName(u"frame_extra_menus")
        self.frame_extra_menus.setMinimumSize(QSize(0, 0))
        self.frame_extra_menus.setMaximumSize(QSize(16777215, 300))
        self.frame_extra_menus.setFont(font2)
        self.frame_extra_menus.setStyleSheet(u"color:#c8c8c8")
        self.layout_menu_bottom = QVBoxLayout(self.frame_extra_menus)

        self.layout_menu_bottom.setSpacing(0)
        self.layout_menu_bottom.setObjectName(u"layout_menu_bottom")
        self.layout_menu_bottom.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_2.addWidget(self.frame_extra_menus, 0, Qt.AlignBottom)


        self.horizontalLayout.addWidget(self.frame_left_menu)

        self.frame_center_right = QFrame(self.frame_center)
        self.frame_center_right.setObjectName(u"frame_center_right")
        palette8 = QPalette()
        brush9 = QBrush(QColor(98, 103, 111, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette8.setBrush(QPalette.Active, QPalette.WindowText, brush9)
        palette8.setBrush(QPalette.Active, QPalette.Button, brush8)
        palette8.setBrush(QPalette.Active, QPalette.Text, brush9)
        palette8.setBrush(QPalette.Active, QPalette.ButtonText, brush9)
        palette8.setBrush(QPalette.Active, QPalette.Base, brush8)
        palette8.setBrush(QPalette.Active, QPalette.Window, brush8)
        brush10 = QBrush(QColor(98, 103, 111, 128))
        brush10.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.Active, QPalette.PlaceholderText, brush10)
#endif
        palette8.setBrush(QPalette.Inactive, QPalette.WindowText, brush9)
        palette8.setBrush(QPalette.Inactive, QPalette.Button, brush8)
        palette8.setBrush(QPalette.Inactive, QPalette.Text, brush9)
        palette8.setBrush(QPalette.Inactive, QPalette.ButtonText, brush9)
        palette8.setBrush(QPalette.Inactive, QPalette.Base, brush8)
        palette8.setBrush(QPalette.Inactive, QPalette.Window, brush8)
        brush11 = QBrush(QColor(98, 103, 111, 128))
        brush11.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush11)
#endif
        palette8.setBrush(QPalette.Disabled, QPalette.WindowText, brush9)
        palette8.setBrush(QPalette.Disabled, QPalette.Button, brush8)
        palette8.setBrush(QPalette.Disabled, QPalette.Text, brush9)
        palette8.setBrush(QPalette.Disabled, QPalette.ButtonText, brush9)
        palette8.setBrush(QPalette.Disabled, QPalette.Base, brush8)
        palette8.setBrush(QPalette.Disabled, QPalette.Window, brush8)
        brush12 = QBrush(QColor(98, 103, 111, 128))
        brush12.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush12)
#endif
        self.frame_center_right.setPalette(palette8)
        self.frame_center_right.setStyleSheet(u"color: rgb(98, 103, 111);")
        self.frame_content = QVBoxLayout(self.frame_center_right)
        self.frame_content.setSpacing(0)
        self.frame_content.setObjectName(u"frame_content")
        self.frame_content.setContentsMargins(0, 0, 0, 0)
        self.frame_content_2 = QFrame(self.frame_center_right)
        self.frame_content_2.setObjectName(u"frame_content_2")
        palette9 = QPalette()
        palette9.setBrush(QPalette.Active, QPalette.WindowText, brush9)
        palette9.setBrush(QPalette.Active, QPalette.Button, brush8)
        palette9.setBrush(QPalette.Active, QPalette.Text, brush9)
        palette9.setBrush(QPalette.Active, QPalette.ButtonText, brush9)
        palette9.setBrush(QPalette.Active, QPalette.Base, brush8)
        palette9.setBrush(QPalette.Active, QPalette.Window, brush8)
        brush13 = QBrush(QColor(98, 103, 111, 128))
        brush13.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette9.setBrush(QPalette.Active, QPalette.PlaceholderText, brush13)
#endif
        palette9.setBrush(QPalette.Inactive, QPalette.WindowText, brush9)
        palette9.setBrush(QPalette.Inactive, QPalette.Button, brush8)
        palette9.setBrush(QPalette.Inactive, QPalette.Text, brush9)
        palette9.setBrush(QPalette.Inactive, QPalette.ButtonText, brush9)
        palette9.setBrush(QPalette.Inactive, QPalette.Base, brush8)
        palette9.setBrush(QPalette.Inactive, QPalette.Window, brush8)
        brush14 = QBrush(QColor(98, 103, 111, 128))
        brush14.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette9.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush14)
#endif
        palette9.setBrush(QPalette.Disabled, QPalette.WindowText, brush9)
        palette9.setBrush(QPalette.Disabled, QPalette.Button, brush8)
        palette9.setBrush(QPalette.Disabled, QPalette.Text, brush9)
        palette9.setBrush(QPalette.Disabled, QPalette.ButtonText, brush9)
        palette9.setBrush(QPalette.Disabled, QPalette.Base, brush8)
        palette9.setBrush(QPalette.Disabled, QPalette.Window, brush8)
        brush15 = QBrush(QColor(98, 103, 111, 128))
        brush15.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette9.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush15)
#endif
        self.frame_content_2.setPalette(palette9)
        self.frame_content_2.setStyleSheet(u"")
        self.verticalLayout_4 = QVBoxLayout(self.frame_content_2)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frame_content_2)
        self.stackedWidget.setObjectName(u"stackedWidget")
        palette10 = QPalette()
        palette10.setBrush(QPalette.Active, QPalette.WindowText, brush9)
        palette10.setBrush(QPalette.Active, QPalette.Button, brush8)
        palette10.setBrush(QPalette.Active, QPalette.Text, brush9)
        palette10.setBrush(QPalette.Active, QPalette.ButtonText, brush9)
        palette10.setBrush(QPalette.Active, QPalette.Base, brush8)
        palette10.setBrush(QPalette.Active, QPalette.Window, brush8)
        brush16 = QBrush(QColor(98, 103, 111, 128))
        brush16.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette10.setBrush(QPalette.Active, QPalette.PlaceholderText, brush16)
#endif
        palette10.setBrush(QPalette.Inactive, QPalette.WindowText, brush9)
        palette10.setBrush(QPalette.Inactive, QPalette.Button, brush8)
        palette10.setBrush(QPalette.Inactive, QPalette.Text, brush9)
        palette10.setBrush(QPalette.Inactive, QPalette.ButtonText, brush9)
        palette10.setBrush(QPalette.Inactive, QPalette.Base, brush8)
        palette10.setBrush(QPalette.Inactive, QPalette.Window, brush8)
        brush17 = QBrush(QColor(98, 103, 111, 128))
        brush17.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette10.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush17)
#endif
        palette10.setBrush(QPalette.Disabled, QPalette.WindowText, brush9)
        palette10.setBrush(QPalette.Disabled, QPalette.Button, brush8)
        palette10.setBrush(QPalette.Disabled, QPalette.Text, brush9)
        palette10.setBrush(QPalette.Disabled, QPalette.ButtonText, brush9)
        palette10.setBrush(QPalette.Disabled, QPalette.Base, brush8)
        palette10.setBrush(QPalette.Disabled, QPalette.Window, brush8)
        brush18 = QBrush(QColor(98, 103, 111, 128))
        brush18.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette10.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush18)
#endif
        self.stackedWidget.setPalette(palette10)
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        palette11 = QPalette()
        palette11.setBrush(QPalette.Active, QPalette.WindowText, brush9)
        palette11.setBrush(QPalette.Active, QPalette.Button, brush8)
        palette11.setBrush(QPalette.Active, QPalette.Text, brush9)
        palette11.setBrush(QPalette.Active, QPalette.ButtonText, brush9)
        palette11.setBrush(QPalette.Active, QPalette.Base, brush8)
        palette11.setBrush(QPalette.Active, QPalette.Window, brush8)
        brush19 = QBrush(QColor(98, 103, 111, 128))
        brush19.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette11.setBrush(QPalette.Active, QPalette.PlaceholderText, brush19)
#endif
        palette11.setBrush(QPalette.Inactive, QPalette.WindowText, brush9)
        palette11.setBrush(QPalette.Inactive, QPalette.Button, brush8)
        palette11.setBrush(QPalette.Inactive, QPalette.Text, brush9)
        palette11.setBrush(QPalette.Inactive, QPalette.ButtonText, brush9)
        palette11.setBrush(QPalette.Inactive, QPalette.Base, brush8)
        palette11.setBrush(QPalette.Inactive, QPalette.Window, brush8)
        brush20 = QBrush(QColor(98, 103, 111, 128))
        brush20.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette11.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush20)
#endif
        palette11.setBrush(QPalette.Disabled, QPalette.WindowText, brush9)
        palette11.setBrush(QPalette.Disabled, QPalette.Button, brush8)
        palette11.setBrush(QPalette.Disabled, QPalette.Text, brush9)
        palette11.setBrush(QPalette.Disabled, QPalette.ButtonText, brush9)
        palette11.setBrush(QPalette.Disabled, QPalette.Base, brush8)
        palette11.setBrush(QPalette.Disabled, QPalette.Window, brush8)
        brush21 = QBrush(QColor(98, 103, 111, 128))
        brush21.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette11.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush21)
#endif
        self.page_home.setPalette(palette11)
        self.page_home.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.verticalLayout_6 = QVBoxLayout(self.page_home)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(50, -1, -1, -1)
        self.label_name = QLabel(self.page_home)
        self.label_name.setObjectName(u"label_name")
        palette12 = QPalette()
        brush22 = QBrush(QColor(200, 200, 200, 255))
        brush22.setStyle(Qt.SolidPattern)
        palette12.setBrush(QPalette.Active, QPalette.WindowText, brush22)
        palette12.setBrush(QPalette.Active, QPalette.Button, brush8)
        palette12.setBrush(QPalette.Active, QPalette.Text, brush22)
        palette12.setBrush(QPalette.Active, QPalette.ButtonText, brush22)
        palette12.setBrush(QPalette.Active, QPalette.Base, brush8)
        palette12.setBrush(QPalette.Active, QPalette.Window, brush8)
        brush23 = QBrush(QColor(200, 200, 200, 128))
        brush23.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette12.setBrush(QPalette.Active, QPalette.PlaceholderText, brush23)
#endif
        palette12.setBrush(QPalette.Inactive, QPalette.WindowText, brush22)
        palette12.setBrush(QPalette.Inactive, QPalette.Button, brush8)
        palette12.setBrush(QPalette.Inactive, QPalette.Text, brush22)
        palette12.setBrush(QPalette.Inactive, QPalette.ButtonText, brush22)
        palette12.setBrush(QPalette.Inactive, QPalette.Base, brush8)
        palette12.setBrush(QPalette.Inactive, QPalette.Window, brush8)
        brush24 = QBrush(QColor(200, 200, 200, 128))
        brush24.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette12.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush24)
#endif
        palette12.setBrush(QPalette.Disabled, QPalette.WindowText, brush22)
        palette12.setBrush(QPalette.Disabled, QPalette.Button, brush8)
        palette12.setBrush(QPalette.Disabled, QPalette.Text, brush22)
        palette12.setBrush(QPalette.Disabled, QPalette.ButtonText, brush22)
        palette12.setBrush(QPalette.Disabled, QPalette.Base, brush8)
        palette12.setBrush(QPalette.Disabled, QPalette.Window, brush8)
        brush25 = QBrush(QColor(200, 200, 200, 128))
        brush25.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette12.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush25)
#endif
        self.label_name.setPalette(palette12)
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(40)
        font3.setBold(True)
        font3.setItalic(False)
        font3.setUnderline(False)
        font3.setWeight(75)
        font3.setKerning(True)
        self.label_name.setFont(font3)
        self.label_name.setStyleSheet(u"color:#c8c8c8")

        self.verticalLayout_6.addWidget(self.label_name)
        
        self.label_intro = QLabel(self.page_home)
        self.label_intro.setObjectName(u"label_intro")
        font4 = QFont()
        font4.setFamily(u"Segoe UI")
        font4.setPointSize(23)
        font4.setBold(True)
        font4.setWeight(75)
        self.label_intro.setFont(font4)
        self.label_intro.setStyleSheet(u"color:#c8c8c8")

        self.verticalLayout_6.addWidget(self.label_intro)

        self.label_space = QLabel(self.page_home)
        self.label_space.setObjectName(u"label_space")

        self.verticalLayout_6.addWidget(self.label_space)

        self.label_first_time = QLabel(self.page_home)
        self.label_first_time.setObjectName(u"label_first_time")
        font4 = QFont()
        font4.setFamily(u"Segoe UI")
        font4.setPointSize(10)
        font4.setWeight(75)
        
        self.label_first_time.setFont(font4)
        self.label_first_time.setStyleSheet(u"color:#62676f;")
        self.label_first_time.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.label_first_time.setMaximumSize(QSize(120000, 30))

        self.verticalLayout_6.addWidget(self.label_first_time)

        self.stackedWidget.addWidget(self.page_home)
        self.page_add = QWidget()
        self.page_add.setObjectName(u"page_add")
        font5 = QFont()
        font5.setKerning(True)
        self.page_add.setFont(font5)
        self.page_add.setFocusPolicy(Qt.NoFocus)
        self.page_add.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.page_add.setAutoFillBackground(False)
        self.verticalLayout_7 = QVBoxLayout(self.page_add)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_add = QFrame(self.page_add)
        self.frame_add.setObjectName(u"frame_add")
        self.frame_add.setMinimumSize(QSize(0, 0))
        font6 = QFont()
        font6.setFamily(u"Segoe UI")
        font6.setPointSize(12)
        self.frame_add.setFont(font6)
        self.frame_add.setStyleSheet(u"color:#c8c8c8;\n"
"\n"
"\n"
"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.gridLayout_3 = QGridLayout(self.frame_add)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_add_password = QLabel(self.frame_add)
        self.label_add_password.setObjectName(u"label_add_password")
        font7 = QFont()
        font7.setFamily(u"Segoe UI")
        font7.setPointSize(15)
        self.label_add_password.setFont(font7)
        self.label_add_password.setAlignment(Qt.AlignCenter)
        self.label_add_password.setMargin(20)

        self.gridLayout_3.addWidget(self.label_add_password, 2, 0, 1, 1)

        self.lineEdit_add_name = QLineEdit(self.frame_add)
        self.lineEdit_add_name.setObjectName(u"lineEdit_add_name")
        self.lineEdit_add_name.setMinimumSize(QSize(0, 50))
        font8 = QFont()
        font8.setFamily(u"Segoe UI")
        font8.setPointSize(15)
        font8.setBold(True)
        font8.setWeight(75)
        self.lineEdit_add_name.setFont(font8)
        self.lineEdit_add_name.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 10px;\n"
"	border: 2px solid rgb(34, 36, 43);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 3px solid rgb(91, 101, 124);\n"
"}")

        self.gridLayout_3.addWidget(self.lineEdit_add_name, 0, 1, 1, 1)

        self.checkBox_add_show = QCheckBox(self.frame_add)
        self.checkBox_add_show.setObjectName(u"checkBox_add_show")
        self.checkBox_add_show.setMinimumSize(QSize(150, 0))
        font9 = QFont()
        font9.setFamily(u"Segoe UI")
        font9.setPointSize(12)
        font9.setBold(False)
        font9.setWeight(50)
        self.checkBox_add_show.setFont(font9)

        self.gridLayout_3.addWidget(self.checkBox_add_show, 2, 2, 1, 1)

        self.label_add_id = QLabel(self.frame_add)
        self.label_add_id.setObjectName(u"label_add_id")
        self.label_add_id.setFont(font7)
        self.label_add_id.setAlignment(Qt.AlignCenter)
        self.label_add_id.setMargin(20)

        self.gridLayout_3.addWidget(self.label_add_id, 1, 0, 1, 1)

        self.lineEdit_add_id = QLineEdit(self.frame_add)
        self.lineEdit_add_id.setObjectName(u"lineEdit_add_id")
        self.lineEdit_add_id.setMinimumSize(QSize(0, 50))
        self.lineEdit_add_id.setFont(font8)
        self.lineEdit_add_id.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 10px;\n"
"	border: 2px solid rgb(34, 36, 43);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 3px solid rgb(91, 101, 124);\n"
"}")

        self.gridLayout_3.addWidget(self.lineEdit_add_id, 1, 1, 1, 1)

        self.pushButton_add = QPushButton(self.frame_add)
        self.pushButton_add.setObjectName(u"pushButton_add")
        self.pushButton_add.setMinimumSize(QSize(0, 50))
        self.pushButton_add.setFont(font8)

        self.gridLayout_3.addWidget(self.pushButton_add, 3, 1, 1, 1)

        self.lineEdit_add_password = QLineEdit(self.frame_add)
        self.lineEdit_add_password.setObjectName(u"lineEdit_add_password")
        self.lineEdit_add_password.setMinimumSize(QSize(0, 50))
        self.lineEdit_add_password.setFont(font8)
        self.lineEdit_add_password.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 10px;\n"
"	border: 2px solid rgb(34, 36, 43);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 3px solid rgb(91, 101, 124);\n"
"}")

        self.gridLayout_3.addWidget(self.lineEdit_add_password, 2, 1, 1, 1)

        self.label_add_name = QLabel(self.frame_add)
        self.label_add_name.setObjectName(u"label_add_name")
        self.label_add_name.setFont(font7)
        self.label_add_name.setStyleSheet(u"c")
        self.label_add_name.setAlignment(Qt.AlignCenter)
        self.label_add_name.setMargin(20)

        self.gridLayout_3.addWidget(self.label_add_name, 0, 0, 1, 1)


        self.verticalLayout_7.addWidget(self.frame_add)

        self.stackedWidget.addWidget(self.page_add)
        self.page_retrieve = QWidget()
        self.page_retrieve.setObjectName(u"page_retrieve")
        palette13 = QPalette()
        palette13.setBrush(QPalette.Active, QPalette.WindowText, brush22)
        palette13.setBrush(QPalette.Active, QPalette.Button, brush8)
        palette13.setBrush(QPalette.Active, QPalette.Text, brush22)
        palette13.setBrush(QPalette.Active, QPalette.ButtonText, brush22)
        palette13.setBrush(QPalette.Active, QPalette.Base, brush8)
        palette13.setBrush(QPalette.Active, QPalette.Window, brush8)
        brush26 = QBrush(QColor(200, 200, 200, 128))
        brush26.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette13.setBrush(QPalette.Active, QPalette.PlaceholderText, brush26)
#endif
        palette13.setBrush(QPalette.Inactive, QPalette.WindowText, brush22)
        palette13.setBrush(QPalette.Inactive, QPalette.Button, brush8)
        palette13.setBrush(QPalette.Inactive, QPalette.Text, brush22)
        palette13.setBrush(QPalette.Inactive, QPalette.ButtonText, brush22)
        palette13.setBrush(QPalette.Inactive, QPalette.Base, brush8)
        palette13.setBrush(QPalette.Inactive, QPalette.Window, brush8)
        brush27 = QBrush(QColor(200, 200, 200, 128))
        brush27.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette13.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush27)
#endif
        palette13.setBrush(QPalette.Disabled, QPalette.WindowText, brush22)
        palette13.setBrush(QPalette.Disabled, QPalette.Button, brush8)
        palette13.setBrush(QPalette.Disabled, QPalette.Text, brush22)
        palette13.setBrush(QPalette.Disabled, QPalette.ButtonText, brush22)
        palette13.setBrush(QPalette.Disabled, QPalette.Base, brush8)
        palette13.setBrush(QPalette.Disabled, QPalette.Window, brush8)
        brush28 = QBrush(QColor(200, 200, 200, 128))
        brush28.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette13.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush28)
#endif
        self.page_retrieve.setPalette(palette13)
        self.page_retrieve.setStyleSheet(u"color:#c8c8c8;")
        self.horizontalLayout_8 = QHBoxLayout(self.page_retrieve)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.frame_list = QFrame(self.page_retrieve)
        self.frame_list.setObjectName(u"frame_list")
        self.frame_list.setMaximumSize(QSize(400, 16777215))
        self.verticalLayout_9 = QVBoxLayout(self.frame_list)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_search = QFrame(self.frame_list)
        self.frame_search.setObjectName(u"frame_search")
        self.frame_search.setMinimumSize(QSize(0, 50))
        self.frame_search.setMaximumSize(QSize(16777215, 40))
        self.horizontalLayout_12 = QHBoxLayout(self.frame_search)
        self.horizontalLayout_12.setSpacing(5)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_search = QLineEdit(self.frame_search)
        self.lineEdit_search.setObjectName(u"lineEdit_search")
        self.lineEdit_search.setMinimumSize(QSize(0, 35))
        self.lineEdit_search.setMaximumSize(QSize(16777215, 35))
        self.lineEdit_search.setStyleSheet(u"\n"
"\n"
"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 3px;\n"
"	border: 2px solid rgb(34, 36, 43);\n"
"	padding-left: 10px;\n"
"	font-size : 15px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")

        self.horizontalLayout_12.addWidget(self.lineEdit_search)

        self.pushButton_search = QPushButton(self.frame_search)
        self.pushButton_search.setObjectName(u"pushButton_search")
        self.pushButton_search.setMinimumSize(QSize(70, 35))
        self.pushButton_search.setMaximumSize(QSize(70, 35))
        self.pushButton_search.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/16x16/cil-magnifying-glass.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_search.setIcon(icon3)

        self.horizontalLayout_12.addWidget(self.pushButton_search)


        self.verticalLayout_9.addWidget(self.frame_search)

#         self.scrollArea = QScrollArea(self.frame_list)
#         self.scrollArea.setObjectName(u"scrollArea")
#         self.scrollArea.setMinimumSize(QSize(400, 0))
#         self.scrollArea.setMaximumSize(QSize(400, 16777215))
#         self.scrollArea.setStyleSheet(u"QScrollArea {\n"
# "	border-radius : 7px;\n"
# "	border: 3px solid rgb(34, 36, 43);\n"
# "    margin-top : 5px\n"
# "}\n"
# "QScrollBar:horizontal {\n"
# "    border: none;\n"
# "    background: rgb(52, 59, 72);\n"
# "    height: 14px;\n"
# "    margin: 0px 21px 0 21px;\n"
# "	border-radius: 0px;\n"
# "}\n"
# " QScrollBar:vertical {\n"
# "	border: none;\n"
# "    background: rgb(52, 59, 72);\n"
# "    width: 14px;\n"
# "    margin: 21px 0 21px 0;\n"
# "	border-radius: 0px;\n"
# " }")
#         self.scrollArea.setWidgetResizable(True)
#         self.scrollAreaWidgetContents = QWidget()
#         self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
#         self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 384, 542))
#         self.verticalLayout_14 = QVBoxLayout(self.scrollAreaWidgetContents)
#         self.verticalLayout_14.setSpacing(10)
#         self.verticalLayout_14.setObjectName(u"verticalLayout_14")
#         self.verticalLayout_14.setContentsMargins(9, 0, 0, 0)
#         self.pushButton_example1 = QPushButton(self.scrollAreaWidgetContents)
#         self.pushButton_example1.setObjectName(u"pushButton_example1")
#         self.pushButton_example1.setMinimumSize(QSize(0, 80))
#         self.pushButton_example1.setMaximumSize(QSize(16777215, 80))
#         self.pushButton_example1.setFont(font8)
#         self.pushButton_example1.setStyleSheet(u"QPushButton{\n"
# "background-color : #32363e;\n"
# "border-radius: 10px;\n"
# "}\n"
# "\n"
# "QPushButton:hover {\n"
# "	border: 2px solid #41454d;\n"
# "}\n"
# "QPushButton:pressed {	\n"
# "	background-color: rgb(35, 40, 49); /* pressed button border = \ubc30\uacbd r+8 g+10 b+12 */\n"
# "	border: 2px solid rgb(43, 50, 61);\n"
# "}\n"
# "\n"
# "")

#         self.verticalLayout_14.addWidget(self.pushButton_example1)

#         self.scrollArea.setWidget(self.scrollAreaWidgetContents)

#         self.verticalLayout_9.addWidget(self.scrollArea)

        self.horizontalLayout_8.addWidget(self.frame_list)

        self.stackedWidget_2 = QStackedWidget(self.page_retrieve)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.stackedWidget_2.setStyleSheet(u"stackedWidget_2{\n"
"page_specific{\\nborder-radius : 7px;\\n	border: 3px solid rgb(34, 36, 43);\\n}\n"
"}")
        self.page_guide = QWidget()
        self.page_guide.setObjectName(u"page_guide")
        self.verticalLayout_11 = QVBoxLayout(self.page_guide)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_guide = QLabel(self.page_guide)
        self.label_guide.setObjectName(u"label_guide")
        font10 = QFont()
        font10.setFamily(u"Segoe UI")
        font10.setPointSize(20)
        font10.setBold(False)
        font10.setWeight(50)
        self.label_guide.setFont(font10)
        self.label_guide.setStyleSheet(u"border-radius : 7px;\n"
"	border: 3px solid rgb(34, 36, 43);")
        self.label_guide.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_guide)

        self.stackedWidget_2.addWidget(self.page_guide)
        self.page_specific = QWidget()
        self.page_specific.setObjectName(u"page_specific")
        self.page_specific.setStyleSheet(u"")
        self.verticalLayout_10 = QVBoxLayout(self.page_specific)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.frame_name_delete = QFrame(self.page_specific)
        self.frame_name_delete.setObjectName(u"frame_name_delete")
        self.frame_name_delete.setMaximumSize(QSize(16777215, 70))
        self.e = QHBoxLayout(self.frame_name_delete)
        self.e.setSpacing(0)
        self.e.setObjectName(u"e")
        self.e.setContentsMargins(0, 0, 12, 0)
        self.label_service_name = QLabel(self.frame_name_delete)
        self.label_service_name.setObjectName(u"label_service_name")
        font11 = QFont()
        font11.setFamily(u"Segoe UI")
        font11.setPointSize(20)
        font11.setBold(True)
        font11.setWeight(75)
        self.label_service_name.setFont(font11)
        self.label_service_name.setStyleSheet(u"padding-left : 100px;")
        self.label_service_name.setAlignment(Qt.AlignCenter)
        self.label_service_name.setIndent(-1)

        self.e.addWidget(self.label_service_name)

        self.pushButton_delete = QPushButton(self.frame_name_delete)
        self.pushButton_delete.setObjectName(u"pushButton_delete")
        self.pushButton_delete.setMaximumSize(QSize(100, 16777215))
        self.pushButton_delete.setFont(font)
        self.pushButton_delete.setStyleSheet(u"color:#c8272f;")

        self.e.addWidget(self.pushButton_delete)


        self.verticalLayout_10.addWidget(self.frame_name_delete)

        self.frame_retrieve = QFrame(self.page_specific)
        self.frame_retrieve.setObjectName(u"frame_retrieve")
        self.frame_retrieve.setMinimumSize(QSize(0, 200))
        self.frame_retrieve.setMaximumSize(QSize(16777215, 300))
        self.frame_retrieve.setStyleSheet(u"QFrame {\n"
"    border-radius : 7px;\n"
"	border: 3px solid rgb(36, 38, 45);\n"
"}")
        self.gridLayout = QGridLayout(self.frame_retrieve)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_password_2 = QLabel(self.frame_retrieve)
        self.label_password_2.setObjectName(u"label_password_2")
        font12 = QFont()
        font12.setFamily(u"Segoe UI")
        font12.setPointSize(12)
        font12.setBold(True)
        font12.setWeight(75)
        self.label_password_2.setFont(font12)
        self.label_password_2.setStyleSheet(u"border-radius : 0; margin-right : 5px")

        self.gridLayout.addWidget(self.label_password_2, 6, 1, 1, 1)

        self.checkBox_retrieve_show = QCheckBox(self.frame_retrieve)
        self.checkBox_retrieve_show.setObjectName(u"checkBox_retrieve_show")
        self.checkBox_retrieve_show.setMaximumSize(QSize(70, 30))

        self.gridLayout.addWidget(self.checkBox_retrieve_show, 6, 2, 1, 1)

        self.pushButton_clipboard_id = QPushButton(self.frame_retrieve)
        self.pushButton_clipboard_id.setObjectName(u"pushButton_clipboard_id")
        self.pushButton_clipboard_id.setMinimumSize(QSize(0, 50))
        self.pushButton_clipboard_id.setMaximumSize(QSize(100, 16777215))
        font13 = QFont()
        font13.setFamily(u"Segoe UI")
        font13.setBold(True)
        font13.setWeight(75)
        self.pushButton_clipboard_id.setFont(font13)

        self.gridLayout.addWidget(self.pushButton_clipboard_id, 1, 3, 1, 1)

        self.label_clipboard_id = QLabel(self.frame_retrieve)
        self.label_clipboard_id.setObjectName(u"label_clipboard_id")
        self.label_clipboard_id.setFont(font2)
        self.label_clipboard_id.setStyleSheet(u"border : None;")
        self.label_clipboard_id.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_clipboard_id, 2, 3, 1, 1)

        self.label_id = QLabel(self.frame_retrieve)
        self.label_id.setObjectName(u"label_id")
        self.label_id.setMinimumSize(QSize(80, 0))
        self.label_id.setMaximumSize(QSize(80, 16777215))
        font14 = QFont()
        font14.setPointSize(12)
        font14.setBold(True)
        font14.setWeight(75)
        self.label_id.setFont(font14)
        self.label_id.setStyleSheet(u"border:None;")
        self.label_id.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_id, 1, 0, 1, 1)

        self.pushButton_clipboard_password = QPushButton(self.frame_retrieve)
        self.pushButton_clipboard_password.setObjectName(u"pushButton_clipboard_password")
        self.pushButton_clipboard_password.setMinimumSize(QSize(0, 50))
        self.pushButton_clipboard_password.setMaximumSize(QSize(100, 16777215))
        self.pushButton_clipboard_password.setFont(font1)

        self.gridLayout.addWidget(self.pushButton_clipboard_password, 6, 3, 1, 1)

        self.label_password = QLabel(self.frame_retrieve)
        self.label_password.setObjectName(u"label_password")
        self.label_password.setMinimumSize(QSize(80, 0))
        self.label_password.setMaximumSize(QSize(80, 16777215))
        self.label_password.setFont(font12)
        self.label_password.setStyleSheet(u"border:None;")
        self.label_password.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_password, 6, 0, 1, 1)

        self.label_id_2 = QLabel(self.frame_retrieve)
        self.label_id_2.setObjectName(u"label_id_2")
        self.label_id_2.setFont(font12)
        self.label_id_2.setStyleSheet(u"border-radius : 0;  margin-right : 5px;")
        self.label_id_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_id_2, 1, 1, 1, 1)

        self.label_clipboard_password = QLabel(self.frame_retrieve)
        self.label_clipboard_password.setObjectName(u"label_clipboard_password")
        self.label_clipboard_password.setStyleSheet(u"border : None;")
        self.label_clipboard_password.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_clipboard_password, 7, 3, 1, 1)


        self.verticalLayout_10.addWidget(self.frame_retrieve)

        self.frame_edit_guide = QFrame(self.page_specific)
        self.frame_edit_guide.setObjectName(u"frame_edit_guide")
        self.frame_edit_guide.setMaximumSize(QSize(16777215, 100))
        self.horizontalLayout_13 = QHBoxLayout(self.frame_edit_guide)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_edit_guide = QLabel(self.frame_edit_guide)
        self.label_edit_guide.setObjectName(u"label_edit_guide")
        self.label_edit_guide.setMinimumSize(QSize(0, 50))
        self.label_edit_guide.setMaximumSize(QSize(16777215, 50))
        font15 = QFont()
        font15.setFamily(u"Segoe UI")
        font15.setPointSize(12)
        font15.setBold(False)
        font15.setItalic(False)
        font15.setUnderline(False)
        font15.setWeight(50)
        font15.setStrikeOut(False)
        self.label_edit_guide.setFont(font15)
        self.label_edit_guide.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.label_edit_guide)


        self.verticalLayout_10.addWidget(self.frame_edit_guide)

        self.frame_edit = QFrame(self.page_specific)
        self.frame_edit.setObjectName(u"frame_edit")
        self.frame_edit.setStyleSheet(u"QFrame {\n"
"    border-radius : 7px;\n"
"	border: 3px solid rgb(36, 38, 45);\n"
"}\n"
"")
        self.gridLayout_2 = QGridLayout(self.frame_edit)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(8)
        self.gridLayout_2.setVerticalSpacing(0)
        self.gridLayout_2.setContentsMargins(10, 0, 0, 0)
        self.lineEdit_edit_id = QLineEdit(self.frame_edit)
        self.lineEdit_edit_id.setObjectName(u"lineEdit_edit_id")
        self.lineEdit_edit_id.setMinimumSize(QSize(0, 40))
        self.lineEdit_edit_id.setMaximumSize(QSize(16777215, 40))
        self.lineEdit_edit_id.setFont(font2)
        self.lineEdit_edit_id.setStyleSheet(u"\n"
"\n"
"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 3px;\n"
"	border: 2px solid rgb(34, 36, 43);\n"
"	padding-left: 10px;\n"
"	font-size : 15px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.lineEdit_edit_id.setMaxLength(20)

        self.gridLayout_2.addWidget(self.lineEdit_edit_id, 0, 2, 1, 1)

        self.label_edit_password = QLabel(self.frame_edit)
        self.label_edit_password.setObjectName(u"label_edit_password")
        self.label_edit_password.setMinimumSize(QSize(80, 40))
        self.label_edit_password.setMaximumSize(QSize(80, 40))
        self.label_edit_password.setFont(font12)
        self.label_edit_password.setStyleSheet(u"border:None;")
        self.label_edit_password.setAlignment(Qt.AlignCenter)
        self.label_edit_password.setMargin(2)

        self.gridLayout_2.addWidget(self.label_edit_password, 1, 0, 1, 1)

        self.lineEdit_edit_password = QLineEdit(self.frame_edit)
        self.lineEdit_edit_password.setObjectName(u"lineEdit_edit_password")
        self.lineEdit_edit_password.setMinimumSize(QSize(0, 40))
        self.lineEdit_edit_password.setMaximumSize(QSize(16777215, 40))
        self.lineEdit_edit_password.setFont(font2)
        self.lineEdit_edit_password.setStyleSheet(u"\n"
"\n"
"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 3px;\n"
"	border: 2px solid rgb(34, 36, 43);\n"
"	padding-left: 10px;\n"
"	font-size : 15px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")

        self.gridLayout_2.addWidget(self.lineEdit_edit_password, 1, 2, 1, 1)

        self.checkBox_edit_show = QCheckBox(self.frame_edit)
        self.checkBox_edit_show.setObjectName(u"checkBox_edit_show")
        self.checkBox_edit_show.setMinimumSize(QSize(70, 0))
        self.checkBox_edit_show.setMaximumSize(QSize(70, 16777215))

        self.gridLayout_2.addWidget(self.checkBox_edit_show, 1, 4, 1, 1)

        self.label_edit_id = QLabel(self.frame_edit)
        self.label_edit_id.setObjectName(u"label_edit_id")
        self.label_edit_id.setMinimumSize(QSize(80, 40))
        self.label_edit_id.setMaximumSize(QSize(80, 40))
        self.label_edit_id.setFont(font12)
        self.label_edit_id.setStyleSheet(u"border:None;")
        self.label_edit_id.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_edit_id, 0, 0, 1, 1)

        self.pushButton_edit_save = QPushButton(self.frame_edit)
        self.pushButton_edit_save.setObjectName(u"pushButton_edit_save")
        self.pushButton_edit_save.setMinimumSize(QSize(0, 35))
        self.pushButton_edit_save.setMaximumSize(QSize(16777215, 35))
        self.pushButton_edit_save.setFont(font12)

        self.gridLayout_2.addWidget(self.pushButton_edit_save, 2, 2, 1, 2)


        self.verticalLayout_10.addWidget(self.frame_edit)

        self.stackedWidget_2.addWidget(self.page_specific)

        self.horizontalLayout_8.addWidget(self.stackedWidget_2)

        self.stackedWidget.addWidget(self.page_retrieve)
        self.page_setting = QWidget()
        self.page_setting.setObjectName(u"page_setting")
        self.verticalLayout_8 = QVBoxLayout(self.page_setting)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_assign = QFrame(self.page_setting)
        self.frame_assign.setObjectName(u"frame_assign")
        self.frame_assign.setMaximumSize(QSize(16777215, 200))
        self.gridLayout_4 = QGridLayout(self.frame_assign)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(3, 3, 3, 3)
        self.label_current = QLabel(self.frame_assign)
        self.label_current.setObjectName(u"label_current")
        font16 = QFont()
        font16.setFamily(u"Segoe UI")
        font16.setPointSize(13)
        self.label_current.setFont(font16)
        self.label_current.setStyleSheet(u"color:#62676f;")

        self.gridLayout_4.addWidget(self.label_current, 1, 0, 1, 1)

        self.pushButton_open_folder = QPushButton(self.frame_assign)
        self.pushButton_open_folder.setObjectName(u"pushButton_open_folder")
        self.pushButton_open_folder.setMaximumSize(QSize(150, 30))
        font17 = QFont()
        font17.setFamily(u"Segoe UI")
        font17.setPointSize(10)
        self.pushButton_open_folder.setFont(font17)
        self.pushButton_open_folder.setFocusPolicy(Qt.StrongFocus)
        self.pushButton_open_folder.setStyleSheet(u"QPushButton {\n"
"color:#c8c8c8;\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/16x16/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_open_folder.setIcon(icon4)

        self.gridLayout_4.addWidget(self.pushButton_open_folder, 1,1,1,1)


        self.pushButton_restore = QPushButton(self.frame_assign)
        self.pushButton_restore.setObjectName(u"pushButton_restore")
        self.pushButton_restore.setMaximumSize(QSize(150, 30))
        font17 = QFont()
        font17.setFamily(u"Segoe UI")
        font17.setPointSize(10)
        self.pushButton_restore.setFont(font17)
        self.pushButton_restore.setFocusPolicy(Qt.StrongFocus)
        self.pushButton_restore.setStyleSheet(u"QPushButton {\n"
"color:#c8c8c8;\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/16x16/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_restore.setIcon(icon4)

        self.gridLayout_4.addWidget(self.pushButton_restore, 2, 1)

        self.label_assign = QLabel(self.frame_assign)
        self.label_assign.setObjectName(u"label_assign")
        self.label_assign.setMaximumSize(QSize(16777215, 40))
        self.label_assign.setFont(font8)
        self.label_assign.setStyleSheet(u"background-color:#272c36;\n"
"color:#c8c8c8;")
        self.label_assign.setMargin(9)

        self.gridLayout_4.addWidget(self.label_assign, 0, 0, 1, 2)


        self.verticalLayout_8.addWidget(self.frame_assign)

        self.frame_nothing_more = QFrame(self.page_setting)
        self.frame_nothing_more.setObjectName(u"frame_nothing_more")
        self.verticalLayout_12 = QVBoxLayout(self.frame_nothing_more)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_nothing_more = QLabel(self.frame_nothing_more)
        self.label_nothing_more.setObjectName(u"label_nothing_more")
        palette14 = QPalette()
        palette14.setBrush(QPalette.Active, QPalette.WindowText, brush22)
        palette14.setBrush(QPalette.Active, QPalette.Button, brush8)
        palette14.setBrush(QPalette.Active, QPalette.Text, brush22)
        palette14.setBrush(QPalette.Active, QPalette.ButtonText, brush22)
        palette14.setBrush(QPalette.Active, QPalette.Base, brush8)
        palette14.setBrush(QPalette.Active, QPalette.Window, brush8)
        brush29 = QBrush(QColor(200, 200, 200, 128))
        brush29.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette14.setBrush(QPalette.Active, QPalette.PlaceholderText, brush29)
#endif
        palette14.setBrush(QPalette.Inactive, QPalette.WindowText, brush22)
        palette14.setBrush(QPalette.Inactive, QPalette.Button, brush8)
        palette14.setBrush(QPalette.Inactive, QPalette.Text, brush22)
        palette14.setBrush(QPalette.Inactive, QPalette.ButtonText, brush22)
        palette14.setBrush(QPalette.Inactive, QPalette.Base, brush8)
        palette14.setBrush(QPalette.Inactive, QPalette.Window, brush8)
        brush30 = QBrush(QColor(200, 200, 200, 128))
        brush30.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette14.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush30)
#endif
        palette14.setBrush(QPalette.Disabled, QPalette.WindowText, brush22)
        palette14.setBrush(QPalette.Disabled, QPalette.Button, brush8)
        palette14.setBrush(QPalette.Disabled, QPalette.Text, brush22)
        palette14.setBrush(QPalette.Disabled, QPalette.ButtonText, brush22)
        palette14.setBrush(QPalette.Disabled, QPalette.Base, brush8)
        palette14.setBrush(QPalette.Disabled, QPalette.Window, brush8)
        brush31 = QBrush(QColor(200, 200, 200, 128))
        brush31.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette14.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush31)
#endif
        self.label_nothing_more.setPalette(palette14)
        self.label_nothing_more.setFont(font10)
        self.label_nothing_more.setStyleSheet(u"color:#c8c8c8;")
        self.label_nothing_more.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_nothing_more)


        self.verticalLayout_8.addWidget(self.frame_nothing_more)

        self.stackedWidget.addWidget(self.page_setting)

        self.verticalLayout_4.addWidget(self.stackedWidget)


        self.frame_content.addWidget(self.frame_content_2)

        self.frame_label_bottom = QFrame(self.frame_center_right)
        self.frame_label_bottom.setObjectName(u"frame_label_bottom")
        self.frame_label_bottom.setMinimumSize(QSize(0, 25))
        self.frame_label_bottom.setMaximumSize(QSize(16777215, 25))
        palette15 = QPalette()
        palette15.setBrush(QPalette.Active, QPalette.WindowText, brush9)
        brush32 = QBrush(QColor(33, 37, 43, 255))
        brush32.setStyle(Qt.SolidPattern)
        palette15.setBrush(QPalette.Active, QPalette.Button, brush32)
        palette15.setBrush(QPalette.Active, QPalette.Text, brush9)
        palette15.setBrush(QPalette.Active, QPalette.ButtonText, brush9)
        palette15.setBrush(QPalette.Active, QPalette.Base, brush32)
        palette15.setBrush(QPalette.Active, QPalette.Window, brush32)
        brush33 = QBrush(QColor(98, 103, 111, 128))
        brush33.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette15.setBrush(QPalette.Active, QPalette.PlaceholderText, brush33)
#endif
        palette15.setBrush(QPalette.Inactive, QPalette.WindowText, brush9)
        palette15.setBrush(QPalette.Inactive, QPalette.Button, brush32)
        palette15.setBrush(QPalette.Inactive, QPalette.Text, brush9)
        palette15.setBrush(QPalette.Inactive, QPalette.ButtonText, brush9)
        palette15.setBrush(QPalette.Inactive, QPalette.Base, brush32)
        palette15.setBrush(QPalette.Inactive, QPalette.Window, brush32)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette15.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush33)
#endif
        palette15.setBrush(QPalette.Disabled, QPalette.WindowText, brush9)
        palette15.setBrush(QPalette.Disabled, QPalette.Button, brush32)
        palette15.setBrush(QPalette.Disabled, QPalette.Text, brush9)
        palette15.setBrush(QPalette.Disabled, QPalette.ButtonText, brush9)
        palette15.setBrush(QPalette.Disabled, QPalette.Base, brush32)
        palette15.setBrush(QPalette.Disabled, QPalette.Window, brush32)
        brush34 = QBrush(QColor(0, 0, 0, 128))
        brush34.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette15.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush34)
#endif
        self.frame_label_bottom.setPalette(palette15)
        self.frame_label_bottom.setLayoutDirection(Qt.LeftToRight)
        self.frame_label_bottom.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.horizontalLayout_6 = QHBoxLayout(self.frame_label_bottom)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_developer = QLabel(self.frame_label_bottom)
        self.label_developer.setObjectName(u"label_developer")
        self.label_developer.setMaximumSize(QSize(120000, 16777215))
        palette16 = QPalette()
        palette16.setBrush(QPalette.Active, QPalette.WindowText, brush9)
        palette16.setBrush(QPalette.Active, QPalette.Button, brush32)
        palette16.setBrush(QPalette.Active, QPalette.Text, brush9)
        palette16.setBrush(QPalette.Active, QPalette.ButtonText, brush9)
        palette16.setBrush(QPalette.Active, QPalette.Base, brush32)
        palette16.setBrush(QPalette.Active, QPalette.Window, brush32)
        brush35 = QBrush(QColor(98, 103, 111, 128))
        brush35.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette16.setBrush(QPalette.Active, QPalette.PlaceholderText, brush35)
#endif
        palette16.setBrush(QPalette.Inactive, QPalette.WindowText, brush9)
        palette16.setBrush(QPalette.Inactive, QPalette.Button, brush32)
        palette16.setBrush(QPalette.Inactive, QPalette.Text, brush9)
        palette16.setBrush(QPalette.Inactive, QPalette.ButtonText, brush9)
        palette16.setBrush(QPalette.Inactive, QPalette.Base, brush32)
        palette16.setBrush(QPalette.Inactive, QPalette.Window, brush32)
        brush36 = QBrush(QColor(98, 103, 111, 128))
        brush36.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette16.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush36)
#endif
        palette16.setBrush(QPalette.Disabled, QPalette.WindowText, brush9)
        palette16.setBrush(QPalette.Disabled, QPalette.Button, brush32)
        palette16.setBrush(QPalette.Disabled, QPalette.Text, brush9)
        palette16.setBrush(QPalette.Disabled, QPalette.ButtonText, brush9)
        palette16.setBrush(QPalette.Disabled, QPalette.Base, brush32)
        palette16.setBrush(QPalette.Disabled, QPalette.Window, brush32)
        brush37 = QBrush(QColor(98, 103, 111, 128))
        brush37.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette16.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush37)
#endif
        self.label_developer.setPalette(palette16)
        font18 = QFont()
        font18.setFamily(u"Segoe UI")
        font18.setBold(False)
        font18.setWeight(50)
        self.label_developer.setFont(font18)
        self.label_developer.setStyleSheet(u"")
        self.label_developer.setLineWidth(0)
        self.label_developer.setMidLineWidth(0)
        self.label_developer.setMargin(0)

        self.horizontalLayout_6.addWidget(self.label_developer)

        self.label_version = QLabel(self.frame_label_bottom)
        self.label_version.setObjectName(u"label_version")
        palette17 = QPalette()
        palette17.setBrush(QPalette.Active, QPalette.WindowText, brush9)
        palette17.setBrush(QPalette.Active, QPalette.Button, brush32)
        palette17.setBrush(QPalette.Active, QPalette.Text, brush9)
        palette17.setBrush(QPalette.Active, QPalette.ButtonText, brush9)
        palette17.setBrush(QPalette.Active, QPalette.Base, brush32)
        palette17.setBrush(QPalette.Active, QPalette.Window, brush32)
        brush38 = QBrush(QColor(98, 103, 111, 128))
        brush38.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette17.setBrush(QPalette.Active, QPalette.PlaceholderText, brush38)
#endif
        palette17.setBrush(QPalette.Inactive, QPalette.WindowText, brush9)
        palette17.setBrush(QPalette.Inactive, QPalette.Button, brush32)
        palette17.setBrush(QPalette.Inactive, QPalette.Text, brush9)
        palette17.setBrush(QPalette.Inactive, QPalette.ButtonText, brush9)
        palette17.setBrush(QPalette.Inactive, QPalette.Base, brush32)
        palette17.setBrush(QPalette.Inactive, QPalette.Window, brush32)
        brush39 = QBrush(QColor(98, 103, 111, 128))
        brush39.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette17.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush39)
#endif
        palette17.setBrush(QPalette.Disabled, QPalette.WindowText, brush9)
        palette17.setBrush(QPalette.Disabled, QPalette.Button, brush32)
        palette17.setBrush(QPalette.Disabled, QPalette.Text, brush9)
        palette17.setBrush(QPalette.Disabled, QPalette.ButtonText, brush9)
        palette17.setBrush(QPalette.Disabled, QPalette.Base, brush32)
        palette17.setBrush(QPalette.Disabled, QPalette.Window, brush32)
        brush40 = QBrush(QColor(98, 103, 111, 128))
        brush40.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette17.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush40)
#endif
        self.label_version.setPalette(palette17)
        self.label_version.setFont(font2)
        self.label_version.setLayoutDirection(Qt.RightToLeft)
        self.label_version.setStyleSheet(u"")
        self.label_version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_version.setMargin(0)
        self.label_version.setTextInteractionFlags(Qt.NoTextInteraction)

        self.horizontalLayout_6.addWidget(self.label_version)

        self.frame_size_grip = QFrame(self.frame_label_bottom)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(20, 0))
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setStyleSheet(u"QSizeGrip {\n"
"	background-image: url(:/icons/icons/16x16/cil-size-grip.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}")
        self.frame_size_grip.setFrameShape(QFrame.StyledPanel)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_6.addWidget(self.frame_size_grip)


        self.frame_content.addWidget(self.frame_label_bottom)


        self.horizontalLayout.addWidget(self.frame_center_right)


        self.verticalLayout.addWidget(self.frame_center)


        self.horizontalLayout_2.addWidget(self.frame_main)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)
        self.stackedWidget_2.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"AccountBox", None))
        self.btn_toggle_menu.setText("")
        self.label_title_bar_top.setText(QCoreApplication.translate("MainWindow", u"wow", None))
#if QT_CONFIG(tooltip)
        self.btn_close.setToolTip(QCoreApplication.translate("MainWindow", u"close", None))
#endif // QT_CONFIG(tooltip)
        self.btn_close.setText("")
#if QT_CONFIG(tooltip)
        self.btn_maximize_restore.setToolTip(QCoreApplication.translate("MainWindow", u"maximize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_maximize_restore.setText("")
#if QT_CONFIG(tooltip)
        self.btn_minimize.setToolTip(QCoreApplication.translate("MainWindow", u"minimize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_minimize.setText("")
        self.label_fileloc.setText(QCoreApplication.translate("MainWindow", u"wow", None))
        self.label_where.setText(QCoreApplication.translate("MainWindow", u"| HOME", None))
        self.label_name.setText(QCoreApplication.translate("MainWindow", u"AccountBox", None))
        self.label_intro.setText(QCoreApplication.translate("MainWindow", u"Manage your account datas more comfortable,\n"
"retrieve them with no anxiety of exposure", None))
        self.label_first_time.setText(QCoreApplication.translate("MainWindow", u"At first, press 'restore' button at Setting", None))
        self.label_space.setText("")
        self.label_add_password.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.lineEdit_add_name.setText("")
        self.lineEdit_add_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Service Name", None))
#if QT_CONFIG(tooltip)
        self.checkBox_add_show.setToolTip(QCoreApplication.translate("MainWindow", u"have a look around before click this", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_add_show.setText(QCoreApplication.translate("MainWindow", u"Show password", None))
        self.label_add_id.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.lineEdit_add_id.setText("")
        self.lineEdit_add_id.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.pushButton_add.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.lineEdit_add_password.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.label_add_name.setText(QCoreApplication.translate("MainWindow", u"Service name", None))
        self.lineEdit_search.setText("")
        self.lineEdit_search.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here", None))
#if QT_CONFIG(tooltip)
        self.pushButton_search.setToolTip(QCoreApplication.translate("MainWindow", u"search", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_search.setText("")


#        self.pushButton_example1.setText(QCoreApplication.translate("MainWindow", u"Facebook", None))


        self.label_guide.setText(QCoreApplication.translate("MainWindow", u"Search services you want\n"
"and click it to retrieve!", None))
        self.label_service_name.setText(QCoreApplication.translate("MainWindow", u"Servicename", None))
#if QT_CONFIG(tooltip)
        self.pushButton_delete.setToolTip(QCoreApplication.translate("MainWindow", u"delete data of this service", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_delete.setText(QCoreApplication.translate("MainWindow", u"DELETE", None))
        self.label_password_2.setText(QCoreApplication.translate("MainWindow", u"password(******)", None))
#if QT_CONFIG(tooltip)
        self.checkBox_retrieve_show.setToolTip(QCoreApplication.translate("MainWindow", u"have a look around before click this", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_retrieve_show.setText(QCoreApplication.translate("MainWindow", u"Show", None))
        self.pushButton_clipboard_id.setText(QCoreApplication.translate("MainWindow", u"copy to\n"
"clipboard", None))
        self.label_clipboard_id.setText("")
        self.label_id.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.pushButton_clipboard_password.setText(QCoreApplication.translate("MainWindow", u"copy to\n"
"clipboard", None))
        self.label_password.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.label_id_2.setText(QCoreApplication.translate("MainWindow", u"id", None))
        self.label_clipboard_password.setText("")
        self.label_edit_guide.setText(QCoreApplication.translate("MainWindow", u"You can edit ID and Password below", None))
#if QT_CONFIG(tooltip)
        self.frame_edit.setToolTip(QCoreApplication.translate("MainWindow", u"", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit_edit_id.setText("")
        self.lineEdit_edit_id.setPlaceholderText(QCoreApplication.translate("MainWindow", u"New ID", None))
        self.label_edit_password.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.lineEdit_edit_password.setText("")
        self.lineEdit_edit_password.setPlaceholderText(QCoreApplication.translate("MainWindow", u"New password", None))
#if QT_CONFIG(tooltip)
        self.checkBox_edit_show.setToolTip(QCoreApplication.translate("MainWindow", u"have a look around before click this", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_edit_show.setText(QCoreApplication.translate("MainWindow", u"Show", None))
        self.label_edit_id.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.pushButton_edit_save.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.label_current.setText(QCoreApplication.translate("MainWindow", u"Current : C:\\Users\\bolt6281\\programming\\Python\\SoloProjects\\AccountBox\\account_data.json", None))
        self.pushButton_open_folder.setText(QCoreApplication.translate("MainWindow", u"Open Folder", None))
        self.pushButton_restore.setText(QCoreApplication.translate("MainWindow", u"Restore", None))
        self.label_assign.setText(QCoreApplication.translate("MainWindow", u"ASSIGN ACCOUNT FILE", None))
        self.label_nothing_more.setText(QCoreApplication.translate("MainWindow", u"Nothing more yet", None))
#if QT_CONFIG(tooltip)
        self.label_developer.setToolTip(QCoreApplication.translate("MainWindow", u"who is the most handsome person", None))
#endif // QT_CONFIG(tooltip)
        self.label_developer.setText(QCoreApplication.translate("MainWindow", u" developed by bolt6281", None))
        self.label_version.setText(QCoreApplication.translate("MainWindow", u"v1.0.0", None))
    # retranslateUi

