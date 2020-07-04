class Style():

    style_bt_standard = (
    '''
    QPushButton {
        background-image: ICON_REPLACE;
        background-position: left center;
        background-repeat: no-repeat;
        border: none;
        margin : 0px;
        border-left: 28px solid rgb(27, 29, 35);
        background-color: rgb(27, 29, 35);
        text-align: left;
        padding-left: 45px;
    }
    QPushButton[Active=true] {
        background-image: ICON_REPLACE;
        background-position: left center;
        background-repeat: no-repeat;
        border: none;
        border-left: 28px solid rgb(27, 29, 35);
        border-right: 5px solid rgb(44, 49, 60);
        background-color: rgb(27, 29, 35);
        text-align: left;
        padding-left: 45px;
    }
    QPushButton:hover {
        background-color: rgb(33, 37, 43);
        border-left: 28px solid rgb(33, 37, 43);
    }
    QPushButton:pressed {
        background-color: rgb(85, 170, 255);
        border-left: 28px solid rgb(85, 170, 255);
    }
    '''
    )

    style_bt_retrieve = (
    '''
    QPushButton{
        background-color : #32363e;
        border-radius: 10px;
    }    
    QPushButton:hover {
        border: 2px solid #41454d;
    }
    QPushButton:pressed {
        background-color: rgb(35, 40, 49);
        /* pressed button border = 배경 r+8 g+10 b+12 */
        border: 2px solid rgb(43, 50, 61);
    }
    '''
    )