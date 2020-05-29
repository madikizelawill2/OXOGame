def css():
    # Global styles
    stylesheet = """
    QPushButton {
        background: #000;
        border: none;
        padding: 16px;
        color: #fff;
        font-size: 12px;
    }


    QPushButton:pressed {
        background: #ECECEC;
        padding: 16px;
        color: #000;
        font-size: 12px;
    }
    QToolButton {
        background: #ECECEC;
        padding: 16px;
        outline: none;
        border: none;

    }
    QToolButton:pressed {
        background: #ECECEC;
        padding: 16px;
        outline: none;

    QToolBuuton:checked {
        background: #ECECEC;
        padding: 16px;
        outline: none;
                            
    }
    QTextEdit {
        height: 32px;
        background: #ECECEC; 
        height: 32px ;
        outline: none;
        border: none;
    }
    QLineEdit {
        background: #ECECEC;
        padding: 16px;
        outline: none;
        border: none;
    }
    """
    return stylesheet
