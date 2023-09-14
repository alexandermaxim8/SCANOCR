from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(350, 350)
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
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.page)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.frame_3 = QtWidgets.QFrame(self.page)
        self.frame_3.setStyleSheet("background: none;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(20, 58, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.mergeButton = QtWidgets.QPushButton(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mergeButton.sizePolicy().hasHeightForWidth())
        self.mergeButton.setSizePolicy(sizePolicy)
        self.mergeButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.mergeButton.setStyleSheet("QPushButton{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.006, x2:1, y2:0, stop:0 #6391C1, stop:0.900498 #58A2C2);\n"
"    border-radius: 20px;\n"
"    font: 63 16pt \"Segoe UI Variable Text Semibold\";\n"
"    color: #ffffff\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #6391c1;\n"
"}\n"
"QPushButton:pressed{\n"
"    border: 2px solid #ffffff;\n"
"}")
        self.mergeButton.setObjectName("mergeButton")
        self.verticalLayout_2.addWidget(self.mergeButton)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.splitButton = QtWidgets.QPushButton(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitButton.sizePolicy().hasHeightForWidth())
        self.splitButton.setSizePolicy(sizePolicy)
        self.splitButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.splitButton.setStyleSheet("QPushButton{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.006, x2:1, y2:0, stop:0 #6391C1, stop:0.900498 #58A2C2);\n"
"    border-radius: 20px;\n"
"    font: 63 16pt \"Segoe UI Variable Text Semibold\";\n"
"    color: #ffffff\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #6391c1;\n"
"}\n"
"QPushButton:pressed{\n"
"    border: 2px solid #ffffff;\n"
"}")
        self.splitButton.setObjectName("splitButton")
        self.verticalLayout_2.addWidget(self.splitButton)
        spacerItem3 = QtWidgets.QSpacerItem(20, 58, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.verticalLayout_2.setStretch(0, 2)
        self.verticalLayout_2.setStretch(1, 2)
        self.verticalLayout_2.setStretch(2, 1)
        self.verticalLayout_2.setStretch(3, 2)
        self.verticalLayout_2.setStretch(4, 2)
        self.horizontalLayout_2.addWidget(self.frame_3)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.horizontalLayout_2.setStretch(0, 2)
        self.horizontalLayout_2.setStretch(1, 7)
        self.horizontalLayout_2.setStretch(2, 2)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.page_2)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame_8 = QtWidgets.QFrame(self.page_2)
        self.frame_8.setStyleSheet("QFrame{\n"
"    background: none;\n"
"}\n"
"\n"
"QLabel{\n"
"    color: #ffffff;\n"
"    font: 63 8pt \"Segoe UI Variable Text Semibold\";\n"
"}")
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.frame_9 = QtWidgets.QFrame(self.frame_8)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_9)
        self.verticalLayout_5.setSpacing(10)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.merge = QtWidgets.QLabel(self.frame_9)
        self.merge.setObjectName("merge")
        self.verticalLayout_5.addWidget(self.merge)
        self.fileList = QtWidgets.QListWidget(self.frame_9)
        self.fileList.setStyleSheet("background-color: rgb(240, 240, 240);\n"
"border-radius: 10px;\n"
"color: rgb(156, 156, 156);\n"
"padding: 3px;")
        self.fileList.setObjectName("fileList")
        item = QtWidgets.QListWidgetItem()
        self.fileList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.fileList.addItem(item)
        self.verticalLayout_5.addWidget(self.fileList)
        self.frame_10 = QtWidgets.QFrame(self.frame_9)
        self.frame_10.setMinimumSize(QtCore.QSize(270, 0))
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_10)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(7)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame_11 = QtWidgets.QFrame(self.frame_10)
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_11)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.addButton = QtWidgets.QPushButton(self.frame_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addButton.sizePolicy().hasHeightForWidth())
        self.addButton.setSizePolicy(sizePolicy)
        self.addButton.setMinimumSize(QtCore.QSize(0, 40))
        self.addButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.addButton.setStyleSheet("QPushButton{\n"
"    background-color: rgb(75, 87, 106);\n"
"    border-radius: 20px;\n"
"    image: url(:/RetryAdd/icons8-add-50.png);\n"
"    padding: 5px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(42, 49, 58);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(42, 49, 58);\n"
"    border: 2px outset #ffffff;\n"
"}")
        self.addButton.setText("")
        self.addButton.setObjectName("addButton")
        self.horizontalLayout_8.addWidget(self.addButton)
        self.upButton = QtWidgets.QPushButton(self.frame_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.upButton.sizePolicy().hasHeightForWidth())
        self.upButton.setSizePolicy(sizePolicy)
        self.upButton.setMinimumSize(QtCore.QSize(0, 40))
        self.upButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.upButton.setStyleSheet("QPushButton{\n"
"    background-color: rgb(75, 87, 106);\n"
"    border-radius: 20px;\n"
"    image: url(:/Arrow/icons8-arrow-48 - up.png);\n"
"    padding: 5px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(42, 49, 58);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(42, 49, 58);\n"
"    border: 2px outset #ffffff;\n"
"}")
        self.upButton.setText("")
        self.upButton.setObjectName("upButton")
        self.horizontalLayout_8.addWidget(self.upButton)
        self.downButton = QtWidgets.QPushButton(self.frame_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.downButton.sizePolicy().hasHeightForWidth())
        self.downButton.setSizePolicy(sizePolicy)
        self.downButton.setMinimumSize(QtCore.QSize(0, 40))
        self.downButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.downButton.setStyleSheet("QPushButton{\n"
"    background-color: rgb(75, 87, 106);\n"
"    border-radius: 20px;\n"
"    image: url(:/Arrow/icons8-arrow-48 - down.png);\n"
"    padding: 5px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(42, 49, 58);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(42, 49, 58);\n"
"    border: 2px outset #ffffff;\n"
"}")
        self.downButton.setText("")
        self.downButton.setObjectName("downButton")
        self.horizontalLayout_8.addWidget(self.downButton)
        self.removeButton = QtWidgets.QPushButton(self.frame_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.removeButton.sizePolicy().hasHeightForWidth())
        self.removeButton.setSizePolicy(sizePolicy)
        self.removeButton.setMinimumSize(QtCore.QSize(0, 40))
        self.removeButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.removeButton.setStyleSheet("QPushButton{\n"
"    background-color: rgb(75, 87, 106);\n"
"    border-radius: 20px;\n"
"    image: url(:/Save/icons8-cross-64.png);\n"
"    padding: 5px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(42, 49, 58);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(42, 49, 58);\n"
"    border: 2px outset #ffffff;\n"
"}")
        self.removeButton.setText("")
        self.removeButton.setObjectName("removeButton")
        self.horizontalLayout_8.addWidget(self.removeButton)
        self.verticalLayout_6.addWidget(self.frame_11)
        self.verticalLayout_5.addWidget(self.frame_10)
        self.frame_13 = QtWidgets.QFrame(self.frame_9)
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_13)
        self.horizontalLayout_10.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        spacerItem5 = QtWidgets.QSpacerItem(115, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem5)
        self.proceedButton = QtWidgets.QPushButton(self.frame_13)
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
        self.horizontalLayout_10.addWidget(self.proceedButton)
        self.horizontalLayout_10.setStretch(0, 5)
        self.horizontalLayout_10.setStretch(1, 2)
        self.verticalLayout_5.addWidget(self.frame_13)
        self.horizontalLayout_7.addWidget(self.frame_9)
        self.verticalLayout_7.addWidget(self.frame_8)
        self.stackedWidget.addWidget(self.page_2)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.page_4)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.page_4)
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
        self.fileButton.setMinimumSize(QtCore.QSize(80, 40))
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
        spacerItem6 = QtWidgets.QSpacerItem(205, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.verticalLayout_4.addWidget(self.frame_2)
        self.verticalLayout_3.addWidget(self.frame_6)
        self.split = QtWidgets.QLabel(self.frame_4)
        self.split.setObjectName("split")
        self.verticalLayout_3.addWidget(self.split)
        self.frame_7 = QtWidgets.QFrame(self.frame_4)
        self.frame_7.setStyleSheet("QSpinBox{\n"
"    background-color: rgb(240, 240, 240);\n"
"    border-radius: 10px;\n"
"    padding-left: 20px;\n"
"}\n"
"QLabel{\n"
"    color: rgb(239, 239, 239);\n"
"}")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.frompage = QtWidgets.QLabel(self.frame_7)
        self.frompage.setObjectName("frompage")
        self.horizontalLayout_6.addWidget(self.frompage)
        self.frompageSpinBox = QtWidgets.QSpinBox(self.frame_7)
        self.frompageSpinBox.setObjectName("frompageSpinBox")
        self.horizontalLayout_6.addWidget(self.frompageSpinBox)
        self.to = QtWidgets.QLabel(self.frame_7)
        self.to.setStyleSheet("")
        self.to.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.to.setObjectName("to")
        self.horizontalLayout_6.addWidget(self.to)
        self.toSpinBox = QtWidgets.QSpinBox(self.frame_7)
        self.toSpinBox.setObjectName("toSpinBox")
        self.horizontalLayout_6.addWidget(self.toSpinBox)
        self.verticalLayout_3.addWidget(self.frame_7)
        self.frame_5 = QtWidgets.QFrame(self.frame_4)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_5.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem7 = QtWidgets.QSpacerItem(115, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem7)
        self.proceedButton_2 = QtWidgets.QPushButton(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.proceedButton_2.sizePolicy().hasHeightForWidth())
        self.proceedButton_2.setSizePolicy(sizePolicy)
        self.proceedButton_2.setMinimumSize(QtCore.QSize(0, 40))
        self.proceedButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.proceedButton_2.setStyleSheet("QPushButton{\n"
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
        self.proceedButton_2.setText("")
        self.proceedButton_2.setIconSize(QtCore.QSize(20, 20))
        self.proceedButton_2.setObjectName("proceedButton_2")
        self.horizontalLayout_5.addWidget(self.proceedButton_2)
        self.horizontalLayout_5.setStretch(0, 5)
        self.horizontalLayout_5.setStretch(1, 2)
        self.verticalLayout_3.addWidget(self.frame_5)
        self.horizontalLayout_4.addWidget(self.frame_4)
        self.verticalLayout.addWidget(self.frame)
        self.stackedWidget.addWidget(self.page_4)
        self.horizontalLayout_3.addWidget(self.stackedWidget)

        self.retranslateUi(Dialog)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.mergeButton.setText(_translate("Dialog", "MERGE"))
        self.splitButton.setText(_translate("Dialog", "SPLIT"))
        self.merge.setText(_translate("Dialog", "Merge:"))
        __sortingEnabled = self.fileList.isSortingEnabled()
        self.fileList.setSortingEnabled(False)
        item = self.fileList.item(0)
        item.setText(_translate("Dialog", "1 example"))
        item = self.fileList.item(1)
        item.setText(_translate("Dialog", "2 example"))
        self.fileList.setSortingEnabled(__sortingEnabled)
        self.source.setText(_translate("Dialog", "Source:"))
        self.filenameLabel.setText(_translate("Dialog", "pdf, jpeg, png, or docx only"))
        self.split.setText(_translate("Dialog", "Split:"))
        self.frompage.setText(_translate("Dialog", "from page"))
        self.to.setText(_translate("Dialog", "to"))
import camera_btn_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
