import camera_btn_rc, logo_btn_rc, camfile, convert, imageadj, mergesplit, saveas
from PyQt5 import QtCore, QtGui, QtWidgets



class Ui_MainWindow(object):
    def open_convert(self):
        self.window = convert.QtWidgets.QDialog()
        convert.Ui_Dialog().setupUi(self.window)
        self.window.show()

    def open_mergesplit(self):
        self.window = mergesplit.QtWidgets.QDialog()
        mergesplit.Ui_Dialog().setupUi(self.window)
        self.window.show()

    def open_OCR(self):
        self.window = camfile.QtWidgets.QDialog()
        camfile.Ui_Dialog().setupUi(self.window)
        self.window.show()

    def open_docscan(self):
        self.window = camfile.QtWidgets.QDialog()
        camfile.Ui_Dialog().setupUi(self.window)
        self.window.show()        

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(986, 822)
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
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.frame_14 = QtWidgets.QFrame(self.frame_9)
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_14)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.recentButton1 = QtWidgets.QPushButton(self.frame_14)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.recentButton1.sizePolicy().hasHeightForWidth())
        self.recentButton1.setSizePolicy(sizePolicy)
        self.recentButton1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.recentButton1.setStyleSheet("QPushButton{\n"
"    background-color: rgb(75, 87, 106);\n"
"    color: #fff;\n"
"    text-align: left;\n"
"}\n"
"QPushButton:hover{\n"
"    text-decoration: underline;\n"
"}\n"
"QPushButton:pressed{\n"
"    color: #000000;\n"
"}")
        self.recentButton1.setFlat(False)
        self.recentButton1.setObjectName("recentButton1")
        self.verticalLayout_8.addWidget(self.recentButton1)
        self.recentFile1 = QtWidgets.QPushButton(self.frame_14)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.recentFile1.sizePolicy().hasHeightForWidth())
        self.recentFile1.setSizePolicy(sizePolicy)
        self.recentFile1.setMinimumSize(QtCore.QSize(90, 25))
        self.recentFile1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.recentFile1.setText("")
        self.recentFile1.setObjectName("recentFile1")
        self.verticalLayout_8.addWidget(self.recentFile1)
        self.verticalLayout_8.setStretch(0, 1)
        self.verticalLayout_8.setStretch(1, 8)
        self.horizontalLayout_7.addWidget(self.frame_14)
        self.frame_10 = QtWidgets.QFrame(self.frame_9)
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_10)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.recentButton2 = QtWidgets.QPushButton(self.frame_10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.recentButton2.sizePolicy().hasHeightForWidth())
        self.recentButton2.setSizePolicy(sizePolicy)
        self.recentButton2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.recentButton2.setStyleSheet("QPushButton{\n"
"    background-color: rgb(75, 87, 106);\n"
"    color: #fff;\n"
"    text-align: left;\n"
"}\n"
"QPushButton:hover{\n"
"    text-decoration: underline;\n"
"}\n"
"QPushButton:pressed{\n"
"    color: #000000;\n"
"}")
        self.recentButton2.setFlat(False)
        self.recentButton2.setObjectName("recentButton2")
        self.verticalLayout_9.addWidget(self.recentButton2)
        self.recentFile2 = QtWidgets.QPushButton(self.frame_10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.recentFile2.sizePolicy().hasHeightForWidth())
        self.recentFile2.setSizePolicy(sizePolicy)
        self.recentFile2.setMinimumSize(QtCore.QSize(90, 25))
        self.recentFile2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.recentFile2.setText("")
        self.recentFile2.setObjectName("recentFile2")
        self.verticalLayout_9.addWidget(self.recentFile2)
        self.verticalLayout_9.setStretch(0, 1)
        self.verticalLayout_9.setStretch(1, 8)
        self.horizontalLayout_7.addWidget(self.frame_10)
        self.frame_11 = QtWidgets.QFrame(self.frame_9)
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame_11)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.recentButton3 = QtWidgets.QPushButton(self.frame_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.recentButton3.sizePolicy().hasHeightForWidth())
        self.recentButton3.setSizePolicy(sizePolicy)
        self.recentButton3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.recentButton3.setStyleSheet("QPushButton{\n"
"    background-color: rgb(75, 87, 106);\n"
"    color: #fff;\n"
"    text-align: left;\n"
"}\n"
"QPushButton:hover{\n"
"    text-decoration: underline;\n"
"}\n"
"QPushButton:pressed{\n"
"    color: #000000;\n"
"}")
        self.recentButton3.setObjectName("recentButton3")
        self.verticalLayout_10.addWidget(self.recentButton3)
        self.recentFile3 = QtWidgets.QPushButton(self.frame_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.recentFile3.sizePolicy().hasHeightForWidth())
        self.recentFile3.setSizePolicy(sizePolicy)
        self.recentFile3.setMinimumSize(QtCore.QSize(90, 25))
        self.recentFile3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.recentFile3.setText("")
        self.recentFile3.setObjectName("recentFile3")
        self.verticalLayout_10.addWidget(self.recentFile3)
        self.verticalLayout_10.setStretch(0, 1)
        self.verticalLayout_10.setStretch(1, 8)
        self.horizontalLayout_7.addWidget(self.frame_11)
        self.frame_12 = QtWidgets.QFrame(self.frame_9)
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.frame_12)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.recentButton4 = QtWidgets.QPushButton(self.frame_12)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.recentButton4.sizePolicy().hasHeightForWidth())
        self.recentButton4.setSizePolicy(sizePolicy)
        self.recentButton4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.recentButton4.setStyleSheet("QPushButton{\n"
"    background-color: rgb(75, 87, 106);\n"
"    color: #fff;\n"
"    text-align: left;\n"
"}\n"
"QPushButton:hover{\n"
"    text-decoration: underline;\n"
"}\n"
"QPushButton:pressed{\n"
"    color: #000000;\n"
"}")
        self.recentButton4.setObjectName("recentButton4")
        self.verticalLayout_11.addWidget(self.recentButton4)
        self.recentFile4 = QtWidgets.QPushButton(self.frame_12)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.recentFile4.sizePolicy().hasHeightForWidth())
        self.recentFile4.setSizePolicy(sizePolicy)
        self.recentFile4.setMinimumSize(QtCore.QSize(90, 25))
        self.recentFile4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.recentFile4.setText("")
        self.recentFile4.setObjectName("recentFile4")
        self.verticalLayout_11.addWidget(self.recentFile4)
        self.verticalLayout_11.setStretch(0, 1)
        self.verticalLayout_11.setStretch(1, 8)
        self.horizontalLayout_7.addWidget(self.frame_12)
        self.frame_13 = QtWidgets.QFrame(self.frame_9)
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.frame_13)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.recentButton5 = QtWidgets.QPushButton(self.frame_13)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.recentButton5.sizePolicy().hasHeightForWidth())
        self.recentButton5.setSizePolicy(sizePolicy)
        self.recentButton5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.recentButton5.setStyleSheet("QPushButton{\n"
"    background-color: rgb(75, 87, 106);\n"
"    color: #fff;\n"
"    text-align: left;\n"
"}\n"
"QPushButton:hover{\n"
"    text-decoration: underline;\n"
"}\n"
"QPushButton:pressed{\n"
"    color: #000000;\n"
"}")
        self.recentButton5.setObjectName("recentButton5")
        self.verticalLayout_12.addWidget(self.recentButton5)
        self.recentFile5 = QtWidgets.QPushButton(self.frame_13)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.recentFile5.sizePolicy().hasHeightForWidth())
        self.recentFile5.setSizePolicy(sizePolicy)
        self.recentFile5.setMinimumSize(QtCore.QSize(90, 25))
        self.recentFile5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.recentFile5.setText("")
        self.recentFile5.setObjectName("recentFile5")
        self.verticalLayout_12.addWidget(self.recentFile5)
        self.verticalLayout_12.setStretch(0, 1)
        self.verticalLayout_12.setStretch(1, 8)
        self.horizontalLayout_7.addWidget(self.frame_13)
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
        self.ocrButton.setMinimumSize(QtCore.QSize(170, 40))
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
        self.ocrButton.clicked.connect(self.open_OCR)
        self.scanButton = QtWidgets.QToolButton(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scanButton.sizePolicy().hasHeightForWidth())
        self.scanButton.setSizePolicy(sizePolicy)
        self.scanButton.setMinimumSize(QtCore.QSize(170, 40))
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
        self.scanButton.clicked.connect(self.open_docscan)
        self.convButton = QtWidgets.QToolButton(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.convButton.sizePolicy().hasHeightForWidth())
        self.convButton.setSizePolicy(sizePolicy)
        self.convButton.setMinimumSize(QtCore.QSize(170, 40))
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
        self.convButton.clicked.connect(self.open_convert)
        self.mergesplitButton = QtWidgets.QToolButton(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mergesplitButton.sizePolicy().hasHeightForWidth())
        self.mergesplitButton.setSizePolicy(sizePolicy)
        self.mergesplitButton.setMinimumSize(QtCore.QSize(170, 40))
        self.mergesplitButton.setMaximumSize(QtCore.QSize(500, 16777215))
        self.mergesplitButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.mergesplitButton.setStyleSheet("QToolButton{\n"
"    background-color: #CEEDC7;\n"
"}\n"
"QToolButton:hover{\n"
"    background-color: rgb(170, 255, 127);\n"
"}")
        self.mergesplitButton.setObjectName("mergesplitButton")
        self.mergesplitButton.clicked.connect(self.open_mergesplit)
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
        self.scrollArea.setStyleSheet("border-radius: 20px;")
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 986, 639))
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
        self.horizontalLayout_4.addWidget(self.adjButton)
        self.cropButton = QtWidgets.QPushButton(self.frame_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cropButton.sizePolicy().hasHeightForWidth())
        self.cropButton.setSizePolicy(sizePolicy)
        self.cropButton.setMinimumSize(QtCore.QSize(60, 60))
        self.cropButton.setMaximumSize(QtCore.QSize(70, 16777215))
        self.cropButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cropButton.setStyleSheet("QPushButton{\n"
"    background-color: rgb(42, 49, 58);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(205, 205, 205);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: #ececec\n"
"}")
        self.cropButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/Setting/icons8-crop-24.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.cropButton.setIcon(icon3)
        self.cropButton.setIconSize(QtCore.QSize(60, 60))
        self.cropButton.setObjectName("cropButton")
        self.horizontalLayout_4.addWidget(self.cropButton)
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
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/Arrow/icons8-arrow-48 - Copy.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.nextButton.setIcon(icon4)
        self.nextButton.setIconSize(QtCore.QSize(50, 50))
        self.nextButton.setObjectName("nextButton")
        self.horizontalLayout_4.addWidget(self.nextButton)
        self.horizontalLayout_4.setStretch(0, 7)
        self.horizontalLayout_4.setStretch(1, 1)
        self.horizontalLayout_4.setStretch(3, 7)
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
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 986, 639))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.previewLabel2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.previewLabel2.setStyleSheet("background: none;")
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
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/RetryAdd/icons8-retry-50.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.retakeButton.setIcon(icon5)
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
        self.horizontalLayout_3.addWidget(self.adjButton2)
        self.cropButton2 = QtWidgets.QPushButton(self.frame_16)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cropButton2.sizePolicy().hasHeightForWidth())
        self.cropButton2.setSizePolicy(sizePolicy)
        self.cropButton2.setMinimumSize(QtCore.QSize(0, 60))
        self.cropButton2.setMaximumSize(QtCore.QSize(70, 16777215))
        self.cropButton2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cropButton2.setStyleSheet("QPushButton{\n"
"    background-color: rgb(42, 49, 58);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(205, 205, 205);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: #ececec\n"
"}")
        self.cropButton2.setText("")
        self.cropButton2.setIcon(icon3)
        self.cropButton2.setIconSize(QtCore.QSize(60, 60))
        self.cropButton2.setObjectName("cropButton2")
        self.horizontalLayout_3.addWidget(self.cropButton2)
        self.addButton = QtWidgets.QPushButton(self.frame_16)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addButton.sizePolicy().hasHeightForWidth())
        self.addButton.setSizePolicy(sizePolicy)
        self.addButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.addButton.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/RetryAdd/icons8-add-50.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.addButton.setIcon(icon6)
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
        self.nextButton2.setIcon(icon4)
        self.nextButton2.setIconSize(QtCore.QSize(50, 50))
        self.nextButton2.setObjectName("nextButton2")
        self.horizontalLayout_3.addWidget(self.nextButton2)
        self.horizontalLayout_3.setStretch(0, 6)
        self.horizontalLayout_3.setStretch(1, 6)
        self.horizontalLayout_3.setStretch(2, 2)
        self.horizontalLayout_3.setStretch(4, 6)
        self.horizontalLayout_3.setStretch(5, 6)
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
        self.menubar.setGeometry(QtCore.QRect(0, 0, 986, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.recentButton1.setText(_translate("MainWindow", "PushButton"))
        self.recentButton2.setText(_translate("MainWindow", "PushButton"))
        self.recentButton3.setText(_translate("MainWindow", "PushButton"))
        self.recentButton4.setText(_translate("MainWindow", "PushButton"))
        self.recentButton5.setText(_translate("MainWindow", "PushButton"))
        self.ocrButton.setText(_translate("MainWindow", "OCR"))
        self.scanButton.setText(_translate("MainWindow", "Document Scanning"))
        self.convButton.setText(_translate("MainWindow", "Convert Format"))
        self.mergesplitButton.setText(_translate("MainWindow", "Merge/Split (PDF)"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
