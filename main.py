import os
import camera_btn_rc, logo_btn_rc, camfile, convert, mergesplit, saveas_2
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMainWindow
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import pyqtSlot

from opencv_cam_return_6 import Scanner

import camera_btn_rc
import logo_btn_rc

import numpy as np
from pdf2image import convert_from_path
from PIL import Image
import cv2
import pytesseract
from functools import partial

poppler_path=r"poppler-23.08.0\Library\bin"
pytesseract.pytesseract.tesseract_cmd = r"pytesseract\tesseract.exe"



def styleScrollbar():
    sStyle = """
        QScrollBar:vertical{
            border: none;
            background-color: rgb(59, 59, 90);
            width: 14px;
            margin: 15px 0 15px 0;
            border-radius: 0px;
        }
        QScrollBar::handle:vertical{
            background-color: rgb(80, 80, 122);
            min-height: 30px;
            border-radius: 7px;
        }
        QScrollBar::handle:vertical:hover{
            background-color: #58A2C2;
        }
        QScrollBar::handle:vertical:pressed{
            background-color: #6391C1;
        }
        QScrollBar::sub-line:vertical{
            border:none;
            background-color: rgb(59, 59, 90);
            height: 15px;
            border-top-left-radius: 7px;
            border-top-right-radius: 7px;
            subcontrol-position: top;
            subcontrol-origin: margin;
        }
        QScrollBar::sub-line:vertical:hover{
            background-color: #58A2C2;
        }
        QScrollBar::sub-line:vertical:pressed{
            background-color: #6391C1;
        }
        QScrollBar::add-line:vertical{
            border:none;
            background-color: rgb(59, 59, 90);
            height: 15px;
            border-bottom-left-radius: 7px;
            border-bottom-right-radius: 7px;
            subcontrol-position: bottom;
            subcontrol-origin: margin;
        }
        QScrollBar::add-line:vertical:hover{
            background-color: #58A2C2;
        }
        QScrollBar::add-line:vertical:pressed{
            background-color: #6391C1;
        }
        QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical{
            background:none;
        }
        QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical{
            background:none;
        }

        QScrollBar:horizontal{
            border: none;
            background-color: rgb(59, 59, 90);
            height: 14px;
            margin: 0 15px 0 15px;
            border-radius: 0px;
        }
        QScrollBar::handle:horizontal{
            background-color: rgb(80, 80, 122);
            min-width: 30px;
            border-radius: 7px;
        }
        QScrollBar::handle:horizontal:hover{
            background-color: #58A2C2;
        }
        QScrollBar::handle:horizontal:pressed{
            background-color: #6391C1;
        }
        QScrollBar::sub-line:horizontal{
            border:none;
            background-color: rgb(59, 59, 90);
            width: 15px;
            border-top-left-radius: 7px;
            border-bottom-left-radius: 7px;
            subcontrol-position: left;
            subcontrol-origin: margin;
        }
        QScrollBar::sub-line:horizontal:hover{
            background-color: #58A2C2;
        }
        QScrollBar::sub-line:horizontal:pressed{
            background-color: #6391C1;
        }
        QScrollBar::add-line:horizontal{
            border:none;
            background-color: rgb(59, 59, 90);
            width: 15px;
            border-top-right-radius: 7px;
            border-bottom-right-radius: 7px;
            subcontrol-position: right;
            subcontrol-origin: margin;
        }
        QScrollBar::add-line:horizontal:hover{
            background-color: #58A2C2;
        }
        QScrollBar::add-line:horizontal:pressed{
            background-color: #6391C1;
        }
        QScrollBar::left-arrow:horizontal, QScrollBar::right-arrow:horizontal{
            background:none;
        }
        QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal{
            background:none;
        }
    """
    return sStyle

