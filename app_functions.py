# made by bolt6281

import os
import json

# load gui
from main import *

# IMPORT FUNCTIONS
from ui_functions import *

# def __init__(self):
    
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


#############################################
# load account data

# check if there is account file
with open(file_loc, "r") as json_file:
    account_data = json.loads(json_file.read())


class Functions(MainWindow):

    def Button_service(self):
        # self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_specific)

        # # GET BT CLICKED
        # btnWidget = self.sender()
        # selected_service = btnWidget.objectName()[4:]

        # self.ui.label_service_name.setText(selected_service)

        # ID = account_data[selected_service]['ID']
        # PASSWORD = account_data[selected_service]['PASSWORD']
        # self.ui.label_id_2.setText(ID)
        # self.ui.label_password_2.setText(PASSWORD)
        pass

    # be used at add_page, edit 
    def save(ID, Password):
        pass
    
    def show_password():
        pass
    
    def OpenFolder(self):
        fname = QFileDialog.getOpenFileName(self)[0]
        self.ui.label_current.setText(fname)

        with open("config.json", "w") as json_file:
            json.dump({"AccountFileLoc": {"LOC": fname}}, json_file)

    def Clipboard():
        pass

    def serach(searched = False):
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
        pass