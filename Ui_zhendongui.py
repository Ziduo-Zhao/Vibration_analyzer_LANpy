# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'g:\24,ADS131CODE\6.zhendongpu\20220220\Vibration_analyzer_LANpy\zhendongui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1024, 760)
        Dialog.setStyleSheet("\n"
"background-color: rgb(244, 244, 244);")
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1024, 760))
        self.tabWidget.setIconSize(QtCore.QSize(20, 20))
        self.tabWidget.setObjectName("tabWidget")
        self.widget = QtWidgets.QWidget()
        self.widget.setObjectName("widget")
        self.groupBox = QtWidgets.QGroupBox(self.widget)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 481, 71))
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(12)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 30, 101, 31))
        self.label.setObjectName("label")
        self.IPADDR = QtWidgets.QTextEdit(self.groupBox)
        self.IPADDR.setGeometry(QtCore.QRect(90, 30, 191, 31))
        self.IPADDR.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.IPADDR.setObjectName("IPADDR")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(290, 30, 91, 31))
        self.label_2.setObjectName("label_2")
        self.IPPORT = QtWidgets.QTextEdit(self.groupBox)
        self.IPPORT.setGeometry(QtCore.QRect(360, 30, 104, 31))
        self.IPPORT.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.IPPORT.setObjectName("IPPORT")
        self.groupBox_2 = QtWidgets.QGroupBox(self.widget)
        self.groupBox_2.setGeometry(QtCore.QRect(520, 10, 261, 71))
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(12)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.CONNECT = QtWidgets.QPushButton(self.groupBox_2)
        self.CONNECT.setGeometry(QtCore.QRect(130, 30, 121, 31))
        font = QtGui.QFont()
        font.setFamily("SimSun")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.CONNECT.setFont(font)
        self.CONNECT.setObjectName("CONNECT")
        self.CONSTA = QtWidgets.QTextBrowser(self.groupBox_2)
        self.CONSTA.setGeometry(QtCore.QRect(15, 31, 111, 31))
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(12)
        self.CONSTA.setFont(font)
        self.CONSTA.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.CONSTA.setObjectName("CONSTA")
        self.groupBox_3 = QtWidgets.QGroupBox(self.widget)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 90, 761, 91))
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(12)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.STASAM = QtWidgets.QPushButton(self.groupBox_3)
        self.STASAM.setGeometry(QtCore.QRect(640, 30, 111, 41))
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.STASAM.setFont(font)
        self.STASAM.setStyleSheet("")
        self.STASAM.setObjectName("STASAM")
        self.SAMQUE = QtWidgets.QPushButton(self.groupBox_3)
        self.SAMQUE.setGeometry(QtCore.QRect(10, 30, 111, 41))
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(13)
        self.SAMQUE.setFont(font)
        self.SAMQUE.setObjectName("SAMQUE")
        self.SAMSET = QtWidgets.QPushButton(self.groupBox_3)
        self.SAMSET.setGeometry(QtCore.QRect(150, 30, 111, 41))
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(13)
        self.SAMSET.setFont(font)
        self.SAMSET.setObjectName("SAMSET")
        self.SAMDATA = QtWidgets.QTextEdit(self.groupBox_3)
        self.SAMDATA.setGeometry(QtCore.QRect(260, 30, 104, 41))
        self.SAMDATA.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.SAMDATA.setObjectName("SAMDATA")
        self.FFTSET = QtWidgets.QPushButton(self.groupBox_3)
        self.FFTSET.setGeometry(QtCore.QRect(370, 30, 151, 41))
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(13)
        self.FFTSET.setFont(font)
        self.FFTSET.setObjectName("FFTSET")
        self.FFTVAL = QtWidgets.QTextEdit(self.groupBox_3)
        self.FFTVAL.setGeometry(QtCore.QRect(520, 30, 104, 41))
        self.FFTVAL.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.FFTVAL.setObjectName("FFTVAL")
        self.groupBox_4 = QtWidgets.QGroupBox(self.widget)
        self.groupBox_4.setGeometry(QtCore.QRect(20, 200, 761, 371))
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(12)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName("groupBox_4")
        self.MESSAGESHOW = QtWidgets.QTextBrowser(self.groupBox_4)
        self.MESSAGESHOW.setGeometry(QtCore.QRect(10, 30, 741, 291))
        self.MESSAGESHOW.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.MESSAGESHOW.setObjectName("MESSAGESHOW")
        self.CLEARMESSAGE = QtWidgets.QPushButton(self.groupBox_4)
        self.CLEARMESSAGE.setGeometry(QtCore.QRect(570, 325, 171, 41))
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(16)
        self.CLEARMESSAGE.setFont(font)
        self.CLEARMESSAGE.setObjectName("CLEARMESSAGE")
        self.groupBox_5 = QtWidgets.QGroupBox(self.widget)
        self.groupBox_5.setGeometry(QtCore.QRect(799, 10, 211, 561))
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(12)
        self.groupBox_5.setFont(font)
        self.groupBox_5.setObjectName("groupBox_5")
        self.OUTSWITCH = QtWidgets.QComboBox(self.groupBox_5)
        self.OUTSWITCH.setGeometry(QtCore.QRect(10, 115, 131, 31))
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(16)
        self.OUTSWITCH.setFont(font)
        self.OUTSWITCH.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.OUTSWITCH.setObjectName("OUTSWITCH")
        self.OUTSWITCH.addItem("")
        self.OUTSWITCH.addItem("")
        self.OUTSWITCH.addItem("")
        self.OUTSWITCHSET = QtWidgets.QPushButton(self.groupBox_5)
        self.OUTSWITCHSET.setGeometry(QtCore.QRect(150, 110, 51, 41))
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(12)
        self.OUTSWITCHSET.setFont(font)
        self.OUTSWITCHSET.setObjectName("OUTSWITCHSET")
        self.WAVESELECT = QtWidgets.QComboBox(self.groupBox_5)
        self.WAVESELECT.setGeometry(QtCore.QRect(10, 190, 191, 31))
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(16)
        self.WAVESELECT.setFont(font)
        self.WAVESELECT.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.WAVESELECT.setObjectName("WAVESELECT")
        self.WAVESELECT.addItem("")
        self.WAVESELECT.addItem("")
        self.WAVESELECT.addItem("")
        self.label_3 = QtWidgets.QLabel(self.groupBox_5)
        self.label_3.setGeometry(QtCore.QRect(10, 230, 151, 31))
        self.label_3.setObjectName("label_3")
        self.OUTVPP = QtWidgets.QTextEdit(self.groupBox_5)
        self.OUTVPP.setGeometry(QtCore.QRect(10, 260, 191, 41))
        self.OUTVPP.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.OUTVPP.setObjectName("OUTVPP")
        self.label_4 = QtWidgets.QLabel(self.groupBox_5)
        self.label_4.setGeometry(QtCore.QRect(11, 314, 141, 31))
        self.label_4.setObjectName("label_4")
        self.OUTFREQ = QtWidgets.QTextEdit(self.groupBox_5)
        self.OUTFREQ.setGeometry(QtCore.QRect(10, 345, 191, 41))
        self.OUTFREQ.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.OUTFREQ.setObjectName("OUTFREQ")
        self.label_5 = QtWidgets.QLabel(self.groupBox_5)
        self.label_5.setGeometry(QtCore.QRect(10, 400, 121, 31))
        self.label_5.setObjectName("label_5")
        self.OUTTIME = QtWidgets.QTextEdit(self.groupBox_5)
        self.OUTTIME.setGeometry(QtCore.QRect(10, 430, 191, 41))
        self.OUTTIME.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.OUTTIME.setObjectName("OUTTIME")
        self.OUTENABLE = QtWidgets.QPushButton(self.groupBox_5)
        self.OUTENABLE.setGeometry(QtCore.QRect(20, 490, 171, 51))
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.OUTENABLE.setFont(font)
        self.OUTENABLE.setStyleSheet("")
        self.OUTENABLE.setObjectName("OUTENABLE")
        self.OUTQUE = QtWidgets.QPushButton(self.groupBox_5)
        self.OUTQUE.setGeometry(QtCore.QRect(20, 40, 171, 51))
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.OUTQUE.setFont(font)
        self.OUTQUE.setStyleSheet("")
        self.OUTQUE.setObjectName("OUTQUE")
        self.label_10 = QtWidgets.QLabel(self.groupBox_5)
        self.label_10.setGeometry(QtCore.QRect(10, 160, 151, 31))
        self.label_10.setObjectName("label_10")
        self.groupBox_7 = QtWidgets.QGroupBox(self.widget)
        self.groupBox_7.setGeometry(QtCore.QRect(20, 650, 991, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox_7.setFont(font)
        self.groupBox_7.setObjectName("groupBox_7")
        self.IN2SWITCH = QtWidgets.QComboBox(self.groupBox_7)
        self.IN2SWITCH.setGeometry(QtCore.QRect(20, 30, 101, 31))
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(16)
        self.IN2SWITCH.setFont(font)
        self.IN2SWITCH.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.IN2SWITCH.setObjectName("IN2SWITCH")
        self.IN2SWITCH.addItem("")
        self.IN2SWITCH.addItem("")
        self.IN2ACDC = QtWidgets.QComboBox(self.groupBox_7)
        self.IN2ACDC.setGeometry(QtCore.QRect(140, 30, 101, 31))
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(16)
        self.IN2ACDC.setFont(font)
        self.IN2ACDC.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.IN2ACDC.setObjectName("IN2ACDC")
        self.IN2ACDC.addItem("")
        self.IN2ACDC.addItem("")
        self.IN2SW = QtWidgets.QComboBox(self.groupBox_7)
        self.IN2SW.setGeometry(QtCore.QRect(260, 30, 101, 31))
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(16)
        self.IN2SW.setFont(font)
        self.IN2SW.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.IN2SW.setObjectName("IN2SW")
        self.IN2SW.addItem("")
        self.IN2SW.addItem("")
        self.IN2IEPE = QtWidgets.QComboBox(self.groupBox_7)
        self.IN2IEPE.setGeometry(QtCore.QRect(450, 30, 101, 31))
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(16)
        self.IN2IEPE.setFont(font)
        self.IN2IEPE.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.IN2IEPE.setObjectName("IN2IEPE")
        self.IN2IEPE.addItem("")
        self.IN2IEPE.addItem("")
        self.IN2IEPE.addItem("")
        self.IN2GAIN = QtWidgets.QComboBox(self.groupBox_7)
        self.IN2GAIN.setGeometry(QtCore.QRect(630, 30, 101, 31))
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(16)
        self.IN2GAIN.setFont(font)
        self.IN2GAIN.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.IN2GAIN.setObjectName("IN2GAIN")
        self.IN2GAIN.addItem("")
        self.IN2GAIN.addItem("")
        self.IN2GAIN.addItem("")
        self.IN2GAIN.addItem("")
        self.IN2GAIN.addItem("")
        self.IN2GAIN.addItem("")
        self.IN2GAIN.addItem("")
        self.IN2GAIN.addItem("")
        self.IN2GAIN.addItem("")
        self.IN2GAIN.addItem("")
        self.IN2GAIN.addItem("")
        self.IN2GAIN.addItem("")
        self.label_8 = QtWidgets.QLabel(self.groupBox_7)
        self.label_8.setGeometry(QtCore.QRect(381, 35, 61, 20))
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.groupBox_7)
        self.label_9.setGeometry(QtCore.QRect(560, 30, 61, 31))
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.IN2SET = QtWidgets.QPushButton(self.groupBox_7)
        self.IN2SET.setGeometry(QtCore.QRect(740, 30, 91, 31))
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(12)
        self.IN2SET.setFont(font)
        self.IN2SET.setObjectName("IN2SET")
        self.IN2DATAQUE = QtWidgets.QPushButton(self.groupBox_7)
        self.IN2DATAQUE.setGeometry(QtCore.QRect(860, 30, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.IN2DATAQUE.setFont(font)
        self.IN2DATAQUE.setObjectName("IN2DATAQUE")
        self.groupBox_6 = QtWidgets.QGroupBox(self.widget)
        self.groupBox_6.setGeometry(QtCore.QRect(20, 575, 991, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox_6.setFont(font)
        self.groupBox_6.setObjectName("groupBox_6")
        self.IN1SWITCH = QtWidgets.QComboBox(self.groupBox_6)
        self.IN1SWITCH.setGeometry(QtCore.QRect(20, 30, 101, 31))
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(16)
        self.IN1SWITCH.setFont(font)
        self.IN1SWITCH.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.IN1SWITCH.setObjectName("IN1SWITCH")
        self.IN1SWITCH.addItem("")
        self.IN1SWITCH.addItem("")
        self.IN1ACDC = QtWidgets.QComboBox(self.groupBox_6)
        self.IN1ACDC.setGeometry(QtCore.QRect(140, 30, 101, 31))
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(16)
        self.IN1ACDC.setFont(font)
        self.IN1ACDC.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.IN1ACDC.setObjectName("IN1ACDC")
        self.IN1ACDC.addItem("")
        self.IN1ACDC.addItem("")
        self.IN1SW = QtWidgets.QComboBox(self.groupBox_6)
        self.IN1SW.setGeometry(QtCore.QRect(260, 30, 101, 31))
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(16)
        self.IN1SW.setFont(font)
        self.IN1SW.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.IN1SW.setObjectName("IN1SW")
        self.IN1SW.addItem("")
        self.IN1SW.addItem("")
        self.IN1IEPE = QtWidgets.QComboBox(self.groupBox_6)
        self.IN1IEPE.setGeometry(QtCore.QRect(450, 30, 101, 31))
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(16)
        self.IN1IEPE.setFont(font)
        self.IN1IEPE.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.IN1IEPE.setObjectName("IN1IEPE")
        self.IN1IEPE.addItem("")
        self.IN1IEPE.addItem("")
        self.IN1IEPE.addItem("")
        self.IN1GAIN = QtWidgets.QComboBox(self.groupBox_6)
        self.IN1GAIN.setGeometry(QtCore.QRect(630, 30, 101, 31))
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(16)
        self.IN1GAIN.setFont(font)
        self.IN1GAIN.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.IN1GAIN.setObjectName("IN1GAIN")
        self.IN1GAIN.addItem("")
        self.IN1GAIN.addItem("")
        self.IN1GAIN.addItem("")
        self.IN1GAIN.addItem("")
        self.IN1GAIN.addItem("")
        self.IN1GAIN.addItem("")
        self.IN1GAIN.addItem("")
        self.IN1GAIN.addItem("")
        self.IN1GAIN.addItem("")
        self.IN1GAIN.addItem("")
        self.IN1GAIN.addItem("")
        self.IN1GAIN.addItem("")
        self.label_6 = QtWidgets.QLabel(self.groupBox_6)
        self.label_6.setGeometry(QtCore.QRect(381, 35, 61, 20))
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.groupBox_6)
        self.label_7.setGeometry(QtCore.QRect(560, 30, 61, 31))
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.IN1SET = QtWidgets.QPushButton(self.groupBox_6)
        self.IN1SET.setGeometry(QtCore.QRect(740, 30, 91, 31))
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(12)
        self.IN1SET.setFont(font)
        self.IN1SET.setObjectName("IN1SET")
        self.IN1DATAQUE = QtWidgets.QPushButton(self.groupBox_6)
        self.IN1DATAQUE.setGeometry(QtCore.QRect(860, 30, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.IN1DATAQUE.setFont(font)
        self.IN1DATAQUE.setObjectName("IN1DATAQUE")
        self.tabWidget.addTab(self.widget, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        self.CONNECT.clicked.connect(Dialog.accept)
        self.SAMQUE.clicked.connect(Dialog.accept)
        self.SAMSET.clicked.connect(Dialog.accept)
        self.FFTSET.clicked.connect(Dialog.accept)
        self.STASAM.clicked.connect(Dialog.accept)
        self.CLEARMESSAGE.clicked.connect(Dialog.accept)
        self.OUTSWITCHSET.clicked.connect(Dialog.accept)
        self.OUTENABLE.clicked.connect(Dialog.accept)
        self.IN1SET.clicked.connect(Dialog.accept)
        self.IN2SET.clicked.connect(Dialog.accept)
        self.IN1DATAQUE.clicked.connect(Dialog.accept)
        self.IN2DATAQUE.clicked.connect(Dialog.accept)
        self.OUTQUE.clicked.connect(Dialog.accept)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "振动信号分析仪上位机-V1.0"))
        self.groupBox.setTitle(_translate("Dialog", "IP设置"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt;\">IP地址：</span></p></body></html>"))
        self.IPADDR.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" dir=\'rtl\' style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">192.168.0.200</span></p></body></html>"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">端口：</span></p></body></html>"))
        self.IPPORT.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" dir=\'rtl\' style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">1000</span></p></body></html>"))
        self.groupBox_2.setTitle(_translate("Dialog", "设备连接"))
        self.CONNECT.setText(_translate("Dialog", "连接设备"))
        self.CONSTA.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'AcadEref\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">未连接</span></p></body></html>"))
        self.groupBox_3.setTitle(_translate("Dialog", "采集/采样设置"))
        self.STASAM.setText(_translate("Dialog", "开始采集"))
        self.SAMQUE.setText(_translate("Dialog", "采样查询"))
        self.SAMSET.setText(_translate("Dialog", "采样设置"))
        self.SAMDATA.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'AcadEref\'; font-size:14pt;\">256</span></p></body></html>"))
        self.FFTSET.setText(_translate("Dialog", "FFT点数设置"))
        self.FFTVAL.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'AcadEref\'; font-size:14pt;\">4096</span></p></body></html>"))
        self.groupBox_4.setTitle(_translate("Dialog", "消息提示"))
        self.CLEARMESSAGE.setText(_translate("Dialog", "清空消息"))
        self.groupBox_5.setTitle(_translate("Dialog", "输出通道"))
        self.OUTSWITCH.setItemText(0, _translate("Dialog", "关闭"))
        self.OUTSWITCH.setItemText(1, _translate("Dialog", "伪差分输出"))
        self.OUTSWITCH.setItemText(2, _translate("Dialog", "差分输出"))
        self.OUTSWITCHSET.setText(_translate("Dialog", "设置"))
        self.WAVESELECT.setItemText(0, _translate("Dialog", "正弦波"))
        self.WAVESELECT.setItemText(1, _translate("Dialog", "随机噪声"))
        self.WAVESELECT.setItemText(2, _translate("Dialog", "正弦波扫频"))
        self.label_3.setText(_translate("Dialog", "波形幅度(Vpp):"))
        self.OUTVPP.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt;\">1.00</span></p></body></html>"))
        self.label_4.setText(_translate("Dialog", "波形频率(Hz):"))
        self.OUTFREQ.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt;\">1.00</span></p></body></html>"))
        self.label_5.setText(_translate("Dialog", "扫频时间(s):"))
        self.OUTTIME.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt;\">1.00</span></p></body></html>"))
        self.OUTENABLE.setText(_translate("Dialog", "输出设置使能"))
        self.OUTQUE.setText(_translate("Dialog", "输出参数查询"))
        self.label_10.setText(_translate("Dialog", "波形类型:"))
        self.groupBox_7.setTitle(_translate("Dialog", "输入通道二"))
        self.IN2SWITCH.setItemText(0, _translate("Dialog", "打开"))
        self.IN2SWITCH.setItemText(1, _translate("Dialog", "关闭"))
        self.IN2ACDC.setItemText(0, _translate("Dialog", "直流"))
        self.IN2ACDC.setItemText(1, _translate("Dialog", "交流"))
        self.IN2SW.setItemText(0, _translate("Dialog", "单端"))
        self.IN2SW.setItemText(1, _translate("Dialog", "差分"))
        self.IN2IEPE.setItemText(0, _translate("Dialog", "关闭"))
        self.IN2IEPE.setItemText(1, _translate("Dialog", "4mA"))
        self.IN2IEPE.setItemText(2, _translate("Dialog", "10mA"))
        self.IN2GAIN.setItemText(0, _translate("Dialog", "1/16"))
        self.IN2GAIN.setItemText(1, _translate("Dialog", "1/8"))
        self.IN2GAIN.setItemText(2, _translate("Dialog", "1/4"))
        self.IN2GAIN.setItemText(3, _translate("Dialog", "1/2"))
        self.IN2GAIN.setItemText(4, _translate("Dialog", "1"))
        self.IN2GAIN.setItemText(5, _translate("Dialog", "2"))
        self.IN2GAIN.setItemText(6, _translate("Dialog", "4"))
        self.IN2GAIN.setItemText(7, _translate("Dialog", "8"))
        self.IN2GAIN.setItemText(8, _translate("Dialog", "16"))
        self.IN2GAIN.setItemText(9, _translate("Dialog", "32"))
        self.IN2GAIN.setItemText(10, _translate("Dialog", "64"))
        self.IN2GAIN.setItemText(11, _translate("Dialog", "128"))
        self.label_8.setText(_translate("Dialog", "IEPE："))
        self.label_9.setText(_translate("Dialog", "增益："))
        self.IN2SET.setText(_translate("Dialog", "配置"))
        self.IN2DATAQUE.setText(_translate("Dialog", "参数查询"))
        self.groupBox_6.setTitle(_translate("Dialog", "输入通道一"))
        self.IN1SWITCH.setItemText(0, _translate("Dialog", "打开"))
        self.IN1SWITCH.setItemText(1, _translate("Dialog", "关闭"))
        self.IN1ACDC.setItemText(0, _translate("Dialog", "直流"))
        self.IN1ACDC.setItemText(1, _translate("Dialog", "交流"))
        self.IN1SW.setItemText(0, _translate("Dialog", "单端"))
        self.IN1SW.setItemText(1, _translate("Dialog", "差分"))
        self.IN1IEPE.setItemText(0, _translate("Dialog", "关闭"))
        self.IN1IEPE.setItemText(1, _translate("Dialog", "4mA"))
        self.IN1IEPE.setItemText(2, _translate("Dialog", "10mA"))
        self.IN1GAIN.setItemText(0, _translate("Dialog", "1/16"))
        self.IN1GAIN.setItemText(1, _translate("Dialog", "1/8"))
        self.IN1GAIN.setItemText(2, _translate("Dialog", "1/4"))
        self.IN1GAIN.setItemText(3, _translate("Dialog", "1/2"))
        self.IN1GAIN.setItemText(4, _translate("Dialog", "1"))
        self.IN1GAIN.setItemText(5, _translate("Dialog", "2"))
        self.IN1GAIN.setItemText(6, _translate("Dialog", "4"))
        self.IN1GAIN.setItemText(7, _translate("Dialog", "8"))
        self.IN1GAIN.setItemText(8, _translate("Dialog", "16"))
        self.IN1GAIN.setItemText(9, _translate("Dialog", "32"))
        self.IN1GAIN.setItemText(10, _translate("Dialog", "64"))
        self.IN1GAIN.setItemText(11, _translate("Dialog", "128"))
        self.label_6.setText(_translate("Dialog", "IEPE："))
        self.label_7.setText(_translate("Dialog", "增益："))
        self.IN1SET.setText(_translate("Dialog", "配置"))
        self.IN1DATAQUE.setText(_translate("Dialog", "参数查询"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.widget), _translate("Dialog", "主界面"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "关于"))
