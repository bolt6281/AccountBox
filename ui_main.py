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
        MainWindow.resize(1000, 720)
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
        brush2.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        brush3 = QBrush(QColor(210, 210, 210, 128))
        brush3.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush3)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        brush4 = QBrush(QColor(210, 210, 210, 128))
        brush4.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        MainWindow.setPalette(palette)
        font = QFont()
        font.setPointSize(25)
        MainWindow.setFont(font)
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
        brush5 = QBrush(QColor(39, 44, 54, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush5)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush5)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush5)
        brush6 = QBrush(QColor(210, 210, 210, 128))
        brush6.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush5)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush5)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush5)
        brush7 = QBrush(QColor(210, 210, 210, 128))
        brush7.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush7)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush5)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush5)
        brush8 = QBrush(QColor(210, 210, 210, 128))
        brush8.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush8)
#endif
        self.centralwidget.setPalette(palette1)
        self.centralwidget.setStyleSheet(u"")
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
        brush9 = QBrush(QColor(210, 210, 210, 128))
        brush9.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Active, QPalette.PlaceholderText, brush9)
#endif
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        brush10 = QBrush(QColor(210, 210, 210, 128))
        brush10.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush10)
#endif
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        brush11 = QBrush(QColor(210, 210, 210, 128))
        brush11.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush11)
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
        brush12 = QBrush(QColor(27, 29, 35, 255))
        brush12.setStyle(Qt.SolidPattern)
        palette4.setBrush(QPalette.Active, QPalette.Button, brush12)
        palette4.setBrush(QPalette.Active, QPalette.Base, brush12)
        palette4.setBrush(QPalette.Active, QPalette.Window, brush12)
        palette4.setBrush(QPalette.Inactive, QPalette.Button, brush12)
        palette4.setBrush(QPalette.Inactive, QPalette.Base, brush12)
        palette4.setBrush(QPalette.Inactive, QPalette.Window, brush12)
        palette4.setBrush(QPalette.Disabled, QPalette.Button, brush12)
        palette4.setBrush(QPalette.Disabled, QPalette.Base, brush12)
        palette4.setBrush(QPalette.Disabled, QPalette.Window, brush12)
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
        brush13 = QBrush(QColor(34, 36, 43, 255))
        brush13.setStyle(Qt.SolidPattern)
        palette5.setBrush(QPalette.Active, QPalette.Button, brush13)
        palette5.setBrush(QPalette.Active, QPalette.Base, brush13)
        palette5.setBrush(QPalette.Active, QPalette.Window, brush13)
        palette5.setBrush(QPalette.Inactive, QPalette.Button, brush13)
        palette5.setBrush(QPalette.Inactive, QPalette.Base, brush13)
        palette5.setBrush(QPalette.Inactive, QPalette.Window, brush13)
        palette5.setBrush(QPalette.Disabled, QPalette.Button, brush13)
        palette5.setBrush(QPalette.Disabled, QPalette.Base, brush13)
        palette5.setBrush(QPalette.Disabled, QPalette.Window, brush13)
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
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_title_bar_top.setFont(font1)
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
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(9)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_fileloc.setFont(font2)
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
        brush14 = QBrush(QColor(98, 103, 102, 255))
        brush14.setStyle(Qt.SolidPattern)
        palette6.setBrush(QPalette.Active, QPalette.WindowText, brush14)
        palette6.setBrush(QPalette.Active, QPalette.Button, brush5)
        palette6.setBrush(QPalette.Active, QPalette.Base, brush5)
        palette6.setBrush(QPalette.Active, QPalette.Window, brush5)
        palette6.setBrush(QPalette.Inactive, QPalette.WindowText, brush14)
        palette6.setBrush(QPalette.Inactive, QPalette.Button, brush5)
        palette6.setBrush(QPalette.Inactive, QPalette.Base, brush5)
        palette6.setBrush(QPalette.Inactive, QPalette.Window, brush5)
        brush15 = QBrush(QColor(120, 120, 120, 255))
        brush15.setStyle(Qt.SolidPattern)
        palette6.setBrush(QPalette.Disabled, QPalette.WindowText, brush15)
        palette6.setBrush(QPalette.Disabled, QPalette.Button, brush5)
        palette6.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette6.setBrush(QPalette.Disabled, QPalette.Window, brush5)
        self.label_where.setPalette(palette6)
        self.label_where.setFont(font2)
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
        brush16 = QBrush(QColor(44, 49, 60, 255))
        brush16.setStyle(Qt.SolidPattern)
        palette7.setBrush(QPalette.Active, QPalette.Button, brush16)
        palette7.setBrush(QPalette.Active, QPalette.Base, brush16)
        palette7.setBrush(QPalette.Active, QPalette.Window, brush16)
        palette7.setBrush(QPalette.Inactive, QPalette.Button, brush16)
        palette7.setBrush(QPalette.Inactive, QPalette.Base, brush16)
        palette7.setBrush(QPalette.Inactive, QPalette.Window, brush16)
        palette7.setBrush(QPalette.Disabled, QPalette.Button, brush16)
        palette7.setBrush(QPalette.Disabled, QPalette.Base, brush16)
        palette7.setBrush(QPalette.Disabled, QPalette.Window, brush16)
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
        self.frame_left_menu.setStyleSheet(u"background-color: rgb(27, 29, 35);")
        self.verticalLayout_2 = QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_menus = QFrame(self.frame_left_menu)
        self.frame_menus.setObjectName(u"frame_menus")
        self.frame_menus.setMaximumSize(QSize(16777215, 1677148))
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setKerning(True)
        font3.setStyleStrategy(QFont.PreferDefault)
        self.frame_menus.setFont(font3)
        self.frame_menus.setStyleSheet(u"color:#c8c8c8")
        self.layout_menus = QVBoxLayout(self.frame_menus)
        self.layout_menus.setSpacing(0)
        self.layout_menus.setObjectName(u"layout_menus")
        self.layout_menus.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.layout_menus.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_2.addWidget(self.frame_menus)

        self.frame_extra_menus = QFrame(self.frame_left_menu)
        self.frame_extra_menus.setObjectName(u"frame_extra_menus")
        self.frame_extra_menus.setMinimumSize(QSize(0, 0))
        self.frame_extra_menus.setMaximumSize(QSize(16777215, 300))
        font4 = QFont()
        font4.setFamily(u"Segoe UI")
        self.frame_extra_menus.setFont(font4)
        self.frame_extra_menus.setStyleSheet(u"color:#c8c8c8")
        self.layout_menu_bottom = QVBoxLayout(self.frame_extra_menus)
        self.layout_menu_bottom.setSpacing(0)
        self.layout_menu_bottom.setObjectName(u"layout_menu_bottom")
        self.layout_menu_bottom.setContentsMargins(0, 0, 0, 25)

        self.verticalLayout_2.addWidget(self.frame_extra_menus)


        self.horizontalLayout.addWidget(self.frame_left_menu)

        self.frame_center_right = QFrame(self.frame_center)
        self.frame_center_right.setObjectName(u"frame_center_right")
        palette8 = QPalette()
        brush17 = QBrush(QColor(98, 103, 111, 255))
        brush17.setStyle(Qt.SolidPattern)
        palette8.setBrush(QPalette.Active, QPalette.WindowText, brush17)
        palette8.setBrush(QPalette.Active, QPalette.Button, brush16)
        palette8.setBrush(QPalette.Active, QPalette.Text, brush17)
        palette8.setBrush(QPalette.Active, QPalette.ButtonText, brush17)
        palette8.setBrush(QPalette.Active, QPalette.Base, brush16)
        palette8.setBrush(QPalette.Active, QPalette.Window, brush16)
        brush18 = QBrush(QColor(98, 103, 111, 128))
        brush18.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.Active, QPalette.PlaceholderText, brush18)
#endif
        palette8.setBrush(QPalette.Inactive, QPalette.WindowText, brush17)
        palette8.setBrush(QPalette.Inactive, QPalette.Button, brush16)
        palette8.setBrush(QPalette.Inactive, QPalette.Text, brush17)
        palette8.setBrush(QPalette.Inactive, QPalette.ButtonText, brush17)
        palette8.setBrush(QPalette.Inactive, QPalette.Base, brush16)
        palette8.setBrush(QPalette.Inactive, QPalette.Window, brush16)
        brush19 = QBrush(QColor(98, 103, 111, 128))
        brush19.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush19)
#endif
        palette8.setBrush(QPalette.Disabled, QPalette.WindowText, brush17)
        palette8.setBrush(QPalette.Disabled, QPalette.Button, brush16)
        palette8.setBrush(QPalette.Disabled, QPalette.Text, brush17)
        palette8.setBrush(QPalette.Disabled, QPalette.ButtonText, brush17)
        palette8.setBrush(QPalette.Disabled, QPalette.Base, brush16)
        palette8.setBrush(QPalette.Disabled, QPalette.Window, brush16)
        brush20 = QBrush(QColor(98, 103, 111, 128))
        brush20.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush20)
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
        palette9.setBrush(QPalette.Active, QPalette.WindowText, brush17)
        palette9.setBrush(QPalette.Active, QPalette.Button, brush16)
        palette9.setBrush(QPalette.Active, QPalette.Text, brush17)
        palette9.setBrush(QPalette.Active, QPalette.ButtonText, brush17)
        palette9.setBrush(QPalette.Active, QPalette.Base, brush16)
        palette9.setBrush(QPalette.Active, QPalette.Window, brush16)
        brush21 = QBrush(QColor(98, 103, 111, 128))
        brush21.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette9.setBrush(QPalette.Active, QPalette.PlaceholderText, brush21)
#endif
        palette9.setBrush(QPalette.Inactive, QPalette.WindowText, brush17)
        palette9.setBrush(QPalette.Inactive, QPalette.Button, brush16)
        palette9.setBrush(QPalette.Inactive, QPalette.Text, brush17)
        palette9.setBrush(QPalette.Inactive, QPalette.ButtonText, brush17)
        palette9.setBrush(QPalette.Inactive, QPalette.Base, brush16)
        palette9.setBrush(QPalette.Inactive, QPalette.Window, brush16)
        brush22 = QBrush(QColor(98, 103, 111, 128))
        brush22.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette9.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush22)
