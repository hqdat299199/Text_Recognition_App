# Form implementation generated from reading ui file 'form1.ui'
#
# Created by: PyQt6 UI code generator 6.3.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import (QMainWindow, QMessageBox, QFileDialog, QApplication)
from PyQt6.QtGui import QImage
from PIL import Image
import pytesseract
import cv2
import os
import numpy as np
import sys
import os.path

class Ui_MainWindow(QMainWindow,QFileDialog):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setMaximumSize(1350, 750)
        MainWindow.setMinimumSize(1350, 750)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(0, 10, 671, 461))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.groupBox.setFont(font)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.lbpic1 = QtWidgets.QLabel(self.groupBox)
        self.lbpic1.setGeometry(QtCore.QRect(10, 40, 321, 361))
        self.lbpic1.setAutoFillBackground(False)
        self.lbpic1.setStyleSheet("background-color: lightgray")
        self.lbpic1.setText("")
        self.lbpic1.setScaledContents(True)
        self.lbpic1.setObjectName("lbpic1")
        self.lbdophangiai = QtWidgets.QLabel(self.groupBox)
        self.lbdophangiai.setGeometry(QtCore.QRect(450, 400, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lbdophangiai.setFont(font)
        self.lbdophangiai.setText("")
        self.lbdophangiai.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.lbdophangiai.setObjectName("lbdophangiai")
        self.label4 = QtWidgets.QLabel(self.groupBox)
        self.label4.setGeometry(QtCore.QRect(160, 400, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label4.setFont(font)
        self.label4.setObjectName("label4")
        self.lbpicpath = QtWidgets.QLabel(self.groupBox)
        self.lbpicpath.setGeometry(QtCore.QRect(160, 430, 381, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lbpicpath.setFont(font)
        self.lbpicpath.setText("")
        self.lbpicpath.setObjectName("lbpicpath")
        self.btnpicpath = QtWidgets.QPushButton(self.groupBox)
        self.btnpicpath.setGeometry(QtCore.QRect(10, 410, 41, 41))
        self.btnpicpath.setObjectName("btnpicpath")
        self.btndananh = QtWidgets.QPushButton(self.groupBox)
        self.btndananh.setGeometry(QtCore.QRect(60, 410, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btndananh.setFont(font)
        self.btndananh.setIconSize(QtCore.QSize(40, 40))
        self.btndananh.setObjectName("btndananh")
        self.btnstart = QtWidgets.QPushButton(self.groupBox)
        self.btnstart.setGeometry(QtCore.QRect(550, 410, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.btnstart.setFont(font)
        self.btnstart.setIconSize(QtCore.QSize(50, 60))
        self.btnstart.setObjectName("btnstart")
        self.lbpic2 = QtWidgets.QLabel(self.groupBox)
        self.lbpic2.setGeometry(QtCore.QRect(340, 40, 321, 361))
        self.lbpic2.setAutoFillBackground(False)
        self.lbpic2.setStyleSheet("background-color: lightgray")
        self.lbpic2.setText("")
        self.lbpic2.setScaledContents(True)
        self.lbpic2.setObjectName("lbpic2")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(90, 10, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(440, 10, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(0, 470, 671, 231))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setStyleSheet("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.lbpath = QtWidgets.QLabel(self.groupBox_2)
        self.lbpath.setGeometry(QtCore.QRect(10, 30, 601, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lbpath.setFont(font)
        self.lbpath.setStyleSheet("background-color: lightgreen")
        self.lbpath.setObjectName("lbpath")
        self.btnpath = QtWidgets.QPushButton(self.groupBox_2)
        self.btnpath.setGeometry(QtCore.QRect(620, 30, 41, 31))
        self.btnpath.setToolTip("")
        self.btnpath.setObjectName("btnpath")
        self.nmsharpen = QtWidgets.QSpinBox(self.groupBox_2)
        self.nmsharpen.setGeometry(QtCore.QRect(180, 110, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.nmsharpen.setFont(font)
        self.nmsharpen.setMinimum(1)
        self.nmsharpen.setMaximum(30)
        self.nmsharpen.setObjectName("nmsharpen")
        self.lbdophangiai_5 = QtWidgets.QLabel(self.groupBox_2)
        self.lbdophangiai_5.setGeometry(QtCore.QRect(10, 190, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbdophangiai_5.setFont(font)
        self.lbdophangiai_5.setObjectName("lbdophangiai_5")
        self.lbdophangiai_6 = QtWidgets.QLabel(self.groupBox_2)
        self.lbdophangiai_6.setGeometry(QtCore.QRect(10, 150, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbdophangiai_6.setFont(font)
        self.lbdophangiai_6.setObjectName("lbdophangiai_6")
        self.nmcontrast = QtWidgets.QSpinBox(self.groupBox_2)
        self.nmcontrast.setGeometry(QtCore.QRect(180, 150, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.nmcontrast.setFont(font)
        self.nmcontrast.setMinimum(1)
        self.nmcontrast.setMaximum(255)
        self.nmcontrast.setObjectName("nmcontrast")
        self.lbdophangiai_4 = QtWidgets.QLabel(self.groupBox_2)
        self.lbdophangiai_4.setGeometry(QtCore.QRect(10, 110, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbdophangiai_4.setFont(font)
        self.lbdophangiai_4.setObjectName("lbdophangiai_4")
        self.lbdophangiai_8 = QtWidgets.QLabel(self.groupBox_2)
        self.lbdophangiai_8.setGeometry(QtCore.QRect(10, 70, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbdophangiai_8.setFont(font)
        self.lbdophangiai_8.setObjectName("lbdophangiai_8")
        self.nmsang = QtWidgets.QSpinBox(self.groupBox_2)
        self.nmsang.setGeometry(QtCore.QRect(180, 70, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.nmsang.setFont(font)
        self.nmsang.setMinimum(-50)
        self.nmsang.setMaximum(50)
        self.nmsang.setObjectName("nmsang")
        self.cbblur = QtWidgets.QComboBox(self.groupBox_2)
        self.cbblur.setGeometry(QtCore.QRect(180, 190, 121, 31))
        self.cbblur.setObjectName("cbblur")
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_3.setGeometry(QtCore.QRect(320, 70, 341, 51))
        self.groupBox_3.setStyleSheet("background-color: lightblue")
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.lbdophangiai_9 = QtWidgets.QLabel(self.groupBox_3)
        self.lbdophangiai_9.setGeometry(QtCore.QRect(10, 10, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbdophangiai_9.setFont(font)
        self.lbdophangiai_9.setObjectName("lbdophangiai_9")
        self.rdbtrang = QtWidgets.QRadioButton(self.groupBox_3)
        self.rdbtrang.setGeometry(QtCore.QRect(170, 10, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rdbtrang.setFont(font)
        self.rdbtrang.setObjectName("rdbtrang")
        self.rdbden = QtWidgets.QRadioButton(self.groupBox_3)
        self.rdbden.setGeometry(QtCore.QRect(270, 10, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rdbden.setFont(font)
        self.rdbden.setObjectName("rdbden")
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_4.setGeometry(QtCore.QRect(320, 120, 341, 51))
        self.groupBox_4.setStyleSheet("background-color: lightblue")
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.rdbviet = QtWidgets.QRadioButton(self.groupBox_4)
        self.rdbviet.setGeometry(QtCore.QRect(270, 10, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rdbviet.setFont(font)
        self.rdbviet.setObjectName("rdbviet")
        self.lbdophangiai_10 = QtWidgets.QLabel(self.groupBox_4)
        self.lbdophangiai_10.setGeometry(QtCore.QRect(10, 10, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbdophangiai_10.setFont(font)
        self.lbdophangiai_10.setObjectName("lbdophangiai_10")
        self.rdbanh = QtWidgets.QRadioButton(self.groupBox_4)
        self.rdbanh.setGeometry(QtCore.QRect(170, 10, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rdbanh.setFont(font)
        self.rdbanh.setObjectName("rdbanh")
        self.groupBox_5 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_5.setGeometry(QtCore.QRect(320, 170, 341, 51))
        self.groupBox_5.setStyleSheet("background-color: lightblue")
        self.groupBox_5.setTitle("")
        self.groupBox_5.setObjectName("groupBox_5")
        self.rdbtat = QtWidgets.QRadioButton(self.groupBox_5)
        self.rdbtat.setGeometry(QtCore.QRect(270, 10, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rdbtat.setFont(font)
        self.rdbtat.setObjectName("rdbtat")
        self.lbdophangiai_11 = QtWidgets.QLabel(self.groupBox_5)
        self.lbdophangiai_11.setGeometry(QtCore.QRect(10, 10, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbdophangiai_11.setFont(font)
        self.lbdophangiai_11.setObjectName("lbdophangiai_11")
        self.rdbbat = QtWidgets.QRadioButton(self.groupBox_5)
        self.rdbbat.setGeometry(QtCore.QRect(170, 10, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rdbbat.setFont(font)
        self.rdbbat.setObjectName("rdbbat")
        self.rtbketqua = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.rtbketqua.setGeometry(QtCore.QRect(670, 50, 671, 651))
        self.rtbketqua.setReadOnly(True)
        self.rtbketqua.setObjectName("rtbketqua")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(900, 20, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1350, 27))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        #setdata
        self.cbblur.addItems(["M???c 1","M???c 3","M???c 5","M???c 7","M???c 9",])
        self.nmcontrast.setValue(255)
        self.nmsharpen.setValue(7)
        #events
        self.btnpicpath.clicked.connect(self.imagedialog)
        self.btndananh.clicked.connect(self.pasteimg)
        self.btnstart.clicked.connect(self.start)
        self.btnpath.clicked.connect(self.pathdialog)
        self.rdbtrang.setChecked(True)
        self.rdbviet.setChecked(True)
        self.rdbtat.setChecked(True)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Nh???n di???n v??n b???n - Phi??n b???n 5.2.3"))
        self.label4.setText(_translate("MainWindow", "K??ch th?????c ???nh:"))
        self.btnpicpath.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Ch???n ???????ng d???n ?????n ???nh c???n nh???n d???ng.</span></p></body></html>"))
        self.btnpicpath.setText(_translate("MainWindow", "..."))
        self.btndananh.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">D??n ???nh ???? copy v??o clipboard tr?????c ????.</span></p></body></html>"))
        self.btndananh.setText(_translate("MainWindow", "D??n ???nh"))
        self.btnstart.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">B???t ?????u nh???n di???n</span></p></body></html>"))
        self.btnstart.setText(_translate("MainWindow", "Nh???n di???n"))
        self.label.setText(_translate("MainWindow", "???nh ?????u v??o"))
        self.lbpicpath.setText(_translate("MainWindow", "..."))
        self.label_2.setText(_translate("MainWindow", "???nh ti???n x??? l??"))
        self.groupBox_2.setTitle(_translate("MainWindow", "T??y ch???nh th??ng s???"))
        self.lbpath.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"justify\"><span style=\" font-size:10pt; font-weight:600;\">Ch???n ???????ng d???n ?????n th?? m???c c??i ?????t Tesseract-OCR nh???m truy c???p v??o c??c th?? vi???n c???n thi???t cho vi???c nh???n di???n v??n b???n.</span></p></body></html>"))
        self.lbpath.setText(_translate("MainWindow", "C:\Program Files\Tesseract-OCR"))
        self.btnpath.setText(_translate("MainWindow", "..."))
        self.nmsharpen.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"justify\"><span style=\" font-size:10pt; font-weight:600;\">??i???u ch???nh ????? s???c n??t c???a ???nh ?????u v??o nh???m nh???n di???n v??n b???n ???????c t???i ??u h??n trong tr?????ng h???p ???nh b??? m???.</span></p><p align=\"justify\"><span style=\" font-size:10pt; font-weight:600;\">T???i thi???u l?? m???c 1 v?? t???i ??a l?? m???c 30.</span></p><p align=\"justify\"><span style=\" font-size:10pt; font-weight:600;\">M???c ?????nh t??? kho???ng m???c 5 ?????n m???c 10 cho k???t qu??? nh???n di???n t???t nh???t trong h???u h???t tr?????ng h???p.</span></p></body></html>"))
        self.lbdophangiai_5.setText(_translate("MainWindow", "L???c m??? kh??? nhi???u:"))
        self.lbdophangiai_6.setText(_translate("MainWindow", "????? t????ng ph???n:"))
        self.nmcontrast.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"justify\"><span style=\" font-size:10pt; font-weight:600;\">??i???u ch???nh ????? t????ng ph???n nh???m nh???n di???n ???nh t???i ??u nh???t trong tr?????ng h???p ???nh b??? qu?? s??ng.</span></p><p align=\"justify\"><span style=\" font-size:10pt; font-weight:600;\">T???i thi???u l?? m???c 1 v?? t???i ??a l?? m???c 255.</span></p><p align=\"justify\"><span style=\" font-size:10pt; font-weight:600;\">M???c ?????nh ??? m???c t???i ??a 255 cho k???t qu??? nh???n di???n t???t nh???t trong h???u h???t tr?????ng h???p.</span></p></body></html>"))
        self.lbdophangiai_4.setText(_translate("MainWindow", "????? s???c n??t:"))
        self.lbdophangiai_8.setText(_translate("MainWindow", "????? s??ng:"))
        self.nmsang.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"justify\"><span style=\" font-size:10pt; font-weight:600;\">??i???u ch???nh ????? s??ng c???a ???nh ?????u v??o nh???m nh???n di???n ???nh t???i ??u nh???t.</span></p><p align=\"justify\"><span style=\" font-size:10pt; font-weight:600;\">????? s??ng m???c t???i thi???u l?? -50 v?? ????? s??ng m???c t???i ??a l?? 50.</span></p></body></html>"))
        self.cbblur.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"justify\"><span style=\" font-size:10pt; font-weight:600;\">Thu???t to??n l??m m??? ???nh ?????u v??o ????? gi???m nhi???u (c??c v???t s??ng, v???t m???c lem,...) nh???m cho ra k???t qu??? nh???n di???n t???t nh???t.</span></p><p align=\"justify\"><span style=\" font-size:10pt; font-weight:600;\">T???i thi???u l?? m???c 1 v?? t???i ??a l?? m???c 9.</span></p><p align=\"justify\"><span style=\" font-size:10pt; font-weight:600;\">M???c ?????nh ??? m???c 1 v?? m???c 3 cho k???t qu??? nh???n di???n t???t nh???t trong h???u h???t tr?????ng h???p.</span></p></body></html>"))
        self.lbdophangiai_9.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"justify\"><span style=\" font-size:10pt; font-weight:600;\">T??y thu???c v??o m??u n???n c???a ???nh m?? ph???n m???m ??p d???ng c??c thu???t to??n x??? l?? ???nh kh??c nhau ????? cho ra k???t qu??? nh???n di???n t???t nh???t.</span></p></body></html>"))
        self.lbdophangiai_9.setText(_translate("MainWindow", "M??u n???n ???nh:"))
        self.rdbtrang.setText(_translate("MainWindow", "Tr???ng"))
        self.rdbden.setText(_translate("MainWindow", "??en"))
        self.rdbviet.setText(_translate("MainWindow", "Vi???t"))
        self.lbdophangiai_10.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"justify\"><span style=\" font-size:10pt; font-weight:600;\">L???a ch???n ng??n ng??? c???n nh???n di???n cho ch??? vi???t tr??n ???nh.</span></p></body></html>"))
        self.lbdophangiai_10.setText(_translate("MainWindow", "Ng??n ng???:"))
        self.rdbanh.setText(_translate("MainWindow", "Anh"))
        self.rdbtat.setText(_translate("MainWindow", "T???t"))
        self.lbdophangiai_11.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Cho ph??p g???p v??n b???n l???i t??? nhi???u l???n nh???n di???n c??c ???nh kh??c nhau.</span></p></body></html>"))
        self.lbdophangiai_11.setText(_translate("MainWindow", "G???p v??n b???n:"))
        self.rdbbat.setText(_translate("MainWindow", "B???t"))
        self.rtbketqua.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">N??i hi???n th??? k???t qu??? nh???n di???n v??n b???n.</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "K???t qu??? nh???n di???n"))

    def closeEvent(self):
        os.remove("temp.png")
        print("thoat")
    #Paste ???nh t??? clipboard
    def pasteimg(self):
        cb = QApplication.clipboard()
        md = cb.mimeData()
        if md.hasImage():
            img = QImage(md.imageData())
            img.save("temp.png","PNG")
            self.lbpic1.setPixmap(QtGui.QPixmap(img))
            self.lbpicpath.setText("Clipboard")
            img1 = cv2.imread("temp.png", flags=cv2.IMREAD_COLOR)
            self.lbdophangiai.setText(str(img1.shape[0]) + "x" + str(img1.shape[1]))
        else:
            QMessageBox.information(self, "L???i ?????c ???nh!", "Kh??ng t??m th???y ???nh n??o ???? copy tr?????c ???? v??o clipboard")
    #L???y ???nh t??? m??y
    def imagedialog(self):
        global imgname
        imgname = QFileDialog.getOpenFileName(self, 'Open file', 'C:\\Users\\hoquo\\Desktop',"Image files (*.jpg *.png *.bmp)")
        if(imgname != ('','')):
            with open(imgname[0]) as f:
                self.lbpicpath.setText(str(imgname[0]))#get ???????ng d???n ???nh
                self.lbpic1.setPixmap(QtGui.QPixmap(imgname[0]))#set ???nh v??o khung
                img1 = cv2.imread(imgname[0], flags=cv2.IMREAD_COLOR)
                self.lbdophangiai.setText(str(img1.shape[0]) + "x" + str(img1.shape[1]))
    #L???y ???????ng d???n Tesseract-OCR
    def pathdialog(self):
        pathname = QFileDialog.getExistingDirectory(self,"Ch???n ???????ng d???n")
        if(pathname != ""):
            if(os.path.exists(pathname + "\\tesseract.exe")) == True:
                self.lbpath.setText(pathname)        
            else: 
                QMessageBox.information(self,"L???i ?????c file","???????ng d???n kh??ng h???p l???!\nKh??ng t??m th???y file tesseract.exe")
        elif(self.lbpath.text() == ""):
            self.lbpath.setText("???????ng d???n ?????n th?? m???c c??i ?????t Tesseract-OCR")
    #B???t ?????u nh???n di???n
    def start(self): 
        #?????c ???nh
        pytesseract.pytesseract.tesseract_cmd = self.lbpath.text() + "\\tesseract.exe"
        if(self.lbpicpath.text() == "..."): QMessageBox.information(self,"L???i ?????c ???nh","Kh??ng t??m th???y ???nh!\nVui l??ng d??n ???nh v??o ????? ti???p t???c.")
        elif(self.lbpath.text() == "???????ng d???n ?????n th?? m???c c??i ?????t Tesseract-OCR"): QMessageBox.information(self,"L???i th?? vi???n","???????ng d???n ?????n th?? vi???n kh??ng ????ng ho???c th?? vi???n ch??a ???????c c??i ?????t.\nKh??ng th??? t??m th???y file tesseract.exe!")
        else:
            pathname = self.lbpath.text()
            if(os.path.exists(pathname + "\\tesseract.exe")) == True: 
                QApplication.setOverrideCursor(QtGui.QCursor(QtCore.Qt.CursorShape.WaitCursor))
                self.lbpath.setText(pathname)
                if(self.lbpicpath.text() == "Clipboard"): img1 = cv2.imread("temp.png")
                else: img1 = cv2.imread(imgname[0], flags=cv2.IMREAD_COLOR)
                #L???y th??ng s??? ????? s??ng
                bright = self.nmsang.value()
                print(bright)
                #L???y th??ng s??? ????? s???c n??t
                sharp = self.nmsharpen.value()
                #L???y th??ng s??? ????? t????ng ph???n
                contrast = self.nmcontrast.value()
                #L???y th??ng s??? l???c m???
                blur = self.cbblur.currentIndex()
                if(blur == 0): numblur = int(1)
                elif(blur == 1): numblur = int(3)
                elif(blur == 2): numblur = int(5)
                elif(blur == 3): numblur = int(7)
                elif(blur == 4): numblur = int(9)
                #L???y th??ng s??? m??u n???n ???nh
                if(self.rdbden.isChecked() == True): maunen = int(0)
                else: maunen = int(1)
                #L???y th??ng s??? ng??n ng???
                if(self.rdbviet.isChecked() == True): language = "vie"
                else: language = "eng"
                #Check g???p v??n b???n
                if(self.rdbbat.isChecked() == True): gop = bool(True)
                else: gop = bool(False)
                #L???y k??ch th?????c ???nh
                w = img1.shape[1]
                h = img1.shape[0]
                #??i???u ch???nh k??ch th?????c ???nh v??? m???c v???a ph???i t???i ??u cho nh???n di???n
                if(w < 200 and h <200 ):
                    if(w > h):
                        width = int(img1.shape[1]*135/100)
                        height = int(img1.shape[0]*150/100)
                    else:
                        width = int(img1.shape[1]*150/100)
                        height = int(img1.shape[0]*135/100)
                elif(w > 1000 and h > 1000):
                    if(w > h):
                        width = int(img1.shape[1]*60/100)
                        height = int(img1.shape[0]*45/100)
                    else:
                        width = int(img1.shape[1]*45/100)
                        height = int(img1.shape[0]*60/100)
                else:
                    width = w
                    height = h
                img_resized = cv2.resize(img1, (width,height), interpolation=cv2.INTER_AREA)
                #T???o mask 
                mask = np.zeros((height, width, 3), dtype=np.uint8)
                mask[:,:] = [bright,bright,bright]
                #T??ng, gi???m ????? s??ng
                if(bright != 0): img_bright = img_resized + mask
                else: img_bright = img_resized
                #L???c m?????t ???nh 1 (t??y ch???n)
                kernel = np.array([ [0, -1, 0],
                                    [-1, sharp,-1],
                                    [0, -1, 0]  ])
                image_sharp1 = cv2.filter2D(img_bright, ddepth=-(sharp), kernel=kernel)
                #N???u ???nh n???n s??ng:
                if(maunen == 1): gray = cv2.cvtColor(image_sharp1, cv2.COLOR_BGR2GRAY)
                #N???u ???nh n???n t???i:
                else:
                    inverse = cv2.bitwise_not(image_sharp1)
                    gray = cv2.cvtColor(inverse, cv2.COLOR_BGR2GRAY)
                #L???c m??? gi???m nhi???u (t??y ch???n)
                img_blur = cv2.medianBlur(gray,numblur)
                #??i???u ch???nh ng?????ng threshold (ph??n t??ch tr???ng ??en)
                thres = cv2.threshold(img_blur, 0, contrast, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
                #L??m m?????t ???nh 2
                kernel = np.array([ [0, -1, 0],
                                    [-1, 5,-1],
                                    [0, -1, 0]  ])
                image_sharp2 = cv2.filter2D(thres, ddepth=-5, kernel=kernel)
                # Ghi t???m ???nh xu???ng ??? c???ng ????? sau ???? apply OCR
                filename = "{}.png".format(os.getpid())
                cv2.imwrite(filename, image_sharp2)
                self.lbpic2.setPixmap(QtGui.QPixmap(filename))
                # Load ???nh v?? apply nh???n d???ng b???ng Tesseract OCR
                text = pytesseract.image_to_string(Image.open(filename), lang= language)
                # X??a ???nh t???m sau khi nh???n d???ng
                os.remove(filename)
                # In d??ng ch??? nh???n d???ng ???????c
                if text == "" : self.rtbketqua.setPlainText("Kh??ng th??? nh???n d???ng ???????c ch??? n??o!\nVui l??ng ch???nh l???i th??ng s??? ???nh v?? th??? l???i!")
                else:
                    #Lo???i b??? kho???ng c??ch d??i (n???u c??)
                    text1 = str(text).lstrip()
                    text2 = str(text1).replace("  "," ")
                    #In ra plaintext
                    if(gop == True): self.rtbketqua.appendPlainText(text2)  
                    else: self.rtbketqua.setPlainText(text2)
                QApplication.restoreOverrideCursor()
            else:
                QMessageBox.information(self,"L???i ?????c file","???????ng d???n kh??ng h???p l???!\nKh??ng t??m th???y file tesseract.exe")
                QApplication.restoreOverrideCursor()
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
