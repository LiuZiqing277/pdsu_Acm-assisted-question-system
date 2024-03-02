# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test1.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QListWidgetItem,
    QMainWindow, QPlainTextEdit, QSizePolicy, QSpacerItem,
    QStatusBar, QTabWidget, QTextBrowser, QVBoxLayout,
    QWidget)

from qfluentwidgets import (LineEdit, ListWidget, PopUpAniStackedWidget, PushButton,
    RadioButton)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1100, 700)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(1100, 700))
        MainWindow.setMaximumSize(QSize(1100, 700))
        MainWindow.setAcceptDrops(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 1, 0, 1, 1)

        self.listWidget_2 = ListWidget(self.centralwidget)
        QListWidgetItem(self.listWidget_2)
        QListWidgetItem(self.listWidget_2)
        QListWidgetItem(self.listWidget_2)
        self.listWidget_2.setObjectName(u"listWidget_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.listWidget_2.sizePolicy().hasHeightForWidth())
        self.listWidget_2.setSizePolicy(sizePolicy1)
        self.listWidget_2.setMinimumSize(QSize(140, 121))
        self.listWidget_2.setMaximumSize(QSize(140, 200))

        self.gridLayout.addWidget(self.listWidget_2, 2, 0, 1, 1)

        self.listWidget = ListWidget(self.centralwidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        self.listWidget.setObjectName(u"listWidget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy2)
        self.listWidget.setMinimumSize(QSize(140, 461))
        self.listWidget.setMaximumSize(QSize(140, 500))

        self.gridLayout.addWidget(self.listWidget, 0, 0, 1, 1)

        self.stackedWidget = PopUpAniStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setSizeIncrement(QSize(2, 1))
        self.PageHome = QWidget()
        self.PageHome.setObjectName(u"PageHome")
        self.gridLayout_3 = QGridLayout(self.PageHome)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.frame = QFrame(self.PageHome)
        self.frame.setObjectName(u"frame")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy3)
        self.frame.setMinimumSize(QSize(631, 241))
        self.frame.setMaximumSize(QSize(640, 250))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(80, 0, 431, 121))
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy4)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(530, 110, 121, 41))
        sizePolicy4.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy4)

        self.gridLayout_3.addWidget(self.frame, 0, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_2, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.PageHome)
        self.PageCopyMode = QWidget()
        self.PageCopyMode.setObjectName(u"PageCopyMode")
        self.horizontalLayout = QHBoxLayout(self.PageCopyMode)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.textBrowser = QTextBrowser(self.PageCopyMode)
        self.textBrowser.setObjectName(u"textBrowser")
        sizePolicy3.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy3)
        self.textBrowser.setMinimumSize(QSize(400, 600))
        self.textBrowser.setMaximumSize(QSize(600, 800))

        self.horizontalLayout.addWidget(self.textBrowser)

        self.tabWidget = QTabWidget(self.PageCopyMode)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy3.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy3)
        self.tabWidget.setMinimumSize(QSize(281, 500))
        self.tabWidget.setMaximumSize(QSize(300, 600))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.formLayoutWidget = QWidget(self.tab)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(20, 10, 217, 191))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(6)
        self.formLayout.setVerticalSpacing(18)
        self.formLayout.setContentsMargins(0, 0, 0, 6)
        self.label_2 = QLabel(self.formLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.lineEdit = LineEdit(self.formLayoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit)

        self.label_3 = QLabel(self.formLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_3)

        self.lineEdit2 = LineEdit(self.formLayoutWidget)
        self.lineEdit2.setObjectName(u"lineEdit2")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEdit2)

        self.label_4 = QLabel(self.formLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_4)

        self.lineEdit_3 = LineEdit(self.formLayoutWidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lineEdit_3)

        self.label_5 = QLabel(self.formLayoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_5)

        self.lineEdit_4 = LineEdit(self.formLayoutWidget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.lineEdit_4)

        self.pushButton = PushButton(self.tab)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(90, 210, 100, 40))
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QSize(100, 40))
        self.pushButton.setMaximumSize(QSize(100, 40))
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.label_14 = QLabel(self.tab_2)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(90, 110, 91, 91))
        self.tabWidget.addTab(self.tab_2, "")

        self.horizontalLayout.addWidget(self.tabWidget)

        self.stackedWidget.addWidget(self.PageCopyMode)
        self.PageAi = QWidget()
        self.PageAi.setObjectName(u"PageAi")
        self.horizontalLayout_2 = QHBoxLayout(self.PageAi)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.textBrowser_2 = QTextBrowser(self.PageAi)
        self.textBrowser_2.setObjectName(u"textBrowser_2")
        sizePolicy3.setHeightForWidth(self.textBrowser_2.sizePolicy().hasHeightForWidth())
        self.textBrowser_2.setSizePolicy(sizePolicy3)

        self.horizontalLayout_2.addWidget(self.textBrowser_2)

        self.frame_3 = QFrame(self.PageAi)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(380, 630))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.pushButton_2 = PushButton(self.frame_3)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(260, 290, 100, 40))
        self.pushButton_2.setMinimumSize(QSize(100, 40))
        self.pushButton_2.setMaximumSize(QSize(91, 40))
        self.frame_2 = QFrame(self.frame_3)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(40, 20, 301, 161))
        self.frame_2.setMinimumSize(QSize(301, 161))
        self.frame_2.setMaximumSize(QSize(301, 161))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label_7 = QLabel(self.frame_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(30, 30, 52, 20))
        self.lineEdit_2 = LineEdit(self.frame_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(100, 30, 157, 20))
        self.label_8 = QLabel(self.frame_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(30, 70, 52, 29))
        self.lineEdit2_2 = LineEdit(self.frame_2)
        self.lineEdit2_2.setObjectName(u"lineEdit2_2")
        self.lineEdit2_2.setGeometry(QRect(100, 70, 157, 20))
        self.groupBox = QGroupBox(self.frame_3)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(40, 240, 181, 181))
        self.radioButtonWenXin = RadioButton(self.groupBox)
        self.radioButtonWenXin.setObjectName(u"radioButtonWenXin")
        self.radioButtonWenXin.setGeometry(QRect(30, 40, 95, 20))
        self.radioButtonGpt35 = RadioButton(self.groupBox)
        self.radioButtonGpt35.setObjectName(u"radioButtonGpt35")
        self.radioButtonGpt35.setGeometry(QRect(30, 90, 131, 20))

        self.horizontalLayout_2.addWidget(self.frame_3)

        self.stackedWidget.addWidget(self.PageAi)
        self.PageHalf = QWidget()
        self.PageHalf.setObjectName(u"PageHalf")
        self.gridLayout_7 = QGridLayout(self.PageHalf)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.ButtonOpenAcm = PushButton(self.PageHalf)
        self.ButtonOpenAcm.setObjectName(u"ButtonOpenAcm")
        sizePolicy3.setHeightForWidth(self.ButtonOpenAcm.sizePolicy().hasHeightForWidth())
        self.ButtonOpenAcm.setSizePolicy(sizePolicy3)
        self.ButtonOpenAcm.setMinimumSize(QSize(101, 41))
        self.ButtonOpenAcm.setMaximumSize(QSize(110, 50))

        self.gridLayout_7.addWidget(self.ButtonOpenAcm, 5, 1, 1, 1)

        self.ButtonInputCode = PushButton(self.PageHalf)
        self.ButtonInputCode.setObjectName(u"ButtonInputCode")
        sizePolicy3.setHeightForWidth(self.ButtonInputCode.sizePolicy().hasHeightForWidth())
        self.ButtonInputCode.setSizePolicy(sizePolicy3)
        self.ButtonInputCode.setMinimumSize(QSize(101, 41))
        self.ButtonInputCode.setMaximumSize(QSize(110, 50))

        self.gridLayout_7.addWidget(self.ButtonInputCode, 7, 1, 1, 1)

        self.lineEdit_6 = LineEdit(self.PageHalf)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setMaximumSize(QSize(170, 20))

        self.gridLayout_7.addWidget(self.lineEdit_6, 3, 1, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 167, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_7.addItem(self.verticalSpacer_3, 8, 1, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 168, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_7.addItem(self.verticalSpacer_4, 6, 1, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 167, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_7.addItem(self.verticalSpacer_5, 4, 1, 1, 1)

        self.plainTextEdit_2 = QPlainTextEdit(self.PageHalf)
        self.plainTextEdit_2.setObjectName(u"plainTextEdit_2")
        sizePolicy3.setHeightForWidth(self.plainTextEdit_2.sizePolicy().hasHeightForWidth())
        self.plainTextEdit_2.setSizePolicy(sizePolicy3)
        self.plainTextEdit_2.setMinimumSize(QSize(400, 600))
        self.plainTextEdit_2.setMaximumSize(QSize(600, 800))

        self.gridLayout_7.addWidget(self.plainTextEdit_2, 0, 0, 9, 1)

        self.lineEdit_5 = LineEdit(self.PageHalf)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setMaximumSize(QSize(170, 20))

        self.gridLayout_7.addWidget(self.lineEdit_5, 2, 1, 1, 1)

        self.stackedWidget.addWidget(self.PageHalf)
        self.PageHomework = QWidget()
        self.PageHomework.setObjectName(u"PageHomework")
        self.gridLayout_6 = QGridLayout(self.PageHomework)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.webEngineView_3 = QWebEngineView(self.PageHomework)
        self.webEngineView_3.setObjectName(u"webEngineView_3")
        self.webEngineView_3.setUrl(QUrl(u"about:blank"))

        self.gridLayout_6.addWidget(self.webEngineView_3, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.PageHomework)
        self.PageChat = QWidget()
        self.PageChat.setObjectName(u"PageChat")
        self.gridLayout_2 = QGridLayout(self.PageChat)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.vBoxLayout = QVBoxLayout()
        self.vBoxLayout.setObjectName(u"vBoxLayout")

        self.gridLayout_2.addLayout(self.vBoxLayout, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.PageChat)
        self.PageSearch = QWidget()
        self.PageSearch.setObjectName(u"PageSearch")
        self.gridLayout_4 = QGridLayout(self.PageSearch)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.webEngineView_2 = QWebEngineView(self.PageSearch)
        self.webEngineView_2.setObjectName(u"webEngineView_2")
        self.webEngineView_2.setUrl(QUrl(u"about:blank"))

        self.gridLayout_4.addWidget(self.webEngineView_2, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.PageSearch)
        self.PageTestCode = QWidget()
        self.PageTestCode.setObjectName(u"PageTestCode")
        self.gridLayout_5 = QGridLayout(self.PageTestCode)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.webEngineView = QWebEngineView(self.PageTestCode)
        self.webEngineView.setObjectName(u"webEngineView")
        self.webEngineView.setUrl(QUrl(u"about:blank"))

        self.gridLayout_5.addWidget(self.webEngineView, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.PageTestCode)
        self.PageMoney = QWidget()
        self.PageMoney.setObjectName(u"PageMoney")
        self.label_10 = QLabel(self.PageMoney)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(120, 20, 401, 531))
        self.label_10.setMaximumSize(QSize(16777215, 531))
        self.label_11 = QLabel(self.PageMoney)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(630, 110, 191, 71))
        self.stackedWidget.addWidget(self.PageMoney)
        self.PageHelp = QWidget()
        self.PageHelp.setObjectName(u"PageHelp")
        self.label_9 = QLabel(self.PageHelp)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(70, 80, 101, 41))
        self.label_9.setMinimumSize(QSize(101, 41))
        self.label_9.setMaximumSize(QSize(101, 41))
        self.lineEdit_8 = LineEdit(self.PageHelp)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setGeometry(QRect(210, 140, 500, 31))
        self.lineEdit_8.setMinimumSize(QSize(500, 31))
        self.lineEdit_8.setMaximumSize(QSize(500, 16777215))
        self.label_13 = QLabel(self.PageHelp)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(70, 140, 101, 41))
        self.label_13.setMinimumSize(QSize(101, 41))
        self.label_13.setMaximumSize(QSize(101, 41))
        self.lineEdit_11 = LineEdit(self.PageHelp)
        self.lineEdit_11.setObjectName(u"lineEdit_11")
        self.lineEdit_11.setGeometry(QRect(210, 80, 500, 31))
        self.lineEdit_11.setMinimumSize(QSize(500, 31))
        self.lineEdit_11.setMaximumSize(QSize(500, 16777215))
        self.lineEdit_10 = LineEdit(self.PageHelp)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        self.lineEdit_10.setGeometry(QRect(210, 190, 500, 31))
        self.lineEdit_10.setMinimumSize(QSize(500, 31))
        self.lineEdit_10.setMaximumSize(QSize(500, 16777215))
        self.textBrowser_4 = QTextBrowser(self.PageHelp)
        self.textBrowser_4.setObjectName(u"textBrowser_4")
        self.textBrowser_4.setGeometry(QRect(100, 350, 401, 41))
        self.textBrowser_4.setStyleSheet(u"background-color: transparent;\n"
"border: none;\n"
"")
        self.textBrowser_4.setOpenExternalLinks(True)
        self.pushButton_3 = PushButton(self.PageHelp)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(770, 80, 100, 40))
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setMinimumSize(QSize(100, 40))
        self.pushButton_3.setMaximumSize(QSize(100, 40))
        self.pushButton_5 = PushButton(self.PageHelp)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(770, 160, 100, 40))
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)
        self.pushButton_5.setMinimumSize(QSize(100, 40))
        self.pushButton_5.setMaximumSize(QSize(100, 40))
        self.stackedWidget.addWidget(self.PageHelp)
        self.PageWriter = QWidget()
        self.PageWriter.setObjectName(u"PageWriter")
        self.gridLayout_8 = QGridLayout(self.PageWriter)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_8.addItem(self.verticalSpacer_6, 3, 0, 1, 1)

        self.textBrowserXiao = QTextBrowser(self.PageWriter)
        self.textBrowserXiao.setObjectName(u"textBrowserXiao")
        self.textBrowserXiao.setMinimumSize(QSize(781, 261))
        self.textBrowserXiao.setStyleSheet(u"background-color: transparent;\n"
"border: none;")

        self.gridLayout_8.addWidget(self.textBrowserXiao, 2, 0, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.textBrowser_3 = QTextBrowser(self.PageWriter)
        self.textBrowser_3.setObjectName(u"textBrowser_3")
        self.textBrowser_3.setMinimumSize(QSize(780, 140))
        font = QFont()
        font.setFamilies([u"\u5e7c\u5706"])
        self.textBrowser_3.setFont(font)
        self.textBrowser_3.setStyleSheet(u"background-color: transparent;\n"
"border: none;\n"
"")
        self.textBrowser_3.setOpenExternalLinks(True)

        self.gridLayout_8.addWidget(self.textBrowser_3, 1, 0, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_8.addItem(self.verticalSpacer_7, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.PageWriter)

        self.gridLayout.addWidget(self.stackedWidget, 0, 1, 3, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Pdsu_Acm\u8f85\u52a9\u89e3\u9898\u7cfb\u7edf-GUI2.0\u7248", None))

        __sortingEnabled = self.listWidget_2.isSortingEnabled()
        self.listWidget_2.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget_2.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u6350\u732e", None));
        ___qlistwidgetitem1 = self.listWidget_2.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u5e2e\u52a9&\u914d\u7f6e", None));
        ___qlistwidgetitem2 = self.listWidget_2.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e\u4f5c\u8005", None));
        self.listWidget_2.setSortingEnabled(__sortingEnabled)


        __sortingEnabled1 = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        ___qlistwidgetitem3 = self.listWidget.item(0)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Home", None));
        ___qlistwidgetitem4 = self.listWidget.item(1)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Copy \u6a21\u5f0f", None));
        ___qlistwidgetitem5 = self.listWidget.item(2)
        ___qlistwidgetitem5.setText(QCoreApplication.translate("MainWindow", u"AI \u6a21\u5f0f", None));
        ___qlistwidgetitem6 = self.listWidget.item(3)
        ___qlistwidgetitem6.setText(QCoreApplication.translate("MainWindow", u"\u534a\u81ea\u52a8\u6a21\u5f0f", None));
        ___qlistwidgetitem7 = self.listWidget.item(4)
        ___qlistwidgetitem7.setText(QCoreApplication.translate("MainWindow", u"\u5199\u4f5c\u4e1a\u4e86\uff01", None));
        ___qlistwidgetitem8 = self.listWidget.item(5)
        ___qlistwidgetitem8.setText(QCoreApplication.translate("MainWindow", u"\u548cAI\u804a\u804a\uff1f", None));
        ___qlistwidgetitem9 = self.listWidget.item(6)
        ___qlistwidgetitem9.setText(QCoreApplication.translate("MainWindow", u"\u4e0a\u7f51\u67e5\u67e5\uff01", None));
        ___qlistwidgetitem10 = self.listWidget.item(7)
        ___qlistwidgetitem10.setText(QCoreApplication.translate("MainWindow", u"\u6d4b\u8bd5\u4ee3\u7801", None));
        ___qlistwidgetitem11 = self.listWidget.item(8)
        ___qlistwidgetitem11.setText(QCoreApplication.translate("MainWindow", u"\u6700\u5927\u5316", None));
        self.listWidget.setSortingEnabled(__sortingEnabled1)

        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:24pt;\">\u5e73\u9876\u5c71\u5b66\u9662Acm\u8f85\u52a9\u89e3\u9898\u7cfb\u7edf</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt;\">By \u5218 \u51ef</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">\u4f60\u7684\u8d26\u53f7</span></p></body></html>", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8d26\u53f7", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">\u4f60\u7684\u5bc6\u7801</span></p></body></html>", None))
        self.lineEdit2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u5bc6\u7801", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">\u76c6\u53cb\u8d26\u53f7</span></p></body></html>", None))
        self.lineEdit_3.setText("")
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8d26\u53f7", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">\u76c6\u53cb\u5bc6\u7801</span></p></body></html>", None))
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u5bc6\u7801", None))
#if QT_CONFIG(tooltip)
        self.pushButton.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u63d0\u4ea4\u540e\uff0c\u5f00\u59cb\u4ece\u76c6\u53cb\u8d26\u53f7\u590d\u5236\u7b54\u6848</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u63d0\u4ea4\u5e76\u8fd0\u884c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"\u586b\u4e00\u4e0b", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">\u4e0d\u51c6\u5907\u5199\u4e86</span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\u4eea\u8868\u76d8", None))
        self.textBrowser_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.pushButton_2.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700;\">\u4e0d\u8981\u91cd\u590d\u70b9\u51fb\uff01</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u63d0\u4ea4\u5e76\u8fd0\u884c", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">\u4f60\u7684\u8d26\u53f7</span></p></body></html>", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Acm\u8d26\u53f7", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">\u4f60\u7684\u5bc6\u7801</span></p></body></html>", None))
        self.lineEdit2_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u5bf9\u5e94\u7684\u5bc6\u7801", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u9009\u4e2aAI", None))
        self.radioButtonWenXin.setText(QCoreApplication.translate("MainWindow", u"\u6587\u5fc3\u4e00\u8a00", None))
        self.radioButtonGpt35.setText(QCoreApplication.translate("MainWindow", u"ChatGPT3.5", None))
        self.ButtonOpenAcm.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u542f\u5b9e\u4f8b", None))
        self.ButtonInputCode.setText(QCoreApplication.translate("MainWindow", u"\u63d0\u4ea4\u4ee3\u7801", None))
        self.lineEdit_6.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u76f8\u5e94\u7684\u5bc6\u7801", None))
        self.plainTextEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8f93\u5165\u8d26\u53f7\u5bc6\u7801\u540e\u5f00\u542f\u5b9e\u4f8b\uff0c\u5728\u5b9e\u4f8b\u4e2d\u6253\u5f00\u4f60\u8981\u505a\u9898\u7684\u5199\u4ee3\u7801\u754c\u9762\uff0c\u7136\u540e\u5c06\u4ee3\u7801\u7c98\u8d34\u5728\u8fd9\u91cc\uff0c\u70b9\u51fb\u63d0\u4ea4\uff0c\u7a0b\u5e8f\u4f1a\u81ea\u52a8\u63d0\u4ea4\u4ee3\u7801\u3002\u5728\u8fd9\u91cc\u8f93\u5165\u4ee3\u7801", None))
        self.lineEdit_5.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u770b\u8fd9\u513f\uff01\u8f93\u5165Acm\u8d26\u6237", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"23", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:24pt;\">\u611f\u8c22\u652f\u6301\uff01</span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:700;\">GPT_API_KEY</span></p></body></html>", None))
        self.lineEdit_8.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8f93\u5165\u6587\u5fc3\u4e00\u8a00\u7684BAIDUID.", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:700;\">\u6587\u5fc3_API_KEY</span></p></body></html>", None))
        self.lineEdit_10.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8f93\u5165\u6587\u5fc3\u4e00\u8a00\u7684BDUSS_BFESS.", None))
        self.textBrowser_4.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"http://www.li-yian.site/2024/02/17/Acm%E8%BE%85%E5%8A%A9%E8%A7%A3%E9%A2%98%E7%B3%BB%E7%BB%9F%E5%B8%AE%E5%8A%A9%E6%96%87%E6%A1%A3/\"><span style=\" font-size:18pt; font-weight:700; text-decoration: underline; color:#0078d4;\">\u70b9\u6211\u770b\u5e2e\u52a9\u6587\u6863</span></a></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.pushButton_3.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u63d0\u4ea4\u540e\uff0c\u5f00\u59cb\u4ece\u76c6\u53cb\u8d26\u53f7\u590d\u5236\u7b54\u6848</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58", None))