#endif
        palette9.setBrush(QPalette.Disabled, QPalette.WindowText, brush17)
        palette9.setBrush(QPalette.Disabled, QPalette.Button, brush16)
        palette9.setBrush(QPalette.Disabled, QPalette.Text, brush17)
        palette9.setBrush(QPalette.Disabled, QPalette.ButtonText, brush17)
        palette9.setBrush(QPalette.Disabled, QPalette.Base, brush16)
        palette9.setBrush(QPalette.Disabled, QPalette.Window, brush16)
        brush23 = QBrush(QColor(98, 103, 111, 128))
        brush23.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette9.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush23)
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
        palette10.setBrush(QPalette.Active, QPalette.WindowText, brush17)
        palette10.setBrush(QPalette.Active, QPalette.Button, brush16)
        palette10.setBrush(QPalette.Active, QPalette.Text, brush17)
        palette10.setBrush(QPalette.Active, QPalette.ButtonText, brush17)
        palette10.setBrush(QPalette.Active, QPalette.Base, brush16)
        palette10.setBrush(QPalette.Active, QPalette.Window, brush16)
        brush24 = QBrush(QColor(98, 103, 111, 128))
        brush24.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette10.setBrush(QPalette.Active, QPalette.PlaceholderText, brush24)
#endif
        palette10.setBrush(QPalette.Inactive, QPalette.WindowText, brush17)
        palette10.setBrush(QPalette.Inactive, QPalette.Button, brush16)
        palette10.setBrush(QPalette.Inactive, QPalette.Text, brush17)
        palette10.setBrush(QPalette.Inactive, QPalette.ButtonText, brush17)
        palette10.setBrush(QPalette.Inactive, QPalette.Base, brush16)
        palette10.setBrush(QPalette.Inactive, QPalette.Window, brush16)
        brush25 = QBrush(QColor(98, 103, 111, 128))
        brush25.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette10.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush25)
#endif
        palette10.setBrush(QPalette.Disabled, QPalette.WindowText, brush17)
        palette10.setBrush(QPalette.Disabled, QPalette.Button, brush16)
        palette10.setBrush(QPalette.Disabled, QPalette.Text, brush17)
        palette10.setBrush(QPalette.Disabled, QPalette.ButtonText, brush17)
        palette10.setBrush(QPalette.Disabled, QPalette.Base, brush16)
        palette10.setBrush(QPalette.Disabled, QPalette.Window, brush16)
        brush26 = QBrush(QColor(98, 103, 111, 128))
        brush26.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette10.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush26)
#endif
        self.stackedWidget.setPalette(palette10)
        self.page_register = QWidget()
        self.page_register.setObjectName(u"page_register")
        self.page_register.setFont(font4)
        self.page_register.setStyleSheet(u"color:#c8c8c8")
        self.verticalLayout_register = QVBoxLayout(self.page_register)
        self.verticalLayout_register.setObjectName(u"verticalLayout_register")
        self.verticalLayout_register.setContentsMargins(-1, 0, -1, 0)
        self.label_register_welcome = QLabel(self.page_register)
        self.label_register_welcome.setObjectName(u"label_register_welcome")
        self.label_register_welcome.setMinimumSize(QSize(0, 200))
        self.label_register_welcome.setMaximumSize(QSize(16777215, 200))
        font5 = QFont()
        font5.setFamily(u"Segoe UI")
        font5.setPointSize(35)
        font5.setBold(True)
        font5.setWeight(75)
        self.label_register_welcome.setFont(font5)

        self.verticalLayout_register.addWidget(self.label_register_welcome)

        self.label_register_explain = QLabel(self.page_register)
        self.label_register_explain.setObjectName(u"label_register_explain")
        self.label_register_explain.setMinimumSize(QSize(0, 120))
        self.label_register_explain.setMaximumSize(QSize(16777215, 120))
        font6 = QFont()
        font6.setFamily(u"Segoe UI")
        font6.setPointSize(18)
        self.label_register_explain.setFont(font6)
        self.label_register_explain.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_register.addWidget(self.label_register_explain)

        self.horizontalFrame_register = QFrame(self.page_register)
        self.horizontalFrame_register.setObjectName(u"horizontalFrame_register")
        self.horizontalFrame_register.setMinimumSize(QSize(0, 30))
        self.horizontalFrame_register.setMaximumSize(QSize(16777215, 100))
        self.horizontalFrame_register.setLayoutDirection(Qt.LeftToRight)
        self.horizontalLayout_9 = QHBoxLayout(self.horizontalFrame_register)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(20, -1, 20, 10)
        self.label_register_guide = QLabel(self.horizontalFrame_register)
        self.label_register_guide.setObjectName(u"label_register_guide")
        self.label_register_guide.setMinimumSize(QSize(0, 50))
        self.label_register_guide.setMaximumSize(QSize(16777215, 50))
        font7 = QFont()
        font7.setFamily(u"Segoe UI")
        font7.setPointSize(15)
        font7.setBold(False)
        font7.setWeight(50)
        self.label_register_guide.setFont(font7)
        self.label_register_guide.setStyleSheet(u"margin-left:130;")
        self.label_register_guide.setAlignment(Qt.AlignCenter)
        self.label_register_guide.setMargin(0)

        self.horizontalLayout_9.addWidget(self.label_register_guide)

        self.pushButton_register_existing = QPushButton(self.horizontalFrame_register)
        self.pushButton_register_existing.setObjectName(u"pushButton_register_existing")
        self.pushButton_register_existing.setMinimumSize(QSize(0, 40))
        self.pushButton_register_existing.setMaximumSize(QSize(120, 40))
        self.pushButton_register_existing.setFont(font4)
        self.pushButton_register_existing.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_9.addWidget(self.pushButton_register_existing)


        self.verticalLayout_register.addWidget(self.horizontalFrame_register)

        self.horizontalFrame_register_password = QFrame(self.page_register)
        self.horizontalFrame_register_password.setObjectName(u"horizontalFrame_register_password")
        self.horizontalLayout_10 = QHBoxLayout(self.horizontalFrame_register_password)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.lineEdit_register = QLineEdit(self.horizontalFrame_register_password)
        self.lineEdit_register.setObjectName(u"lineEdit_register")
        self.lineEdit_register.setMinimumSize(QSize(0, 50))
        self.lineEdit_register.setMaximumSize(QSize(16777215, 50))
        font8 = QFont()
        font8.setFamily(u"Segoe UI")
        font8.setPointSize(15)
        self.lineEdit_register.setFont(font8)
        self.lineEdit_register.setStyleSheet(u"QLineEdit {\n"
"margin-left:100px;\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 10px;\n"
"	border: 2px solid rgb(34, 36, 43);\n"
"	padding-left: 10px;\n"
"	color:#c8c8c8;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 3px solid rgb(91, 101, 124);\n"
"}")
        self.lineEdit_register.setAlignment(Qt.AlignCenter)
        self.lineEdit_register.setReadOnly(False)

        self.horizontalLayout_10.addWidget(self.lineEdit_register)

        self.checkBox_register = QCheckBox(self.horizontalFrame_register_password)
        self.checkBox_register.setObjectName(u"checkBox_register")
        self.checkBox_register.setMinimumSize(QSize(100, 0))
        self.checkBox_register.setMaximumSize(QSize(100, 16777215))
        font9 = QFont()
        font9.setFamily(u"Segoe UI")
        font9.setPointSize(12)
        self.checkBox_register.setFont(font9)
        self.checkBox_register.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_10.addWidget(self.checkBox_register)


        self.verticalLayout_register.addWidget(self.horizontalFrame_register_password)

        self.label_2 = QLabel(self.page_register)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 50))
        self.label_2.setMaximumSize(QSize(16777215, 50))

        self.verticalLayout_register.addWidget(self.label_2)

        self.pushButton_register = QPushButton(self.page_register)
        self.pushButton_register.setObjectName(u"pushButton_register")
        self.pushButton_register.setMinimumSize(QSize(300, 40))
        self.pushButton_register.setMaximumSize(QSize(300, 40))
        font10 = QFont()
        font10.setFamily(u"Segoe UI")
        font10.setPointSize(12)
        font10.setBold(False)
        font10.setWeight(50)
        self.pushButton_register.setFont(font10)
        self.pushButton_register.setStyleSheet(u"")

        self.verticalLayout_register.addWidget(self.pushButton_register)

        self.label_register_space = QLabel(self.page_register)
        self.label_register_space.setObjectName(u"label_register_space")
        self.label_register_space.setMinimumSize(QSize(0, 50))
        self.label_register_space.setMaximumSize(QSize(16777215, 50))
        font11 = QFont()
        font11.setFamily(u"Segoe UI")
        font11.setPointSize(12)
        font11.setBold(False)
        font11.setItalic(False)
        font11.setWeight(50)
        self.label_register_space.setFont(font11)
        self.label_register_space.setAutoFillBackground(False)
        self.label_register_space.setStyleSheet(u"margin-bottom:60px; color:#c8272f;margin-top:20px")
        self.label_register_space.setAlignment(Qt.AlignCenter)

        self.verticalLayout_register.addWidget(self.label_register_space)

        self.stackedWidget.addWidget(self.page_register)
        self.page_login = QWidget()
        self.page_login.setObjectName(u"page_login")
        self.page_login.setFont(font4)
        self.page_login.setStyleSheet(u"color:#c8c8c8")
        self.verticalLayout_login = QVBoxLayout(self.page_login)
        self.verticalLayout_login.setObjectName(u"verticalLayout_login")
        self.verticalLayout_login.setContentsMargins(-1, 0, -1, 0)
        self.label_login_1 = QLabel(self.page_login)
        self.label_login_1.setObjectName(u"label_login_1")
        self.label_login_1.setMinimumSize(QSize(0, 200))
        self.label_login_1.setMaximumSize(QSize(16777215, 200))
        self.label_login_1.setFont(font5)

        self.verticalLayout_login.addWidget(self.label_login_1)

        self.label_login_2 = QLabel(self.page_login)
        self.label_login_2.setObjectName(u"label_login_2")
        self.label_login_2.setMinimumSize(QSize(0, 120))
        self.label_login_2.setMaximumSize(QSize(16777215, 120))
        font12 = QFont()
        font12.setFamily(u"Segoe UI")
        font12.setPointSize(18)
        font12.setBold(False)
        font12.setWeight(50)
        self.label_login_2.setFont(font12)
        self.label_login_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_login.addWidget(self.label_login_2)

        self.label_login_3 = QLabel(self.page_login)
        self.label_login_3.setObjectName(u"label_login_3")
        self.label_login_3.setFont(font8)
        self.label_login_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_login.addWidget(self.label_login_3)

        self.horizontalFrame_login = QFrame(self.page_login)
        self.horizontalFrame_login.setObjectName(u"horizontalFrame_login")
        self.horizontalLayout_16 = QHBoxLayout(self.horizontalFrame_login)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(9, 9, 9, 9)
        self.lineEdit_login = QLineEdit(self.horizontalFrame_login)
        self.lineEdit_login.setObjectName(u"lineEdit_login")
        self.lineEdit_login.setMinimumSize(QSize(0, 50))
        self.lineEdit_login.setMaximumSize(QSize(16777215, 50))
        self.lineEdit_login.setFont(font8)
        self.lineEdit_login.setStyleSheet(u"QLineEdit {\n"
"margin-left:100px;\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 10px;\n"
"	border: 2px solid rgb(34, 36, 43);\n"
"	padding-left: 10px;\n"
"	color:#c8c8c8;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 3px solid rgb(91, 101, 124);\n"
"}")
        self.lineEdit_login.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_16.addWidget(self.lineEdit_login)

        self.checkBox_login = QCheckBox(self.horizontalFrame_login)
        self.checkBox_login.setObjectName(u"checkBox_login")
        self.checkBox_login.setMinimumSize(QSize(100, 0))
        self.checkBox_login.setMaximumSize(QSize(100, 16777215))
        self.checkBox_login.setFont(font9)

        self.horizontalLayout_16.addWidget(self.checkBox_login)


        self.verticalLayout_login.addWidget(self.horizontalFrame_login)

        self.label_login_space2 = QLabel(self.page_login)
        self.label_login_space2.setObjectName(u"label_login_space2")
        self.label_login_space2.setMinimumSize(QSize(0, 50))
        self.label_login_space2.setMaximumSize(QSize(16777215, 50))

        self.verticalLayout_login.addWidget(self.label_login_space2)

        self.pushButton_login = QPushButton(self.page_login)
        self.pushButton_login.setObjectName(u"pushButton_login")
        self.pushButton_login.setMinimumSize(QSize(300, 40))
        self.pushButton_login.setMaximumSize(QSize(300, 40))
        self.pushButton_login.setFont(font9)
        self.pushButton_login.setStyleSheet(u"")

        self.verticalLayout_login.addWidget(self.pushButton_login)

        self.label_login_space = QLabel(self.page_login)
        self.label_login_space.setObjectName(u"label_login_space")
        self.label_login_space.setMinimumSize(QSize(0, 50))
        self.label_login_space.setMaximumSize(QSize(16777215, 50))
        self.label_login_space.setStyleSheet(u"margin-bottom:60px; color:#c8272f;margin-top:20px")
        self.label_login_space.setAlignment(Qt.AlignCenter)

        self.verticalLayout_login.addWidget(self.label_login_space)

        self.stackedWidget.addWidget(self.page_login)
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        palette11 = QPalette()
        palette11.setBrush(QPalette.Active, QPalette.WindowText, brush17)
        palette11.setBrush(QPalette.Active, QPalette.Button, brush16)
        palette11.setBrush(QPalette.Active, QPalette.Text, brush17)
        palette11.setBrush(QPalette.Active, QPalette.ButtonText, brush17)
        palette11.setBrush(QPalette.Active, QPalette.Base, brush16)
        palette11.setBrush(QPalette.Active, QPalette.Window, brush16)
        brush27 = QBrush(QColor(98, 103, 111, 128))
        brush27.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette11.setBrush(QPalette.Active, QPalette.PlaceholderText, brush27)
