from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(332, 320)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(330, 320))
        Dialog.setMaximumSize(QtCore.QSize(350, 350))
        Dialog.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #36404B, stop:1 #181D23);")
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setStyleSheet("background: none;\n"
"font: 63 8pt \"Segoe UI Variable Text Semibold\";\n"
"color: #ffffff;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.highlight = QtWidgets.QLabel(self.frame_2)
        self.highlight.setObjectName("highlight")
        self.horizontalLayout_3.addWidget(self.highlight)
        spacerItem = QtWidgets.QSpacerItem(204, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.highlightNum = QtWidgets.QLabel(self.frame_2)
        self.highlightNum.setStyleSheet("color: rgb(157, 157, 157)")
        self.highlightNum.setObjectName("highlightNum")
        self.horizontalLayout_3.addWidget(self.highlightNum)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.highlightSlider = QtWidgets.QSlider(self.frame)
        self.highlightSlider.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.highlightSlider.setMinimum(-100)
        self.highlightSlider.setMaximum(100)
        self.highlightSlider.setOrientation(QtCore.Qt.Horizontal)
        self.highlightSlider.setObjectName("highlightSlider")
        self.verticalLayout_2.addWidget(self.highlightSlider)
        self.saturationNum = QtWidgets.QFrame(self.frame)
        self.saturationNum.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.saturationNum.setFrameShadow(QtWidgets.QFrame.Raised)
        self.saturationNum.setObjectName("saturationNum")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.saturationNum)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(7)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.saturation = QtWidgets.QLabel(self.saturationNum)
        self.saturation.setObjectName("saturation")
        self.horizontalLayout_4.addWidget(self.saturation)
        spacerItem1 = QtWidgets.QSpacerItem(197, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.label_4 = QtWidgets.QLabel(self.saturationNum)
        self.label_4.setStyleSheet("color: rgb(157, 157, 157)")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.verticalLayout_2.addWidget(self.saturationNum)
        self.saturationSlider = QtWidgets.QSlider(self.frame)
        self.saturationSlider.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.saturationSlider.setMinimum(-100)
        self.saturationSlider.setMaximum(100)
        self.saturationSlider.setOrientation(QtCore.Qt.Horizontal)
        self.saturationSlider.setObjectName("saturationSlider")
        self.verticalLayout_2.addWidget(self.saturationSlider)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.contrast = QtWidgets.QLabel(self.frame_4)
        self.contrast.setObjectName("contrast")
        self.horizontalLayout_2.addWidget(self.contrast)
        spacerItem2 = QtWidgets.QSpacerItem(208, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.contrastNum = QtWidgets.QLabel(self.frame_4)
        self.contrastNum.setStyleSheet("color: rgb(157, 157, 157)")
        self.contrastNum.setObjectName("contrastNum")
        self.horizontalLayout_2.addWidget(self.contrastNum)
        self.verticalLayout_2.addWidget(self.frame_4)
        self.contrastSlider = QtWidgets.QSlider(self.frame)
        self.contrastSlider.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.contrastSlider.setMinimum(-100)
        self.contrastSlider.setMaximum(100)
        self.contrastSlider.setOrientation(QtCore.Qt.Horizontal)
        self.contrastSlider.setObjectName("contrastSlider")
        self.verticalLayout_2.addWidget(self.contrastSlider)
        self.exposureNum = QtWidgets.QFrame(self.frame)
        self.exposureNum.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.exposureNum.setFrameShadow(QtWidgets.QFrame.Raised)
        self.exposureNum.setObjectName("exposureNum")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.exposureNum)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.exposure = QtWidgets.QLabel(self.exposureNum)
        self.exposure.setObjectName("exposure")
        self.horizontalLayout.addWidget(self.exposure)
        spacerItem3 = QtWidgets.QSpacerItem(204, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.label_8 = QtWidgets.QLabel(self.exposureNum)
        self.label_8.setStyleSheet("color: rgb(157, 157, 157)")
        self.label_8.setObjectName("label_8")
        self.horizontalLayout.addWidget(self.label_8)
        self.verticalLayout_2.addWidget(self.exposureNum)
        self.exposureSlider = QtWidgets.QSlider(self.frame)
        self.exposureSlider.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.exposureSlider.setMinimum(-100)
        self.exposureSlider.setMaximum(100)
        self.exposureSlider.setOrientation(QtCore.Qt.Horizontal)
        self.exposureSlider.setObjectName("exposureSlider")
        self.verticalLayout_2.addWidget(self.exposureSlider)
        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(Dialog)
        self.highlightSlider.valueChanged['int'].connect(self.highlightNum.setNum) # type: ignore
        self.saturationSlider.valueChanged['int'].connect(self.label_4.setNum) # type: ignore
        self.contrastSlider.valueChanged['int'].connect(self.contrastNum.setNum) # type: ignore
        self.exposureSlider.valueChanged['int'].connect(self.label_8.setNum) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.highlight.setText(_translate("Dialog", "Highlight"))
        self.highlightNum.setText(_translate("Dialog", "0"))
        self.saturation.setText(_translate("Dialog", "Saturation"))
        self.label_4.setText(_translate("Dialog", "0"))
        self.contrast.setText(_translate("Dialog", "Contrast"))
        self.contrastNum.setText(_translate("Dialog", "0"))
        self.exposure.setText(_translate("Dialog", "Exposure"))
        self.label_8.setText(_translate("Dialog", "0"))
import camera_btn_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