def styleButton(prevnext):
    if prevnext==1:
            sStyle = """
                QPushButton{
	                background-color: qlineargradient(spread:pad, x1:0, y1:0.006, x2:1, y2:0, stop:0 rgba(38, 215, 1, 255), stop:0.880597 rgba(0, 171, 8, 255));
                        border-radius: 20px;
                }
                QPushButton:hover{
	                background-color: rgb(36, 212, 1);
                }
                QPushButton:pressed{
	                background-color: #ececec
                }
                
                """
    elif prevnext==2:
            sStyle = """
                QPushButton{
	                background-color: qlineargradient(spread:pad, x1:0, y1:0.006, x2:1, y2:0, stop:0.18408 rgba(210, 72, 0, 255), stop:1 rgba(254, 135, 97, 255));
                        border-radius: 20px;
                }
                QPushButton:hover{
	                background-color: rgb(252, 133, 93);
                }
                QPushButton:pressed{
	                background-color: #ececec
                }
                
                """
    else:
            sStyle = """
                QPushButton{
	                background-color: qlineargradient(spread:pad, x1:0, y1:0.006, x2:1, y2:0, stop:0 #6391C1, stop:0.900498 #58A2C2);
                        border-radius: 20px;
                }
                QPushButton:hover{
	                background-color: #6391c1;
                }
                QPushButton:pressed{
	                background-color: #ececec
                }
                
                """
            
    return sStyle