#endif
        palette11.setBrush(QPalette.Inactive, QPalette.WindowText, brush17)
        palette11.setBrush(QPalette.Inactive, QPalette.Button, brush16)
        palette11.setBrush(QPalette.Inactive, QPalette.Text, brush17)
        palette11.setBrush(QPalette.Inactive, QPalette.ButtonText, brush17)
        palette11.setBrush(QPalette.Inactive, QPalette.Base, brush16)
        palette11.setBrush(QPalette.Inactive, QPalette.Window, brush16)
        brush28 = QBrush(QColor(98, 103, 111, 128))
        brush28.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette11.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush28)
#endif
        palette11.setBrush(QPalette.Disabled, QPalette.WindowText, brush17)
        palette11.setBrush(QPalette.Disabled, QPalette.Button, brush16)
        palette11.setBrush(QPalette.Disabled, QPalette.Text, brush17)
        palette11.setBrush(QPalette.Disabled, QPalette.ButtonText, brush17)
        palette11.setBrush(QPalette.Disabled, QPalette.Base, brush16)
        palette11.setBrush(QPalette.Disabled, QPalette.Window, brush16)
        brush29 = QBrush(QColor(98, 103, 111, 128))
        brush29.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette11.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush29)
#endif
        self.page_home.setPalette(palette11)
        self.page_home.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.verticalLayout_home = QVBoxLayout(self.page_home)
        self.verticalLayout_home.setObjectName(u"verticalLayout_home")
        self.verticalLayout_home.setContentsMargins(50, -1, -1, -1)
        self.label_home_name = QLabel(self.page_home)
        self.label_home_name.setObjectName(u"label_home_name")
        self.label_home_name.setMinimumSize(QSize(0, 200))
        palette12 = QPalette()
        brush30 = QBrush(QColor(200, 200, 200, 255))
        brush30.setStyle(Qt.SolidPattern)
        palette12.setBrush(QPalette.Active, QPalette.WindowText, brush30)
        palette12.setBrush(QPalette.Active, QPalette.Button, brush16)
        palette12.setBrush(QPalette.Active, QPalette.Text, brush30)
        palette12.setBrush(QPalette.Active, QPalette.ButtonText, brush30)
        palette12.setBrush(QPalette.Active, QPalette.Base, brush16)
        palette12.setBrush(QPalette.Active, QPalette.Window, brush16)
        brush31 = QBrush(QColor(200, 200, 200, 128))
        brush31.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette12.setBrush(QPalette.Active, QPalette.PlaceholderText, brush31)
#endif
        palette12.setBrush(QPalette.Inactive, QPalette.WindowText, brush30)
        palette12.setBrush(QPalette.Inactive, QPalette.Button, brush16)
        palette12.setBrush(QPalette.Inactive, QPalette.Text, brush30)
        palette12.setBrush(QPalette.Inactive, QPalette.ButtonText, brush30)
        palette12.setBrush(QPalette.Inactive, QPalette.Base, brush16)
        palette12.setBrush(QPalette.Inactive, QPalette.Window, brush16)
        brush32 = QBrush(QColor(200, 200, 200, 128))
        brush32.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette12.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush32)
#endif
        palette12.setBrush(QPalette.Disabled, QPalette.WindowText, brush30)
        palette12.setBrush(QPalette.Disabled, QPalette.Button, brush16)
        palette12.setBrush(QPalette.Disabled, QPalette.Text, brush30)
        palette12.setBrush(QPalette.Disabled, QPalette.ButtonText, brush30)
        palette12.setBrush(QPalette.Disabled, QPalette.Base, brush16)
        palette12.setBrush(QPalette.Disabled, QPalette.Window, brush16)
        brush33 = QBrush(QColor(200, 200, 200, 128))
        brush33.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette12.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush33)
