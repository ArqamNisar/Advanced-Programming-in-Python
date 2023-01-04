
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPlainTextEdit,
    QPushButton, QSizePolicy, QStackedWidget, QStatusBar,QTableWidget, QMessageBox,QTabWidget,
    QTableWidget, QTableWidgetItem, QWidget)

from PySide6.QtUiTools import QUiLoader
from ui_Home import Ui_MainWindow
import mysql.connector 

database = mysql.connector.connect(host="192.168.100.132", user="arqam", password="Vk18arsh", db="electronicsinventory")
curs = database.cursor()
loader = QUiLoader()

class Ui_IMSLogin(object):
    def setupUi(self, IMSLogin):
        if not IMSLogin.objectName():
            IMSLogin.setObjectName(u"IMSLogin")
        IMSLogin.resize(800, 600)
        self.centralwidget = QWidget(IMSLogin)
        self.centralwidget.setObjectName(u"centralwidget")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, -10, 871, 601))
        self.stackedWidget.setStyleSheet("background-color:rgb(170, 85, 0);")
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.lineEdit = QLineEdit(self.page_3)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(140, 70, 113, 20))
        self.lineEdit.setStyleSheet("background-color:rgb(255, 255, 255);")
        self.page_3.setStyleSheet("background-color: rgb(170, 85, 0)")
        font = QFont()
        font.setPointSize(9)
        font.setBold(True)
        self.usename = QLabel(self.page_3)
        self.usename.setFont(font)
        self.usename.setObjectName(u"usename")
        self.usename.setGeometry(QRect(50, 70, 81, 16))
        self.usename.setStyleSheet("color: rgb(255, 255, 255); ")
        self.label_2 = QLabel(self.page_3)
        self.label_2.setFont(font)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(50, 100, 81, 16))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        
        self.lineEdit_2 = QLineEdit(self.page_3)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(140, 100, 113, 20))
        self.lineEdit_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lineEdit_2.setEchoMode(QLineEdit.Password)
        self.pushButton = QPushButton(self.page_3,clicked = lambda: self.hometab())
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setFont(font)
        self.pushButton.setGeometry(QRect(160, 140, 75, 23))
        self.pushButton.setStyleSheet("background-color:rgb(255, 255, 255);")
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.page_4.setStyleSheet("background-color:rgb(170, 85, 0);")
        self.pushButton_3 = QPushButton(self.page_4,clicked=lambda:self.showPrinters())
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(20, 130, 171, 41))
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_4 = QPushButton(self.page_4,clicked=lambda:self.showSensors())
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(20, 190, 171, 41))
        self.pushButton_4.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.pushButton_2 = QPushButton(self.page_4,clicked=lambda:self.showMicro())
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(20, 70, 171, 41))
        self.pushButton_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.pushButton_5 = QPushButton(self.page_4,clicked=lambda:self.showTransformers())
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(20, 250, 171, 41))
        self.pushButton_5.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.pushButton_6 = QPushButton(self.page_4)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(10, 10, 171, 41))
        self.pushButton_6.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.pushButton_13 = QPushButton(self.page_4,clicked=lambda:self.openinv())
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setGeometry(QRect(180, 10, 171, 41))
        self.pushButton_13.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.pushButton_14 = QPushButton(self.page_4,clicked=lambda:self.Accounts())
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setGeometry(QRect(350, 10, 171, 41))
        self.pushButton_14.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.page_5.setStyleSheet(u"background-color: rgb(170, 85, 0);")
        self.label_3 = QLabel(self.page_5)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(60, 40, 141, 111))
        self.label_3.setStyleSheet(u"image: url(:/newPrefix/Training set/1..jpg);")
        self.plainTextEdit = QPlainTextEdit(self.page_5)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(60, 160, 141, 51))
        self.plainTextEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_4 = QLabel(self.page_5)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(280, 40, 141, 111))
        self.label_4.setStyleSheet(u"image: url(:/newPrefix/Training set/2.jpg);")
        self.plainTextEdit_2 = QPlainTextEdit(self.page_5)
        self.plainTextEdit_2.setObjectName(u"plainTextEdit_2")
        self.plainTextEdit_2.setGeometry(QRect(280, 160, 151, 51))
        self.plainTextEdit_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_5 = QLabel(self.page_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(60, 220, 141, 111))
        self.label_5.setStyleSheet(u"image: url(:/newPrefix/Training set/4.jpg);")
        self.plainTextEdit_3 = QPlainTextEdit(self.page_5)
        self.plainTextEdit_3.setObjectName(u"plainTextEdit_3")
        self.plainTextEdit_3.setGeometry(QRect(60, 340, 151, 51))
        self.plainTextEdit_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_6 = QLabel(self.page_5)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(290, 220, 141, 111))
        self.label_6.setStyleSheet(u"image: url(:/newPrefix/Training set/8.PNG);")
        self.plainTextEdit_4 = QPlainTextEdit(self.page_5)
        self.plainTextEdit_4.setObjectName(u"plainTextEdit_4")
        self.plainTextEdit_4.setGeometry(QRect(290, 340, 151, 51))
        self.plainTextEdit_4.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_7 = QLabel(self.page_5)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(60, 400, 141, 111))
        self.label_7.setStyleSheet(u"image: url(:/newPrefix/Training set/3.jpg);")
        self.plainTextEdit_5 = QPlainTextEdit(self.page_5)
        self.plainTextEdit_5.setObjectName(u"plainTextEdit_5")
        self.plainTextEdit_5.setGeometry(QRect(60, 510, 151, 51))
        self.plainTextEdit_5.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.stackedWidget.addWidget(self.page_5)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.page_6.setStyleSheet(u"background-color: rgb(170, 85, 0);")
        self.plainTextEdit_21 = QPlainTextEdit(self.page_6)
        self.plainTextEdit_21.setObjectName(u"plainTextEdit_21")
        self.plainTextEdit_21.setGeometry(QRect(30, 150, 151, 51))
        self.plainTextEdit_21.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_29 = QLabel(self.page_6)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(30, 30, 141, 111))
        self.label_29.setStyleSheet(u"image: url(:/newPrefix/Training set/6.jpg);")
        self.label_30 = QLabel(self.page_6)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setGeometry(QRect(280, 30, 141, 111))
        self.label_30.setStyleSheet(u"image: url(:/newPrefix/Training set/7.PNG);")
        self.plainTextEdit_22 = QPlainTextEdit(self.page_6)
        self.plainTextEdit_22.setObjectName(u"plainTextEdit_22")
        self.plainTextEdit_22.setGeometry(QRect(280, 150, 171, 61))
        self.plainTextEdit_22.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"")
        self.stackedWidget.addWidget(self.page_6)
        self.page_19 = QWidget()
        self.page_19.setObjectName(u"page_19")
        self.page_19.setStyleSheet(u"background-color: rgb(170, 85, 0);")
        self.plainTextEdit_23 = QPlainTextEdit(self.page_19)
        self.plainTextEdit_23.setObjectName(u"plainTextEdit_23")
        self.plainTextEdit_23.setGeometry(QRect(10, 150, 171, 51))
        self.plainTextEdit_23.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_31 = QLabel(self.page_19)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(10, 30, 141, 111))
        self.label_31.setStyleSheet(u"image: url(:/newPrefix/Training set/10.JPG);")
        self.label_32 = QLabel(self.page_19)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setGeometry(QRect(320, 30, 141, 111))
        self.label_32.setStyleSheet(u"image: url(:/newPrefix/Training set/9.JPG);")
        self.plainTextEdit_24 = QPlainTextEdit(self.page_19)
        self.plainTextEdit_24.setObjectName(u"plainTextEdit_24")
        self.plainTextEdit_24.setGeometry(QRect(320, 150, 171, 51))
        self.plainTextEdit_24.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_33 = QLabel(self.page_19)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setGeometry(QRect(10, 210, 141, 111))
        self.label_33.setStyleSheet(u"image: url(:/newPrefix/Training set/13.jpg);")
        self.plainTextEdit_25 = QPlainTextEdit(self.page_19)
        self.plainTextEdit_25.setObjectName(u"plainTextEdit_25")
        self.plainTextEdit_25.setGeometry(QRect(10, 330, 161, 51))
        self.plainTextEdit_25.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_34 = QLabel(self.page_19)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setGeometry(QRect(320, 210, 141, 111))
        self.label_34.setStyleSheet(u"image: url(:/newPrefix/Training set/8f82ca99-5261-41bf-bf73-17038f0eaef0.jpg);")
        self.plainTextEdit_26 = QPlainTextEdit(self.page_19)
        self.plainTextEdit_26.setObjectName(u"plainTextEdit_26")
        self.plainTextEdit_26.setGeometry(QRect(320, 330, 181, 51))
        self.plainTextEdit_26.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_35 = QLabel(self.page_19)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setGeometry(QRect(20, 390, 151, 101))
        self.label_35.setStyleSheet(u"image: url(:/newPrefix/Training set/45.jpg);")
        self.plainTextEdit_27 = QPlainTextEdit(self.page_19)
        self.plainTextEdit_27.setObjectName(u"plainTextEdit_27")
        self.plainTextEdit_27.setGeometry(QRect(10, 500, 231, 51))
        self.plainTextEdit_27.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.stackedWidget.addWidget(self.page_19)
        self.page_20 = QWidget()
        self.page_20.setObjectName(u"page_20")
        self.page_20.setStyleSheet(u"background-color: rgb(170, 85, 0);")
        self.label_36 = QLabel(self.page_20)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setGeometry(QRect(230, 80, 141, 111))
        self.label_36.setStyleSheet(u"image:url(:/newPrefix/Training set/transformer.jpg);")
        self.plainTextEdit_28 = QPlainTextEdit(self.page_20)
        self.plainTextEdit_28.setObjectName(u"plainTextEdit_28")
        self.plainTextEdit_28.setGeometry(QRect(220, 200, 171, 61))
        self.plainTextEdit_28.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.stackedWidget.addWidget(self.page_20)
        self.page_21 = QWidget()
        self.page_21.setObjectName(u"page_21")
        self.label = QLabel(self.page_21)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(60, 120, 121, 41))
        self.label.setStyleSheet(u"background-color: rgb(170, 85, 0);")
        self.lineEdit_5 = QLineEdit(self.page_21)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(290, 130, 131, 20))
        self.lineEdit_5.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lineEdit_6 = QLineEdit(self.page_21)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setGeometry(QRect(290, 210, 133, 20))
        self.lineEdit_6.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.a = self.lineEdit_6.text() 
        self.b = self.lineEdit_2.text()
        self.pushButton_15 = QPushButton(self.page_21,clicked=lambda: self.Setnewpass())
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setGeometry(QRect(170, 300, 141, 31))
        self.pushButton_15.setStyleSheet(u"background-color: rgb(170, 85, 0);")
        self.label_14 = QLabel(self.page_21)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(60, 190, 121, 41))
        self.label_14.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.stackedWidget.addWidget(self.page_21)
        self.page_22 = QWidget()
        self.page_22.setObjectName(u"page_22")
        self.Inventory = QStackedWidget(self.page_22)
        self.Inventory.setObjectName(u"Inventory")
        self.Inventory.setGeometry(QRect(-90, -20, 971, 741))
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.Inventory.setFont(font)
        self.Inventory.setStyleSheet(u"background-color: rgb(170, 85, 0);")
        self.DisplayForm = QWidget()
        self.DisplayForm.setObjectName(u"DisplayForm")
        self.DisplayForm.setAutoFillBackground(False)
        self.pushButton_25 = QPushButton(self.DisplayForm)
        self.pushButton_25.setObjectName(u"pushButton_25")
        self.pushButton_25.setGeometry(QRect(275, 145, 151, 31))
        self.pushButton_25.setStyleSheet(u"\n"
"	background-color:#ffffff;\n"
"")
        self.pushButton_26 = QPushButton(self.DisplayForm,clicked=lambda:self.showInv())
        self.pushButton_26.setObjectName(u"pushButton_26")
        self.pushButton_26.setGeometry(QRect(150, 300, 168, 31))
        self.pushButton_26.setStyleSheet(u"\n"
"	background-color:#ffffff;\n"
"")
        
        self.Inventory.addWidget(self.DisplayForm)
        self.stackedWidget.addWidget(self.page_22)
        self.page_23 = QWidget()
        self.page_23.setObjectName(u"page_23")
        self.Inventory_2 = QStackedWidget(self.page_23)
        self.Inventory_2.setObjectName(u"Inventory_2")
        self.Inventory_2.setGeometry(QRect(-40, 10, 801, 571))
        self.Inventory_2.setFont(font)
        self.Inventory_2.setStyleSheet(u"background-color: rgb(170, 85, 0);")
        self.AddRemoveForm = QWidget()
        self.AddRemoveForm.setObjectName(u"AddRemoveForm")
        self.Edit_Inventory = QLineEdit(self.AddRemoveForm)
        self.Edit_Inventory.setFont(font)
        self.Edit_Inventory.setObjectName(u"Edit_Inventory")
        self.Edit_Inventory.setGeometry(QRect(100, 80, 161, 51))
        self.Edit_Inventory.setStyleSheet(u"#Edit_Inventory{\n"
"	color:#ffffff;\n"
"}")
        self.Edit_Inventory_2 = QLineEdit(self.AddRemoveForm)
        self.Edit_Inventory_2.setObjectName(u"Edit_Inventory_2")
        self.Edit_Inventory_2.setGeometry(QRect(100, 130, 161, 51))
        self.Edit_Inventory_2.setFont(font)
        self.Edit_Inventory_2.setStyleSheet(u"#Edit_Inventory_2{\n"
"	color:#ffffff;\n"
"}")
        self.lineEdit_16 = QLineEdit(self.AddRemoveForm)
        self.lineEdit_16.setObjectName(u"lineEdit_16")
        self.lineEdit_16.setGeometry(QRect(410, 190, 151, 51))
        self.lineEdit_16.setStyleSheet(u"\n"
"	background-color:#ffffff;\n"
"")
        self.lineEdit_17 = QLineEdit(self.AddRemoveForm)
        self.lineEdit_17.setObjectName(u"lineEdit_17")
        self.lineEdit_17.setGeometry(QRect(410, 80, 151, 51))
        self.lineEdit_17.setStyleSheet(u"\n"
"	background-color:#ffffff;\n"
"")
        self.pushButton_24 = QPushButton(self.AddRemoveForm,clicked=lambda: self.addremprod())
        self.pushButton_24.setObjectName(u"pushButton_24")
        self.pushButton_24.setGeometry(QRect(240, 70, 291, 91))
        self.pushButton_24.setFont(font)
        self.pushButton_24.setStyleSheet(u"\n"
"	background-color:#ffffff;\n"
"")

        
        self.Inventory_2.addWidget(self.AddRemoveForm)
        self.stackedWidget.addWidget(self.page_23)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.tableWidget = QTableWidget(self.page)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.tableWidget.rowCount() < 13):
            self.tableWidget.setRowCount(13)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(12, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget.setItem(1, 0, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget.setItem(1, 1, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget.setItem(2, 0, __qtablewidgetitem20)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(60, 50, 451, 411))
        self.tableWidget.setStyleSheet(u"background-color: #C0C0C0;\n"
"alternate-background-color:#606060;\n"
"selection-background-color: #282828;")
        self.stackedWidget.addWidget(self.page)
        IMSLogin.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(IMSLogin)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        IMSLogin.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(IMSLogin)
        self.statusbar.setObjectName(u"statusbar")
        IMSLogin.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addSeparator()

        self.retranslateUi(IMSLogin)

        self.stackedWidget.setCurrentIndex(0)
        self.Inventory.setCurrentIndex(0)
        self.Inventory_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(IMSLogin)
    # setupUi

    def retranslateUi(self, IMSLogin):
        IMSLogin.setWindowTitle(QCoreApplication.translate("IMSLogin", u"Inventory Management System (Electronic Store)", None))
        self.usename.setText(QCoreApplication.translate("IMSLogin", u"Username", None))
        self.label_2.setText(QCoreApplication.translate("IMSLogin", u"Password", None))
        self.pushButton.setText(QCoreApplication.translate("IMSLogin", u"Login", None))
        self.pushButton_3.setText(QCoreApplication.translate("IMSLogin", u"Printers", None))
        self.pushButton_4.setText(QCoreApplication.translate("IMSLogin", u"Sensors", None))
        self.pushButton_2.setText(QCoreApplication.translate("IMSLogin", u"Microcontrollers", None))
        self.pushButton_5.setText(QCoreApplication.translate("IMSLogin", u"Transformers", None))
        self.pushButton_6.setText(QCoreApplication.translate("IMSLogin", u"Products", None))
        self.pushButton_13.setText(QCoreApplication.translate("IMSLogin", u"Inventory", None))
        self.pushButton_14.setText(QCoreApplication.translate("IMSLogin", u"Account Settings", None))

        self.label.setText(QCoreApplication.translate("IMSLogin", u"New Password", None))
        
        self.pushButton_15.setText(QCoreApplication.translate("IMSLogin", u"Set New Password", None))
        self.pushButton_25.setText(QCoreApplication.translate("IMSLogin", u"Add/Remove from Inventory", None))
        self.label_14.setText(QCoreApplication.translate("IMSLogin", u"Confirm Password", None))
        self.pushButton_24.setText(QCoreApplication.translate("IMSLogin", u"Add/Remove Products", None))
        self.Edit_Inventory.setText(QCoreApplication.translate("IMSLogin", u"Product Name:", None))
        self.Edit_Inventory_2.setText(QCoreApplication.translate("IMSLogin", u"     Quantity:", None))
        self.pushButton_26.setText(QCoreApplication.translate("IMSLogin", u"Show Inventory", None))

        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("IMSLogin", u"Product", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("IMSLogin", u"Category", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("IMSLogin", u"Price", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("IMSLogin", u"Units", None));
        ___qtablewidgetitem4 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("IMSLogin", u"1", None));
        ___qtablewidgetitem5 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("IMSLogin", u"2", None));
        ___qtablewidgetitem6 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("IMSLogin", u"3", None));
        ___qtablewidgetitem7 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("IMSLogin", u"4", None));
        ___qtablewidgetitem8 = self.tableWidget.verticalHeaderItem(4)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("IMSLogin", u"5", None));
        ___qtablewidgetitem9 = self.tableWidget.verticalHeaderItem(5)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("IMSLogin", u"6", None));
        ___qtablewidgetitem10 = self.tableWidget.verticalHeaderItem(6)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("IMSLogin", u"7", None));
        ___qtablewidgetitem11 = self.tableWidget.verticalHeaderItem(7)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("IMSLogin", u"8", None));
        ___qtablewidgetitem12 = self.tableWidget.verticalHeaderItem(8)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("IMSLogin", u"9", None));
        ___qtablewidgetitem13 = self.tableWidget.verticalHeaderItem(9)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("IMSLogin", u"10", None));
        ___qtablewidgetitem14 = self.tableWidget.verticalHeaderItem(10)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("IMSLogin", u"11", None));
        ___qtablewidgetitem15 = self.tableWidget.verticalHeaderItem(11)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("IMSLogin", u"12", None));
        ___qtablewidgetitem16 = self.tableWidget.verticalHeaderItem(12)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("IMSLogin", u"13", None));
        # ___qtablewidgetitem17 = self.tableWidget.verticalHeaderItem(13)
        # ___qtablewidgetitem17.setText(QCoreApplication.translate("IMSLogin", u"14", None));        
        # ___qtablewidgetitem18 = self.tableWidget.verticalHeaderItem(14)
        # ___qtablewidgetitem18.setText(QCoreApplication.translate("IMSLogin", u"15", None));
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.menuFile.setTitle(QCoreApplication.translate("IMSLogin", u"File", None))
    # retranslateUi

    def hometab(self):
            curs.execute("select * from login")
            result = curs.fetchall()

            if self.lineEdit.text() == result[0][0] and self.lineEdit_2.text() == result[0][1]:
                
                self.stackedWidget.addWidget(self.page_3)
                self.page_4 = QWidget()
                self.page_4.setObjectName(u"page_4")
                # self.page_4.setStyleSheet('background-color: red;')
                self.page_4.setStyleSheet("background-image:url(4.jpg);")
                                        #  u"background-position: center;")
            else:
                    msg = QMessageBox()
                    msg.setText("Invalid username or password.")
                    msg.exec()           
                
            
                    
    def openinv(self):
                self.stackedWidget.addWidget(self.page_21)
                self.page_22 = QWidget()
                self.page_22.setObjectName(u"page_22")
                self.Inventory = QStackedWidget(self.page_22)
                self.Inventory.setObjectName(u"Inventory")
                self.Inventory.setGeometry(QRect(-90, -20, 971, 741))
                font = QFont()
                font.setPointSize(16)
                font.setBold(True)
                self.Inventory.setFont(font)
                self.Inventory.setStyleSheet(u"background-color: rgb(170, 85, 0);")
                self.DisplayForm = QWidget()
                self.DisplayForm.setObjectName(u"DisplayForm")
                self.DisplayForm.setAutoFillBackground(False)
                self.DisplayForm.setStyleSheet(u"background-color: rgb(170, 85, 0);")
                
                self.pushButton_25 = QPushButton(self.DisplayForm,clicked=lambda:self.addremprod())
                self.pushButton_25.setObjectName(u"pushButton_25")
                self.pushButton_25.setGeometry(QRect(300, 145, 168, 31))
                self.pushButton_25.setStyleSheet(u"\n"
        "	background-color:#ffffff;\n"
        "")
                self.pushButton_26 = QPushButton(self.DisplayForm,clicked=lambda:self.showInv())
                self.pushButton_26.setObjectName(u"pushButton_26")
                self.pushButton_26.setGeometry(QRect(120, 145, 168, 31))
                self.pushButton_26.setStyleSheet(u"\n"
        "	background-color:#ffffff;\n"
        "")
                self.pushButton_25.setText(QCoreApplication.translate("IMSLogin", u"Add/Remove from Inventory", None))
                self.pushButton_26.setText(QCoreApplication.translate("IMSLogin", u"Show Inventory", None))
                self.DisplayForm.show()
                
    def Accounts(self):
                self.stackedWidget.addWidget(self.page_20)
                self.page_21 = QWidget()
                self.page_21.setObjectName(u"page_21")
                self.page_21.setStyleSheet(u"background-color: rgb(170, 85, 0);")
                font = QFont()
                font.setPointSize(13)
                font.setBold(True)
                self.label = QLabel(self.page_21)
                self.label.setFont(font)
                self.label.setObjectName(u"label")
                self.label.setGeometry(QRect(60, 120, 121, 41))
                self.label.setStyleSheet(u"color: rgb(255,255,255);")
                self.lineEdit_5 = QLineEdit(self.page_21)
                self.lineEdit_5.setObjectName(u"lineEdit_5")
                self.lineEdit_5.setGeometry(QRect(290, 130, 131, 20))
                self.lineEdit_5.setStyleSheet(u"background-color: rgb(255, 255, 255);")
                self.lineEdit_6 = QLineEdit(self.page_21)
                self.lineEdit_6.setObjectName(u"lineEdit_6")
                self.lineEdit_6.setGeometry(QRect(290, 200, 133, 20))
                self.lineEdit_6.setStyleSheet(u"background-color: rgb(255, 255, 255);")
                self.pushButton_15 = QPushButton(self.page_21,clicked=lambda: self.Setnewpass())
                self.pushButton_15.setObjectName(u"pushButton_15")
                self.pushButton_15.setGeometry(QRect(170, 300, 141, 31))
                self.pushButton_15.setStyleSheet(u"background-color: rgb(255, 255, 255);")
                self.label_14 = QLabel(self.page_21)
                self.label_14.setFont(font)
                self.label_14.setObjectName(u"label_14")
                self.label_14.setGeometry(QRect(60, 190, 151, 41))
                self.label_14.setStyleSheet(u"color: rgb(255,255,255);")
                
                self.label.setText(QCoreApplication.translate("IMSLogin", u"New Password", None))
                self.label_14.setText(QCoreApplication.translate("IMSLogin", u"Confirm Password", None))
                self.pushButton_15.setText(QCoreApplication.translate("IMSLogin", u"Set New Password", None))
                #MainWindow.hide()
                self.page_21.show()
        

                
                # for row_number, row_data in enumerate(result):
                #         self.tableWidget.insertRow(row_number)
                #         for column_number, data in enumerate(row_data):
                #                 self.tableWidget.setItem(row_number, column_number,QTableWidgetItem(str(data)))        
    

    def addremprod(self):
                self.stackedWidget.addWidget(self.page_22)
                font = QFont()
                font.setPointSize(11)
                font.setBold(True)
                self.page_23 = QWidget()
                self.page_23.setObjectName(u"page_23")
                self.Inventory_2 = QStackedWidget(self.page_23)
                self.Inventory_2.setObjectName(u"Inventory_2")
                self.Inventory_2.setGeometry(QRect(-40, 10, 801, 571))
                self.Inventory_2.setFont(font)
                self.Inventory_2.setStyleSheet(u"background-color: rgb(170, 85, 0);")
                self.AddRemoveForm = QWidget()
                self.AddRemoveForm.setObjectName(u"AddRemoveForm")
                self.AddRemoveForm.setStyleSheet("background-color: rgb(170, 85, 0);")
                self.Edit_Inventory = QLabel(self.AddRemoveForm)
                self.Edit_Inventory.setObjectName(u"Edit_Inventory")
                self.Edit_Inventory.setFont(font)
                self.Edit_Inventory.setGeometry(QRect(100, 80, 161, 51))
                self.Edit_Inventory.setStyleSheet(u"#Edit_Inventory{\n"
        "	color:#ffffff;\n"
        "}")
                self.Edit_Inventory_2 = QLabel(self.AddRemoveForm)
                self.Edit_Inventory_2.setObjectName(u"Edit_Inventory_2")
                self.Edit_Inventory_2.setGeometry(QRect(100, 120, 161, 51))
                self.Edit_Inventory_2.setFont(font)
                self.Edit_Inventory_2.setStyleSheet(u"#Edit_Inventory_2{\n"
        "	color:#ffffff;\n"
        "}")
                self.Edit_Inventory_3 = QLabel(self.AddRemoveForm)
                self.Edit_Inventory_3.setObjectName(u"Edit_Inventory_3")
                self.Edit_Inventory_3.setFont(font)
                self.Edit_Inventory_3.setGeometry(QRect(100, 160, 161, 51))
                self.Edit_Inventory_3.setStyleSheet(u"#Edit_Inventory_3{\n"
        "	color:#ffffff;\n"
        "}")
                self.Edit_Inventory_4 = QLabel(self.AddRemoveForm)
                self.Edit_Inventory_4.setObjectName(u"Edit_Inventory_4")
                self.Edit_Inventory_4.setGeometry(QRect(100, 200, 161, 51))
                self.Edit_Inventory_4.setFont(font)
                self.Edit_Inventory_4.setStyleSheet(u"#Edit_Inventory_4{\n"
        "	color:#ffffff;\n"
        "}")
                self.lineEdit_17 = QLineEdit(self.AddRemoveForm)
                self.lineEdit_17.setObjectName(u"lineEdit_17")
                self.lineEdit_17.setGeometry(QRect(300, 95, 151, 23))
                self.lineEdit_17.setStyleSheet(u"\n"
        "	background-color:#ffffff;\n"
        "")
                self.lineEdit_16 = QLineEdit(self.AddRemoveForm)
                self.lineEdit_16.setObjectName(u"lineEdit_16")
                self.lineEdit_16.setGeometry(QRect(300, 135, 151, 23))
                self.lineEdit_16.setStyleSheet(u"\n"
        "	background-color:#ffffff;\n"
        "")

                self.lineEdit_p = QLineEdit(self.AddRemoveForm)
                self.lineEdit_p.setObjectName(u"lineEdit_p")
                self.lineEdit_p.setGeometry(QRect(300, 175, 151, 23))
                self.lineEdit_p.setStyleSheet(u"\n"
        "	background-color:#ffffff;\n"
        "")
                self.lineEdit_u = QLineEdit(self.AddRemoveForm)
                self.lineEdit_u.setObjectName(u"lineEdit_u")
                self.lineEdit_u.setGeometry(QRect(300, 215, 151, 23))
                self.lineEdit_u.setStyleSheet(u"\n"
        "	background-color:#ffffff;\n"
        "")
                self.pushButton_27 = QPushButton(self.AddRemoveForm,clicked=lambda:self.addtoinv())
                self.pushButton_27.setObjectName(u"pushButton_25")
                self.pushButton_27.setGeometry(QRect(100, 260, 168, 31))
                self.pushButton_27.setStyleSheet(u"\n"
"	background-color:#ffffff;\n"
"")
                self.pushButton_28 = QPushButton(self.AddRemoveForm,clicked=lambda:self.remfromInv())
                self.pushButton_28.setObjectName(u"pushButton_26")
                self.pushButton_28.setGeometry(QRect(280, 260, 168, 31))
                self.pushButton_28.setStyleSheet(u"\n"
"	background-color:#ffffff;\n"
"")
                self.Edit_Inventory.setText(QCoreApplication.translate("IMSLogin", u"Product Name", None))
                self.Edit_Inventory_2.setText(QCoreApplication.translate("IMSLogin", u"Category", None))
                self.Edit_Inventory_3.setText(QCoreApplication.translate("IMSLogin", u"Price", None))
                self.Edit_Inventory_4.setText(QCoreApplication.translate("IMSLogin", u"Units", None))
                self.pushButton_27.setText(QCoreApplication.translate("IMSLogin", u"Add to Inventory", None))
                self.pushButton_28.setText(QCoreApplication.translate("IMSLogin", u"Remove from Inventory", None))

                
                self.AddRemoveForm.show()
                self.DisplayForm.hide()
                
                
                # self.Inventory_2.addWidget(self.AddRemoveForm)
                self.stackedWidget.addWidget(self.page_23)
                self.page = QWidget()
                self.page.setObjectName(u"page")
                self.tableWidget = QTableWidget(self.page)
                if (self.tableWidget.columnCount() < 4):
                        self.tableWidget.setColumnCount(4)
                        __qtablewidgetitem = QTableWidgetItem()
                        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
                        __qtablewidgetitem1 = QTableWidgetItem()
                        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
                        __qtablewidgetitem2 = QTableWidgetItem()
                        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
                        __qtablewidgetitem3 = QTableWidgetItem()
                        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
                if (self.tableWidget.rowCount() < 13):
                        self.tableWidget.setRowCount(13)
                        __qtablewidgetitem4 = QTableWidgetItem()
                        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem4)
                        __qtablewidgetitem5 = QTableWidgetItem()
                        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem5)
                        __qtablewidgetitem6 = QTableWidgetItem()
                        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem6)
                        __qtablewidgetitem7 = QTableWidgetItem()
                        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem7)
                        __qtablewidgetitem8 = QTableWidgetItem()
                        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem8)
                        __qtablewidgetitem9 = QTableWidgetItem()
                        self.tableWidget.setVerticalHeaderItem(5, __qtablewidgetitem9)
                        __qtablewidgetitem10 = QTableWidgetItem()
                        self.tableWidget.setVerticalHeaderItem(6, __qtablewidgetitem10)
                        __qtablewidgetitem11 = QTableWidgetItem()
                        self.tableWidget.setVerticalHeaderItem(7, __qtablewidgetitem11)
                        __qtablewidgetitem12 = QTableWidgetItem()
                        self.tableWidget.setVerticalHeaderItem(8, __qtablewidgetitem12)
                        __qtablewidgetitem13 = QTableWidgetItem()
                        self.tableWidget.setVerticalHeaderItem(9, __qtablewidgetitem13)
                        __qtablewidgetitem14 = QTableWidgetItem()
                        self.tableWidget.setVerticalHeaderItem(10, __qtablewidgetitem14)
                        __qtablewidgetitem15 = QTableWidgetItem()
                        self.tableWidget.setVerticalHeaderItem(11, __qtablewidgetitem15)
                        __qtablewidgetitem16 = QTableWidgetItem()
                        self.tableWidget.setVerticalHeaderItem(12, __qtablewidgetitem16)
                        __qtablewidgetitem17 = QTableWidgetItem()
                        self.tableWidget.setItem(0, 0, __qtablewidgetitem17)
                        __qtablewidgetitem18 = QTableWidgetItem()
                        self.tableWidget.setItem(1, 0, __qtablewidgetitem18)
                        __qtablewidgetitem19 = QTableWidgetItem()
                        self.tableWidget.setItem(1, 1, __qtablewidgetitem19)
                        __qtablewidgetitem20 = QTableWidgetItem()
                        self.tableWidget.setItem(2, 0, __qtablewidgetitem20)
                self.tableWidget.setObjectName(u"tableWidget")
                self.tableWidget.setGeometry(QRect(60, 50, 451, 411))
                self.tableWidget.setStyleSheet(u"background-color: #C0C0C0;\n"
        "alternate-background-color:#606060;\n"
        "selection-background-color: #282828;")
                self.page.show()
                self.stackedWidget.addWidget(self.page)
                ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
                ___qtablewidgetitem.setText(QCoreApplication.translate("IMSLogin", u"Product", None));
                ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
                ___qtablewidgetitem1.setText(QCoreApplication.translate("IMSLogin", u"Category", None));
                ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
                ___qtablewidgetitem2.setText(QCoreApplication.translate("IMSLogin", u"Price", None));
                ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
                ___qtablewidgetitem3.setText(QCoreApplication.translate("IMSLogin", u"Units", None));

    def addtoinv(self):
                
                self.stackedWidget.addWidget(self.page_23)
                self.page = QWidget()
                self.page.setObjectName(u"page")
                self.tableWidget = QTableWidget(self.page)
                self.stackedWidget.addWidget(self.page_23)
                self.page = QWidget()
                self.page.setObjectName(u"page")
                self.tableWidget = QTableWidget(self.page)
                if (self.tableWidget.columnCount() < 4):
                        self.tableWidget.setColumnCount(4)
                        __qtablewidgetitem = QTableWidgetItem()
                        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
                        __qtablewidgetitem1 = QTableWidgetItem()
                        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
                        __qtablewidgetitem2 = QTableWidgetItem()
                        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
                        __qtablewidgetitem3 = QTableWidgetItem()
                        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
                if (self.tableWidget.rowCount() < 20):
                        self.tableWidget.setRowCount(13)
                        __qtablewidgetitem4 = QTableWidgetItem()
                        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem4)
                        __qtablewidgetitem5 = QTableWidgetItem()
                        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem5)
                        __qtablewidgetitem6 = QTableWidgetItem()
                        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem6)
                        __qtablewidgetitem7 = QTableWidgetItem()
                        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem7)
                        __qtablewidgetitem8 = QTableWidgetItem()
                        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem8)
                        __qtablewidgetitem9 = QTableWidgetItem()
                        self.tableWidget.setVerticalHeaderItem(5, __qtablewidgetitem9)
                        __qtablewidgetitem10 = QTableWidgetItem()
                        self.tableWidget.setVerticalHeaderItem(6, __qtablewidgetitem10)
                        __qtablewidgetitem11 = QTableWidgetItem()
                        self.tableWidget.setVerticalHeaderItem(7, __qtablewidgetitem11)
                        __qtablewidgetitem12 = QTableWidgetItem()
                        self.tableWidget.setVerticalHeaderItem(8, __qtablewidgetitem12)
                        __qtablewidgetitem13 = QTableWidgetItem()
                        self.tableWidget.setVerticalHeaderItem(9, __qtablewidgetitem13)
                        __qtablewidgetitem14 = QTableWidgetItem()
                        self.tableWidget.setVerticalHeaderItem(10, __qtablewidgetitem14)
                        __qtablewidgetitem15 = QTableWidgetItem()
                        self.tableWidget.setVerticalHeaderItem(11, __qtablewidgetitem15)
                        __qtablewidgetitem16 = QTableWidgetItem()
                        self.tableWidget.setVerticalHeaderItem(12, __qtablewidgetitem16)
                        __qtablewidgetitem17 = QTableWidgetItem()
                        self.tableWidget.setItem(0, 0, __qtablewidgetitem17)
                        __qtablewidgetitem18 = QTableWidgetItem()
                        self.tableWidget.setItem(1, 0, __qtablewidgetitem18)
                        __qtablewidgetitem19 = QTableWidgetItem()
                        self.tableWidget.setItem(1, 1, __qtablewidgetitem19)
                        __qtablewidgetitem20 = QTableWidgetItem()
                        self.tableWidget.setItem(2, 0, __qtablewidgetitem20)
                        self.tableWidget.setObjectName(u"tableWidget")
                        self.tableWidget.setGeometry(QRect(60, 50, 451, 411))
                        self.tableWidget.setStyleSheet(u"background-color: #C0C0C0;\n"
                "alternate-background-color:#606060;\n"
                "selection-background-color: #282828;")
                self.page.show()        
                ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
                ___qtablewidgetitem.setText(QCoreApplication.translate("IMSLogin", u"Product", None));
                ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
                ___qtablewidgetitem1.setText(QCoreApplication.translate("IMSLogin", u"Category", None));
                ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
                ___qtablewidgetitem2.setText(QCoreApplication.translate("IMSLogin", u"Price", None));
                ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
                ___qtablewidgetitem3.setText(QCoreApplication.translate("IMSLogin", u"Units", None));
                ___qtablewidgetitem4 = self.tableWidget.verticalHeaderItem(0)
                ___qtablewidgetitem4.setText(QCoreApplication.translate("IMSLogin", u"1", None));
                ___qtablewidgetitem5 = self.tableWidget.verticalHeaderItem(1)
                ___qtablewidgetitem5.setText(QCoreApplication.translate("IMSLogin", u"2", None));
                ___qtablewidgetitem6 = self.tableWidget.verticalHeaderItem(2)
                ___qtablewidgetitem6.setText(QCoreApplication.translate("IMSLogin", u"3", None));
                ___qtablewidgetitem7 = self.tableWidget.verticalHeaderItem(3)
                ___qtablewidgetitem7.setText(QCoreApplication.translate("IMSLogin", u"4", None));
                ___qtablewidgetitem8 = self.tableWidget.verticalHeaderItem(4)
                ___qtablewidgetitem8.setText(QCoreApplication.translate("IMSLogin", u"5", None));
                ___qtablewidgetitem9 = self.tableWidget.verticalHeaderItem(5)
                ___qtablewidgetitem9.setText(QCoreApplication.translate("IMSLogin", u"6", None));
                ___qtablewidgetitem10 = self.tableWidget.verticalHeaderItem(6)
                ___qtablewidgetitem10.setText(QCoreApplication.translate("IMSLogin", u"7", None));
                ___qtablewidgetitem11 = self.tableWidget.verticalHeaderItem(7)
                ___qtablewidgetitem11.setText(QCoreApplication.translate("IMSLogin", u"8", None));
                ___qtablewidgetitem12 = self.tableWidget.verticalHeaderItem(8)
                ___qtablewidgetitem12.setText(QCoreApplication.translate("IMSLogin", u"9", None));
                ___qtablewidgetitem13 = self.tableWidget.verticalHeaderItem(9)
                ___qtablewidgetitem13.setText(QCoreApplication.translate("IMSLogin", u"10", None));
                ___qtablewidgetitem14 = self.tableWidget.verticalHeaderItem(10)
                ___qtablewidgetitem14.setText(QCoreApplication.translate("IMSLogin", u"11", None));
                ___qtablewidgetitem15 = self.tableWidget.verticalHeaderItem(11)
                ___qtablewidgetitem15.setText(QCoreApplication.translate("IMSLogin", u"12", None));
                ___qtablewidgetitem16 = self.tableWidget.verticalHeaderItem(12)
                ___qtablewidgetitem16.setText(QCoreApplication.translate("IMSLogin", u"13", None));

                __sortingEnabled = self.tableWidget.isSortingEnabled()
                self.tableWidget.setSortingEnabled(False)
                self.tableWidget.setSortingEnabled(__sortingEnabled)
                self.tableWidget.setRowCount(0)
                
                curs.execute("insert into inventory(Product, Category, Price,Units) values(%s, %s, %s, %s)",(self.lineEdit_17.text(),self.lineEdit_16.text(),self.lineEdit_p.text(),self.lineEdit_u.text()))

                curs.execute("select * from inventory")
                result = curs.fetchall()                
                database.commit() 
                for row_number, row_data in enumerate(result):
                        self.tableWidget.insertRow(row_number)
                        for column_number, data in enumerate(row_data):
                                self.tableWidget.setItem(row_number, column_number,QTableWidgetItem(str(data)))        
                msg = QMessageBox()
                msg.setText("Data entered successfully.")
                msg.exec()
                
    def remfromInv(self):
                
                self.stackedWidget.addWidget(self.page_23)
                self.page = QWidget()
                self.page.setObjectName(u"page")
                self.tableWidget = QTableWidget(self.page)
                self.stackedWidget.addWidget(self.page_23)
                self.page = QWidget()
                self.page.setObjectName(u"page")
                self.tableWidget = QTableWidget(self.page)
                if (self.tableWidget.columnCount() < 4):
                        self.tableWidget.setColumnCount(4)
                        __qtablewidgetitem = QTableWidgetItem()
                        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
                        __qtablewidgetitem1 = QTableWidgetItem()
                        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
                        __qtablewidgetitem2 = QTableWidgetItem()
                        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
                        __qtablewidgetitem3 = QTableWidgetItem()
                        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
                if (self.tableWidget.rowCount() < 20):
                        self.tableWidget.setRowCount(13)
                        __qtablewidgetitem4 = QTableWidgetItem()
                        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem4)
                        __qtablewidgetitem5 = QTableWidgetItem()
                        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem5)
                        __qtablewidgetitem6 = QTableWidgetItem()
                        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem6)
                        __qtablewidgetitem7 = QTableWidgetItem()
                        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem7)
                        __qtablewidgetitem8 = QTableWidgetItem()
                        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem8)
                        __qtablewidgetitem9 = QTableWidgetItem()
                        self.tableWidget.setVerticalHeaderItem(5, __qtablewidgetitem9)
                        __qtablewidgetitem10 = QTableWidgetItem()
                        self.tableWidget.setVerticalHeaderItem(6, __qtablewidgetitem10)
                        __qtablewidgetitem11 = QTableWidgetItem()
                        self.tableWidget.setVerticalHeaderItem(7, __qtablewidgetitem11)
                        __qtablewidgetitem12 = QTableWidgetItem()
                        self.tableWidget.setVerticalHeaderItem(8, __qtablewidgetitem12)
                        __qtablewidgetitem13 = QTableWidgetItem()
                        self.tableWidget.setVerticalHeaderItem(9, __qtablewidgetitem13)
                        __qtablewidgetitem14 = QTableWidgetItem()
                        self.tableWidget.setVerticalHeaderItem(10, __qtablewidgetitem14)
                        __qtablewidgetitem15 = QTableWidgetItem()
                        self.tableWidget.setVerticalHeaderItem(11, __qtablewidgetitem15)
                        __qtablewidgetitem16 = QTableWidgetItem()
                        self.tableWidget.setVerticalHeaderItem(12, __qtablewidgetitem16)
                        __qtablewidgetitem17 = QTableWidgetItem()
                        self.tableWidget.setItem(0, 0, __qtablewidgetitem17)
                        __qtablewidgetitem18 = QTableWidgetItem()
                        self.tableWidget.setItem(1, 0, __qtablewidgetitem18)
                        __qtablewidgetitem19 = QTableWidgetItem()
                        self.tableWidget.setItem(1, 1, __qtablewidgetitem19)
                        __qtablewidgetitem20 = QTableWidgetItem()
                        self.tableWidget.setItem(2, 0, __qtablewidgetitem20)
                        self.tableWidget.setObjectName(u"tableWidget")
                        self.tableWidget.setGeometry(QRect(60, 50, 451, 411))
                        self.tableWidget.setStyleSheet(u"background-color: #C0C0C0;\n"
                "alternate-background-color:#606060;\n"
                "selection-background-color: #282828;")
                self.page.show()        
                ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
                ___qtablewidgetitem.setText(QCoreApplication.translate("IMSLogin", u"Product", None));
                ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
                ___qtablewidgetitem1.setText(QCoreApplication.translate("IMSLogin", u"Category", None));
                ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
                ___qtablewidgetitem2.setText(QCoreApplication.translate("IMSLogin", u"Price", None));
                ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
                ___qtablewidgetitem3.setText(QCoreApplication.translate("IMSLogin", u"Units", None));
                ___qtablewidgetitem4 = self.tableWidget.verticalHeaderItem(0)
                ___qtablewidgetitem4.setText(QCoreApplication.translate("IMSLogin", u"1", None));
                ___qtablewidgetitem5 = self.tableWidget.verticalHeaderItem(1)
                ___qtablewidgetitem5.setText(QCoreApplication.translate("IMSLogin", u"2", None));
                ___qtablewidgetitem6 = self.tableWidget.verticalHeaderItem(2)
                ___qtablewidgetitem6.setText(QCoreApplication.translate("IMSLogin", u"3", None));
                ___qtablewidgetitem7 = self.tableWidget.verticalHeaderItem(3)
                ___qtablewidgetitem7.setText(QCoreApplication.translate("IMSLogin", u"4", None));
                ___qtablewidgetitem8 = self.tableWidget.verticalHeaderItem(4)
                ___qtablewidgetitem8.setText(QCoreApplication.translate("IMSLogin", u"5", None));
                ___qtablewidgetitem9 = self.tableWidget.verticalHeaderItem(5)
                ___qtablewidgetitem9.setText(QCoreApplication.translate("IMSLogin", u"6", None));
                ___qtablewidgetitem10 = self.tableWidget.verticalHeaderItem(6)
                ___qtablewidgetitem10.setText(QCoreApplication.translate("IMSLogin", u"7", None));
                ___qtablewidgetitem11 = self.tableWidget.verticalHeaderItem(7)
                ___qtablewidgetitem11.setText(QCoreApplication.translate("IMSLogin", u"8", None));
                ___qtablewidgetitem12 = self.tableWidget.verticalHeaderItem(8)
                ___qtablewidgetitem12.setText(QCoreApplication.translate("IMSLogin", u"9", None));
                ___qtablewidgetitem13 = self.tableWidget.verticalHeaderItem(9)
                ___qtablewidgetitem13.setText(QCoreApplication.translate("IMSLogin", u"10", None));
                ___qtablewidgetitem14 = self.tableWidget.verticalHeaderItem(10)
                ___qtablewidgetitem14.setText(QCoreApplication.translate("IMSLogin", u"11", None));
                ___qtablewidgetitem15 = self.tableWidget.verticalHeaderItem(11)
                ___qtablewidgetitem15.setText(QCoreApplication.translate("IMSLogin", u"12", None));
                ___qtablewidgetitem16 = self.tableWidget.verticalHeaderItem(12)
                ___qtablewidgetitem16.setText(QCoreApplication.translate("IMSLogin", u"13", None));

                __sortingEnabled = self.tableWidget.isSortingEnabled()
                self.tableWidget.setSortingEnabled(False)
                self.tableWidget.setSortingEnabled(__sortingEnabled)
                self.tableWidget.setRowCount(0)
                
                curs.execute("delete from inventory where Product=%s and Category = %s and Price = %s and Units = %s limit 1",(self.lineEdit_17.text(),self.lineEdit_16.text(),self.lineEdit_p.text(),self.lineEdit_u.text()))
                print("Data deleted...")
                
                
                curs.execute("select * from inventory")
                result = curs.fetchall()                
                database.commit()
                for row_number, row_data in enumerate(result):
                        self.tableWidget.insertRow(row_number)
                        for column_number, data in enumerate(row_data):
                                self.tableWidget.setItem(row_number, column_number,QTableWidgetItem(str(data)))        

                msg = QMessageBox()
                msg.setText("Data deleted successfully.")
                msg.exec() 
                
                
    def Setnewpass(self):
                if self.lineEdit_5.text() == self.lineEdit_6.text():
                        curs.execute("update login set passw = %s",(self.lineEdit_5.text(),))
                        database.commit()
                        
                        self.page_21.hide()
                        MainWindow.hide()
                        msg = QMessageBox()
                        msg.setText("Please login again to use the app.")
                        msg.exec()                               

                        
                                                        
                else:
                        msg = QMessageBox()
                        msg.setText("Passwords don't match.")
                        msg.exec()                               

    def showInv(self):
                self.stackedWidget.addWidget(self.page_23)
                self.page = QWidget()
                self.page.setObjectName(u"page")
                self.tableWidget = QTableWidget(self.page)
                self.stackedWidget.addWidget(self.page_23)
                self.page = QWidget()
                self.page.setObjectName(u"page")
                self.tableWidget = QTableWidget(self.page)
                if (self.tableWidget.columnCount() < 4):
                        self.tableWidget.setColumnCount(4)
                        __qtablewidgetitem = QTableWidgetItem()
                        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
                        __qtablewidgetitem1 = QTableWidgetItem()
                        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
                        __qtablewidgetitem2 = QTableWidgetItem()
                        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
                        __qtablewidgetitem3 = QTableWidgetItem()
                        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
                if (self.tableWidget.rowCount() < 13):
                        self.tableWidget.setRowCount(13)
                        __qtablewidgetitem4 = QTableWidgetItem()
                        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem4)
                        __qtablewidgetitem5 = QTableWidgetItem()
                        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem5)
                        __qtablewidgetitem6 = QTableWidgetItem()
                        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem6)
                        __qtablewidgetitem7 = QTableWidgetItem()
                        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem7)
                        __qtablewidgetitem8 = QTableWidgetItem()
                        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem8)
                        __qtablewidgetitem9 = QTableWidgetItem()
                        self.tableWidget.setVerticalHeaderItem(5, __qtablewidgetitem9)
                        __qtablewidgetitem10 = QTableWidgetItem()
                        self.tableWidget.setVerticalHeaderItem(6, __qtablewidgetitem10)
                        __qtablewidgetitem11 = QTableWidgetItem()
                        self.tableWidget.setVerticalHeaderItem(7, __qtablewidgetitem11)
                        __qtablewidgetitem12 = QTableWidgetItem()
                        self.tableWidget.setVerticalHeaderItem(8, __qtablewidgetitem12)
                        __qtablewidgetitem13 = QTableWidgetItem()
                        self.tableWidget.setVerticalHeaderItem(9, __qtablewidgetitem13)
                        __qtablewidgetitem14 = QTableWidgetItem()
                        self.tableWidget.setVerticalHeaderItem(10, __qtablewidgetitem14)
                        __qtablewidgetitem15 = QTableWidgetItem()
                        self.tableWidget.setVerticalHeaderItem(11, __qtablewidgetitem15)
                        __qtablewidgetitem16 = QTableWidgetItem()
                        self.tableWidget.setVerticalHeaderItem(12, __qtablewidgetitem16)
                        __qtablewidgetitem17 = QTableWidgetItem()
                        self.tableWidget.setItem(0, 0, __qtablewidgetitem17)
                        __qtablewidgetitem18 = QTableWidgetItem()
                        self.tableWidget.setItem(1, 0, __qtablewidgetitem18)
                        __qtablewidgetitem19 = QTableWidgetItem()
                        self.tableWidget.setItem(1, 1, __qtablewidgetitem19)
                        __qtablewidgetitem20 = QTableWidgetItem()
                        self.tableWidget.setItem(2, 0, __qtablewidgetitem20)
                        self.tableWidget.setObjectName(u"tableWidget")
                        self.tableWidget.setGeometry(QRect(60, 50, 451, 411))
                        self.tableWidget.setStyleSheet(u"background-color: #C0C0C0;\n"
                "alternate-background-color:#606060;\n"
                "selection-background-color: #282828;")
                self.page.show()        
                ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
                ___qtablewidgetitem.setText(QCoreApplication.translate("IMSLogin", u"Product", None));
                ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
                ___qtablewidgetitem1.setText(QCoreApplication.translate("IMSLogin", u"Category", None));
                ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
                ___qtablewidgetitem2.setText(QCoreApplication.translate("IMSLogin", u"Price", None));
                ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
                ___qtablewidgetitem3.setText(QCoreApplication.translate("IMSLogin", u"Units", None));
                ___qtablewidgetitem4 = self.tableWidget.verticalHeaderItem(0)
                ___qtablewidgetitem4.setText(QCoreApplication.translate("IMSLogin", u"1", None));
                ___qtablewidgetitem5 = self.tableWidget.verticalHeaderItem(1)
                ___qtablewidgetitem5.setText(QCoreApplication.translate("IMSLogin", u"2", None));
                ___qtablewidgetitem6 = self.tableWidget.verticalHeaderItem(2)
                ___qtablewidgetitem6.setText(QCoreApplication.translate("IMSLogin", u"3", None));
                ___qtablewidgetitem7 = self.tableWidget.verticalHeaderItem(3)
                ___qtablewidgetitem7.setText(QCoreApplication.translate("IMSLogin", u"4", None));
                ___qtablewidgetitem8 = self.tableWidget.verticalHeaderItem(4)
                ___qtablewidgetitem8.setText(QCoreApplication.translate("IMSLogin", u"5", None));
                ___qtablewidgetitem9 = self.tableWidget.verticalHeaderItem(5)
                ___qtablewidgetitem9.setText(QCoreApplication.translate("IMSLogin", u"6", None));
                ___qtablewidgetitem10 = self.tableWidget.verticalHeaderItem(6)
                ___qtablewidgetitem10.setText(QCoreApplication.translate("IMSLogin", u"7", None));
                ___qtablewidgetitem11 = self.tableWidget.verticalHeaderItem(7)
                ___qtablewidgetitem11.setText(QCoreApplication.translate("IMSLogin", u"8", None));
                ___qtablewidgetitem12 = self.tableWidget.verticalHeaderItem(8)
                ___qtablewidgetitem12.setText(QCoreApplication.translate("IMSLogin", u"9", None));
                ___qtablewidgetitem13 = self.tableWidget.verticalHeaderItem(9)
                ___qtablewidgetitem13.setText(QCoreApplication.translate("IMSLogin", u"10", None));
                ___qtablewidgetitem14 = self.tableWidget.verticalHeaderItem(10)
                ___qtablewidgetitem14.setText(QCoreApplication.translate("IMSLogin", u"11", None));
                ___qtablewidgetitem15 = self.tableWidget.verticalHeaderItem(11)
                ___qtablewidgetitem15.setText(QCoreApplication.translate("IMSLogin", u"12", None));
                ___qtablewidgetitem16 = self.tableWidget.verticalHeaderItem(12)
                ___qtablewidgetitem16.setText(QCoreApplication.translate("IMSLogin", u"13", None));

                __sortingEnabled = self.tableWidget.isSortingEnabled()
                self.tableWidget.setSortingEnabled(False)
                self.tableWidget.setSortingEnabled(__sortingEnabled)
                self.tableWidget.setRowCount(0)
                
                curs.execute("select * from inventory")
                result = curs.fetchall()
                
                for row_number, row_data in enumerate(result):
                        self.tableWidget.insertRow(row_number)
                        for column_number, data in enumerate(row_data):
                                self.tableWidget.setItem(row_number, column_number,QTableWidgetItem(str(data)))        
                
    def showMicro(self):
                self.stackedWidget.addWidget(self.page_23)
                self.page = QWidget()
                self.page.setObjectName(u"page")
                self.tableWidget = QTableWidget(self.page)
                self.stackedWidget.addWidget(self.page_23)
                self.page = QWidget()
                self.page.setObjectName(u"page")
                self.tableWidget = QTableWidget(self.page)
                if (self.tableWidget.columnCount() < 4):
                        self.tableWidget.setColumnCount(4)
                        __qtablewidgetitem = QTableWidgetItem()
                        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
                        __qtablewidgetitem1 = QTableWidgetItem()
                        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
                        __qtablewidgetitem2 = QTableWidgetItem()
                        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
                        __qtablewidgetitem3 = QTableWidgetItem()
                        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
                if (self.tableWidget.rowCount() < 13):
                        self.tableWidget.setRowCount(13)
                        __qtablewidgetitem4 = QTableWidgetItem()
                        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem4)
                        __qtablewidgetitem5 = QTableWidgetItem()
                        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem5)
                        __qtablewidgetitem6 = QTableWidgetItem()
                        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem6)
                        __qtablewidgetitem7 = QTableWidgetItem()
                        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem7)
                        __qtablewidgetitem8 = QTableWidgetItem()
                        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem8)
                        __qtablewidgetitem9 = QTableWidgetItem()
                        self.tableWidget.setVerticalHeaderItem(5, __qtablewidgetitem9)
                        __qtablewidgetitem10 = QTableWidgetItem()
                        self.tableWidget.setVerticalHeaderItem(6, __qtablewidgetitem10)
                        __qtablewidgetitem11 = QTableWidgetItem()
                        self.tableWidget.setVerticalHeaderItem(7, __qtablewidgetitem11)
                        __qtablewidgetitem12 = QTableWidgetItem()
                        self.tableWidget.setVerticalHeaderItem(8, __qtablewidgetitem12)
                        __qtablewidgetitem13 = QTableWidgetItem()
                        self.tableWidget.setVerticalHeaderItem(9, __qtablewidgetitem13)
                        __qtablewidgetitem14 = QTableWidgetItem()
                        self.tableWidget.setVerticalHeaderItem(10, __qtablewidgetitem14)
                        __qtablewidgetitem15 = QTableWidgetItem()
                        self.tableWidget.setVerticalHeaderItem(11, __qtablewidgetitem15)
                        __qtablewidgetitem16 = QTableWidgetItem()
                        self.tableWidget.setVerticalHeaderItem(12, __qtablewidgetitem16)
                        __qtablewidgetitem17 = QTableWidgetItem()
                        self.tableWidget.setItem(0, 0, __qtablewidgetitem17)
                        __qtablewidgetitem18 = QTableWidgetItem()
                        self.tableWidget.setItem(1, 0, __qtablewidgetitem18)
                        __qtablewidgetitem19 = QTableWidgetItem()
                        self.tableWidget.setItem(1, 1, __qtablewidgetitem19)
                        __qtablewidgetitem20 = QTableWidgetItem()
                        self.tableWidget.setItem(2, 0, __qtablewidgetitem20)
                        self.tableWidget.setObjectName(u"tableWidget")
                        self.tableWidget.setGeometry(QRect(60, 50, 451, 411))
                        self.tableWidget.setStyleSheet(u"background-color: #C0C0C0;\n"
                "alternate-background-color:#606060;\n"
                "selection-background-color: #282828;")
                self.page.show()        
                ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
                ___qtablewidgetitem.setText(QCoreApplication.translate("IMSLogin", u"Product", None));
                ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
                ___qtablewidgetitem1.setText(QCoreApplication.translate("IMSLogin", u"Category", None));
                ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
                ___qtablewidgetitem2.setText(QCoreApplication.translate("IMSLogin", u"Price", None));
                ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
                ___qtablewidgetitem3.setText(QCoreApplication.translate("IMSLogin", u"Units", None));
                ___qtablewidgetitem4 = self.tableWidget.verticalHeaderItem(0)
                ___qtablewidgetitem4.setText(QCoreApplication.translate("IMSLogin", u"1", None));
                ___qtablewidgetitem5 = self.tableWidget.verticalHeaderItem(1)
                ___qtablewidgetitem5.setText(QCoreApplication.translate("IMSLogin", u"2", None));
                ___qtablewidgetitem6 = self.tableWidget.verticalHeaderItem(2)
                ___qtablewidgetitem6.setText(QCoreApplication.translate("IMSLogin", u"3", None));
                ___qtablewidgetitem7 = self.tableWidget.verticalHeaderItem(3)
                ___qtablewidgetitem7.setText(QCoreApplication.translate("IMSLogin", u"4", None));
                ___qtablewidgetitem8 = self.tableWidget.verticalHeaderItem(4)
                ___qtablewidgetitem8.setText(QCoreApplication.translate("IMSLogin", u"5", None));
                ___qtablewidgetitem9 = self.tableWidget.verticalHeaderItem(5)
                ___qtablewidgetitem9.setText(QCoreApplication.translate("IMSLogin", u"6", None));
                ___qtablewidgetitem10 = self.tableWidget.verticalHeaderItem(6)
                ___qtablewidgetitem10.setText(QCoreApplication.translate("IMSLogin", u"7", None));
                ___qtablewidgetitem11 = self.tableWidget.verticalHeaderItem(7)
                ___qtablewidgetitem11.setText(QCoreApplication.translate("IMSLogin", u"8", None));
                ___qtablewidgetitem12 = self.tableWidget.verticalHeaderItem(8)
                ___qtablewidgetitem12.setText(QCoreApplication.translate("IMSLogin", u"9", None));
                ___qtablewidgetitem13 = self.tableWidget.verticalHeaderItem(9)
                ___qtablewidgetitem13.setText(QCoreApplication.translate("IMSLogin", u"10", None));
                ___qtablewidgetitem14 = self.tableWidget.verticalHeaderItem(10)
                ___qtablewidgetitem14.setText(QCoreApplication.translate("IMSLogin", u"11", None));
                ___qtablewidgetitem15 = self.tableWidget.verticalHeaderItem(11)
                ___qtablewidgetitem15.setText(QCoreApplication.translate("IMSLogin", u"12", None));
                ___qtablewidgetitem16 = self.tableWidget.verticalHeaderItem(12)
                ___qtablewidgetitem16.setText(QCoreApplication.translate("IMSLogin", u"13", None));

                __sortingEnabled = self.tableWidget.isSortingEnabled()
                self.tableWidget.setSortingEnabled(False)
                self.tableWidget.setSortingEnabled(__sortingEnabled)
                self.tableWidget.setRowCount(0)
                
                curs.execute("select * from microcontroller")
                result = curs.fetchall()
                
                for row_number, row_data in enumerate(result):
                        self.tableWidget.insertRow(row_number)
                        for column_number, data in enumerate(row_data):
                                self.tableWidget.setItem(row_number, column_number,QTableWidgetItem(str(data)))        
     
    def showPrinters(self):
                self.stackedWidget.addWidget(self.page_23)
                self.page = QWidget()
                self.page.setObjectName(u"page")
                self.tableWidget = QTableWidget(self.page)
                self.stackedWidget.addWidget(self.page_23)
                self.page = QWidget()
                self.page.setObjectName(u"page")
                self.tableWidget = QTableWidget(self.page)
                if (self.tableWidget.columnCount() < 4):
                        self.tableWidget.setColumnCount(4)
                        __qtablewidgetitem = QTableWidgetItem()
                        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
                        __qtablewidgetitem1 = QTableWidgetItem()
                        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
                        __qtablewidgetitem2 = QTableWidgetItem()
                        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
                        __qtablewidgetitem3 = QTableWidgetItem()
                        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
                if (self.tableWidget.rowCount() < 13):
                        self.tableWidget.setRowCount(13)
                        __qtablewidgetitem4 = QTableWidgetItem()
                        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem4)
                        __qtablewidgetitem5 = QTableWidgetItem()
                        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem5)
                        __qtablewidgetitem6 = QTableWidgetItem()
                        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem6)
                        __qtablewidgetitem7 = QTableWidgetItem()
                        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem7)
                        __qtablewidgetitem8 = QTableWidgetItem()
                        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem8)
                        __qtablewidgetitem9 = QTableWidgetItem()
                        self.tableWidget.setVerticalHeaderItem(5, __qtablewidgetitem9)
                        __qtablewidgetitem10 = QTableWidgetItem()
                        self.tableWidget.setVerticalHeaderItem(6, __qtablewidgetitem10)
                        __qtablewidgetitem11 = QTableWidgetItem()
                        self.tableWidget.setVerticalHeaderItem(7, __qtablewidgetitem11)
                        __qtablewidgetitem12 = QTableWidgetItem()
                        self.tableWidget.setVerticalHeaderItem(8, __qtablewidgetitem12)
                        __qtablewidgetitem13 = QTableWidgetItem()
                        self.tableWidget.setVerticalHeaderItem(9, __qtablewidgetitem13)
                        __qtablewidgetitem14 = QTableWidgetItem()
                        self.tableWidget.setVerticalHeaderItem(10, __qtablewidgetitem14)
                        __qtablewidgetitem15 = QTableWidgetItem()
                        self.tableWidget.setVerticalHeaderItem(11, __qtablewidgetitem15)
                        __qtablewidgetitem16 = QTableWidgetItem()
                        self.tableWidget.setVerticalHeaderItem(12, __qtablewidgetitem16)
                        __qtablewidgetitem17 = QTableWidgetItem()
                        self.tableWidget.setItem(0, 0, __qtablewidgetitem17)
                        __qtablewidgetitem18 = QTableWidgetItem()
                        self.tableWidget.setItem(1, 0, __qtablewidgetitem18)
                        __qtablewidgetitem19 = QTableWidgetItem()
                        self.tableWidget.setItem(1, 1, __qtablewidgetitem19)
                        __qtablewidgetitem20 = QTableWidgetItem()
                        self.tableWidget.setItem(2, 0, __qtablewidgetitem20)
                        self.tableWidget.setObjectName(u"tableWidget")
                        self.tableWidget.setGeometry(QRect(60, 50, 451, 411))
                        self.tableWidget.setStyleSheet(u"background-color: #C0C0C0;\n"
                "alternate-background-color:#606060;\n"
                "selection-background-color: #282828;")
                self.page.show()        
                ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
                ___qtablewidgetitem.setText(QCoreApplication.translate("IMSLogin", u"Product", None));
                ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
                ___qtablewidgetitem1.setText(QCoreApplication.translate("IMSLogin", u"Category", None));
                ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
                ___qtablewidgetitem2.setText(QCoreApplication.translate("IMSLogin", u"Price", None));
                ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
                ___qtablewidgetitem3.setText(QCoreApplication.translate("IMSLogin", u"Units", None));
                ___qtablewidgetitem4 = self.tableWidget.verticalHeaderItem(0)
                ___qtablewidgetitem4.setText(QCoreApplication.translate("IMSLogin", u"1", None));
                ___qtablewidgetitem5 = self.tableWidget.verticalHeaderItem(1)
                ___qtablewidgetitem5.setText(QCoreApplication.translate("IMSLogin", u"2", None));
                ___qtablewidgetitem6 = self.tableWidget.verticalHeaderItem(2)
                ___qtablewidgetitem6.setText(QCoreApplication.translate("IMSLogin", u"3", None));
                ___qtablewidgetitem7 = self.tableWidget.verticalHeaderItem(3)
                ___qtablewidgetitem7.setText(QCoreApplication.translate("IMSLogin", u"4", None));
                ___qtablewidgetitem8 = self.tableWidget.verticalHeaderItem(4)
                ___qtablewidgetitem8.setText(QCoreApplication.translate("IMSLogin", u"5", None));
                ___qtablewidgetitem9 = self.tableWidget.verticalHeaderItem(5)
                ___qtablewidgetitem9.setText(QCoreApplication.translate("IMSLogin", u"6", None));
                ___qtablewidgetitem10 = self.tableWidget.verticalHeaderItem(6)
                ___qtablewidgetitem10.setText(QCoreApplication.translate("IMSLogin", u"7", None));
                ___qtablewidgetitem11 = self.tableWidget.verticalHeaderItem(7)
                ___qtablewidgetitem11.setText(QCoreApplication.translate("IMSLogin", u"8", None));
                ___qtablewidgetitem12 = self.tableWidget.verticalHeaderItem(8)
                ___qtablewidgetitem12.setText(QCoreApplication.translate("IMSLogin", u"9", None));
                ___qtablewidgetitem13 = self.tableWidget.verticalHeaderItem(9)
                ___qtablewidgetitem13.setText(QCoreApplication.translate("IMSLogin", u"10", None));
                ___qtablewidgetitem14 = self.tableWidget.verticalHeaderItem(10)
                ___qtablewidgetitem14.setText(QCoreApplication.translate("IMSLogin", u"11", None));
                ___qtablewidgetitem15 = self.tableWidget.verticalHeaderItem(11)
                ___qtablewidgetitem15.setText(QCoreApplication.translate("IMSLogin", u"12", None));
                ___qtablewidgetitem16 = self.tableWidget.verticalHeaderItem(12)
                ___qtablewidgetitem16.setText(QCoreApplication.translate("IMSLogin", u"13", None));

                __sortingEnabled = self.tableWidget.isSortingEnabled()
                self.tableWidget.setSortingEnabled(False)
                self.tableWidget.setSortingEnabled(__sortingEnabled)
                self.tableWidget.setRowCount(0)
                
                curs.execute("select * from printers")
                result = curs.fetchall()
                
                for row_number, row_data in enumerate(result):
                        self.tableWidget.insertRow(row_number)
                        for column_number, data in enumerate(row_data):
                                self.tableWidget.setItem(row_number, column_number,QTableWidgetItem(str(data)))        
     

    def showSensors(self):
                self.stackedWidget.addWidget(self.page_23)
                self.page = QWidget()
                self.page.setObjectName(u"page")
                self.tableWidget = QTableWidget(self.page)
                self.stackedWidget.addWidget(self.page_23)
                self.page = QWidget()
                self.page.setObjectName(u"page")
                self.tableWidget = QTableWidget(self.page)
                if (self.tableWidget.columnCount() < 4):
                        self.tableWidget.setColumnCount(4)
                        __qtablewidgetitem = QTableWidgetItem()
                        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
                        __qtablewidgetitem1 = QTableWidgetItem()
                        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
                        __qtablewidgetitem2 = QTableWidgetItem()
                        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
                        __qtablewidgetitem3 = QTableWidgetItem()
                        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
                if (self.tableWidget.rowCount() < 13):
                        self.tableWidget.setRowCount(13)
                        __qtablewidgetitem4 = QTableWidgetItem()
                        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem4)
                        __qtablewidgetitem5 = QTableWidgetItem()
                        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem5)
                        __qtablewidgetitem6 = QTableWidgetItem()
                        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem6)
                        __qtablewidgetitem7 = QTableWidgetItem()
                        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem7)
                        __qtablewidgetitem8 = QTableWidgetItem()
                        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem8)
                        __qtablewidgetitem9 = QTableWidgetItem()
                        self.tableWidget.setVerticalHeaderItem(5, __qtablewidgetitem9)
                        __qtablewidgetitem10 = QTableWidgetItem()
                        self.tableWidget.setVerticalHeaderItem(6, __qtablewidgetitem10)
                        __qtablewidgetitem11 = QTableWidgetItem()
                        self.tableWidget.setVerticalHeaderItem(7, __qtablewidgetitem11)
                        __qtablewidgetitem12 = QTableWidgetItem()
                        self.tableWidget.setVerticalHeaderItem(8, __qtablewidgetitem12)
                        __qtablewidgetitem13 = QTableWidgetItem()
                        self.tableWidget.setVerticalHeaderItem(9, __qtablewidgetitem13)
                        __qtablewidgetitem14 = QTableWidgetItem()
                        self.tableWidget.setVerticalHeaderItem(10, __qtablewidgetitem14)
                        __qtablewidgetitem15 = QTableWidgetItem()
                        self.tableWidget.setVerticalHeaderItem(11, __qtablewidgetitem15)
                        __qtablewidgetitem16 = QTableWidgetItem()
                        self.tableWidget.setVerticalHeaderItem(12, __qtablewidgetitem16)
                        __qtablewidgetitem17 = QTableWidgetItem()
                        self.tableWidget.setItem(0, 0, __qtablewidgetitem17)
                        __qtablewidgetitem18 = QTableWidgetItem()
                        self.tableWidget.setItem(1, 0, __qtablewidgetitem18)
                        __qtablewidgetitem19 = QTableWidgetItem()
                        self.tableWidget.setItem(1, 1, __qtablewidgetitem19)
                        __qtablewidgetitem20 = QTableWidgetItem()
                        self.tableWidget.setItem(2, 0, __qtablewidgetitem20)
                        self.tableWidget.setObjectName(u"tableWidget")
                        self.tableWidget.setGeometry(QRect(60, 50, 451, 411))
                        self.tableWidget.setStyleSheet(u"background-color: #C0C0C0;\n"
                "alternate-background-color:#606060;\n"
                "selection-background-color: #282828;")
                self.page.show()        
                ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
                ___qtablewidgetitem.setText(QCoreApplication.translate("IMSLogin", u"Product", None));
                ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
                ___qtablewidgetitem1.setText(QCoreApplication.translate("IMSLogin", u"Category", None));
                ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
                ___qtablewidgetitem2.setText(QCoreApplication.translate("IMSLogin", u"Price", None));
                ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
                ___qtablewidgetitem3.setText(QCoreApplication.translate("IMSLogin", u"Units", None));
                ___qtablewidgetitem4 = self.tableWidget.verticalHeaderItem(0)
                ___qtablewidgetitem4.setText(QCoreApplication.translate("IMSLogin", u"1", None));
                ___qtablewidgetitem5 = self.tableWidget.verticalHeaderItem(1)
                ___qtablewidgetitem5.setText(QCoreApplication.translate("IMSLogin", u"2", None));
                ___qtablewidgetitem6 = self.tableWidget.verticalHeaderItem(2)
                ___qtablewidgetitem6.setText(QCoreApplication.translate("IMSLogin", u"3", None));
                ___qtablewidgetitem7 = self.tableWidget.verticalHeaderItem(3)
                ___qtablewidgetitem7.setText(QCoreApplication.translate("IMSLogin", u"4", None));
                ___qtablewidgetitem8 = self.tableWidget.verticalHeaderItem(4)
                ___qtablewidgetitem8.setText(QCoreApplication.translate("IMSLogin", u"5", None));
                ___qtablewidgetitem9 = self.tableWidget.verticalHeaderItem(5)
                ___qtablewidgetitem9.setText(QCoreApplication.translate("IMSLogin", u"6", None));
                ___qtablewidgetitem10 = self.tableWidget.verticalHeaderItem(6)
                ___qtablewidgetitem10.setText(QCoreApplication.translate("IMSLogin", u"7", None));
                ___qtablewidgetitem11 = self.tableWidget.verticalHeaderItem(7)
                ___qtablewidgetitem11.setText(QCoreApplication.translate("IMSLogin", u"8", None));
                ___qtablewidgetitem12 = self.tableWidget.verticalHeaderItem(8)
                ___qtablewidgetitem12.setText(QCoreApplication.translate("IMSLogin", u"9", None));
                ___qtablewidgetitem13 = self.tableWidget.verticalHeaderItem(9)
                ___qtablewidgetitem13.setText(QCoreApplication.translate("IMSLogin", u"10", None));
                ___qtablewidgetitem14 = self.tableWidget.verticalHeaderItem(10)
                ___qtablewidgetitem14.setText(QCoreApplication.translate("IMSLogin", u"11", None));
                ___qtablewidgetitem15 = self.tableWidget.verticalHeaderItem(11)
                ___qtablewidgetitem15.setText(QCoreApplication.translate("IMSLogin", u"12", None));
                ___qtablewidgetitem16 = self.tableWidget.verticalHeaderItem(12)
                ___qtablewidgetitem16.setText(QCoreApplication.translate("IMSLogin", u"13", None));

                __sortingEnabled = self.tableWidget.isSortingEnabled()
                self.tableWidget.setSortingEnabled(False)
                self.tableWidget.setSortingEnabled(__sortingEnabled)
                self.tableWidget.setRowCount(0)
                
                curs.execute("select * from sensors")
                result = curs.fetchall()
                
                for row_number, row_data in enumerate(result):
                        self.tableWidget.insertRow(row_number)
                        for column_number, data in enumerate(row_data):
                                self.tableWidget.setItem(row_number, column_number,QTableWidgetItem(str(data)))        
     
    def showTransformers(self):
                self.stackedWidget.addWidget(self.page_23)
                self.page = QWidget()
                self.page.setObjectName(u"page")
                self.tableWidget = QTableWidget(self.page)
                self.stackedWidget.addWidget(self.page_23)
                self.page = QWidget()
                self.page.setObjectName(u"page")
                self.tableWidget = QTableWidget(self.page)
                if (self.tableWidget.columnCount() < 4):
                        self.tableWidget.setColumnCount(4)
                        __qtablewidgetitem = QTableWidgetItem()
                        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
                        __qtablewidgetitem1 = QTableWidgetItem()
                        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
                        __qtablewidgetitem2 = QTableWidgetItem()
                        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
                        __qtablewidgetitem3 = QTableWidgetItem()
                        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
                if (self.tableWidget.rowCount() < 13):
                        self.tableWidget.setRowCount(13)
                        __qtablewidgetitem4 = QTableWidgetItem()
                        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem4)
                        __qtablewidgetitem5 = QTableWidgetItem()
                        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem5)
                        __qtablewidgetitem6 = QTableWidgetItem()
                        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem6)
                        __qtablewidgetitem7 = QTableWidgetItem()
                        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem7)
                        __qtablewidgetitem8 = QTableWidgetItem()
                        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem8)
                        __qtablewidgetitem9 = QTableWidgetItem()
                        self.tableWidget.setVerticalHeaderItem(5, __qtablewidgetitem9)
                        __qtablewidgetitem10 = QTableWidgetItem()
                        self.tableWidget.setVerticalHeaderItem(6, __qtablewidgetitem10)
                        __qtablewidgetitem11 = QTableWidgetItem()
                        self.tableWidget.setVerticalHeaderItem(7, __qtablewidgetitem11)
                        __qtablewidgetitem12 = QTableWidgetItem()
                        self.tableWidget.setVerticalHeaderItem(8, __qtablewidgetitem12)
                        __qtablewidgetitem13 = QTableWidgetItem()
                        self.tableWidget.setVerticalHeaderItem(9, __qtablewidgetitem13)
                        __qtablewidgetitem14 = QTableWidgetItem()
                        self.tableWidget.setVerticalHeaderItem(10, __qtablewidgetitem14)
                        __qtablewidgetitem15 = QTableWidgetItem()
                        self.tableWidget.setVerticalHeaderItem(11, __qtablewidgetitem15)
                        __qtablewidgetitem16 = QTableWidgetItem()
                        self.tableWidget.setVerticalHeaderItem(12, __qtablewidgetitem16)
                        __qtablewidgetitem17 = QTableWidgetItem()
                        self.tableWidget.setItem(0, 0, __qtablewidgetitem17)
                        __qtablewidgetitem18 = QTableWidgetItem()
                        self.tableWidget.setItem(1, 0, __qtablewidgetitem18)
                        __qtablewidgetitem19 = QTableWidgetItem()
                        self.tableWidget.setItem(1, 1, __qtablewidgetitem19)
                        __qtablewidgetitem20 = QTableWidgetItem()
                        self.tableWidget.setItem(2, 0, __qtablewidgetitem20)
                        self.tableWidget.setObjectName(u"tableWidget")
                        self.tableWidget.setGeometry(QRect(60, 50, 451, 411))
                        self.tableWidget.setStyleSheet(u"background-color: #C0C0C0;\n"
                "alternate-background-color:#606060;\n"
                "selection-background-color: #282828;")
                self.page.show()        
                ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
                ___qtablewidgetitem.setText(QCoreApplication.translate("IMSLogin", u"Product", None));
                ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
                ___qtablewidgetitem1.setText(QCoreApplication.translate("IMSLogin", u"Category", None));
                ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
                ___qtablewidgetitem2.setText(QCoreApplication.translate("IMSLogin", u"Price", None));
                ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
                ___qtablewidgetitem3.setText(QCoreApplication.translate("IMSLogin", u"Units", None));
                ___qtablewidgetitem4 = self.tableWidget.verticalHeaderItem(0)
                ___qtablewidgetitem4.setText(QCoreApplication.translate("IMSLogin", u"1", None));
                ___qtablewidgetitem5 = self.tableWidget.verticalHeaderItem(1)
                ___qtablewidgetitem5.setText(QCoreApplication.translate("IMSLogin", u"2", None));
                ___qtablewidgetitem6 = self.tableWidget.verticalHeaderItem(2)
                ___qtablewidgetitem6.setText(QCoreApplication.translate("IMSLogin", u"3", None));
                ___qtablewidgetitem7 = self.tableWidget.verticalHeaderItem(3)
                ___qtablewidgetitem7.setText(QCoreApplication.translate("IMSLogin", u"4", None));
                ___qtablewidgetitem8 = self.tableWidget.verticalHeaderItem(4)
                ___qtablewidgetitem8.setText(QCoreApplication.translate("IMSLogin", u"5", None));
                ___qtablewidgetitem9 = self.tableWidget.verticalHeaderItem(5)
                ___qtablewidgetitem9.setText(QCoreApplication.translate("IMSLogin", u"6", None));
                ___qtablewidgetitem10 = self.tableWidget.verticalHeaderItem(6)
                ___qtablewidgetitem10.setText(QCoreApplication.translate("IMSLogin", u"7", None));
                ___qtablewidgetitem11 = self.tableWidget.verticalHeaderItem(7)
                ___qtablewidgetitem11.setText(QCoreApplication.translate("IMSLogin", u"8", None));
                ___qtablewidgetitem12 = self.tableWidget.verticalHeaderItem(8)
                ___qtablewidgetitem12.setText(QCoreApplication.translate("IMSLogin", u"9", None));
                ___qtablewidgetitem13 = self.tableWidget.verticalHeaderItem(9)
                ___qtablewidgetitem13.setText(QCoreApplication.translate("IMSLogin", u"10", None));
                ___qtablewidgetitem14 = self.tableWidget.verticalHeaderItem(10)
                ___qtablewidgetitem14.setText(QCoreApplication.translate("IMSLogin", u"11", None));
                ___qtablewidgetitem15 = self.tableWidget.verticalHeaderItem(11)
                ___qtablewidgetitem15.setText(QCoreApplication.translate("IMSLogin", u"12", None));
                ___qtablewidgetitem16 = self.tableWidget.verticalHeaderItem(12)
                ___qtablewidgetitem16.setText(QCoreApplication.translate("IMSLogin", u"13", None));

                __sortingEnabled = self.tableWidget.isSortingEnabled()
                self.tableWidget.setSortingEnabled(False)
                self.tableWidget.setSortingEnabled(__sortingEnabled)
                self.tableWidget.setRowCount(0)
                
                curs.execute("select * from transformers")
                result = curs.fetchall()
                
                for row_number, row_data in enumerate(result):
                        self.tableWidget.insertRow(row_number)
                        for column_number, data in enumerate(row_data):
                                self.tableWidget.setItem(row_number, column_number,QTableWidgetItem(str(data)))        
     
         
import sys
app = QApplication(sys.argv) 
MainWindow = QMainWindow()
ui = Ui_IMSLogin()
ui.setupUi(MainWindow)
MainWindow.showNormal()
app.exec()