#if QT_CONFIG(tooltip)
        self.pushButton_5.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u63d0\u4ea4\u540e\uff0c\u5f00\u59cb\u4ece\u76c6\u53cb\u8d26\u53f7\u590d\u5236\u7b54\u6848</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58", None))
        self.textBrowserXiao.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.textBrowser_3.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'\u5e7c\u5706'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Microsoft YaHei UI'; font-size:14pt;\">\u4f5c\u8005\uff1a\u5218\u51ef</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Microsoft YaHei UI'; font-size:14pt;\">\u535a\u5ba2\uff1a</span><a href=\"http://www.li-yian.site\"><span style=\" font-family:'Microsoft "
                        "YaHei UI'; font-size:14pt; text-decoration: underline; color:#0078d4;\">http://www.li-yian.site</span></a></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Microsoft YaHei UI'; font-size:14pt;\">bug\u53cd\u9988\uff1a2153853451@qq.com</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Microsoft YaHei UI'; font-size:14pt;\">github\u5730\u5740\uff1a</span><a href=\"https://github.com/LiuZiqing277/pdsu_Acm-assisted-question-system\"><span style=\" font-family:'Microsoft YaHei UI'; font-size:14pt; text-decoration: underline; color:#0078d4;\">https://github.com/LiuZiqing277/pdsu_Acm-assisted-question-system</span></a></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\"> </span></p>\n"
"<p st"
                        "yle=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">\u4ee3\u7801\u6539\u5584\u540e\u5c06\u5f00\u6e90\u5728github</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Microsoft YaHei UI'; font-size:14pt;\"><br /></p></body></html>", None))
    # retranslateUi