#endif
        self.label_home_name.setPalette(palette12)
        font13 = QFont()
        font13.setFamily(u"Segoe UI")
        font13.setPointSize(40)
        font13.setBold(True)
        font13.setItalic(False)
        font13.setUnderline(False)
        font13.setWeight(75)
        font13.setKerning(True)
        self.label_home_name.setFont(font13)
        self.label_home_name.setStyleSheet(u"color:#c8c8c8")

        self.verticalLayout_home.addWidget(self.label_home_name)

        self.label_home_intro = QLabel(self.page_home)
        self.label_home_intro.setObjectName(u"label_home_intro")
        self.label_home_intro.setMinimumSize(QSize(0, 160))
        font14 = QFont()
        font14.setFamily(u"Segoe UI")
        font14.setPointSize(23)
        font14.setBold(True)
        font14.setWeight(75)
        self.label_home_intro.setFont(font14)
        self.label_home_intro.setStyleSheet(u"color:#c8c8c8")

        self.verticalLayout_home.addWidget(self.label_home_intro)

        self.label_home_space = QLabel(self.page_home)
        self.label_home_space.setObjectName(u"label_home_space")
        self.label_home_space.setMinimumSize(QSize(0, 170))
        self.label_home_space.setMaximumSize(QSize(16777215, 170))

        self.verticalLayout_home.addWidget(self.label_home_space)

        self.pushButton_home_button = QPushButton(self.page_home)
        self.pushButton_home_button.setObjectName(u"pushButton_home_button")
        self.pushButton_home_button.setMinimumSize(QSize(400, 50))
        self.pushButton_home_button.setMaximumSize(QSize(400, 50))
        self.pushButton_home_button.setFont(font9)
        self.pushButton_home_button.setStyleSheet(u"color:#c8c8c8;")

        self.verticalLayout_home.addWidget(self.pushButton_home_button)

        self.label_home_space2 = QLabel(self.page_home)
        self.label_home_space2.setObjectName(u"label_home_space2")
        self.label_home_space2.setMinimumSize(QSize(0, 50))
        self.label_home_space2.setMaximumSize(QSize(16777215, 50))

        self.verticalLayout_home.addWidget(self.label_home_space2)

        self.stackedWidget.addWidget(self.page_home)
        self.page_add = QWidget()
        self.page_add.setObjectName(u"page_add")
        font15 = QFont()
        font15.setKerning(True)
        self.page_add.setFont(font15)
        self.page_add.setFocusPolicy(Qt.NoFocus)
        self.page_add.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.page_add.setAutoFillBackground(False)
        self.page_add.setStyleSheet(u"/* COMBOBOX */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/16x16/icons/16x16/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(85, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}")
        self.verticalLayout_7 = QVBoxLayout(self.page_add)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.stackedWidget_add = QStackedWidget(self.page_add)
        self.stackedWidget_add.setObjectName(u"stackedWidget_add")
        self.page_add_tag = QWidget()
        self.page_add_tag.setObjectName(u"page_add_tag")
        self.verticalLayout_add_tag = QVBoxLayout(self.page_add_tag)
        self.verticalLayout_add_tag.setSpacing(0)
        self.verticalLayout_add_tag.setObjectName(u"verticalLayout_add_tag")
        self.verticalLayout_add_tag.setContentsMargins(0, 0, 0, 0)
        self.label_add_tag = QLabel(self.page_add_tag)
        self.label_add_tag.setObjectName(u"label_add_tag")
        self.label_add_tag.setMinimumSize(QSize(0, 150))
        self.label_add_tag.setMaximumSize(QSize(16777215, 150))
        font16 = QFont()
        font16.setFamily(u"Segoe UI")
        font16.setPointSize(20)
        self.label_add_tag.setFont(font16)
        self.label_add_tag.setStyleSheet(u"color : #c8c8c8")
        self.label_add_tag.setAlignment(Qt.AlignCenter)

        self.verticalLayout_add_tag.addWidget(self.label_add_tag)

        self.comboBox_add_tag = QComboBox(self.page_add_tag)
        self.comboBox_add_tag.addItem("")
        self.comboBox_add_tag.addItem("")
        self.comboBox_add_tag.setObjectName(u"comboBox_add_tag")
        self.comboBox_add_tag.setMinimumSize(QSize(500, 0))
        self.comboBox_add_tag.setMaximumSize(QSize(500, 16777215))
        self.comboBox_add_tag.setFont(font16)
        self.comboBox_add_tag.setStyleSheet(u"color:#c8c8c8")

        self.verticalLayout_add_tag.addWidget(self.comboBox_add_tag)

        self.pushButton_add_tag = QPushButton(self.page_add_tag)
        self.pushButton_add_tag.setObjectName(u"pushButton_add_tag")
        self.pushButton_add_tag.setMinimumSize(QSize(500, 50))
        self.pushButton_add_tag.setMaximumSize(QSize(500, 50))
        self.pushButton_add_tag.setFont(font8)
        self.pushButton_add_tag.setStyleSheet(u"color:#c8c8c8;")

        self.verticalLayout_add_tag.addWidget(self.pushButton_add_tag)

        self.stackedWidget_add.addWidget(self.page_add_tag)
        self.page_add_detail = QWidget()
        self.page_add_detail.setObjectName(u"page_add_detail")
        self.verticalLayout_add_detail = QVBoxLayout(self.page_add_detail)
        self.verticalLayout_add_detail.setObjectName(u"verticalLayout_add_detail")
        self.gridFrame_add_detail = QFrame(self.page_add_detail)
        self.gridFrame_add_detail.setObjectName(u"gridFrame_add_detail")
        self.gridLayout_add_detail = QGridLayout(self.gridFrame_add_detail)
        self.gridLayout_add_detail.setObjectName(u"gridLayout_add_detail")
        self.label_example = QLabel(self.gridFrame_add_detail)
        self.label_example.setObjectName(u"label_example")

        self.gridLayout_add_detail.addWidget(self.label_example, 0, 0, 1, 1)

        self.lineEdit_add_detail = QLineEdit(self.gridFrame_add_detail)
        self.lineEdit_add_detail.setObjectName(u"lineEdit_add_detail")

        self.gridLayout_add_detail.addWidget(self.lineEdit_add_detail, 0, 1, 1, 1)


        self.verticalLayout_add_detail.addWidget(self.gridFrame_add_detail)

        self.pushButton_btn_add = QPushButton(self.page_add_detail)
        self.pushButton_btn_add.setObjectName(u"pushButton_btn_add")
        self.pushButton_btn_add.setMinimumSize(QSize(150, 35))
        self.pushButton_btn_add.setMaximumSize(QSize(150, 35))
        font17 = QFont()
        font17.setFamily(u"Segoe UI")
        font17.setPointSize(13)
        font17.setBold(False)
        font17.setWeight(50)
        self.pushButton_btn_add.setFont(font17)
        self.pushButton_btn_add.setStyleSheet(u"color:#c8c8c8;")

        self.verticalLayout_add_detail.addWidget(self.pushButton_btn_add)

        self.pushButton_add_detail = QPushButton(self.page_add_detail)
        self.pushButton_add_detail.setObjectName(u"pushButton_add_detail")
        self.pushButton_add_detail.setMinimumSize(QSize(500, 50))
        self.pushButton_add_detail.setMaximumSize(QSize(500, 50))
        self.pushButton_add_detail.setFont(font8)
        self.pushButton_add_detail.setStyleSheet(u"color:#c8c8c8;")

        self.verticalLayout_add_detail.addWidget(self.pushButton_add_detail)

        self.stackedWidget_add.addWidget(self.page_add_detail)

        self.verticalLayout_7.addWidget(self.stackedWidget_add)

        self.stackedWidget.addWidget(self.page_add)
        self.page_retrieve = QWidget()
        self.page_retrieve.setObjectName(u"page_retrieve")
        palette13 = QPalette()
        palette13.setBrush(QPalette.Active, QPalette.WindowText, brush30)
        palette13.setBrush(QPalette.Active, QPalette.Button, brush16)
        palette13.setBrush(QPalette.Active, QPalette.Text, brush30)
        palette13.setBrush(QPalette.Active, QPalette.ButtonText, brush30)
        palette13.setBrush(QPalette.Active, QPalette.Base, brush16)
        palette13.setBrush(QPalette.Active, QPalette.Window, brush16)
        brush34 = QBrush(QColor(200, 200, 200, 128))
        brush34.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette13.setBrush(QPalette.Active, QPalette.PlaceholderText, brush34)
#endif
        palette13.setBrush(QPalette.Inactive, QPalette.WindowText, brush30)
        palette13.setBrush(QPalette.Inactive, QPalette.Button, brush16)
        palette13.setBrush(QPalette.Inactive, QPalette.Text, brush30)
        palette13.setBrush(QPalette.Inactive, QPalette.ButtonText, brush30)
        palette13.setBrush(QPalette.Inactive, QPalette.Base, brush16)
        palette13.setBrush(QPalette.Inactive, QPalette.Window, brush16)
        brush35 = QBrush(QColor(200, 200, 200, 128))
        brush35.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette13.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush35)
#endif
        palette13.setBrush(QPalette.Disabled, QPalette.WindowText, brush30)
        palette13.setBrush(QPalette.Disabled, QPalette.Button, brush16)
        palette13.setBrush(QPalette.Disabled, QPalette.Text, brush30)
        palette13.setBrush(QPalette.Disabled, QPalette.ButtonText, brush30)
        palette13.setBrush(QPalette.Disabled, QPalette.Base, brush16)
        palette13.setBrush(QPalette.Disabled, QPalette.Window, brush16)
        brush36 = QBrush(QColor(200, 200, 200, 128))
        brush36.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette13.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush36)
