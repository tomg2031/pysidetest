# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TestWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
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
from PySide6.QtWidgets import (QApplication, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QWidget)

class Ui_testWindow(object):
    def setupUi(self, testWindow):
        if not testWindow.objectName():
            testWindow.setObjectName(u"testWindow")
        testWindow.resize(800, 600)
        self.centralwidget = QWidget(testWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.mypushButton = QPushButton(self.centralwidget)
        self.mypushButton.setObjectName(u"mypushButton")
        self.mypushButton.setGeometry(QRect(230, 140, 271, 151))
        self.mylineEdit = QLineEdit(self.centralwidget)
        self.mylineEdit.setObjectName(u"mylineEdit")
        self.mylineEdit.setGeometry(QRect(230, 100, 271, 22))
        testWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(testWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        testWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(testWindow)
        self.statusbar.setObjectName(u"statusbar")
        testWindow.setStatusBar(self.statusbar)

        self.retranslateUi(testWindow)

        QMetaObject.connectSlotsByName(testWindow)
    # setupUi

    def retranslateUi(self, testWindow):
        testWindow.setWindowTitle(QCoreApplication.translate("testWindow", u"MainWindow", None))
        self.mypushButton.setText(QCoreApplication.translate("testWindow", u"GO", None))
    # retranslateUi

