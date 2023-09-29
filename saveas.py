from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QWidget

class Ui_Dialog(object):
    def saveButton_clicked(self):
        if self.res:
            index = self.extComboBox.currentIndex()
            if index == 0:
                pdf = self.res[0]
                pdf_name = QFileDialog.getSaveFileName(QtWidgets.QDialog(), "Save file", self.res[0], "PDF (*.pdf)")
                if pdf_name:
                    pdf.save(pdf_name[0], "PDF")
            elif index == 1:
                image = self.res[0]
                img_name = QFileDialog.getSaveFileName(QtWidgets.QDialog(), "Save file", self.res[0], "jpeg (*.jpeg)")
                image.save(img_name[0], "JPEG")
            elif index == 2:
                image = self.res[0]
                img_name = QFileDialog.getSaveFileName(QtWidgets.QDialog(), "Save file", self.res[0], "png (*.png)")
                image.save(img_name[0], "PNG")
            
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
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_4 = QtWidgets.QFrame(Dialog)
        self.frame_4.setStyleSheet("background:none;\n"
"color: #ffffff;\n"
"font: 63 8pt \"Segoe UI Variable Text Semibold\";")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.filename = QtWidgets.QLabel(self.frame_4)
        self.filename.setObjectName("filename")
        self.verticalLayout_3.addWidget(self.filename)
        self.filenameEdit = QtWidgets.QLineEdit(self.frame_4)
        self.filenameEdit.setStyleSheet("background-color: rgb(240, 240, 240);\n"
"border-radius: 10px;\n"
"padding: 3px;\n"
"color: #000000;")
        self.filenameEdit.setText("")
        self.filenameEdit.setObjectName("filenameEdit")
        self.verticalLayout_3.addWidget(self.filenameEdit)
        self.extension = QtWidgets.QLabel(self.frame_4)
        self.extension.setObjectName("extension")
        self.verticalLayout_3.addWidget(self.extension)
        self.extComboBox = QtWidgets.QComboBox(self.frame_4)
        self.extComboBox.setMinimumSize(QtCore.QSize(0, 50))
        self.extComboBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.extComboBox.setStyleSheet("QComboBox{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.006, x2:1, y2:0, stop:0 #6391C1, stop:0.900498 #58A2C2);\n"
"    border-radius: 20px;\n"
"    color: rgb(214, 214, 214);\n"
"    font: 63 16pt \"Segoe UI Variable Text Semibold\";\n"
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
        self.verticalLayout_3.addWidget(self.extComboBox)
        self.frame_5 = QtWidgets.QFrame(self.frame_4)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_5.setContentsMargins(-1, 11, -1, 11)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem = QtWidgets.QSpacerItem(115, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.saveButton = QtWidgets.QPushButton(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.saveButton.sizePolicy().hasHeightForWidth())
        self.saveButton.setSizePolicy(sizePolicy)
        self.saveButton.setMinimumSize(QtCore.QSize(0, 40))
        self.saveButton.setMaximumSize(QtCore.QSize(16777215, 42))
        self.saveButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.saveButton.setStyleSheet("QPushButton{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.006, x2:1, y2:0, stop:0 rgba(38, 215, 1, 255), stop:0.880597 rgba(0, 171, 8, 255));\n"
"    border-radius: 20px;\n"
"    image: url(:/Save/icons8-save-50.png);\n"
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
        self.saveButton.setText("")
        self.saveButton.setIconSize(QtCore.QSize(20, 20))
        self.saveButton.setObjectName("saveButton")
        self.horizontalLayout_5.addWidget(self.saveButton)
        self.horizontalLayout_5.setStretch(0, 5)
        self.horizontalLayout_5.setStretch(1, 2)
        self.verticalLayout_3.addWidget(self.frame_5)
        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 2)
        self.verticalLayout_3.setStretch(2, 1)
        self.verticalLayout_3.setStretch(3, 2)
        self.verticalLayout_3.setStretch(4, 2)
        self.verticalLayout.addWidget(self.frame_4)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.filename.setText(_translate("Dialog", "File name:"))
        self.extension.setText(_translate("Dialog", "Extension:"))
        self.extComboBox.setItemText(0, _translate("Dialog", ".pdf"))
        self.extComboBox.setItemText(1, _translate("Dialog", ".jpeg"))
        self.extComboBox.setItemText(2, _translate("Dialog", ".png"))
import camera_btn_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