#endif
        self.page_retrieve.setPalette(palette13)
        self.page_retrieve.setStyleSheet(u"color:#c8c8c8;")
        self.horizontalLayout_8 = QHBoxLayout(self.page_retrieve)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.frame_list = QFrame(self.page_retrieve)
        self.frame_list.setObjectName(u"frame_list")
        self.frame_list.setMaximumSize(QSize(400, 16777215))
        self.verticalLayout_scrollContents = QVBoxLayout(self.frame_list)
        self.verticalLayout_scrollContents.setSpacing(0)
        self.verticalLayout_scrollContents.setObjectName(u"verticalLayout_scrollContents")
        self.verticalLayout_scrollContents.setContentsMargins(0, 0, 0, 0)
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
        self.lineEdit_search.setFont(font4)
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

        self.comboBox_search = QComboBox(self.frame_search)
        self.comboBox_search.addItem("")
        self.comboBox_search.setObjectName(u"comboBox_search")
        self.comboBox_search.setMinimumSize(QSize(120, 35))
        self.comboBox_search.setMaximumSize(QSize(120, 35))
        font18 = QFont()
        font18.setFamily(u"Segoe UI")
        font18.setPointSize(10)
        self.comboBox_search.setFont(font18)
        self.comboBox_search.setStyleSheet(u"/* COMBOBOX */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/16x16/icons/16x16/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(85, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}")

        self.horizontalLayout_12.addWidget(self.comboBox_search)

        self.pushButton_search = QPushButton(self.frame_search)
        self.pushButton_search.setObjectName(u"pushButton_search")
        self.pushButton_search.setMinimumSize(QSize(70, 35))
        self.pushButton_search.setMaximumSize(QSize(70, 35))
        self.pushButton_search.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/16x16/cil-magnifying-glass.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_search.setIcon(icon3)

        self.horizontalLayout_12.addWidget(self.pushButton_search)


        self.verticalLayout_scrollContents.addWidget(self.frame_search)

        self.scrollArea = QScrollArea(self.frame_list)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMinimumSize(QSize(400, 0))
        self.scrollArea.setMaximumSize(QSize(400, 16777215))
        self.scrollArea.setStyleSheet(u"QScrollArea {\n"
"	border-radius : 7px;\n"
"	border: 3px solid rgb(34, 36, 43);\n"
"    margin-top : 5px\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 384, 537))
        self.verticalLayout_search = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_search.setSpacing(10)
        self.verticalLayout_search.setObjectName(u"verticalLayout_search")
        self.verticalLayout_search.setContentsMargins(9, 0, 0, 0)
        self.pushButton_example1 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_example1.setObjectName(u"pushButton_example1")
        self.pushButton_example1.setMinimumSize(QSize(375, 80))
        self.pushButton_example1.setMaximumSize(QSize(475, 80))
        font19 = QFont()
        font19.setFamily(u"Segoe UI")
        font19.setPointSize(15)
        font19.setBold(True)
        font19.setWeight(75)
        self.pushButton_example1.setFont(font19)
        self.pushButton_example1.setStyleSheet(u"QPushButton{\n"
"background-color : #32363e;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border: 2px solid #41454d;\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49); /* pressed button border = \ubc30\uacbd r+8 g+10 b+12 */\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"")

        self.verticalLayout_search.addWidget(self.pushButton_example1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_scrollContents.addWidget(self.scrollArea)


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
        self.label_guide.setMinimumSize(QSize(0, 0))
        self.label_guide.setMaximumSize(QSize(16777215, 16777215))
        font20 = QFont()
        font20.setFamily(u"Segoe UI")
        font20.setPointSize(20)
        font20.setBold(False)
        font20.setWeight(50)
        self.label_guide.setFont(font20)
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
        self.label_retrieve_tag = QLabel(self.frame_name_delete)
        self.label_retrieve_tag.setObjectName(u"label_retrieve_tag")
        font21 = QFont()
        font21.setFamily(u"Segoe UI")
        font21.setPointSize(12)
        font21.setBold(True)
        font21.setWeight(75)
        self.label_retrieve_tag.setFont(font21)
        self.label_retrieve_tag.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.e.addWidget(self.label_retrieve_tag)

        self.label_service_name = QLabel(self.frame_name_delete)
        self.label_service_name.setObjectName(u"label_service_name")
        font22 = QFont()
        font22.setFamily(u"Segoe UI")
        font22.setPointSize(20)
        font22.setBold(True)
        font22.setWeight(75)
        self.label_service_name.setFont(font22)
        self.label_service_name.setStyleSheet(u"margin-right:100")
        self.label_service_name.setAlignment(Qt.AlignCenter)
        self.label_service_name.setIndent(-1)

        self.e.addWidget(self.label_service_name)

        self.pushButton_delete = QPushButton(self.frame_name_delete)
        self.pushButton_delete.setObjectName(u"pushButton_delete")
        self.pushButton_delete.setMaximumSize(QSize(80, 16777215))
        self.pushButton_delete.setFont(font1)
        self.pushButton_delete.setStyleSheet(u"color:#c8272f;")

        self.e.addWidget(self.pushButton_delete)


        self.verticalLayout_10.addWidget(self.frame_name_delete)

        self.frame_retrieve = QFrame(self.page_specific)
        self.frame_retrieve.setObjectName(u"frame_retrieve")
        self.frame_retrieve.setMinimumSize(QSize(0, 200))
        self.frame_retrieve.setMaximumSize(QSize(16777215, 200))
        self.frame_retrieve.setStyleSheet(u"QFrame {\n"
"    border-radius : 7px;\n"
"	border: 3px solid rgb(36, 38, 45);\n"
"}")
        self.gridLayout_retrieve = QGridLayout(self.frame_retrieve)
        self.gridLayout_retrieve.setObjectName(u"gridLayout_retrieve")
        self.pushButton_clipboard_password = QPushButton(self.frame_retrieve)
        self.pushButton_clipboard_password.setObjectName(u"pushButton_clipboard_password")
        self.pushButton_clipboard_password.setMinimumSize(QSize(0, 50))
        self.pushButton_clipboard_password.setMaximumSize(QSize(100, 16777215))
        font23 = QFont()
        font23.setFamily(u"Segoe UI")
        font23.setPointSize(11)
        font23.setBold(True)
        font23.setWeight(75)
        self.pushButton_clipboard_password.setFont(font23)

        self.gridLayout_retrieve.addWidget(self.pushButton_clipboard_password, 5, 3, 1, 1)

        self.pushButton_clipboard_id = QPushButton(self.frame_retrieve)
        self.pushButton_clipboard_id.setObjectName(u"pushButton_clipboard_id")
        self.pushButton_clipboard_id.setMinimumSize(QSize(0, 50))
        self.pushButton_clipboard_id.setMaximumSize(QSize(100, 16777215))
        font24 = QFont()
        font24.setFamily(u"Segoe UI")
        font24.setBold(True)
        font24.setWeight(75)
        self.pushButton_clipboard_id.setFont(font24)

        self.gridLayout_retrieve.addWidget(self.pushButton_clipboard_id, 1, 3, 1, 1)

        self.label_password_2 = QLabel(self.frame_retrieve)
        self.label_password_2.setObjectName(u"label_password_2")
        self.label_password_2.setFont(font21)
        self.label_password_2.setStyleSheet(u"border-radius : 0;")
        self.label_password_2.setMargin(0)

        self.gridLayout_retrieve.addWidget(self.label_password_2, 5, 1, 1, 1)

        self.label_password = QLabel(self.frame_retrieve)
        self.label_password.setObjectName(u"label_password")
        self.label_password.setMinimumSize(QSize(80, 0))
        self.label_password.setMaximumSize(QSize(80, 16777215))
        self.label_password.setFont(font21)
        self.label_password.setStyleSheet(u"border:None;")
        self.label_password.setAlignment(Qt.AlignCenter)

        self.gridLayout_retrieve.addWidget(self.label_password, 5, 0, 1, 1)

        self.checkBox_retrieve_show = QCheckBox(self.frame_retrieve)
        self.checkBox_retrieve_show.setObjectName(u"checkBox_retrieve_show")
        self.checkBox_retrieve_show.setMaximumSize(QSize(70, 30))

        self.gridLayout_retrieve.addWidget(self.checkBox_retrieve_show, 5, 2, 1, 1)

        self.label_id = QLabel(self.frame_retrieve)
        self.label_id.setObjectName(u"label_id")
        self.label_id.setMinimumSize(QSize(80, 0))
        self.label_id.setMaximumSize(QSize(80, 16777215))
        self.label_id.setFont(font21)
        self.label_id.setStyleSheet(u"border:None;")
        self.label_id.setAlignment(Qt.AlignCenter)

        self.gridLayout_retrieve.addWidget(self.label_id, 1, 0, 1, 1)

        self.label_id_2 = QLabel(self.frame_retrieve)
        self.label_id_2.setObjectName(u"label_id_2")
        self.label_id_2.setFont(font21)
        self.label_id_2.setStyleSheet(u"border-radius : 0;")
        self.label_id_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_retrieve.addWidget(self.label_id_2, 1, 1, 1, 1)


        self.verticalLayout_10.addWidget(self.frame_retrieve)

        self.horizontalFrame_retrieve = QFrame(self.page_specific)
        self.horizontalFrame_retrieve.setObjectName(u"horizontalFrame_retrieve")
        self.horizontalFrame_retrieve.setMinimumSize(QSize(0, 40))
        self.horizontalFrame_retrieve.setMaximumSize(QSize(16777215, 40))
        self.horizontalLayout_retrieve = QHBoxLayout(self.horizontalFrame_retrieve)
        self.horizontalLayout_retrieve.setSpacing(0)
        self.horizontalLayout_retrieve.setObjectName(u"horizontalLayout_retrieve")
        self.horizontalLayout_retrieve.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_10.addWidget(self.horizontalFrame_retrieve)

        self.label_retrieve_space = QLabel(self.page_specific)
        self.label_retrieve_space.setObjectName(u"label_retrieve_space")

        self.verticalLayout_10.addWidget(self.label_retrieve_space)

        self.stackedWidget_2.addWidget(self.page_specific)

        self.horizontalLayout_8.addWidget(self.stackedWidget_2)

        self.stackedWidget.addWidget(self.page_retrieve)
        self.page_setting = QWidget()
        self.page_setting.setObjectName(u"page_setting")
        self.page_setting.setStyleSheet(u"QPushButton{\n"
"background-color : #32363e;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border: 2px solid #41454d;\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49); /* pressed button border = \ubc30\uacbd r+8 g+10 b+12 */\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"")
        self.verticalLayout_8 = QVBoxLayout(self.page_setting)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_assign = QLabel(self.page_setting)
        self.label_assign.setObjectName(u"label_assign")
        self.label_assign.setMinimumSize(QSize(0, 40))
        self.label_assign.setMaximumSize(QSize(16777215, 40))
        self.label_assign.setFont(font19)
        self.label_assign.setStyleSheet(u"background-color:#272c36;\n"
"color:#c8c8c8;")
        self.label_assign.setMargin(9)

        self.verticalLayout_8.addWidget(self.label_assign)

        self.frame_assign = QFrame(self.page_setting)
        self.frame_assign.setObjectName(u"frame_assign")
        self.frame_assign.setMinimumSize(QSize(0, 150))
        self.frame_assign.setMaximumSize(QSize(16777215, 150))
        self.gridLayout_assign = QGridLayout(self.frame_assign)
        self.gridLayout_assign.setObjectName(u"gridLayout_assign")
        self.gridLayout_assign.setContentsMargins(3, 3, 3, 3)
        self.pushButton_open_folder = QPushButton(self.frame_assign)
        self.pushButton_open_folder.setObjectName(u"pushButton_open_folder")
        self.pushButton_open_folder.setMaximumSize(QSize(150, 30))
        self.pushButton_open_folder.setFont(font18)
        self.pushButton_open_folder.setFocusPolicy(Qt.StrongFocus)
        self.pushButton_open_folder.setStyleSheet(u"color:#c8c8c8;")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/16x16/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_open_folder.setIcon(icon4)

        self.gridLayout_assign.addWidget(self.pushButton_open_folder, 3, 0, 1, 1)

        self.pushButton_restore = QPushButton(self.frame_assign)
        self.pushButton_restore.setObjectName(u"pushButton_restore")
        self.pushButton_restore.setMaximumSize(QSize(150, 30))
        self.pushButton_restore.setFont(font18)
        self.pushButton_restore.setStyleSheet(u"color:#c8c8c8;")

        self.gridLayout_assign.addWidget(self.pushButton_restore, 3, 1, 1, 1)

        self.label_current = QLabel(self.frame_assign)
        self.label_current.setObjectName(u"label_current")
        font25 = QFont()
        font25.setFamily(u"Segoe UI")
        font25.setPointSize(13)
        self.label_current.setFont(font25)
        self.label_current.setStyleSheet(u"color:#62676f;")

        self.gridLayout_assign.addWidget(self.label_current, 1, 0, 1, 1)


        self.verticalLayout_8.addWidget(self.frame_assign)

        self.gridFrame_chkey = QFrame(self.page_setting)
        self.gridFrame_chkey.setObjectName(u"gridFrame_chkey")
        self.gridFrame_chkey.setFont(font8)
        self.gridFrame_chkey.setLayoutDirection(Qt.LeftToRight)
        self.gridLayout_password = QGridLayout(self.gridFrame_chkey)
        self.gridLayout_password.setObjectName(u"gridLayout_password")
        self.gridLayout_password.setHorizontalSpacing(3)
        self.gridLayout_password.setVerticalSpacing(6)
        self.gridLayout_password.setContentsMargins(3, 3, 3, 3)
        self.label_chkey_error = QLabel(self.gridFrame_chkey)
        self.label_chkey_error.setObjectName(u"label_chkey_error")

        self.gridLayout_password.addWidget(self.label_chkey_error, 4, 0, 1, 1)

        self.lineEdit_chkey_old = QLineEdit(self.gridFrame_chkey)
        self.lineEdit_chkey_old.setObjectName(u"lineEdit_chkey_old")
        self.lineEdit_chkey_old.setMinimumSize(QSize(0, 40))
        font26 = QFont()
        self.lineEdit_chkey_old.setFont(font26)
        self.lineEdit_chkey_old.setStyleSheet(u"\n"
"\n"
"QLineEdit {\n"
"	margin-left:20px;\n"
"	margin-right:20px;\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 3px;\n"
"	border: 2px solid rgb(34, 36, 43);\n"
"	padding-left: 10px;\n"
"	font-size : 15px;\n"
"	color:#c8c8c8;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")

        self.gridLayout_password.addWidget(self.lineEdit_chkey_old, 2, 1, 1, 1)

        self.label_chkey_old = QLabel(self.gridFrame_chkey)
        self.label_chkey_old.setObjectName(u"label_chkey_old")
        self.label_chkey_old.setFont(font9)
        self.label_chkey_old.setStyleSheet(u"color : #c8c8c8;")

        self.gridLayout_password.addWidget(self.label_chkey_old, 2, 0, 1, 1)

        self.checkBox_chkey1 = QCheckBox(self.gridFrame_chkey)
        self.checkBox_chkey1.setObjectName(u"checkBox_chkey1")
        self.checkBox_chkey1.setFont(font9)
        self.checkBox_chkey1.setStyleSheet(u"color:#c8c8c8;")

        self.gridLayout_password.addWidget(self.checkBox_chkey1, 2, 2, 1, 1)

        self.label_chkey_new = QLabel(self.gridFrame_chkey)
        self.label_chkey_new.setObjectName(u"label_chkey_new")
        self.label_chkey_new.setFont(font10)
        self.label_chkey_new.setStyleSheet(u"color : #c8c8c8;")

        self.gridLayout_password.addWidget(self.label_chkey_new, 3, 0, 1, 1)

        self.checkBox_chkey2 = QCheckBox(self.gridFrame_chkey)
        self.checkBox_chkey2.setObjectName(u"checkBox_chkey2")
        self.checkBox_chkey2.setFont(font9)
        self.checkBox_chkey2.setStyleSheet(u"color:#c8c8c8; margin-right:20")

        self.gridLayout_password.addWidget(self.checkBox_chkey2, 3, 2, 1, 1)

        self.lineEdit_chkey_new = QLineEdit(self.gridFrame_chkey)
        self.lineEdit_chkey_new.setObjectName(u"lineEdit_chkey_new")
        self.lineEdit_chkey_new.setMinimumSize(QSize(0, 40))
        self.lineEdit_chkey_new.setFont(font26)
        self.lineEdit_chkey_new.setStyleSheet(u"QLineEdit {\n"
"	margin-left:20px;\n"
"	margin-right:20px;\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 3px;\n"
"	border: 2px solid rgb(34, 36, 43);\n"
"	padding-left: 10px;\n"
"	font-size : 15px;\n"
"	color:#c8c8c8;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")

        self.gridLayout_password.addWidget(self.lineEdit_chkey_new, 3, 1, 1, 1)

        self.pushButton_chkey = QPushButton(self.gridFrame_chkey)
        self.pushButton_chkey.setObjectName(u"pushButton_chkey")
        self.pushButton_chkey.setMinimumSize(QSize(300, 40))
        self.pushButton_chkey.setMaximumSize(QSize(300, 40))
        self.pushButton_chkey.setFont(font9)
        self.pushButton_chkey.setStyleSheet(u"color:#c8c8c8;")

        self.gridLayout_password.addWidget(self.pushButton_chkey, 4, 1, 1, 1)

        self.label_chkey = QLabel(self.gridFrame_chkey)
        self.label_chkey.setObjectName(u"label_chkey")
        self.label_chkey.setMinimumSize(QSize(0, 40))
        self.label_chkey.setMaximumSize(QSize(16777215, 40))
        self.label_chkey.setFont(font19)
        self.label_chkey.setStyleSheet(u"background-color:#272c36;\n"
"color:#c8c8c8;")
        self.label_chkey.setMargin(9)

        self.gridLayout_password.addWidget(self.label_chkey, 1, 0, 1, 4)


        self.verticalLayout_8.addWidget(self.gridFrame_chkey)

        self.gridFrame = QFrame(self.page_setting)
        self.gridFrame.setObjectName(u"gridFrame")
        self.gridLayout_4 = QGridLayout(self.gridFrame)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setHorizontalSpacing(6)
        self.gridLayout_4.setContentsMargins(3, 3, 3, 3)
        self.label_setting_update = QLabel(self.gridFrame)
        self.label_setting_update.setObjectName(u"label_setting_update")
        self.label_setting_update.setMinimumSize(QSize(0, 180))
        self.label_setting_update.setMaximumSize(QSize(16777215, 180))
        self.label_setting_update.setFont(font16)
        self.label_setting_update.setStyleSheet(u"color:#c8c8c8;")
        self.label_setting_update.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_setting_update, 0, 0, 1, 1)


        self.verticalLayout_8.addWidget(self.gridFrame)

        self.stackedWidget.addWidget(self.page_setting)
        self.page_tag_management = QWidget()
        self.page_tag_management.setObjectName(u"page_tag_management")
        self.page_tag_management.setStyleSheet(u"QPushButton{\n"
"background-color : #32363e;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border: 2px solid #41454d;\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49); /* pressed button border = \ubc30\uacbd r+8 g+10 b+12 */\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"")
        self.verticalLayout_12 = QVBoxLayout(self.page_tag_management)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.horizontalFrame_tag = QFrame(self.page_tag_management)
        self.horizontalFrame_tag.setObjectName(u"horizontalFrame_tag")
        self.horizontalFrame_tag.setFont(font4)
        self.horizontalFrame_tag.setStyleSheet(u"color:#c8c8c8;\n"
"")
        self.horizontalLayout_11 = QHBoxLayout(self.horizontalFrame_tag)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.verticalFrame_tag = QFrame(self.horizontalFrame_tag)
        self.verticalFrame_tag.setObjectName(u"verticalFrame_tag")
        self.verticalFrame_tag.setMinimumSize(QSize(550, 0))
        self.verticalFrame_tag.setMaximumSize(QSize(550, 16777215))
        self.verticalLayout_16 = QVBoxLayout(self.verticalFrame_tag)
        self.verticalLayout_16.setSpacing(6)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(3, 3, 3, 3)
        self.label_tag = QLabel(self.verticalFrame_tag)
        self.label_tag.setObjectName(u"label_tag")
        self.label_tag.setMaximumSize(QSize(16777215, 50))
        self.label_tag.setFont(font7)
        self.label_tag.setStyleSheet(u"background-color:#272c36;\n"
"color:#c8c8c8;")
        self.label_tag.setAlignment(Qt.AlignCenter)
        self.label_tag.setMargin(9)

        self.verticalLayout_16.addWidget(self.label_tag)

        self.horizontalFrame_tag_2 = QFrame(self.verticalFrame_tag)
        self.horizontalFrame_tag_2.setObjectName(u"horizontalFrame_tag_2")
        self.horizontalFrame_tag_2.setMinimumSize(QSize(0, 100))
        self.horizontalFrame_tag_2.setMaximumSize(QSize(16777215, 100))
        self.horizontalLayout_14 = QHBoxLayout(self.horizontalFrame_tag_2)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_tag_name = QLabel(self.horizontalFrame_tag_2)
        self.label_tag_name.setObjectName(u"label_tag_name")
        self.label_tag_name.setFont(font9)

        self.horizontalLayout_14.addWidget(self.label_tag_name)

        self.lineEdit_tag_name = QLineEdit(self.horizontalFrame_tag_2)
        self.lineEdit_tag_name.setObjectName(u"lineEdit_tag_name")
        self.lineEdit_tag_name.setMinimumSize(QSize(0, 40))
        self.lineEdit_tag_name.setMaximumSize(QSize(16777215, 40))
        self.lineEdit_tag_name.setFont(font4)
        self.lineEdit_tag_name.setStyleSheet(u"\n"
"\n"
"QLineEdit {\n"
"	margin-left:20px;\n"
"	margin-right:20px;\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 3px;\n"
"	border: 2px solid rgb(34, 36, 43);\n"
"	padding-left: 10px;\n"
"	font-size : 15px;\n"
"	color:#c8c8c8;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")

        self.horizontalLayout_14.addWidget(self.lineEdit_tag_name)


        self.verticalLayout_16.addWidget(self.horizontalFrame_tag_2)

        self.gridFrame_slot = QFrame(self.verticalFrame_tag)
        self.gridFrame_slot.setObjectName(u"gridFrame_slot")
        self.gridLayout_slot = QGridLayout(self.gridFrame_slot)
        self.gridLayout_slot.setObjectName(u"gridLayout_slot")
        self.gridLayout_slot.setContentsMargins(3, 3, 3, 3)
        self.checkBox_slot = QCheckBox(self.gridFrame_slot)
        self.checkBox_slot.setObjectName(u"checkBox_slot")
        self.checkBox_slot.setMinimumSize(QSize(100, 40))
        self.checkBox_slot.setMaximumSize(QSize(100, 40))
        self.checkBox_slot.setFont(font9)

        self.gridLayout_slot.addWidget(self.checkBox_slot, 1, 2, 1, 1)

        self.lineEdit_slot = QLineEdit(self.gridFrame_slot)
        self.lineEdit_slot.setObjectName(u"lineEdit_slot")
        self.lineEdit_slot.setMinimumSize(QSize(0, 40))
        self.lineEdit_slot.setMaximumSize(QSize(16777215, 40))
        self.lineEdit_slot.setFont(font4)
        self.lineEdit_slot.setStyleSheet(u"\n"
"\n"
"QLineEdit {\n"
"	margin-left:20px;\n"
"	margin-right:20px;\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 3px;\n"
"	border: 2px solid rgb(34, 36, 43);\n"
"	padding-left: 10px;\n"
"	font-size : 15px;\n"
"	color:#c8c8c8;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")

        self.gridLayout_slot.addWidget(self.lineEdit_slot, 1, 0, 1, 1)

        self.pushButton_slot = QPushButton(self.gridFrame_slot)
        self.pushButton_slot.setObjectName(u"pushButton_slot")
        self.pushButton_slot.setMinimumSize(QSize(100, 40))
        self.pushButton_slot.setMaximumSize(QSize(100, 40))
        self.pushButton_slot.setFont(font9)
        self.pushButton_slot.setStyleSheet(u"")

        self.gridLayout_slot.addWidget(self.pushButton_slot, 1, 3, 1, 1)


        self.verticalLayout_16.addWidget(self.gridFrame_slot)

        self.pushButton_tag_add = QPushButton(self.verticalFrame_tag)
        self.pushButton_tag_add.setObjectName(u"pushButton_tag_add")
        self.pushButton_tag_add.setMinimumSize(QSize(120, 50))
        self.pushButton_tag_add.setMaximumSize(QSize(120, 50))
        self.pushButton_tag_add.setFont(font8)
        self.pushButton_tag_add.setStyleSheet(u"margin-bottom:20px;")

        self.verticalLayout_16.addWidget(self.pushButton_tag_add)

        self.pushButton_create_tag = QPushButton(self.verticalFrame_tag)
        self.pushButton_create_tag.setObjectName(u"pushButton_create_tag")
        self.pushButton_create_tag.setMinimumSize(QSize(0, 50))
        self.pushButton_create_tag.setMaximumSize(QSize(600, 50))
        self.pushButton_create_tag.setFont(font9)
        self.pushButton_create_tag.setStyleSheet(u"")

        self.verticalLayout_16.addWidget(self.pushButton_create_tag)


        self.horizontalLayout_11.addWidget(self.verticalFrame_tag)

        self.verticalFrame_tag_scroll = QFrame(self.horizontalFrame_tag)
        self.verticalFrame_tag_scroll.setObjectName(u"verticalFrame_tag_scroll")
        self.verticalLayout_tags = QVBoxLayout(self.verticalFrame_tag_scroll)
        self.verticalLayout_tags.setObjectName(u"verticalLayout_tags")
        self.scrollArea_tag = QScrollArea(self.verticalFrame_tag_scroll)
        self.scrollArea_tag.setObjectName(u"scrollArea_tag")
        self.scrollArea_tag.setStyleSheet(u"QScrollArea {\n"
"	border-radius : 7px;\n"
"	border: 3px solid rgb(34, 36, 43);\n"
"    margin-top : 5px\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }")
        self.scrollArea_tag.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 310, 551))
        self.verticalLayout_tag = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_tag.setObjectName(u"verticalLayout_tag")
        self.horizontalWidget = QWidget(self.scrollAreaWidgetContents_2)
        self.horizontalWidget.setObjectName(u"horizontalWidget")
        self.horizontalWidget.setMaximumSize(QSize(16777215, 70))
        self.horizontalWidget.setStyleSheet(u"border-radius : 7px;\n"
"border: 3px solid rgb(34, 36, 43);\n"
"")
        self.horizontalLayout_tag_example = QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout_tag_example.setSpacing(0)
        self.horizontalLayout_tag_example.setObjectName(u"horizontalLayout_tag_example")
        self.label_tag_example = QLabel(self.horizontalWidget)
        self.label_tag_example.setObjectName(u"label_tag_example")
        self.label_tag_example.setFont(font9)
        self.label_tag_example.setStyleSheet(u"border:0;")
        self.label_tag_example.setMargin(9)

        self.horizontalLayout_tag_example.addWidget(self.label_tag_example)

        self.pushButton_tag_example = QPushButton(self.horizontalWidget)
        self.pushButton_tag_example.setObjectName(u"pushButton_tag_example")
        self.pushButton_tag_example.setMinimumSize(QSize(100, 40))
        self.pushButton_tag_example.setMaximumSize(QSize(100, 40))
        self.pushButton_tag_example.setFont(font9)
        self.pushButton_tag_example.setStyleSheet(u"border:0;")

        self.horizontalLayout_tag_example.addWidget(self.pushButton_tag_example)


        self.verticalLayout_tag.addWidget(self.horizontalWidget)

        self.scrollArea_tag.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_tags.addWidget(self.scrollArea_tag)


        self.horizontalLayout_11.addWidget(self.verticalFrame_tag_scroll)


        self.verticalLayout_12.addWidget(self.horizontalFrame_tag)

        self.stackedWidget.addWidget(self.page_tag_management)

        self.verticalLayout_4.addWidget(self.stackedWidget)


        self.frame_content.addWidget(self.frame_content_2)

        self.frame_label_bottom = QFrame(self.frame_center_right)
        self.frame_label_bottom.setObjectName(u"frame_label_bottom")
        self.frame_label_bottom.setMinimumSize(QSize(0, 25))
        self.frame_label_bottom.setMaximumSize(QSize(16777215, 25))
        palette14 = QPalette()
        palette14.setBrush(QPalette.Active, QPalette.WindowText, brush17)
        brush37 = QBrush(QColor(33, 37, 43, 255))
        brush37.setStyle(Qt.SolidPattern)
        palette14.setBrush(QPalette.Active, QPalette.Button, brush37)
        palette14.setBrush(QPalette.Active, QPalette.Text, brush17)
        palette14.setBrush(QPalette.Active, QPalette.ButtonText, brush17)
        palette14.setBrush(QPalette.Active, QPalette.Base, brush37)
        palette14.setBrush(QPalette.Active, QPalette.Window, brush37)
        brush38 = QBrush(QColor(98, 103, 111, 128))
        brush38.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette14.setBrush(QPalette.Active, QPalette.PlaceholderText, brush38)
#endif
        palette14.setBrush(QPalette.Inactive, QPalette.WindowText, brush17)
        palette14.setBrush(QPalette.Inactive, QPalette.Button, brush37)
        palette14.setBrush(QPalette.Inactive, QPalette.Text, brush17)
        palette14.setBrush(QPalette.Inactive, QPalette.ButtonText, brush17)
        palette14.setBrush(QPalette.Inactive, QPalette.Base, brush37)
        palette14.setBrush(QPalette.Inactive, QPalette.Window, brush37)
        brush39 = QBrush(QColor(98, 103, 111, 128))
        brush39.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette14.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush39)
#endif
        palette14.setBrush(QPalette.Disabled, QPalette.WindowText, brush17)
        palette14.setBrush(QPalette.Disabled, QPalette.Button, brush37)
        palette14.setBrush(QPalette.Disabled, QPalette.Text, brush17)
        palette14.setBrush(QPalette.Disabled, QPalette.ButtonText, brush17)
        palette14.setBrush(QPalette.Disabled, QPalette.Base, brush37)
        palette14.setBrush(QPalette.Disabled, QPalette.Window, brush37)
        brush40 = QBrush(QColor(98, 103, 111, 128))
        brush40.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette14.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush40)
