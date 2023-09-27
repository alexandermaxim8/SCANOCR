from PyQt5 import QtCore, QtGui, QtWidgets
from PyPDF2 import PdfReader, PdfWriter
from PyQt5.QtWidgets import QFileDialog, QWidget
import sys, os, io
import numpy as np
import camera_btn_rc, logo_btn_rc
import img2pdf
from pdf2docx import *
from pdf2image import convert_from_path
from docx2pdf import convert
from PIL import Image

poppler_path = r"poppler-23.08.0\Library\bin"

class Ui_Dialog(object):
    def fileButton_clicked(self):
        self.res = False
        self.res, self.format = QFileDialog.getOpenFileNames(QtWidgets.QDialog(), "Open File", "C:/Users/Asus/Downloads", "PDF File, (*.pdf);; JPEG File, (*.jpeg);; JPG File (*.jpg);; PNG File (*.png);; DOCX, (*docx)")
        if self.res:
            self.filenameLabel.setText(self.res[0])
            if self.format == 'PDF File, (*.pdf)':
                reader = PdfReader(self.res[0])
            elif self.format == 'JPEG File, (*.jpeg)' or self.format == 'JPG File (*.jpg)':
                image = Image.open(self.res[0])
            elif self.format == 'PNG File (*.png)':
                image = Image.open(self.res[0])
            elif self.format == 'DOCX, (*docx)':
                pass

    def proceedButton_clicked(self):
        self.stackedWidget.setCurrentIndex(1)
        self.proceedButton.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor)) 
        
    def saveButton_clicked(self):
        if self.res:
            index = self.extComboBox.currentIndex()
            #self.res, self.format = QFileDialog.getOpenFileNames(QtWidgets.QDialog(), "Open File", "C:/Users/Asus/Downloads", "PDF File, (*.pdf);; JPEG File, (*.jpeg);; JPG File (*.jpg);; PNG File (*.png);; DOCX, (*docx)")
            if self.format == 'PDF File, (*.pdf)':
                if index == 1:
                    images = convert_from_path(pdf_path=self.res[0], poppler_path=poppler_path)                
                    for image in images:
                        img_name = QFileDialog.getSaveFileName(QtWidgets.QDialog(), "Save converted file", self.res[0]+"_converted_", "jpeg (*.jpeg)")
                        image.save(img_name[0], "JPEG")

                elif index == 2:
                    images = convert_from_path(pdf_path=self.res[0], poppler_path=poppler_path)                
                    for image in images:
                        img_name = QFileDialog.getSaveFileName(QtWidgets.QDialog(), "Save converted file", self.res[0]+"_converted_", "png (*.png)")
                        image.save(img_name[0], "PNG")
                elif index == 3:
                    with open(pdf, "rb") as f:
                        reader = PdfReader(f)
                        writer = PdfWriter()
                    pdf = reader
                    docx = self.res[0]
                    conv = Converter(pdf)
                    conv.convert(docx)
                    output_filename, _ = QFileDialog.getSaveFileName(QtWidgets.QDialog(), "Save converted file", self.res[0]+"_converted", "docx (*.docx)")

            elif self.format == 'JPEG File (*.jpeg)':
                if index == 0:
                    image = Image.open(self.res[0])
                    pdf = img2pdf.convert()
                    with open(pdf, "rb") as f:
                        reader = PdfReader(f)
                        writer = PdfWriter()
                    output_filename, _ = QFileDialog.getSaveFileName(QtWidgets.QDialog(), "Save converted file", self.res[0]+"_converted", "PDF (*.pdf)")
                    if output_filename:
                        with open(output_filename, 'wb') as output_file:
                            writer.write(output_file)
                elif index == 1:
                    pass
                elif index == 2:
                    pass
                elif index == 3:
                    
                    output_filename, _ = QFileDialog.getSaveFileName(QtWidgets.QDialog(), "Save converted file", self.res[0]+"_converted", "docx (*.docx)")
            elif self.format == 'PNG File (*.png)':
                if index == 0:
                    image = Image.open(self.res[0])
                    pdf = img2pdf.convert()
                    with open(pdf, "rb") as f:
                        reader = PdfReader(f)
                        writer = PdfWriter()
                    output_filename, _ = QFileDialog.getSaveFileName(QtWidgets.QDialog(), "Save converted file", self.res[0]+"_converted", "PDF (*.pdf)")
                    if output_filename:
                        with open(output_filename, 'wb') as output_file:
                            writer.write(output_file)                  
                elif index == 1:
                    pass
                elif index == 2:
                    pass
                elif index == 3:
                    
                    output_filename, _ = QFileDialog.getSaveFileName(QtWidgets.QDialog(), "Save converted file", self.res[0]+"_converted", "docx (*.docx)")
            elif self.format == 'DOCX File (*.docx)':
                if index == 0:
                    with open(self.res[0], "rb") as f:
                        reader = PdfReader(f)
                        writer = PdfWriter()
                    output_filename, _ = QFileDialog.getSaveFileName(QtWidgets.QDialog(), "Save converted file", self.res[0]+"_converted", "PDF (*.pdf)")
                    if output_filename:
                        with open(output_filename, 'wb') as output_file:
                            writer.write(output_file)
                elif index == 1:
                    pass
                elif index == 2:
                    pass
                elif index == 3:
                    pass

        else:
            pass

    def cancelButton_clicked(self):
        self.res = False
        self.stackedWidget.setCurrentIndex(0)
        self.cancelButton.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor)) 

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(330, 320)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(330, 320))
        Dialog.setMaximumSize(QtCore.QSize(350, 350))
        Dialog.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #36404B, stop:1 #181D23);")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.stackedWidget = QtWidgets.QStackedWidget(Dialog)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.page)
        self.frame.setStyleSheet("QFrame{\n"
"    background: none;\n"
"}\n"
"\n"
"QLabel{\n"
"    color: #ffffff;\n"
"    font: 63 8pt \"Segoe UI Variable Text Semibold\";\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.source = QtWidgets.QLabel(self.frame_4)
        self.source.setObjectName("source")
        self.verticalLayout_3.addWidget(self.source)
        self.filenameLabel = QtWidgets.QLineEdit(self.frame_4)
        self.filenameLabel.setStyleSheet("background-color: rgb(240, 240, 240);\n"
"border-radius: 10px;\n"
"color: rgb(156, 156, 156);\n"
"padding: 3px;")
        self.filenameLabel.setReadOnly(True)
        self.filenameLabel.setObjectName("filenameLabel")
        self.verticalLayout_3.addWidget(self.filenameLabel)
        self.frame_6 = QtWidgets.QFrame(self.frame_4)
        self.frame_6.setMinimumSize(QtCore.QSize(270, 0))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(7)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_2 = QtWidgets.QFrame(self.frame_6)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.fileButton = QtWidgets.QPushButton(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fileButton.sizePolicy().hasHeightForWidth())
        self.fileButton.setSizePolicy(sizePolicy)
        self.fileButton.setMinimumSize(QtCore.QSize(0, 40))
        self.fileButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.fileButton.setStyleSheet("QPushButton{\n"
"    background-color: rgb(75, 87, 106);\n"
"    border-radius: 20px;\n"
"    image: url(:/OCR/icons8-text-40.png);\n"
"    padding: 5px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(42, 49, 58);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(42, 49, 58);\n"
"    border: 2px outset #ffffff;\n"
"}")
        self.fileButton.setText("")
        self.fileButton.setObjectName("fileButton")
        self.horizontalLayout.addWidget(self.fileButton)
        self.fileButton.clicked.connect(self.fileButton_clicked)
        spacerItem = QtWidgets.QSpacerItem(205, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 5)
        self.verticalLayout_4.addWidget(self.frame_2)
        self.verticalLayout_3.addWidget(self.frame_6)
        self.destination = QtWidgets.QLabel(self.frame_4)
        self.destination.setObjectName("destination")
        self.verticalLayout_3.addWidget(self.destination)
        self.extComboBox = QtWidgets.QComboBox(self.frame_4)
        self.extComboBox.setMinimumSize(QtCore.QSize(0, 50))
        self.extComboBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.extComboBox.setStyleSheet("QComboBox{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.006, x2:1, y2:0, stop:0 #6391C1, stop:0.900498 #58A2C2);\n"
"    border-radius: 20px;\n"
"    color: rgb(214, 214, 214);\n"
"    font: 63 16pt \"Segoe UI Variable Text Semibold\";\n"
"    padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"    border: 2px solid #ffffff;\n"
"}\n"
"QComboBox:pressed{\n"
"    border: 0px;\n"
"    background-color: #6391c1;\n"
"}\n"
"QComboBox QAbstractItemView{\n"
"    background-color: rgb(39, 47, 55);\n"
"    selection-background-color: rgb(88, 162, 194);\n"
"}")
        self.extComboBox.setObjectName("extComboBox")
        self.extComboBox.addItem("")
        self.extComboBox.addItem("")
        self.extComboBox.addItem("")
        self.extComboBox.addItem("")
        self.verticalLayout_3.addWidget(self.extComboBox)
        self.frame_5 = QtWidgets.QFrame(self.frame_4)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_5.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem1 = QtWidgets.QSpacerItem(115, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.proceedButton = QtWidgets.QPushButton(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.proceedButton.sizePolicy().hasHeightForWidth())
        self.proceedButton.setSizePolicy(sizePolicy)
        self.proceedButton.setMinimumSize(QtCore.QSize(0, 40))
        self.proceedButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.proceedButton.setStyleSheet("QPushButton{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.006, x2:1, y2:0, stop:0 rgba(38, 215, 1, 255), stop:0.880597 rgba(0, 171, 8, 255));\n"
"    border-radius: 20px;\n"
"    image: url(:/Arrow/icons8-arrow-48 - Copy.png);\n"
"    padding: 5px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(36, 212, 1);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(36, 212, 1);\n"
"    image: url(:/Arrow/icons8-arrow-48-bright.png);\n"
"    border: 2px outset #ffffff;\n"
"}")
        self.proceedButton.setText("")
        self.proceedButton.setIconSize(QtCore.QSize(20, 20))
        self.proceedButton.setObjectName("proceedButton")
        self.horizontalLayout_5.addWidget(self.proceedButton)
        self.proceedButton.clicked.connect(self.proceedButton_clicked)
        self.horizontalLayout_5.setStretch(0, 5)
        self.horizontalLayout_5.setStretch(1, 2)
        self.verticalLayout_3.addWidget(self.frame_5)
        self.horizontalLayout_4.addWidget(self.frame_4)
        self.verticalLayout.addWidget(self.frame)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.page_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.frame_3 = QtWidgets.QFrame(self.page_2)
        self.frame_3.setStyleSheet("background: none;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem3 = QtWidgets.QSpacerItem(20, 58, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.saveButton = QtWidgets.QPushButton(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.saveButton.sizePolicy().hasHeightForWidth())
        self.saveButton.setSizePolicy(sizePolicy)
        self.saveButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.saveButton.setStyleSheet("QPushButton {\n"
"    border-radius: 20px;\n"
"    color: #ffffff;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.006, x2:1, y2:0, stop:0 rgba(38, 215, 1, 255), stop:0.880597 rgba(0, 171, 8, 255));\n"
"    font: 63 16pt \"Segoe UI Variable Text Semibold\";\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(36, 212, 1);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(36, 212, 1);\n"
"    border: 2px solid #ffffff;\n"
"}")
        self.saveButton.setObjectName("saveButton")
        self.verticalLayout_2.addWidget(self.saveButton)
        self.saveButton.clicked.connect(self.saveButton_clicked)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem4)
        self.cancelButton = QtWidgets.QPushButton(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cancelButton.sizePolicy().hasHeightForWidth())
        self.cancelButton.setSizePolicy(sizePolicy)
        self.cancelButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cancelButton.setStyleSheet("QPushButton {\n"
"    border-radius: 20px;\n"
"    color: #ffffff;\n"
"    background-color: rgb(75, 87, 106);\n"
"    color: rgb(214, 214, 214);\n"
"    font: 63 16pt \"Segoe UI Variable Text Semibold\";\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(42, 49, 58);\n"
"}\n"
"QPushButton:pressed{\n"
"    border: 2px solid #ffffff;\n"
"}")
        self.cancelButton.setObjectName("cancelButton")
        self.verticalLayout_2.addWidget(self.cancelButton)
        self.cancelButton.clicked.connect(self.cancelButton_clicked)
        spacerItem5 = QtWidgets.QSpacerItem(20, 58, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem5)
        self.verticalLayout_2.setStretch(0, 2)
        self.verticalLayout_2.setStretch(1, 2)
        self.verticalLayout_2.setStretch(2, 1)
        self.verticalLayout_2.setStretch(3, 2)
        self.verticalLayout_2.setStretch(4, 2)
        self.horizontalLayout_2.addWidget(self.frame_3)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.horizontalLayout_2.setStretch(0, 2)
        self.horizontalLayout_2.setStretch(1, 7)
        self.horizontalLayout_2.setStretch(2, 2)
        self.stackedWidget.addWidget(self.page_2)
        self.horizontalLayout_3.addWidget(self.stackedWidget)

        self.retranslateUi(Dialog)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.source.setText(_translate("Dialog", "Source:"))
        self.filenameLabel.setText(_translate("Dialog", "pdf, jpeg, png, or docx only"))
        self.destination.setText(_translate("Dialog", "Destination:"))
        self.extComboBox.setItemText(0, _translate("Dialog", ".pdf"))
        self.extComboBox.setItemText(1, _translate("Dialog", ".jpeg"))
        self.extComboBox.setItemText(2, _translate("Dialog", ".png"))
        self.extComboBox.setItemText(3, _translate("Dialog", ".docx"))
        self.saveButton.setText(_translate("Dialog", "SAVE"))
        self.cancelButton.setText(_translate("Dialog", "CANCEL"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
