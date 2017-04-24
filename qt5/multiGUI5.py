# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BardEx.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1000, 310)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../Users/spear/Desktop/candy.PNG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet("QToolTip\n"
"{\n"
"     border: 1px solid black;\n"
"     background-color: #ffa02f;\n"
"     padding: 1px;\n"
"     border-radius: 3px;\n"
"     opacity: 100;\n"
"}\n"
"\n"
"QWidget\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"}\n"
"\n"
"QWidget:item:hover\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #ca0619);\n"
"    color: #000000;\n"
"}\n"
"\n"
"QWidget:item:selected\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QMenuBar::item\n"
"{\n"
"    background: transparent;\n"
"}\n"
"\n"
"QMenuBar::item:selected\n"
"{\n"
"    background: transparent;\n"
"    border: 1px solid #ffaa00;\n"
"}\n"
"\n"
"QMenuBar::item:pressed\n"
"{\n"
"    background: #444;\n"
"    border: 1px solid #000;\n"
"    background-color: QLinearGradient(\n"
"        x1:0, y1:0,\n"
"        x2:0, y2:1,\n"
"        stop:1 #212121,\n"
"        stop:0.4 #343434/*,\n"
"        stop:0.2 #343434,\n"
"        stop:0.1 #ffaa00*/\n"
"    );\n"
"    margin-bottom:-1px;\n"
"    padding-bottom:1px;\n"
"}\n"
"\n"
"QMenu\n"
"{\n"
"    border: 1px solid #000;\n"
"}\n"
"\n"
"QMenu::item\n"
"{\n"
"    padding: 2px 20px 2px 20px;\n"
"}\n"
"\n"
"QMenu::item:selected\n"
"{\n"
"    color: #000000;\n"
"}\n"
"\n"
"QWidget:disabled\n"
"{\n"
"    color: #404040;\n"
"    background-color: #323232;\n"
"}\n"
"\n"
"QAbstractItemView\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4d4d4d, stop: 0.1 #646464, stop: 1 #5d5d5d);\n"
"}\n"
"\n"
"QWidget:focus\n"
"{\n"
"    /*border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);*/\n"
"}\n"
"\n"
"QLineEdit\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4d4d4d, stop: 0 #646464, stop: 1 #5d5d5d);\n"
"    padding: 1px;\n"
"    border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius: 5;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"    border-width: 1px;\n"
"    border-color: #1e1e1e;\n"
"    border-style: solid;\n"
"    border-radius: 6;\n"
"    padding: 3px;\n"
"    font-size: 15px;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
"}\n"
"\n"
"QComboBox\n"
"{\n"
"    selection-background-color: #ffaa00;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"    border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius: 5;\n"
"}\n"
"\n"
"QComboBox:hover,QPushButton:hover\n"
"{\n"
"    border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"\n"
"QComboBox:on\n"
"{\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
"    selection-background-color: #ffaa00;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    border: 2px solid darkgray;\n"
"    selection-background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"     subcontrol-origin: padding;\n"
"     subcontrol-position: top right;\n"
"     width: 15px;\n"
"\n"
"     border-left-width: 0px;\n"
"     border-left-color: darkgray;\n"
"     border-left-style: solid; /* just a single line */\n"
"     border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"     border-bottom-right-radius: 3px;\n"
" }\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"     image: url(:/down_arrow.png);\n"
"}\n"
"\n"
"QGroupBox:focus\n"
"{\n"
"border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QTextEdit:focus\n"
"{\n"
"    border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"     border: 1px solid #222222;\n"
"     background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0.0 #121212, stop: 0.2 #282828, stop: 1 #484848);\n"
"     height: 7px;\n"
"     margin: 0px 16px 0 16px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal\n"
"{\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 0.5 #d7801a, stop: 1 #ffa02f);\n"
"      min-height: 20px;\n"
"      border-radius: 2px;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"      width: 14px;\n"
"      subcontrol-position: right;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"      width: 14px;\n"
"     subcontrol-position: left;\n"
"     subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::right-arrow:horizontal, QScrollBar::left-arrow:horizontal\n"
"{\n"
"      border: 1px solid black;\n"
"      width: 1px;\n"
"      height: 1px;\n"
"      background: white;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"      background: none;\n"
"}\n"
"\n"
"QScrollBar:vertical\n"
"{\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0.0 #121212, stop: 0.2 #282828, stop: 1 #484848);\n"
"      width: 7px;\n"
"      margin: 16px 0 16px 0;\n"
"      border: 1px solid #222222;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical\n"
"{\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 0.5 #d7801a, stop: 1 #ffa02f);\n"
"      min-height: 20px;\n"
"      border-radius: 2px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical\n"
"{\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"      height: 14px;\n"
"      subcontrol-position: bottom;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical\n"
"{\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #d7801a, stop: 1 #ffa02f);\n"
"      height: 14px;\n"
"      subcontrol-position: top;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical\n"
"{\n"
"      border: 1px solid black;\n"
"      width: 1px;\n"
"      height: 1px;\n"
"      background: white;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
"{\n"
"      background: none;\n"
"}\n"
"\n"
"QTextEdit\n"
"{\n"
"    background-color: #242424;\n"
"}\n"
"\n"
"QPlainTextEdit\n"
"{\n"
"    background-color: #242424;\n"
"}\n"
"\n"
"QHeaderView::section\n"
"{\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #616161, stop: 0.5 #505050, stop: 0.6 #434343, stop:1 #656565);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"}\n"
"\n"
"QCheckBox:disabled\n"
"{\n"
"color: #414141;\n"
"}\n"
"\n"
"QDockWidget::title\n"
"{\n"
"    text-align: center;\n"
"    spacing: 3px; /* spacing between items in the tool bar */\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #323232, stop: 0.5 #242424, stop:1 #323232);\n"
"}\n"
"\n"
"QDockWidget::close-button, QDockWidget::float-button\n"
"{\n"
"    text-align: center;\n"
"    spacing: 1px; /* spacing between items in the tool bar */\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #323232, stop: 0.5 #242424, stop:1 #323232);\n"
"}\n"
"\n"
"QDockWidget::close-button:hover, QDockWidget::float-button:hover\n"
"{\n"
"    background: #242424;\n"
"}\n"
"\n"
"QDockWidget::close-button:pressed, QDockWidget::float-button:pressed\n"
"{\n"
"    padding: 1px -1px -1px 1px;\n"
"}\n"
"\n"
"QMainWindow::separator\n"
"{\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #161616, stop: 0.5 #151515, stop: 0.6 #212121, stop:1 #343434);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #4c4c4c;\n"
"    spacing: 3px; /* spacing between items in the tool bar */\n"
"}\n"
"\n"
"QMainWindow::separator:hover\n"
"{\n"
"\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #d7801a, stop:0.5 #b56c17 stop:1 #ffa02f);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"    spacing: 3px; /* spacing between items in the tool bar */\n"
"}\n"
"\n"
"QToolBar::handle\n"
"{\n"
"     spacing: 3px; /* spacing between items in the tool bar */\n"
"     background: url(:/images/handle.png);\n"
"}\n"
"\n"
"QMenu::separator\n"
"{\n"
"    height: 2px;\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #161616, stop: 0.5 #151515, stop: 0.6 #212121, stop:1 #343434);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    margin-left: 10px;\n"
"    margin-right: 5px;\n"
"}\n"
"\n"
"QProgressBar\n"
"{\n"
"    border: 2px solid grey;\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: #d7801a;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    color: #b1b1b1;\n"
"    border: 1px solid #444;\n"
"    border-bottom-style: none;\n"
"    background-color: #323232;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    padding-top: 3px;\n"
"    padding-bottom: 2px;\n"
"    margin-right: -1px;\n"
"}\n"
"\n"
"QTabWidget::pane {\n"
"    border: 1px solid #444;\n"
"    top: 1px;\n"
"}\n"
"\n"
"QTabBar::tab:last\n"
"{\n"
"    margin-right: 0; /* the last selected tab has nothing to overlap with on the right */\n"
"    border-top-right-radius: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:first:!selected\n"
"{\n"
" margin-left: 0px; /* the last selected tab has nothing to overlap with on the right */\n"
"\n"
"\n"
"    border-top-left-radius: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:!selected\n"
"{\n"
"    color: #b1b1b1;\n"
"    border-bottom-style: solid;\n"
"    margin-top: 3px;\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:1 #212121, stop:.4 #343434);\n"
"}\n"
"\n"
"QTabBar::tab:selected\n"
"{\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"    margin-bottom: 0px;\n"
"}\n"
"\n"
"QTabBar::tab:!selected:hover\n"
"{\n"
"    /*border-top: 2px solid #ffaa00;\n"
"    padding-bottom: 3px;*/\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:1 #212121, stop:0.4 #343434, stop:0.2 #343434, stop:0.1 #ffaa00);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked, QRadioButton::indicator:unchecked{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"    border: 1px solid #b1b1b1;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked\n"
"{\n"
"    background-color: qradialgradient(\n"
"        cx: 0.5, cy: 0.5,\n"
"        fx: 0.5, fy: 0.5,\n"
"        radius: 1.0,\n"
"        stop: 0.25 #ffaa00,\n"
"        stop: 0.3 #323232\n"
"    );\n"
"}\n"
"\n"
"QCheckBox::indicator{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"    border: 1px solid #b1b1b1;\n"
"    width: 9px;\n"
"    height: 9px;\n"
"}\n"
"\n"
"QRadioButton::indicator\n"
"{\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QRadioButton::indicator:hover, QCheckBox::indicator:hover\n"
"{\n"
"    border: 1px solid #ffaa00;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked\n"
"{\n"
"    image:url(:/images/checkbox.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:disabled, QRadioButton::indicator:disabled\n"
"{\n"
"    border: 1px solid #444;\n"
"}")
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 981, 291))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.tab)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 981, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_ = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_.setObjectName("horizontalLayout_")
        self.input_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.input_label.setObjectName("input_label")
        self.horizontalLayout_.addWidget(self.input_label)
        self.input_lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.input_lineEdit.setObjectName("input_lineEdit")
        self.horizontalLayout_.addWidget(self.input_lineEdit)
        self.input_pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.input_pushButton.setObjectName("input_pushButton")
        self.horizontalLayout_.addWidget(self.input_pushButton)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.tab)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 50, 981, 51))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.output_label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.output_label.setObjectName("output_label")
        self.horizontalLayout_2.addWidget(self.output_label)
        self.output_lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.output_lineEdit.setObjectName("output_lineEdit")
        self.horizontalLayout_2.addWidget(self.output_lineEdit)
        self.output_pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.output_pushButton.setObjectName("output_pushButton")
        self.horizontalLayout_2.addWidget(self.output_pushButton)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.tab)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(420, 100, 561, 51))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.improvise_pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.improvise_pushButton.setObjectName("improvise_pushButton")
        self.horizontalLayout_3.addWidget(self.improvise_pushButton)
        self.horizontalLayoutWidget_7 = QtWidgets.QWidget(self.tab)
        self.horizontalLayoutWidget_7.setGeometry(QtCore.QRect(0, 100, 191, 51))
        self.horizontalLayoutWidget_7.setObjectName("horizontalLayoutWidget_7")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_7)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.iteraion_spinBox = QtWidgets.QSpinBox(self.horizontalLayoutWidget_7)
        self.iteraion_spinBox.setMinimum(10)
        self.iteraion_spinBox.setProperty("value", 50)
        self.iteraion_spinBox.setObjectName("iteraion_spinBox")
        self.horizontalLayout.addWidget(self.iteraion_spinBox)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.tab_2)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(0, 0, 981, 51))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_1 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_1.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_1.setObjectName("horizontalLayout_1")
        self.input_label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.input_label_2.setObjectName("input_label_2")
        self.horizontalLayout_1.addWidget(self.input_label_2)
        self.train_input_lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_4)
        self.train_input_lineEdit.setObjectName("train_input_lineEdit")
        self.horizontalLayout_1.addWidget(self.train_input_lineEdit)
        self.train_input_pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        self.train_input_pushButton.setObjectName("train_input_pushButton")
        self.horizontalLayout_1.addWidget(self.train_input_pushButton)
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.tab_2)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(0, 50, 981, 51))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.output_label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        self.output_label_2.setObjectName("output_label_2")
        self.horizontalLayout_4.addWidget(self.output_label_2)
        self.train_output_lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_5)
        self.train_output_lineEdit.setObjectName("train_output_lineEdit")
        self.horizontalLayout_4.addWidget(self.train_output_lineEdit)
        self.train_output_pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_5)
        self.train_output_pushButton.setObjectName("train_output_pushButton")
        self.horizontalLayout_4.addWidget(self.train_output_pushButton)
        self.horizontalLayoutWidget_6 = QtWidgets.QWidget(self.tab_2)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(420, 100, 561, 51))
        self.horizontalLayoutWidget_6.setObjectName("horizontalLayoutWidget_6")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_6)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        self.train_pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_6)
        self.train_pushButton.setObjectName("train_pushButton")
        self.horizontalLayout_5.addWidget(self.train_pushButton)
        self.horizontalLayoutWidget_11 = QtWidgets.QWidget(self.tab_2)
        self.horizontalLayoutWidget_11.setGeometry(QtCore.QRect(0, 100, 191, 51))
        self.horizontalLayoutWidget_11.setObjectName("horizontalLayoutWidget_11")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_11)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget_11)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_9.addWidget(self.label_5)
        self.train_iteraion_spinBox = QtWidgets.QSpinBox(self.horizontalLayoutWidget_11)
        self.train_iteraion_spinBox.setMinimum(10)
        self.train_iteraion_spinBox.setMaximum(9999)
        self.train_iteraion_spinBox.setProperty("value", 100)
        self.train_iteraion_spinBox.setObjectName("train_iteraion_spinBox")
        self.horizontalLayout_9.addWidget(self.train_iteraion_spinBox)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.horizontalLayoutWidget_8 = QtWidgets.QWidget(self.tab_5)
        self.horizontalLayoutWidget_8.setGeometry(QtCore.QRect(0, 0, 981, 51))
        self.horizontalLayoutWidget_8.setObjectName("horizontalLayoutWidget_8")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_8)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.input_label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_8)
        self.input_label_3.setObjectName("input_label_3")
        self.horizontalLayout_6.addWidget(self.input_label_3)
        self.generation_table_lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_8)
        self.generation_table_lineEdit.setObjectName("generation_table_lineEdit")
        self.horizontalLayout_6.addWidget(self.generation_table_lineEdit)
        self.generate_table_pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_8)
        self.generate_table_pushButton.setObjectName("generate_table_pushButton")
        self.horizontalLayout_6.addWidget(self.generate_table_pushButton)
        self.horizontalLayoutWidget_9 = QtWidgets.QWidget(self.tab_5)
        self.horizontalLayoutWidget_9.setGeometry(QtCore.QRect(0, 50, 981, 51))
        self.horizontalLayoutWidget_9.setObjectName("horizontalLayoutWidget_9")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_9)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.input_label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget_9)
        self.input_label_4.setObjectName("input_label_4")
        self.horizontalLayout_7.addWidget(self.input_label_4)
        self.generation_weight_lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_9)
        self.generation_weight_lineEdit.setObjectName("generation_weight_lineEdit")
        self.horizontalLayout_7.addWidget(self.generation_weight_lineEdit)
        self.generate_weight_pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_9)
        self.generate_weight_pushButton.setObjectName("generate_weight_pushButton")
        self.horizontalLayout_7.addWidget(self.generate_weight_pushButton)
        self.horizontalLayoutWidget_10 = QtWidgets.QWidget(self.tab_5)
        self.horizontalLayoutWidget_10.setGeometry(QtCore.QRect(420, 200, 561, 51))
        self.horizontalLayoutWidget_10.setObjectName("horizontalLayoutWidget_10")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_10)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget_10)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_8.addWidget(self.label_4)
        self.generate_pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_10)
        self.generate_pushButton.setObjectName("generate_pushButton")
        self.horizontalLayout_8.addWidget(self.generate_pushButton)
        self.horizontalLayoutWidget_13 = QtWidgets.QWidget(self.tab_5)
        self.horizontalLayoutWidget_13.setGeometry(QtCore.QRect(0, 100, 981, 51))
        self.horizontalLayoutWidget_13.setObjectName("horizontalLayoutWidget_13")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_13)
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.output_label_6 = QtWidgets.QLabel(self.horizontalLayoutWidget_13)
        self.output_label_6.setObjectName("output_label_6")
        self.horizontalLayout_12.addWidget(self.output_label_6)
        self.generation_sample_lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_13)
        self.generation_sample_lineEdit.setObjectName("generation_sample_lineEdit")
        self.horizontalLayout_12.addWidget(self.generation_sample_lineEdit)
        self.generate_sample_pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_13)
        self.generate_sample_pushButton.setObjectName("generate_sample_pushButton")
        self.horizontalLayout_12.addWidget(self.generate_sample_pushButton)
        self.horizontalLayoutWidget_12 = QtWidgets.QWidget(self.tab_5)
        self.horizontalLayoutWidget_12.setGeometry(QtCore.QRect(0, 150, 981, 51))
        self.horizontalLayoutWidget_12.setObjectName("horizontalLayoutWidget_12")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_12)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.output_label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget_12)
        self.output_label_4.setObjectName("output_label_4")
        self.horizontalLayout_10.addWidget(self.output_label_4)
        self.generation_output_lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_12)
        self.generation_output_lineEdit.setObjectName("generation_output_lineEdit")
        self.horizontalLayout_10.addWidget(self.generation_output_lineEdit)
        self.generate_output_pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_12)
        self.generate_output_pushButton.setObjectName("generate_output_pushButton")
        self.horizontalLayout_10.addWidget(self.generate_output_pushButton)
        self.tabWidget.addTab(self.tab_5, "")

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Bard"))
        self.input_label.setText(_translate("Dialog", "  미디 파일 "))
        self.input_pushButton.setText(_translate("Dialog", "찾아보기"))
        self.output_label.setText(_translate("Dialog", "  출력 경로 "))
        self.output_pushButton.setText(_translate("Dialog", "찾아보기"))
        self.label.setText(_translate("Dialog", "입력 파일과 출력 경로 설정 후 생성버튼을 눌러주세요"))
        self.improvise_pushButton.setText(_translate("Dialog", "생성"))
        self.label_3.setText(_translate("Dialog", "  학습 횟수"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Improvise Mode"))
        self.input_label_2.setText(_translate("Dialog", "  미디 경로 "))
        self.train_input_pushButton.setText(_translate("Dialog", "찾아보기"))
        self.output_label_2.setText(_translate("Dialog", "  출력 경로 "))
        self.train_output_pushButton.setText(_translate("Dialog", "찾아보기"))
        self.label_2.setText(_translate("Dialog", "미디 경로와 출력 경로 설정 후 학습버튼을 눌러주세요"))
        self.train_pushButton.setText(_translate("Dialog", "학습"))
        self.label_5.setText(_translate("Dialog", "  학습 횟수"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Train Mode"))
        self.input_label_3.setText(_translate("Dialog", "  테이블 파일"))
        self.generate_table_pushButton.setText(_translate("Dialog", "찾아보기"))
        self.input_label_4.setText(_translate("Dialog", "  가중치 파일"))
        self.generate_weight_pushButton.setText(_translate("Dialog", "찾아보기"))
        self.label_4.setText(_translate("Dialog", "입력 파일과 출력 경로 설정 후 생성버튼을 눌러주세요"))
        self.generate_pushButton.setText(_translate("Dialog", "생성"))
        self.output_label_6.setText(_translate("Dialog", "    샘플 파일 "))
        self.generate_sample_pushButton.setText(_translate("Dialog", "찾아보기"))
        self.output_label_4.setText(_translate("Dialog", "    출력 경로 "))
        self.generate_output_pushButton.setText(_translate("Dialog", "찾아보기"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("Dialog", "Generation Mode"))