#endif
        self.frame_label_bottom.setPalette(palette14)
        self.frame_label_bottom.setLayoutDirection(Qt.LeftToRight)
        self.frame_label_bottom.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.horizontalLayout_6 = QHBoxLayout(self.frame_label_bottom)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_developer = QLabel(self.frame_label_bottom)
        self.label_developer.setObjectName(u"label_developer")
        self.label_developer.setMaximumSize(QSize(120000, 16777215))
        palette15 = QPalette()
        palette15.setBrush(QPalette.Active, QPalette.WindowText, brush17)
        palette15.setBrush(QPalette.Active, QPalette.Button, brush37)
        palette15.setBrush(QPalette.Active, QPalette.Text, brush17)
        palette15.setBrush(QPalette.Active, QPalette.ButtonText, brush17)
        palette15.setBrush(QPalette.Active, QPalette.Base, brush37)
        palette15.setBrush(QPalette.Active, QPalette.Window, brush37)
        brush41 = QBrush(QColor(98, 103, 111, 128))
        brush41.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette15.setBrush(QPalette.Active, QPalette.PlaceholderText, brush41)
#endif
        palette15.setBrush(QPalette.Inactive, QPalette.WindowText, brush17)
        palette15.setBrush(QPalette.Inactive, QPalette.Button, brush37)
        palette15.setBrush(QPalette.Inactive, QPalette.Text, brush17)
        palette15.setBrush(QPalette.Inactive, QPalette.ButtonText, brush17)
        palette15.setBrush(QPalette.Inactive, QPalette.Base, brush37)
        palette15.setBrush(QPalette.Inactive, QPalette.Window, brush37)
        brush42 = QBrush(QColor(98, 103, 111, 128))
        brush42.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette15.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush42)
