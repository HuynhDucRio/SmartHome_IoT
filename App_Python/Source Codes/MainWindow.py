# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(762, 873)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Background = QtWidgets.QFrame(self.centralwidget)
        self.Background.setGeometry(QtCore.QRect(0, 0, 761, 831))
        self.Background.setStyleSheet("QFrame{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(77, 77, 127, 255))\n"
"}")
        self.Background.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Background.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Background.setObjectName("Background")
        self.BatteryValue = QtWidgets.QProgressBar(self.Background)
        self.BatteryValue.setGeometry(QtCore.QRect(610, 550, 61, 241))
        font = QtGui.QFont()
        font.setStrikeOut(False)
        self.BatteryValue.setFont(font)
        self.BatteryValue.setProperty("value", 50)
        self.BatteryValue.setOrientation(QtCore.Qt.Vertical)
        self.BatteryValue.setObjectName("BatteryValue")
        self.DownloadSpeed = QtWidgets.QFrame(self.Background)
        self.DownloadSpeed.setGeometry(QtCore.QRect(0, 40, 320, 320))
        self.DownloadSpeed.setStyleSheet("background-color: rgb(77, 77, 255);")
        self.DownloadSpeed.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.DownloadSpeed.setFrameShadow(QtWidgets.QFrame.Raised)
        self.DownloadSpeed.setObjectName("DownloadSpeed")
        self.ProgressCircularDS = QtWidgets.QFrame(self.DownloadSpeed)
        self.ProgressCircularDS.setGeometry(QtCore.QRect(10, 10, 300, 300))
        self.ProgressCircularDS.setStyleSheet("QFrame{\n"
"    border-radius: 150px;\n"
"    background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.749 rgba(85, 0, 255, 0), stop:0.750 rgba(100, 255, 0, 255));\n"
"}")
        self.ProgressCircularDS.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.ProgressCircularDS.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ProgressCircularDS.setObjectName("ProgressCircularDS")
        self.circularBgCircular = QtWidgets.QFrame(self.DownloadSpeed)
        self.circularBgCircular.setGeometry(QtCore.QRect(10, 10, 300, 300))
        self.circularBgCircular.setStyleSheet("QFrame{\n"
"    border-radius: 150px;\n"
"    background-color: rgba(97, 97, 97,120);\n"
"}")
        self.circularBgCircular.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.circularBgCircular.setFrameShadow(QtWidgets.QFrame.Raised)
        self.circularBgCircular.setObjectName("circularBgCircular")
        self.containerCircular = QtWidgets.QFrame(self.DownloadSpeed)
        self.containerCircular.setGeometry(QtCore.QRect(25, 25, 270, 270))
        self.containerCircular.setStyleSheet("QFrame{\n"
"border-radius:135px;\n"
"background-color: rgb(0, 0, 127)\n"
"} ")
        self.containerCircular.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.containerCircular.setFrameShadow(QtWidgets.QFrame.Raised)
        self.containerCircular.setObjectName("containerCircular")
        self.labelDSValue = QtWidgets.QLabel(self.containerCircular)
        self.labelDSValue.setGeometry(QtCore.QRect(54, 70, 171, 116))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(40)
        self.labelDSValue.setFont(font)
        self.labelDSValue.setStyleSheet("background-color: none;\n"
"color:#FFFFFF")
        self.labelDSValue.setAlignment(QtCore.Qt.AlignCenter)
        self.labelDSValue.setObjectName("labelDSValue")
        self.labelBatteryPercentage = QtWidgets.QLabel(self.Background)
        self.labelBatteryPercentage.setGeometry(QtCore.QRect(590, 690, 101, 25))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(40)
        font.setBold(False)
        font.setWeight(50)
        self.labelBatteryPercentage.setFont(font)
        self.labelBatteryPercentage.setStyleSheet("background-color: none;\n"
"color : rgb(0, 0, 0);")
        self.labelBatteryPercentage.setAlignment(QtCore.Qt.AlignCenter)
        self.labelBatteryPercentage.setObjectName("labelBatteryPercentage")
        self.label_2 = QtWidgets.QLabel(self.Background)
        self.label_2.setGeometry(QtCore.QRect(580, 790, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.Temperature = QtWidgets.QFrame(self.Background)
        self.Temperature.setGeometry(QtCore.QRect(320, 0, 201, 831))
        self.Temperature.setStyleSheet("background-color: rgb(255, 77, 127);")
        self.Temperature.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Temperature.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Temperature.setObjectName("Temperature")
        self.frame_2 = QtWidgets.QFrame(self.Temperature)
        self.frame_2.setGeometry(QtCore.QRect(0, 670, 161, 161))
        self.frame_2.setStyleSheet("QFrame{\n"
"    border-color: rgb(0, 0, 0);\n"
"    border-radius: 80px;\n"
"    background-color:;\n"
"    background-color:rgb(0, 170, 255);\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.labelTemperature = QtWidgets.QLabel(self.frame_2)
        self.labelTemperature.setGeometry(QtCore.QRect(0, 40, 151, 71))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(40)
        self.labelTemperature.setFont(font)
        self.labelTemperature.setStyleSheet("background-color: none;\n"
"color:#FFFFFF")
        self.labelTemperature.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTemperature.setObjectName("labelTemperature")
        self.labelPercentageCircular_5 = QtWidgets.QLabel(self.frame_2)
        self.labelPercentageCircular_5.setGeometry(QtCore.QRect(130, 0, 51, 81))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(40)
        self.labelPercentageCircular_5.setFont(font)
        self.labelPercentageCircular_5.setStyleSheet("background-color: none;\n"
"color:#FFFFFF")
        self.labelPercentageCircular_5.setAlignment(QtCore.Qt.AlignCenter)
        self.labelPercentageCircular_5.setObjectName("labelPercentageCircular_5")
        self.frame_5 = QtWidgets.QFrame(self.Temperature)
        self.frame_5.setGeometry(QtCore.QRect(40, 80, 81, 200))
        self.frame_5.setStyleSheet("QFrame{\n"
"    background-color: rgb(255, 0, 0);\n"
"}")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.labelPercentageCircular_4 = QtWidgets.QLabel(self.Temperature)
        self.labelPercentageCircular_4.setGeometry(QtCore.QRect(100, 190, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(40)
        self.labelPercentageCircular_4.setFont(font)
        self.labelPercentageCircular_4.setStyleSheet("background-color: none;\n"
"color:#FFFFFF")
        self.labelPercentageCircular_4.setAlignment(QtCore.Qt.AlignCenter)
        self.labelPercentageCircular_4.setObjectName("labelPercentageCircular_4")
        self.labelPercentageCircular_6 = QtWidgets.QLabel(self.Temperature)
        self.labelPercentageCircular_6.setGeometry(QtCore.QRect(100, 360, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(40)
        self.labelPercentageCircular_6.setFont(font)
        self.labelPercentageCircular_6.setStyleSheet("background-color: none;\n"
"color:#FFFFFF")
        self.labelPercentageCircular_6.setAlignment(QtCore.Qt.AlignCenter)
        self.labelPercentageCircular_6.setObjectName("labelPercentageCircular_6")
        self.labelPercentageCircular_7 = QtWidgets.QLabel(self.Temperature)
        self.labelPercentageCircular_7.setGeometry(QtCore.QRect(100, 120, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(40)
        self.labelPercentageCircular_7.setFont(font)
        self.labelPercentageCircular_7.setStyleSheet("background-color: none;\n"
"color:#FFFFFF")
        self.labelPercentageCircular_7.setAlignment(QtCore.Qt.AlignCenter)
        self.labelPercentageCircular_7.setObjectName("labelPercentageCircular_7")
        self.labelPercentageCircular_8 = QtWidgets.QLabel(self.Temperature)
        self.labelPercentageCircular_8.setGeometry(QtCore.QRect(60, 250, 181, 71))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(40)
        self.labelPercentageCircular_8.setFont(font)
        self.labelPercentageCircular_8.setStyleSheet("background-color: none;\n"
"color:#FFFFFF")
        self.labelPercentageCircular_8.setAlignment(QtCore.Qt.AlignCenter)
        self.labelPercentageCircular_8.setObjectName("labelPercentageCircular_8")
        self.labelPercentageCircular_3 = QtWidgets.QLabel(self.Temperature)
        self.labelPercentageCircular_3.setGeometry(QtCore.QRect(60, 300, 181, 71))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(40)
        self.labelPercentageCircular_3.setFont(font)
        self.labelPercentageCircular_3.setStyleSheet("background-color: none;\n"
"color:#FFFFFF")
        self.labelPercentageCircular_3.setAlignment(QtCore.Qt.AlignCenter)
        self.labelPercentageCircular_3.setObjectName("labelPercentageCircular_3")
        self.labelPercentageCircular_9 = QtWidgets.QLabel(self.Temperature)
        self.labelPercentageCircular_9.setGeometry(QtCore.QRect(60, 580, 181, 71))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(40)
        self.labelPercentageCircular_9.setFont(font)
        self.labelPercentageCircular_9.setStyleSheet("background-color: none;\n"
"color:#FFFFFF")
        self.labelPercentageCircular_9.setAlignment(QtCore.Qt.AlignCenter)
        self.labelPercentageCircular_9.setObjectName("labelPercentageCircular_9")
        self.labelPercentageCircular_11 = QtWidgets.QLabel(self.Temperature)
        self.labelPercentageCircular_11.setGeometry(QtCore.QRect(100, 480, 101, 51))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(40)
        self.labelPercentageCircular_11.setFont(font)
        self.labelPercentageCircular_11.setStyleSheet("background-color: none;\n"
"color:#FFFFFF")
        self.labelPercentageCircular_11.setAlignment(QtCore.Qt.AlignCenter)
        self.labelPercentageCircular_11.setObjectName("labelPercentageCircular_11")
        self.labelPercentageCircular_12 = QtWidgets.QLabel(self.Temperature)
        self.labelPercentageCircular_12.setGeometry(QtCore.QRect(70, 420, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(40)
        self.labelPercentageCircular_12.setFont(font)
        self.labelPercentageCircular_12.setStyleSheet("background-color: none;\n"
"color:#FFFFFF")
        self.labelPercentageCircular_12.setAlignment(QtCore.Qt.AlignCenter)
        self.labelPercentageCircular_12.setObjectName("labelPercentageCircular_12")
        self.labelPercentageCircular_10 = QtWidgets.QLabel(self.Temperature)
        self.labelPercentageCircular_10.setGeometry(QtCore.QRect(90, 540, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(40)
        self.labelPercentageCircular_10.setFont(font)
        self.labelPercentageCircular_10.setStyleSheet("background-color: none;\n"
"color:#FFFFFF")
        self.labelPercentageCircular_10.setAlignment(QtCore.Qt.AlignCenter)
        self.labelPercentageCircular_10.setObjectName("labelPercentageCircular_10")
        self.labelPercentageCircular_13 = QtWidgets.QLabel(self.Temperature)
        self.labelPercentageCircular_13.setGeometry(QtCore.QRect(80, 50, 131, 71))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(40)
        self.labelPercentageCircular_13.setFont(font)
        self.labelPercentageCircular_13.setStyleSheet("background-color: none;\n"
"color:#FFFFFF")
        self.labelPercentageCircular_13.setAlignment(QtCore.Qt.AlignCenter)
        self.labelPercentageCircular_13.setObjectName("labelPercentageCircular_13")
        self.frame_6 = QtWidgets.QFrame(self.Temperature)
        self.frame_6.setGeometry(QtCore.QRect(40, 280, 81, 200))
        self.frame_6.setStyleSheet("QFrame{\n"
"    \n"
"    background-color: rgb(255, 255, 127);\n"
"}")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.frame_7 = QtWidgets.QFrame(self.Temperature)
        self.frame_7.setGeometry(QtCore.QRect(40, 480, 81, 200))
        self.frame_7.setStyleSheet("QFrame{\n"
"    \n"
"    background-color: rgb(0, 170, 255);\n"
"}")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.tempValue = QtWidgets.QFrame(self.Temperature)
        self.tempValue.setGeometry(QtCore.QRect(40, 79, 81, 600))
        self.tempValue.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tempValue.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tempValue.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tempValue.setObjectName("tempValue")
        self.label_3 = QtWidgets.QLabel(self.Temperature)
        self.label_3.setGeometry(QtCore.QRect(-10, 10, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.UploadSpeed = QtWidgets.QFrame(self.Background)
        self.UploadSpeed.setGeometry(QtCore.QRect(0, 400, 320, 320))
        self.UploadSpeed.setStyleSheet("QFrame{\n"
"    background-color:rgb(255, 205, 255);\n"
"}")
        self.UploadSpeed.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.UploadSpeed.setFrameShadow(QtWidgets.QFrame.Raised)
        self.UploadSpeed.setObjectName("UploadSpeed")
        self.ProgressCircularUS = QtWidgets.QFrame(self.UploadSpeed)
        self.ProgressCircularUS.setGeometry(QtCore.QRect(10, 10, 300, 300))
        self.ProgressCircularUS.setStyleSheet("QFrame{\n"
"    border-radius: 150px;\n"
"    background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.749 rgba(85, 0, 255, 0), stop:0.750 rgba(255, 255, 0, 255));\n"
"}")
        self.ProgressCircularUS.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.ProgressCircularUS.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ProgressCircularUS.setObjectName("ProgressCircularUS")
        self.circularBgCircular_3 = QtWidgets.QFrame(self.UploadSpeed)
        self.circularBgCircular_3.setGeometry(QtCore.QRect(10, 10, 300, 300))
        self.circularBgCircular_3.setStyleSheet("QFrame{\n"
"    border-radius: 150px;\n"
"    background-color: rgba(97, 97, 97,120);\n"
"}")
        self.circularBgCircular_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.circularBgCircular_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.circularBgCircular_3.setObjectName("circularBgCircular_3")
        self.containerCircular_3 = QtWidgets.QFrame(self.UploadSpeed)
        self.containerCircular_3.setGeometry(QtCore.QRect(25, 25, 270, 270))
        self.containerCircular_3.setStyleSheet("QFrame{\n"
"border-radius:135px;\n"
"background-color: rgb(0, 0, 127)\n"
"} ")
        self.containerCircular_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.containerCircular_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.containerCircular_3.setObjectName("containerCircular_3")
        self.labelUSValue = QtWidgets.QLabel(self.containerCircular_3)
        self.labelUSValue.setGeometry(QtCore.QRect(20, 90, 221, 101))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(40)
        self.labelUSValue.setFont(font)
        self.labelUSValue.setStyleSheet("background-color: none;\n"
"color:#FFFFFF")
        self.labelUSValue.setAlignment(QtCore.Qt.AlignCenter)
        self.labelUSValue.setObjectName("labelUSValue")
        self.labelUS = QtWidgets.QLabel(self.Background)
        self.labelUS.setGeometry(QtCore.QRect(0, 360, 321, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.labelUS.setFont(font)
        self.labelUS.setStyleSheet("QFrame{\n"
"    background-color:rgb(255, 205, 255);\n"
"}")
        self.labelUS.setAlignment(QtCore.Qt.AlignCenter)
        self.labelUS.setObjectName("labelUS")
        self.Light_fr = QtWidgets.QFrame(self.Background)
        self.Light_fr.setGeometry(QtCore.QRect(520, 0, 241, 181))
        self.Light_fr.setStyleSheet("QFrame{\n"
"    background-color:rgb(255, 255, 255);\n"
"}")
        self.Light_fr.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Light_fr.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Light_fr.setObjectName("Light_fr")
        self.Light = QtWidgets.QLabel(self.Light_fr)
        self.Light.setGeometry(QtCore.QRect(50, 0, 131, 111))
        self.Light.setText("")
        self.Light.setPixmap(QtGui.QPixmap(":/Light_img/den0.png"))
        self.Light.setScaledContents(False)
        self.Light.setObjectName("Light")
        self.LightButtonON = QtWidgets.QPushButton(self.Light_fr)
        self.LightButtonON.setGeometry(QtCore.QRect(14, 130, 81, 31))
        self.LightButtonON.setObjectName("LightButtonON")
        self.LightButtonOFF = QtWidgets.QPushButton(self.Light_fr)
        self.LightButtonOFF.setGeometry(QtCore.QRect(140, 130, 81, 31))
        self.LightButtonOFF.setObjectName("LightButtonOFF")
        self.AirPur_fr = QtWidgets.QFrame(self.Background)
        self.AirPur_fr.setGeometry(QtCore.QRect(520, 180, 241, 181))
        self.AirPur_fr.setStyleSheet("QFrame{\n"
"    background-color:rgb(255, 255, 255);\n"
"}")
        self.AirPur_fr.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.AirPur_fr.setFrameShadow(QtWidgets.QFrame.Raised)
        self.AirPur_fr.setObjectName("AirPur_fr")
        self.AirPurButtonON = QtWidgets.QPushButton(self.AirPur_fr)
        self.AirPurButtonON.setGeometry(QtCore.QRect(14, 130, 81, 31))
        self.AirPurButtonON.setObjectName("AirPurButtonON")
        self.AirPurButtonOFF = QtWidgets.QPushButton(self.AirPur_fr)
        self.AirPurButtonOFF.setGeometry(QtCore.QRect(140, 130, 81, 31))
        self.AirPurButtonOFF.setObjectName("AirPurButtonOFF")
        self.AirPur = QtWidgets.QLabel(self.AirPur_fr)
        self.AirPur.setGeometry(QtCore.QRect(70, 10, 101, 101))
        self.AirPur.setText("")
        self.AirPur.setTextFormat(QtCore.Qt.RichText)
        self.AirPur.setPixmap(QtGui.QPixmap(":/AirPur_img/kk0.png"))
        self.AirPur.setScaledContents(True)
        self.AirPur.setObjectName("AirPur")
        self.AirCon_fr = QtWidgets.QFrame(self.Background)
        self.AirCon_fr.setGeometry(QtCore.QRect(520, 360, 241, 181))
        self.AirCon_fr.setStyleSheet("QFrame{\n"
"    background-color:rgb(255, 255, 255);\n"
"}")
        self.AirCon_fr.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.AirCon_fr.setFrameShadow(QtWidgets.QFrame.Raised)
        self.AirCon_fr.setObjectName("AirCon_fr")
        self.AirCon = QtWidgets.QLabel(self.AirCon_fr)
        self.AirCon.setGeometry(QtCore.QRect(50, 30, 131, 111))
        self.AirCon.setText("")
        self.AirCon.setPixmap(QtGui.QPixmap(":/AirCon_img/dh0.png"))
        self.AirCon.setScaledContents(True)
        self.AirCon.setObjectName("AirCon")
        self.AirConButtonON = QtWidgets.QPushButton(self.AirCon_fr)
        self.AirConButtonON.setGeometry(QtCore.QRect(14, 130, 81, 31))
        self.AirConButtonON.setObjectName("AirConButtonON")
        self.AirConButtonOFF = QtWidgets.QPushButton(self.AirCon_fr)
        self.AirConButtonOFF.setGeometry(QtCore.QRect(140, 130, 81, 31))
        self.AirConButtonOFF.setObjectName("AirConButtonOFF")
        self.labelDS = QtWidgets.QLabel(self.Background)
        self.labelDS.setGeometry(QtCore.QRect(0, 0, 321, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.labelDS.setFont(font)
        self.labelDS.setStyleSheet("background-color: rgb(77, 77, 255);")
        self.labelDS.setAlignment(QtCore.Qt.AlignCenter)
        self.labelDS.setObjectName("labelDS")
        self.UploadSpeed.raise_()
        self.labelUS.raise_()
        self.labelDS.raise_()
        self.BatteryValue.raise_()
        self.DownloadSpeed.raise_()
        self.labelBatteryPercentage.raise_()
        self.label_2.raise_()
        self.Temperature.raise_()
        self.Light_fr.raise_()
        self.AirPur_fr.raise_()
        self.AirCon_fr.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 762, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelDSValue.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:24pt;\">0</span><span style=\" font-size:24pt; vertical-align:super;\">%</span></p></body></html>"))
        self.labelBatteryPercentage.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">0</span><span style=\" font-size:16pt; vertical-align:super;\">%</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "Battery"))
        self.labelTemperature.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:31pt; vertical-align:super;\">°</span><span style=\" font-size:31pt;\">C</span></p></body></html>"))
        self.labelPercentageCircular_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; color:#000000;\">0</span></p><p><br/></p></body></html>"))
        self.labelPercentageCircular_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; color:#000000;\">80</span></p><p><br/></p></body></html>"))
        self.labelPercentageCircular_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; color:#000000;\">50</span></p><p><br/></p></body></html>"))
        self.labelPercentageCircular_7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; color:#000000;\">90</span></p></body></html>"))
        self.labelPercentageCircular_8.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; color:#000000;\">70</span></p><p><br/></p></body></html>"))
        self.labelPercentageCircular_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; color:#000000;\">60</span></p><p><br/></p></body></html>"))
        self.labelPercentageCircular_9.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; color:#000000;\">10</span></p></body></html>"))
        self.labelPercentageCircular_11.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; color:#000000;\">30</span></p></body></html>"))
        self.labelPercentageCircular_12.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; color:#000000;\">40</span></p><p><br/></p></body></html>"))
        self.labelPercentageCircular_10.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; color:#000000;\">20</span></p></body></html>"))
        self.labelPercentageCircular_13.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; color:#000000;\">100</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "Temperature"))
        self.labelUSValue.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">400mg/m3</span></p></body></html>"))
        self.labelUS.setText(_translate("MainWindow", "Dust Density"))
        self.LightButtonON.setText(_translate("MainWindow", "Light on"))
        self.LightButtonOFF.setText(_translate("MainWindow", "Light off"))
        self.AirPurButtonON.setText(_translate("MainWindow", "AirPur on"))
        self.AirPurButtonOFF.setText(_translate("MainWindow", "AirPur off"))
        self.AirConButtonON.setText(_translate("MainWindow", "AirCon on"))
        self.AirConButtonOFF.setText(_translate("MainWindow", "AirCon off"))
        self.labelDS.setText(_translate("MainWindow", "Humidity"))
import Img_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())