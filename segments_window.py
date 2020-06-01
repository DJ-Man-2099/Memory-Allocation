# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'segments_window.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import DavidDatabase
import DavidAlgorithms
from holes_window import Ui_holes_Form


class Ui_segment_Form(object):
    def __init__(self):
        pass

    def setupUi(self, segment_Form):
        segment_Form.setObjectName("segment_Form")
        segment_Form.resize(740, 586)

        self.base_limit_index = 0

        #############################################################################################################
        #############################################################################################################
        #############################################################################################################
        # Main Window Styling
        segment_Form.setStyleSheet('background-color:	lightyellow')
        #############################################################################################################
        #############################################################################################################
        #############################################################################################################

        self.table_index = 0
        self.process_list_row_index = 0
        self.no_of_processes = 0

        self.title_label = QtWidgets.QLabel(segment_Form)
        self.title_label.setGeometry(QtCore.QRect(120, 10, 201, 20))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.title_label.setFont(font)
        self.title_label.setObjectName("title_label")

        self.rem_process_btn = QtWidgets.QPushButton(segment_Form)
        self.rem_process_btn.setGeometry(QtCore.QRect(500, 520, 91, 30))
        self.rem_process_btn.setObjectName("add_process_btn")
        self.rem_process_btn.setStyleSheet("background-color:slategray")
        self.rem_process_btn.clicked.connect(self.rem_process_clicked)


        self.segments_table = QtWidgets.QTableWidget(segment_Form)
        self.segments_table.setGeometry(QtCore.QRect(130, 200, 221, 301))
        self.segments_table.setColumnCount(2)
        self.segments_table.setObjectName("segments_table")

        self.process_list_table = QtWidgets.QTableWidget(segment_Form)
        self.process_list_table.setGeometry(QtCore.QRect(500, 200, 120, 301))
        self.process_list_table.setRowCount(9)
        self.process_list_table.setColumnCount(1)
        for i in Ui_holes_Form.processes_list:
            self.process_list_table.setItem(self.process_list_row_index, 0, QtWidgets.QTableWidgetItem(i.Name))
            self.process_list_row_index += 1
            self.no_of_processes += 1
        self.process_list_table.setEditTriggers(QtWidgets.QTreeView.NoEditTriggers)
        self.process_list_table.setObjectName("process_list_table")

        self.process_list_lbl = QtWidgets.QLabel(segment_Form)
        self.process_list_lbl.setGeometry(QtCore.QRect(500, 170, 100, 20))
        self.process_list_lbl.setObjectName("process_name_entry_lbl")
        font = QtGui.QFont()
        font.setPointSize(14)
        self.process_list_lbl.setFont(font)

        self.process_name_entry = QtWidgets.QLineEdit(segment_Form)
        self.process_name_entry.setGeometry(QtCore.QRect(180, 60, 113, 20))
        self.process_name_entry.setObjectName("process_name_entry")

        self.process_name_entry_lbl = QtWidgets.QLabel(segment_Form)
        self.process_name_entry_lbl.setGeometry(QtCore.QRect(300, 60, 100, 20))
        self.process_name_entry_lbl.setObjectName("process_name_entry_lbl")

        self.number_of_segements_entry = QtWidgets.QLineEdit(segment_Form)
        self.number_of_segements_entry.setGeometry(QtCore.QRect(30, 100, 113, 20))
        self.number_of_segements_entry.setObjectName("number_of_segements_entry")
        self.segment_name_entry = QtWidgets.QLineEdit(segment_Form)
        self.segment_name_entry.setGeometry(QtCore.QRect(180, 100, 113, 20))
        self.segment_name_entry.setObjectName("segment_name_entry")
        self.segment_size_entry = QtWidgets.QLineEdit(segment_Form)
        self.segment_size_entry.setGeometry(QtCore.QRect(320, 100, 113, 20))
        self.segment_size_entry.setObjectName("segment_size_entry")
        self.number_of_segments_lbl = QtWidgets.QLabel(segment_Form)
        self.number_of_segments_lbl.setGeometry(QtCore.QRect(36, 120, 101, 20))
        self.number_of_segments_lbl.setObjectName("number_of_segments_lbl")
        self.segment_name_lbl = QtWidgets.QLabel(segment_Form)
        self.segment_name_lbl.setGeometry(QtCore.QRect(200, 120, 71, 20))
        self.segment_name_lbl.setObjectName("segment_name_lbl")
        self.segment_size_lbl = QtWidgets.QLabel(segment_Form)
        self.segment_size_lbl.setGeometry(QtCore.QRect(340, 120, 71, 21))
        self.segment_size_lbl.setObjectName("segment_size_lbl")
        self.segment_name_lbl_2 = QtWidgets.QLabel(segment_Form)
        self.segment_name_lbl_2.setGeometry(QtCore.QRect(150, 180, 71, 20))
        self.segment_name_lbl_2.setObjectName("segment_name_lbl_2")
        self.segment_size_lbl_2 = QtWidgets.QLabel(segment_Form)
        self.segment_size_lbl_2.setGeometry(QtCore.QRect(260, 180, 71, 18))
        self.segment_size_lbl_2.setObjectName("segment_size_lbl_2")
        self.submit_segment_btn = QtWidgets.QPushButton(segment_Form)
        self.submit_segment_btn.setGeometry(QtCore.QRect(280, 520, 91, 30))
        self.submit_segment_btn.setObjectName("submit_segment_btn")

        self.submit_segment_size_btn = QtWidgets.QPushButton(segment_Form)
        self.submit_segment_size_btn.setGeometry(QtCore.QRect(100, 520, 145, 30))
        self.submit_segment_size_btn.setObjectName("submit_segment_size_btn")

        self.process_name_lbl = QtWidgets.QLabel(segment_Form)
        self.process_name_lbl.setGeometry(QtCore.QRect(180, 150, 120, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.process_name_lbl.setFont(font)
        self.process_name_lbl.setObjectName("process_name_lbl")
        ##############################################################################################################################
        ##############################################################################################################################
        ##############################################################################################################################
        ##############################################################################################################################
        # Styling Sheets
        ##############################################################################################################################
        ##############################################################################################################################
        ##############################################################################################################################
        ##############################################################################################################################

        self.process_name_entry.setStyleSheet("background-color:white")
        self.number_of_segements_entry.setStyleSheet("background-color:white")
        self.segment_name_entry.setStyleSheet("background-color:white")
        self.segment_size_entry.setStyleSheet("background-color:white")

        self.submit_segment_btn.setStyleSheet("background-color:slategray")
        self.submit_segment_size_btn.setStyleSheet("background-color:slategray")

        self.segments_table.setStyleSheet("background-color:white")
        self.process_list_table.setStyleSheet("background-color:white")

        ##############################################################################################################################
        ##############################################################################################################################
        ##############################################################################################################################
        ##############################################################################################################################
        # Buttons click handling connections
        self.submit_segment_btn.clicked.connect(self.submit_segment_clicked)
        self.submit_segment_size_btn.clicked.connect(self.submit_segment_size_clicked)

        ##############################################################################################################################
        ##############################################################################################################################
        ##############################################################################################################################
        ##############################################################################################################################

        self.retranslateUi(segment_Form)
        QtCore.QMetaObject.connectSlotsByName(segment_Form)
        for process in Ui_holes_Form.total_memory_for_holes_window.Processes:
            self.process_list_table.setItem(self.process_list_row_index, 0, QtWidgets.QTableWidgetItem(str(process)))
            self.process_list_row_index += 1

    def retranslateUi(self, segment_Form):
        _translate = QtCore.QCoreApplication.translate
        segment_Form.setWindowTitle(_translate("segment_Form", "Segments Window"))
        self.title_label.setText(_translate("segment_Form", "Processes Window"))
        self.process_name_entry_lbl.setText(_translate("segment_Form", "Enter process name"))
        self.process_list_lbl.setText(_translate("segment_Form", "Process list"))
        self.number_of_segments_lbl.setText(_translate("segment_Form", "Number of segments"))
        self.segment_name_lbl.setText(_translate("segment_Form", "Segment name"))
        self.segment_size_lbl.setText(_translate("segment_Form", "Segment size"))
        self.segment_name_lbl_2.setText(_translate("segment_Form", "Segment name"))
        self.segment_size_lbl_2.setText(_translate("segment_Form", "Segment size"))
        self.submit_segment_btn.setText(_translate("segment_Form", "Submit segment"))
        self.submit_segment_size_btn.setText(_translate("segment_Form", "Submit Process"))
        self.process_name_lbl.setText(_translate("segment_Form", "Process Table"))
        self.rem_process_btn.setText(_translate("segment_Form", "Remove Program"))
        ##############################################################################################################################
        ##############################################################################################################################
        ##############################################################################################################################
        ##############################################################################################################################
        # Button click handling functions
        ##############################################################################################################################
        ##############################################################################################################################
        ##############################################################################################################################
        ##############################################################################################################################

    def submit_segment_clicked(self):
        if self.segment_name_entry.text() != "" and self.segment_size_entry.text() != "":
            # Creating the Database
            try:
                if Ui_holes_Form.processes_list[self.process_list_row_index].Seg_Num > \
                        Ui_holes_Form.processes_list[self.process_list_row_index].Segments.__len__():
                    Ui_holes_Form.processes_list[self.process_list_row_index].Segments[self.segment_name_entry.text()] = int(
                        self.segment_size_entry.text())
            ###################
                    self.segments_table.setItem(self.table_index, 0,
                                                QtWidgets.QTableWidgetItem(self.segment_name_entry.text()))
                    self.segments_table.setItem(self.table_index, 1,
                                                QtWidgets.QTableWidgetItem(self.segment_size_entry.text()))
                    self.table_index += 1
                else:
                    error_msg = QtWidgets.QMessageBox()
                    error_msg.setWindowTitle("Segment Error")
                    error_msg.setText("Segment Number Exceeded")
                    error_msg.setIcon(QtWidgets.QMessageBox.Critical)
                    error_msg.exec_()
                self.segment_name_entry.clear()
                self.segment_size_entry.clear()
            except IndexError:
                error_msg = QtWidgets.QMessageBox()
                error_msg.setWindowTitle("Segment Error")
                error_msg.setText("Please Enter a Process First")
                error_msg.setIcon(QtWidgets.QMessageBox.Critical)
                error_msg.exec_()
            except:
                error_msg = QtWidgets.QMessageBox()
                error_msg.setWindowTitle("Segment Error")
                error_msg.setText("Please Enter a Valid Segment Size")
                error_msg.setIcon(QtWidgets.QMessageBox.Critical)
                error_msg.exec_()
        else:
            error_msg = QtWidgets.QMessageBox()
            error_msg.setWindowTitle("Segment Error")
            error_msg.setText("Please Enter a Segment Name and Size")
            error_msg.setIcon(QtWidgets.QMessageBox.Critical)
            error_msg.exec_()

    def submit_segment_size_clicked(self):
        try:
            if self.process_name_entry.text() != "":
                p = DavidDatabase.Process(self.process_name_entry.text())
                p.Seg_Num = int(self.number_of_segements_entry.text())
                Ui_holes_Form.processes_list.append(p)
                self.table_index = 0
                self.process_list_row_index = self.no_of_processes
                self.no_of_processes += 1
                self.segments_table.clear()
                self.process_name_lbl.setText("Process:" + self.process_name_entry.text())
                self.segments_table.setRowCount(int(self.number_of_segements_entry.text()))
                self.add_process_clicked()
            else:
                error_msg = QtWidgets.QMessageBox()
                error_msg.setWindowTitle("Process Error")
                error_msg.setText("Please Enter a Process Name")
                error_msg.setIcon(QtWidgets.QMessageBox.Critical)
                error_msg.exec_()
            self.process_name_entry.clear()
            self.number_of_segements_entry.clear()
        except:
            error_msg = QtWidgets.QMessageBox()
            error_msg.setWindowTitle("Process Error")
            error_msg.setText("Please Enter a Valid Number of Segments")
            error_msg.setIcon(QtWidgets.QMessageBox.Critical)
            error_msg.exec_()

    def add_process_clicked(self):
        self.process_list_table.setItem(self.no_of_processes-1, 0,
                                        QtWidgets.QTableWidgetItem(self.process_name_entry.text()))

    def fill_seg_table(self):
        self.table_index = 0
        self.process_list_row_index = self.process_list_table.currentRow()
        self.segments_table.clear()
        self.segments_table.setRowCount(Ui_holes_Form.processes_list[self.process_list_row_index].Seg_Num)
        self.process_name_lbl.setText("Process:" + self.process_list_table.currentItem().text())
        for i in Ui_holes_Form.processes_list[self.process_list_row_index].Segments:
            self.segments_table.setItem(self.table_index, 0, QtWidgets.QTableWidgetItem(i))
            self.segments_table.setItem(self.table_index, 1, QtWidgets.QTableWidgetItem(str(
                Ui_holes_Form.processes_list[self.process_list_row_index].Segments[i])))
            self.table_index += 1

    def rem_process_clicked(self):
        try:
            Ui_holes_Form.processes_list.pop(self.process_list_table.currentRow())
            self.process_list_table.removeRow(self.process_list_table.currentRow())
            self.segments_table.clear()
            self.process_name_lbl.setText("Process Table")
            self.no_of_processes = 0
            self.process_list_row_index = 0
            for i in Ui_holes_Form.processes_list:
                self.process_list_table.setItem(self.process_list_row_index, 0, QtWidgets.QTableWidgetItem(i.Name))
                self.process_list_row_index += 1
                self.no_of_processes += 1
        except:
            error_msg = QtWidgets.QMessageBox()
            error_msg.setWindowTitle("Process Error")
            error_msg.setText("Please Choose a Process First")
            error_msg.setIcon(QtWidgets.QMessageBox.Critical)
            error_msg.exec_()



##############################################################################################################################
##############################################################################################################################
##############################################################################################################################
##############################################################################################################################
##############################################################################################################################
##############################################################################################################################
##############################################################################################################################
##############################################################################################################################


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    segment_Form = QtWidgets.QWidget()
    ui = Ui_segment_Form()
    ui.setupUi(segment_Form)
    segment_Form.show()
    sys.exit(app.exec_())