#endif
        palette15.setBrush(QPalette.Disabled, QPalette.WindowText, brush17)
        palette15.setBrush(QPalette.Disabled, QPalette.Button, brush37)
        palette15.setBrush(QPalette.Disabled, QPalette.Text, brush17)
        palette15.setBrush(QPalette.Disabled, QPalette.ButtonText, brush17)
        palette15.setBrush(QPalette.Disabled, QPalette.Base, brush37)
        palette15.setBrush(QPalette.Disabled, QPalette.Window, brush37)
        brush43 = QBrush(QColor(98, 103, 111, 128))
        brush43.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette15.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush43)
#endif
        self.label_developer.setPalette(palette15)
        font27 = QFont()
        font27.setFamily(u"Segoe UI")
        font27.setBold(False)
        font27.setWeight(50)
        self.label_developer.setFont(font27)
        self.label_developer.setStyleSheet(u"")
        self.label_developer.setLineWidth(0)
        self.label_developer.setMidLineWidth(0)
        self.label_developer.setMargin(0)

        self.horizontalLayout_6.addWidget(self.label_developer)

        self.label_version = QLabel(self.frame_label_bottom)
        self.label_version.setObjectName(u"label_version")
        palette16 = QPalette()
        palette16.setBrush(QPalette.Active, QPalette.WindowText, brush17)
        palette16.setBrush(QPalette.Active, QPalette.Button, brush37)
        palette16.setBrush(QPalette.Active, QPalette.Text, brush17)
        palette16.setBrush(QPalette.Active, QPalette.ButtonText, brush17)
        palette16.setBrush(QPalette.Active, QPalette.Base, brush37)
        palette16.setBrush(QPalette.Active, QPalette.Window, brush37)
        brush44 = QBrush(QColor(98, 103, 111, 128))
        brush44.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette16.setBrush(QPalette.Active, QPalette.PlaceholderText, brush44)