class Ui_MainWindow(object):
    def cam_captured(self):
        self.cam_pressed = 1

    def saveas(self):
        self.window = saveas_2.QtWidgets.QDialog()
        self.ui = saveas_2.Ui_Dialog()
        self.ui.setupUi(self.window)
        self.ui.saveButton.clicked.connect(lambda: self.ui.processing(self.temp_png, self.isOCR))
        self.window.show()
               
    @pyqtSlot()
    def onClicked(self, index):
        self.cap = cv2.VideoCapture(0)
        while (self.cap.isOpened()):
            ret, frame = self.cap.read()
            if ret == True:
                self.displayImage(frame,index, 1)
                cv2.waitKey()
            else:
                print('return not found')
                self.cap.release()
                cv2.destroyAllWindows()

    def displayImage(self, image, index, window=1):
        print(index)
        image = cv2.resize(image, (720, 480))
        qformat = QImage.Format_Indexed8
        if len(image.shape) == 3:
            if image.shape[2] == 4:
                qformat = QImage.Format_RGBA8888
            else:
                qformat = QImage.Format_RGB888
        outImage = QImage(image, image.shape[1], image.shape[0], image.strides[0], qformat)
        outImage = outImage.rgbSwapped()
        outImage = outImage.mirrored(True, False)
        self.cameraLabel.setPixmap(QPixmap.fromImage(outImage))
        self.cameraLabel.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.img_name = False
        if self.cam_pressed == 1:
            if self.isOCR == False:
                pil_image = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
                flipped_pil_image=pil_image.transpose(Image.FLIP_LEFT_RIGHT)
                image = cv2.cvtColor(np.array(flipped_pil_image), cv2.COLOR_RGB2BGR)
            self.img_name = f"temp/temp_{index}.png"
            self.img_name2 = f"temp2/temp_{index}.png"
            cv2.imwrite(self.img_name, image)
            cv2.imwrite(self.img_name2, image)
            self.cam_pressed = 0
            print("berhasil_capture")
            self.stackedWidget.setCurrentIndex(3)
            self.cap.release()
            cv2.destroyAllWindows()
        elif self.stackedWidget.currentIndex()!=2:
            self.cap.release()
            cv2.destroyAllWindows()
            return None     

    def addButton_clicked(self):
        index = self.current_page_index + 1
        self.stackedWidget.setCurrentIndex(2)
        self.onClicked(index)
        if self.img_name:
            self.temp_png.append(self.img_name)
            self.temp_png2.append(self.img_name2)
            self.current_page_index = index
            self.show_page(index)

    def retakeButton_clicked(self):
        index = self.current_page_index
        self.stackedWidget.setCurrentIndex(2)
        self.onClicked(index)
        if self.img_name:
            self.temp_png[index] = self.img_name
            self.temp_png2[index] = self.img_name2
            self.show_page(index)

    def show_next_page(self):
        if(self.stackedWidget.currentIndex()==1):
            if self.current_page_index < len(self.temp_png) - 2:
                self.nextButton.setStyleSheet(styleButton(0))
                self.previousButton.setStyleSheet(styleButton(0))
                self.current_page_index += 1
            elif self.current_page_index == len(self.temp_png) - 2:
                self.nextButton.setStyleSheet(styleButton(1))
                self.previousButton.setStyleSheet(styleButton(0))
                self.current_page_index += 1
            elif self.current_page_index == len(self.temp_png) - 1:
                self.saveas()
            self.show_page(self.current_page_index)
            print(self.current_page_index)
        elif(self.stackedWidget.currentIndex()==3):
            if self.current_page_index < len(self.temp_png) - 2:
                self.nextButton2.setStyleSheet(styleButton(0))
                self.prevButton2.setStyleSheet(styleButton(0))
                self.current_page_index += 1
            elif self.current_page_index == len(self.temp_png) - 2:
                self.nextButton2.setStyleSheet(styleButton(1))
                self.prevButton2.setStyleSheet(styleButton(0))
                self.current_page_index += 1
            elif self.current_page_index == len(self.temp_png) - 1:
                self.saveas()
            self.show_page(self.current_page_index)
            print(self.current_page_index)


    def show_previous_page(self):
        if(self.stackedWidget.currentIndex()==1):
            if self.current_page_index == 1:
                self.previousButton.setStyleSheet(styleButton(2))
                self.nextButton.setStyleSheet(styleButton(0))
                self.current_page_index -= 1
            elif self.current_page_index > 1:
                self.nextButton.setStyleSheet(styleButton(0))
                self.previousButton.setStyleSheet(styleButton(0))
                self.current_page_index -= 1
            elif self.current_page_index == 0:
                self.home_clicked()
            self.show_page(self.current_page_index)
            print(self.current_page_index)
        elif(self.stackedWidget.currentIndex()==3):
            if self.current_page_index == 1:
                self.prevButton2.setStyleSheet(styleButton(2))
                self.nextButton2.setStyleSheet(styleButton(0))
                self.current_page_index -= 1
            elif self.current_page_index > 1:
                self.nextButton2.setStyleSheet(styleButton(0))
                self.prevButton2.setStyleSheet(styleButton(0))
                self.current_page_index -= 1
            elif self.current_page_index == 0:
                self.home_clicked()
            self.show_page(self.current_page_index)
    def dari_opencv(self):
        scanner=Scanner('gambar',self.temp_png2[self.current_page_index])
        return scanner
    def adjButton_clicked(self):
        if self.crop_clicked == False:

            self.crop_clicked= True
            scanner = self.dari_opencv()
            scanner.inisiasi_awal()
            scanner.mouse()
            scanner.trackbar_parameter()
            cv2.namedWindow('parameter')

            while True:
                scanner.camera_atau_gambar()
                _, contour_frame=scanner.contour()
                frame_BGR= scanner.resize_full()
                if self.isOCR == False:
                    frame_BGR=scanner.kertas(frame_BGR)
                preview=cv2.resize(frame_BGR, dsize=(int(frame_BGR.shape[1]/2), int(frame_BGR.shape[0]/2)))
                cv2.imshow("kontur", contour_frame)
                cv2.imshow("preview", preview)
                cv2.moveWindow("preview",0,300)

                frame_RGB   = cv2.cvtColor(frame_BGR, cv2.COLOR_BGR2RGB)
                tombol = cv2.waitKey(1)
                if (tombol == ord("s")or (tombol == 27)):
                    self.crop_gambar=frame_RGB
                    self.kosong=False
                    self.crop_clicked = False
                    path_simpan=f"temp/temp_{self.current_page_index}.png"
                    self.temp_png[self.current_page_index] = path_simpan
                    cv2.destroyWindow("kontur")
                    cv2.destroyWindow("parameter")
                    cv2.destroyWindow("preview")
                    cv2.imwrite(path_simpan, frame_BGR)
                    self.show_page(self.current_page_index)
                    return None
                
    def show_page(self, index):
        if self.isOCR == True:
            self.statusbar.showMessage(f"Pages: {index+1}/{len(self.temp_png)}")
        else:
            self.statusbar.showMessage(f"Pages: {index+1}/{len(self.temp_png)} (adjust/crop to scan!)")
        if(self.stackedWidget.currentIndex()==1):
            if 0 <= index < len(self.temp_png):
                if self.kosong is False:
                    frame=self.crop_gambar
                    image = QPixmap.fromImage(QImage(frame.data, frame.shape[1], frame.shape[0], frame.shape[1] * 3, QImage.Format_RGB888))
                    self.kosong =True
                else:
                    image = QPixmap(self.temp_png[index])

                self.previewLabel.setPixmap(image)
                self.previewLabel.setAlignment(QtCore.Qt.AlignCenter)
                self.nextButton.setStyleSheet(styleButton(0))
                self.previousButton.setStyleSheet(styleButton(0))
                if index == len(self.temp_png)-1:
                    self.nextButton.setStyleSheet(styleButton(1))
                if index == 0:
                    self.previousButton.setStyleSheet(styleButton(2))
        elif(self.stackedWidget.currentIndex()==3):
            if 0 <= index < len(self.temp_png):
                image = QPixmap(self.temp_png[index])
                self.previewLabel2.setPixmap(image)
                self.previewLabel2.setAlignment(QtCore.Qt.AlignCenter)
                self.nextButton2.setStyleSheet(styleButton(0))
                self.prevButton2.setStyleSheet(styleButton(0))
                if index == len(self.temp_png)-1:
                    self.nextButton2.setStyleSheet(styleButton(1))
                if index == 0:
                    self.prevButton2.setStyleSheet(styleButton(2))

    def open_camviewer(self):
        self.stackedWidget.setCurrentIndex(2)
        self.window.close()
        self.temp_png = []
        self.temp_png2 = []
        self.onClicked(0)
        if self.img_name:
            self.temp_png.append(self.img_name)
            self.temp_png2.append(self.img_name2)
            print(self.temp_png)
            self.show_page(0)
            self.current_page_index = 0

    def open_docviewer(self):
        res, format = QFileDialog.getOpenFileNames(QtWidgets.QDialog(), "Open File", "C:/Users/Asus/Downloads", "JPG File (*.jpg);;PNG File (*.png);;PDF File (*.pdf)")
        saving_folder = r"temp"
        saving_folder2 = r"temp2"
        self.temp_png = []
        self.temp_png2 = []
        if (format == "PDF File (*.pdf)"):
            c=0
            for i in range(len(res)):
                pages=convert_from_path(pdf_path=res[i], poppler_path=poppler_path)
                for page in pages:
                    img_name = f"temp_{c}.png"
                    page.save(os.path.join(saving_folder, img_name), "PNG")
                    page.save(os.path.join(saving_folder2, img_name), "PNG")
                    self.temp_png.append(os.path.join(saving_folder, img_name))
                    self.temp_png2.append(os.path.join(saving_folder2, img_name))
                    c+=1
                
        elif(format == "JPG File (*.jpg)" or format == "PNG File (*.png)"):
            for i in range(len(res)):
                img_name = f"temp_{i}.{format[12:15]}"
                image = Image.open(res[i])
                image.save(os.path.join(saving_folder, img_name))
                image.save(os.path.join(saving_folder2, img_name))
                self.temp_png.append(os.path.join(saving_folder, img_name))
                self.temp_png2.append(os.path.join(saving_folder2, img_name))
        else:
            return
        print(self.temp_png)
        self.previousButton.setStyleSheet(styleButton(2))
        self.nextButton.setStyleSheet(styleButton(1))
        if len(self.temp_png)>0:
            self.nextButton.setStyleSheet(styleButton(0))
        self.current_page_index = 0
        self.stackedWidget.setCurrentIndex(1)
        self.show_page(0)
        self.window.close()

    def open_convert(self):
        self.window = convert.QtWidgets.QDialog()
        self.ui = convert.Ui_Dialog()
        self.ui.setupUi(self.window)
        self.window.show()

    def open_mergesplit(self):
        self.window = mergesplit.QtWidgets.QDialog()
        self.ui = mergesplit.Ui_Dialog()
        self.ui.setupUi(self.window)
        self.window.show()

    def open_OCR(self):
        self.isOCR = True
        self.window = camfile.QtWidgets.QDialog()
        self.ui = camfile.Ui_Dialog()
        self.ui.setupUi(self.window)
        self.ui.camButton.clicked.connect(self.open_camviewer)
        self.ui.locfileButton.clicked.connect(self.open_docviewer)
        self.window.show()

    def open_docscan(self):
        self.isOCR = False
        self.window = camfile.QtWidgets.QDialog()
        self.ui = camfile.Ui_Dialog()
        self.ui.setupUi(self.window)
        self.ui.locfileButton.clicked.connect(self.open_docviewer)
        self.ui.camButton.clicked.connect(self.open_camviewer)
        self.window.show()
        
    def setupUi(self, MainWindow):
        self.kosong= True
        self.crop_clicked= False
    
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1004, 824)
        MainWindow.setAnimated(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #36404B, stop:1 #181D23);")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("background: none;")
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_5 = QtWidgets.QFrame(self.frame)
        self.frame_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_5.setLineWidth(0)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.Header = QtWidgets.QFrame(self.frame_5)
        self.Header.setMinimumSize(QtCore.QSize(0, 50))
        self.Header.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0.006, x2:1, y2:0, stop:0 #6391C1, stop:0.900498 #58A2C2);\n"
"border-bottom-left-radius: 20px;\n"
"border-bottom-right-radius: 20px;")
        self.Header.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Header.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Header.setObjectName("Header")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.Header)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.pushButton_2 = QtWidgets.QPushButton(self.Header)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("background: none;")
        self.pushButton_2.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Logo/SCANOCR_logo_white.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(200, 200))
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_5.addWidget(self.pushButton_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.verticalLayout_5.addWidget(self.Header)
        self.horizontalLayout.addWidget(self.frame_5)
        self.verticalLayout.addWidget(self.frame)
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_2 = QtWidgets.QFrame(self.page)
        self.frame_2.setAutoFillBackground(False)
        self.frame_2.setStyleSheet("background: none;\n"
"\n"
"\n"
"\n"
"")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setLineWidth(0)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setContentsMargins(40, 40, 40, 0)
        self.horizontalLayout_2.setSpacing(40)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_9 = QtWidgets.QFrame(self.frame_2)
        self.frame_9.setMaximumSize(QtCore.QSize(922, 414))
        self.frame_9.setMaximumSize(QtCore.QSize(1050, 500))
        self.frame_9.setStyleSheet("QFrame {\n"
"    border-radius: 20px;\n"
"    background-color: #4B576A;\n"
"}\n"
"\n"
"QPushButton{\n"
"    background-color: #ffffff;\n"
"    border-radius: 10px;\n"
"    font: 63 8pt \"Segoe UI Variable Text Semibold\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #ddd;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    border-radius: 20px;\n"
"}")
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_9)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label = QtWidgets.QLabel(self.frame_9)
        self.label.setStyleSheet("border-radius: 20px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.horizontalLayout_7.addWidget(self.label)
        homepage = QPixmap(r"images\icons\homepage.jpg")
        self.label.setPixmap(homepage)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setStyleSheet("border-radius: 20px;")
        homepage = QPixmap(r"images\icons\SCANOCR_foreveryone.png")
        self.label.setPixmap(homepage)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.horizontalLayout_2.addWidget(self.frame_9)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.page)
        self.frame_3.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame_3.setStyleSheet("QFrame{\n"
"    background: none;\n"
"}\n"
"\n"
"QToolButton {\n"
"    font: 63 10pt \"Segoe UI Variable Text Semibold\";\n"
"    color: rgb(75, 87, 106);\n"
"    border-radius: 20px;\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"    color: rgb(31, 37, 45);\n"
"}")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(80, 30, 80, 50)
        self.gridLayout.setSpacing(20)
        self.gridLayout.setObjectName("gridLayout")
        self.ocrButton = QtWidgets.QToolButton(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ocrButton.sizePolicy().hasHeightForWidth())
        self.ocrButton.setSizePolicy(sizePolicy)
        self.ocrButton.setMinimumSize(QtCore.QSize(170, 79))
        self.ocrButton.setMaximumSize(QtCore.QSize(500, 16777215))
        self.ocrButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ocrButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.ocrButton.setStyleSheet("QToolButton{\n"
"    background-color: #EF9595;\n"
"}\n"
"QToolButton:hover{\n"
"    background-color: rgb(255, 85, 127);\n"
"}")
        self.ocrButton.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.ocrButton.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.ocrButton.setAutoRaise(False)
        self.ocrButton.setArrowType(QtCore.Qt.NoArrow)
        self.ocrButton.setObjectName("ocrButton")
        self.gridLayout.addWidget(self.ocrButton, 0, 1, 1, 1)
        self.scanButton = QtWidgets.QToolButton(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scanButton.sizePolicy().hasHeightForWidth())
        self.scanButton.setSizePolicy(sizePolicy)
        self.scanButton.setMinimumSize(QtCore.QSize(170, 79))
        self.scanButton.setMaximumSize(QtCore.QSize(500, 16777215))
        self.scanButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.scanButton.setStyleSheet("QToolButton{\n"
"    background-color: #F1C27B;\n"
"}\n"
"QToolButton:hover{\n"
"    background-color: rgb(255, 170, 0);\n"
"}")
        self.scanButton.setObjectName("scanButton")
        self.gridLayout.addWidget(self.scanButton, 1, 1, 1, 1)
        self.convButton = QtWidgets.QToolButton(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.convButton.sizePolicy().hasHeightForWidth())
        self.convButton.setSizePolicy(sizePolicy)
        self.convButton.setMinimumSize(QtCore.QSize(170, 79))
        self.convButton.setMaximumSize(QtCore.QSize(500, 16777215))
        self.convButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.convButton.setStyleSheet("QToolButton{\n"
"    background-color: #95BDFF;\n"
"}\n"
"QToolButton:hover{\n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.convButton.setObjectName("convButton")
        self.gridLayout.addWidget(self.convButton, 0, 2, 1, 1)
        self.mergesplitButton = QtWidgets.QToolButton(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mergesplitButton.sizePolicy().hasHeightForWidth())
        self.mergesplitButton.setSizePolicy(sizePolicy)
        self.mergesplitButton.setMinimumSize(QtCore.QSize(170, 79))
        self.mergesplitButton.setMaximumSize(QtCore.QSize(500, 16777215))
        self.mergesplitButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.mergesplitButton.setStyleSheet("QToolButton{\n"
"    background-color: #CEEDC7;\n"
"}\n"
"QToolButton:hover{\n"
"    background-color: rgb(170, 255, 127);\n"
"}")
        self.mergesplitButton.setObjectName("mergesplitButton")
        self.gridLayout.addWidget(self.mergesplitButton, 1, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 0, 3, 1, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 4)
        self.gridLayout.setColumnStretch(2, 4)
        self.gridLayout.setColumnStretch(3, 1)
        self.verticalLayout_2.addWidget(self.frame_3)
        self.verticalLayout_2.setStretch(0, 7)
        self.verticalLayout_2.setStretch(1, 4)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.page_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_4 = QtWidgets.QFrame(self.page_2)
        self.frame_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.scrollArea = QtWidgets.QScrollArea(self.frame_4)
        self.scrollArea.setStyleSheet(styleScrollbar())
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 100, 30))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.previewLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.previewLabel.setStyleSheet("background: none;")
        self.previewLabel.setText("")
        self.previewLabel.setObjectName("previewLabel")
        self.verticalLayout_6.addWidget(self.previewLabel)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_4.addWidget(self.scrollArea)
        self.frame_7 = QtWidgets.QFrame(self.frame_4)
        self.frame_7.setStyleSheet("QFrame{\n"
"    border-top-left-radius: 20px;\n"
"    border-top-right-radius: 20px;\n"
"    background-color: #4B576A;\n"
"}\n"
"QPushButton{\n"
"    border-radius: 20px;\n"
"}")
        self.frame_7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.previousButton = QtWidgets.QPushButton(self.frame_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.previousButton.sizePolicy().hasHeightForWidth())
        self.previousButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.previousButton.setFont(font)
        self.previousButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.previousButton.setStyleSheet("QPushButton{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.006, x2:1, y2:0, stop:0.18408 rgba(210, 72, 0, 255), stop:1 rgba(254, 135, 97, 255));\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(252, 133, 93);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: #ececec\n"
"}")
        self.previousButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Arrow/icons8-arrow-48.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.previousButton.setIcon(icon1)
        self.previousButton.setIconSize(QtCore.QSize(50, 50))
        self.previousButton.setObjectName("previousButton")
        self.horizontalLayout_4.addWidget(self.previousButton)
        self.adjButton = QtWidgets.QPushButton(self.frame_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.adjButton.sizePolicy().hasHeightForWidth())
        self.adjButton.setSizePolicy(sizePolicy)
        self.adjButton.setMinimumSize(QtCore.QSize(60, 60))
        self.adjButton.setMaximumSize(QtCore.QSize(70, 16777215))
        self.adjButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.adjButton.setStyleSheet("QPushButton{\n"
"    background-color: rgb(42, 49, 58);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(205, 205, 205);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: #ececec\n"
"}")
        self.adjButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/Setting/icons8-adjust-50.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.adjButton.setIcon(icon2)
        self.adjButton.setIconSize(QtCore.QSize(40, 40))
        self.adjButton.setObjectName("adjButton")
        self.adjButton.clicked.connect(self.adjButton_clicked)
        self.horizontalLayout_4.addWidget(self.adjButton)
        self.nextButton = QtWidgets.QPushButton(self.frame_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nextButton.sizePolicy().hasHeightForWidth())
        self.nextButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.nextButton.setFont(font)
        self.nextButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.nextButton.setStyleSheet("QPushButton{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.006, x2:1, y2:0, stop:0 rgba(38, 215, 1, 255), stop:0.880597 rgba(0, 171, 8, 255));\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(36, 212, 1);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: #ececec\n"
"}")
        self.nextButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/Arrow/icons8-arrow-48 - Copy.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.nextButton.setIcon(icon3)
        self.nextButton.setIconSize(QtCore.QSize(50, 50))
        self.nextButton.setObjectName("nextButton")
        self.horizontalLayout_4.addWidget(self.nextButton)
        self.horizontalLayout_4.setStretch(0, 7)
        self.horizontalLayout_4.setStretch(1, 1)
        self.horizontalLayout_4.setStretch(2, 7)
        self.verticalLayout_4.addWidget(self.frame_7)
        self.verticalLayout_4.setStretch(0, 9)
        self.verticalLayout_4.setStretch(1, 1)
        self.verticalLayout_3.addWidget(self.frame_4)
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.page_3)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.cameraLabel = QtWidgets.QLabel(self.page_3)
        self.cameraLabel.setStyleSheet("background-color: #000000; border-radius: 20px;")
        self.cameraLabel.setText("")
        self.cameraLabel.setObjectName("cameraLabel")
        self.verticalLayout_7.addWidget(self.cameraLabel)
        self.frame_8 = QtWidgets.QFrame(self.page_3)
        self.frame_8.setStyleSheet("QFrame { \n"
"    background: none;\n"
"}\n"
"\n"
"QPushButton{\n"
"    image: url(:/CamIcon/icons8-camera-640.png);\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 30px\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(205, 205, 205);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(32, 38, 46);\n"
"    image: url(:/CamIcon/icons8-camera-64.png);\n"
"}\n"
"")
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem4 = QtWidgets.QSpacerItem(507, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem4)
        self.camButton = QtWidgets.QPushButton(self.frame_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.camButton.sizePolicy().hasHeightForWidth())
        self.camButton.setSizePolicy(sizePolicy)
        self.camButton.setMinimumSize(QtCore.QSize(100, 60))
        self.camButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.camButton.setStyleSheet("")
        self.camButton.setText("")
        self.camButton.setDefault(True)
        self.camButton.setFlat(False)
        self.camButton.setObjectName("camButton")
        self.horizontalLayout_6.addWidget(self.camButton)
        spacerItem5 = QtWidgets.QSpacerItem(507, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem5)
        self.verticalLayout_7.addWidget(self.frame_8)
        self.verticalLayout_7.setStretch(0, 8)
        self.verticalLayout_7.setStretch(1, 1)
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.page_4)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.frame_15 = QtWidgets.QFrame(self.page_4)
        self.frame_15.setStyleSheet("")
        self.frame_15.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.frame_15)
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.frame_15)
        self.scrollArea_2.setStyleSheet("")
        self.scrollArea_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 100, 30))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.previewLabel2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.previewLabel2.setStyleSheet(styleScrollbar())
        self.previewLabel2.setText("")
        self.previewLabel2.setObjectName("previewLabel2")
        self.verticalLayout_15.addWidget(self.previewLabel2)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_14.addWidget(self.scrollArea_2)
        self.frame_16 = QtWidgets.QFrame(self.frame_15)
        self.frame_16.setStyleSheet("QFrame{\n"
"    border-top-left-radius: 20px;\n"
"    border-top-right-radius: 20px;\n"
"    background-color: #4B576A;\n"
"}\n"
"QPushButton{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.006, x2:1, y2:0, stop:0 #6391C1, stop:0.900498 #58A2C2);\n"
"    border-radius: 20px;\n"
"    color: #ffffff;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: #6391c1;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: #ececec\n"
"}")
        self.frame_16.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_16)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.prevButton2 = QtWidgets.QPushButton(self.frame_16)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.prevButton2.sizePolicy().hasHeightForWidth())
        self.prevButton2.setSizePolicy(sizePolicy)
        self.prevButton2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.prevButton2.setText("")
        self.prevButton2.setIcon(icon1)
        self.prevButton2.setIconSize(QtCore.QSize(50, 50))
        self.prevButton2.setObjectName("prevButton2")
        self.horizontalLayout_3.addWidget(self.prevButton2)
        self.retakeButton = QtWidgets.QPushButton(self.frame_16)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.retakeButton.sizePolicy().hasHeightForWidth())
        self.retakeButton.setSizePolicy(sizePolicy)
        self.retakeButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.retakeButton.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/RetryAdd/icons8-retry-50.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.retakeButton.setIcon(icon4)
        self.retakeButton.setIconSize(QtCore.QSize(40, 40))
        self.retakeButton.setObjectName("retakeButton")
        self.horizontalLayout_3.addWidget(self.retakeButton)
        self.adjButton2 = QtWidgets.QPushButton(self.frame_16)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.adjButton2.sizePolicy().hasHeightForWidth())
        self.adjButton2.setSizePolicy(sizePolicy)
        self.adjButton2.setMinimumSize(QtCore.QSize(0, 60))
        self.adjButton2.setMaximumSize(QtCore.QSize(70, 16777215))
        self.adjButton2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.adjButton2.setStyleSheet("QPushButton{\n"
"    background-color: rgb(42, 49, 58);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(205, 205, 205);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: #ececec\n"
"}")
        self.adjButton2.setText("")
        self.adjButton2.setIcon(icon2)
        self.adjButton2.setIconSize(QtCore.QSize(40, 40))
        self.adjButton2.setObjectName("adjButton2")
        self.adjButton2.clicked.connect(self.adjButton_clicked)
        self.horizontalLayout_3.addWidget(self.adjButton2)
        self.addButton = QtWidgets.QPushButton(self.frame_16)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addButton.sizePolicy().hasHeightForWidth())
        self.addButton.setSizePolicy(sizePolicy)
        self.addButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.addButton.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/RetryAdd/icons8-add-50.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.addButton.setIcon(icon5)
        self.addButton.setIconSize(QtCore.QSize(40, 40))
        self.addButton.setObjectName("addButton")
        self.horizontalLayout_3.addWidget(self.addButton)
        self.nextButton2 = QtWidgets.QPushButton(self.frame_16)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nextButton2.sizePolicy().hasHeightForWidth())
        self.nextButton2.setSizePolicy(sizePolicy)
        self.nextButton2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.nextButton2.setText("")
        self.nextButton2.setIcon(icon3)
        self.nextButton2.setIconSize(QtCore.QSize(50, 50))
        self.nextButton2.setObjectName("nextButton2")
        self.horizontalLayout_3.addWidget(self.nextButton2)
        self.horizontalLayout_3.setStretch(0, 6)
        self.horizontalLayout_3.setStretch(1, 6)
        self.horizontalLayout_3.setStretch(2, 2)
        self.horizontalLayout_3.setStretch(3, 6)
        self.horizontalLayout_3.setStretch(4, 6)
        self.verticalLayout_14.addWidget(self.frame_16)
        self.verticalLayout_14.setStretch(0, 9)
        self.verticalLayout_14.setStretch(1, 1)
        self.verticalLayout_13.addWidget(self.frame_15)
        self.stackedWidget.addWidget(self.page_4)
        self.verticalLayout.addWidget(self.stackedWidget)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 15)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1004, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton_2.clicked.connect(self.home_clicked)
        self.ocrButton.clicked.connect(self.open_OCR)
        self.scanButton.clicked.connect(self.open_docscan)
        self.convButton.clicked.connect(self.open_convert)
        self.mergesplitButton.clicked.connect(self.open_mergesplit)
        self.previousButton.clicked.connect(self.show_previous_page)
        self.camButton.clicked.connect(self.cam_captured)
        self.prevButton2.clicked.connect(self.show_previous_page)
        self.retakeButton.clicked.connect(self.retakeButton_clicked)
        self.addButton.clicked.connect(self.addButton_clicked)
        self.nextButton.clicked.connect(self.show_next_page)
        self.nextButton2.clicked.connect(self.show_next_page)
        self.cam_pressed=0

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ocrButton.setText(_translate("MainWindow", "OCR"))
        self.scanButton.setText(_translate("MainWindow", "Document Scanning"))
        self.convButton.setText(_translate("MainWindow", "Convert Format"))
        self.mergesplitButton.setText(_translate("MainWindow", "Merge/Split (PDF)"))

    def home_clicked(self):
        self.stackedWidget.setCurrentIndex(0)
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