#endif
        palette16.setBrush(QPalette.Inactive, QPalette.WindowText, brush17)
        palette16.setBrush(QPalette.Inactive, QPalette.Button, brush37)
        palette16.setBrush(QPalette.Inactive, QPalette.Text, brush17)
        palette16.setBrush(QPalette.Inactive, QPalette.ButtonText, brush17)
        palette16.setBrush(QPalette.Inactive, QPalette.Base, brush37)
        palette16.setBrush(QPalette.Inactive, QPalette.Window, brush37)
        brush45 = QBrush(QColor(98, 103, 111, 128))
        brush45.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette16.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush45)
#endif
        palette16.setBrush(QPalette.Disabled, QPalette.WindowText, brush17)
        palette16.setBrush(QPalette.Disabled, QPalette.Button, brush37)
        palette16.setBrush(QPalette.Disabled, QPalette.Text, brush17)
        palette16.setBrush(QPalette.Disabled, QPalette.ButtonText, brush17)
        palette16.setBrush(QPalette.Disabled, QPalette.Base, brush37)
        palette16.setBrush(QPalette.Disabled, QPalette.Window, brush37)
        brush46 = QBrush(QColor(98, 103, 111, 128))
        brush46.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette16.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush46)
#endif
        self.label_version.setPalette(palette16)
        self.label_version.setFont(font4)
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

        self.stackedWidget.setCurrentIndex(6)
        self.stackedWidget_add.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(0)


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
        self.label_register_welcome.setText(QCoreApplication.translate("MainWindow", u"Welcome to AccountBox!", None))
        self.label_register_explain.setText(QCoreApplication.translate("MainWindow", u"AccountBox encrypts your data with AES256 algorithm.\n"
"The key you create will be used to encrypt and decrypt the data.", None))
        self.label_register_guide.setText(QCoreApplication.translate("MainWindow", u"Create your key", None))
        self.pushButton_register_existing.setText(QCoreApplication.translate("MainWindow", u"I'm not first", None))
        self.lineEdit_register.setText("")
        self.lineEdit_register.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type key", None))
        self.checkBox_register.setText(QCoreApplication.translate("MainWindow", u"Show", None))
        self.label_2.setText("")
        self.pushButton_register.setText(QCoreApplication.translate("MainWindow", u"Register", None))
#if QT_CONFIG(accessibility)
        self.label_register_space.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.label_register_space.setText("")
        self.label_login_1.setText(QCoreApplication.translate("MainWindow", u"Welcome back to AccountBox!", None))
        self.label_login_2.setText(QCoreApplication.translate("MainWindow", u"Key is used to encrypt and decrypt your account data.\n"
"If you type wrong key, your data won't be decrypted correctly.", None))
        self.label_login_3.setText(QCoreApplication.translate("MainWindow", u"Type your key", None))
        self.lineEdit_login.setText("")
        self.lineEdit_login.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type key", None))
        self.checkBox_login.setText(QCoreApplication.translate("MainWindow", u"Show", None))
        self.label_login_space2.setText("")
        self.pushButton_login.setText(QCoreApplication.translate("MainWindow", u"Enter", None))
        self.label_login_space.setText("")
        self.label_home_name.setText(QCoreApplication.translate("MainWindow", u"AccountBox", None))
        self.label_home_intro.setText(QCoreApplication.translate("MainWindow", u"Manage your account data conveniently.\n"
"And retrieve them with no anxiety of exposure", None))
        self.label_home_space.setText("")
        self.pushButton_home_button.setText(QCoreApplication.translate("MainWindow", u"Change Key", None))
        self.label_home_space2.setText("")
        self.label_add_tag.setText(QCoreApplication.translate("MainWindow", u"Select tag", None))
        self.comboBox_add_tag.setItemText(0, QCoreApplication.translate("MainWindow", u"test1", None))
        self.comboBox_add_tag.setItemText(1, QCoreApplication.translate("MainWindow", u"test2", None))

        self.pushButton_add_tag.setText(QCoreApplication.translate("MainWindow", u"Select", None))
        self.label_example.setText(QCoreApplication.translate("MainWindow", u"Service Name", None))
        self.pushButton_btn_add.setText(QCoreApplication.translate("MainWindow", u"Select other tag", None))
        self.pushButton_add_detail.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.lineEdit_search.setText("")
        self.lineEdit_search.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here", None))
        self.comboBox_search.setItemText(0, QCoreApplication.translate("MainWindow", u"wow", None))

#if QT_CONFIG(tooltip)
        self.pushButton_search.setToolTip(QCoreApplication.translate("MainWindow", u"search", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_search.setText("")
        self.pushButton_example1.setText(QCoreApplication.translate("MainWindow", u"Facebook", None))
        self.label_guide.setText(QCoreApplication.translate("MainWindow", u"Search services you want\n"
"and click it to retrieve!", None))
        self.label_retrieve_tag.setText(QCoreApplication.translate("MainWindow", u"#TAG", None))
        self.label_service_name.setText(QCoreApplication.translate("MainWindow", u"Service name", None))
#if QT_CONFIG(tooltip)
        self.pushButton_delete.setToolTip(QCoreApplication.translate("MainWindow", u"delete data of this service", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_delete.setText(QCoreApplication.translate("MainWindow", u"DELETE", None))
        self.pushButton_clipboard_password.setText(QCoreApplication.translate("MainWindow", u"copy to\n"
"clipboard", None))
        self.pushButton_clipboard_id.setText(QCoreApplication.translate("MainWindow", u"copy to\n"
"clipboard", None))
        self.label_password_2.setText(QCoreApplication.translate("MainWindow", u"Set by tag", None))
        self.label_password.setText(QCoreApplication.translate("MainWindow", u"Set by tag", None))
#if QT_CONFIG(tooltip)
        self.checkBox_retrieve_show.setToolTip(QCoreApplication.translate("MainWindow", u"have a look around before click this", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_retrieve_show.setText(QCoreApplication.translate("MainWindow", u"Show", None))
        self.label_id.setText(QCoreApplication.translate("MainWindow", u"Set by tag", None))
        self.label_id_2.setText(QCoreApplication.translate("MainWindow", u"Set by tag", None))
        self.label_retrieve_space.setText("")
        self.label_assign.setText(QCoreApplication.translate("MainWindow", u"ACCOUNT DATA ASSIGNMENT", None))
        self.pushButton_open_folder.setText(QCoreApplication.translate("MainWindow", u"Reassign data", None))
#if QT_CONFIG(tooltip)
        self.pushButton_restore.setToolTip(QCoreApplication.translate("MainWindow", u"Create empty account data at same direction of AccountBox", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_restore.setText(QCoreApplication.translate("MainWindow", u"Restore account data", None))
        self.label_current.setText(QCoreApplication.translate("MainWindow", u"Current : C:\\Users\\bolt6281\\programming\\Python\\SoloProjects\\AccountBox\\account_data.json", None))
        self.label_chkey_error.setText("")
        self.label_chkey_old.setText(QCoreApplication.translate("MainWindow", u"Old key", None))
        self.checkBox_chkey1.setText(QCoreApplication.translate("MainWindow", u"Show", None))
        self.label_chkey_new.setText(QCoreApplication.translate("MainWindow", u"New key", None))
        self.checkBox_chkey2.setText(QCoreApplication.translate("MainWindow", u"Show", None))
        self.lineEdit_chkey_new.setText("")
        self.pushButton_chkey.setText(QCoreApplication.translate("MainWindow", u"Change", None))
        self.label_chkey.setText(QCoreApplication.translate("MainWindow", u"CHANGE KEY", None))
        self.label_setting_update.setText(QCoreApplication.translate("MainWindow", u"Update Later . . .", None))
        self.label_tag.setText(QCoreApplication.translate("MainWindow", u"Create tag", None))
        self.label_tag_name.setText(QCoreApplication.translate("MainWindow", u"Tag name", None))
        self.checkBox_slot.setText(QCoreApplication.translate("MainWindow", u"Invisible", None))
        self.pushButton_slot.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.pushButton_tag_add.setText(QCoreApplication.translate("MainWindow", u"Add Slot", None))
        self.pushButton_create_tag.setText(QCoreApplication.translate("MainWindow", u"Create tag", None))
        self.label_tag_example.setText(QCoreApplication.translate("MainWindow", u"Tag 1", None))
        self.pushButton_tag_example.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
#if QT_CONFIG(tooltip)
        self.label_developer.setToolTip(QCoreApplication.translate("MainWindow", u"who is the most handsome person", None))
#endif // QT_CONFIG(tooltip)
        self.label_developer.setText(QCoreApplication.translate("MainWindow", u" developed by bolt6281", None))
        self.label_version.setText(QCoreApplication.translate("MainWindow", u"v2.0.0", None))
    # retranslateUi

