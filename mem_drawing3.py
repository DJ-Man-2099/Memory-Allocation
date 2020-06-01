# -*- coding: utf-8 -*-
#
# Form implementation generated from reading ui file 'mem_drawing3.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

#
# from PyQt5 import QtCore, QtGui, QtWidgets
# import DavidDatabase
# # import these before using the method
# from PyQt5.QtGui import *
# from PyQt5.QtWidgets import *
# from PyQt5.QtCore import *
# from PyQt5.uic import loadUiType
# from PyQt5 import QtCore, QtGui, QtWidgets
# import sys
#
#
# class Ui_memory_Form(object):
#     def setupUi(self, Form):
#         Form.setObjectName("Form")
#         Form.resize(439, 436)
#         self.label = QtWidgets.QLabel(Form)
#         self.label.setGeometry(QtCore.QRect(130, 10, 221, 21))
#         font = QtGui.QFont()
#         font.setPointSize(16)
#         font.setBold(True)
#         font.setWeight(75)
#         self.label.setFont(font)
#         self.label.setObjectName("label")
#
#         self.retranslateUi(Form)
#         QtCore.QMetaObject.connectSlotsByName(Form)
#
#
#
#     def retranslateUi(self, Form):
#         _translate = QtCore.QCoreApplication.translate
#         Form.setWindowTitle(_translate("Form", "Memory Layout"))
#         self.label.setText(_translate("Form", "Memory Layout"))
#
#
#
#
#     def draw(self, pro_segment, holes, memory_size):
#         starting_address = []
#         segment_data = []
#
#         for key in pro_segment.keys():
#             starting_address.append(key)
#         for value in pro_segment.values():
#             segment_data.append(value)
#
#         scene = QtWidgets.QGraphicsScene()
#         self.graphicsView.setScene(scene)
#         pen = QtGui.QPen(QtCore.Qt.black, 3)
#         memory_color = QtGui.QBrush(QtCore.Qt.black)
#         holes_color = QtGui.QBrush(QtCore.Qt.darkGray)
#         segments_color = QtGui.QBrush(QtCore.Qt.white)
#         r = QtCore.QRectF(QtCore.QPointF(50, 0), QtCore.QSizeF(110, memory_size))
#         scene.addRect(r, pen, memory_color)
#         mem_start = QGraphicsSimpleTextItem('0')
#         scene.addItem(mem_start)
#         mem_start.setPos(0, -7)
#         mem_start.setScale(1.4)
#         mem_end = QGraphicsSimpleTextItem(str(memory_size))
#         scene.addItem(mem_end)
#         mem_end.setPos(0, memory_size - 7)
#         mem_end.setScale(1.4)
#
#         for i in range(len(starting_address)):
#             # Segment size
#             r = QtCore.QRectF(QtCore.QPointF(50, starting_address[i]), QtCore.QSizeF(110, segment_data[i][2]))
#             scene.addRect(r, pen, segments_color)
#             # Segment name
#             seg_name = QGraphicsSimpleTextItem(segment_data[i][1])
#             scene.addItem(seg_name)
#             seg_name.setPos(68, starting_address[i] + segment_data[i][2] / 2 - 10)
#             seg_name.setScale(1.4)
#             # Parent process of the segment
#             pro_name = QGraphicsSimpleTextItem(segment_data[i][0])
#             scene.addItem(pro_name)
#             pro_name.setPos(68, starting_address[i] + segment_data[i][2] / 2 - 25)
#             pro_name.setScale(1.4)
#             # Starting address of the segment
#             start = QGraphicsSimpleTextItem(str(starting_address[i]))
#             scene.addItem(start)
#             start.setPos(0, starting_address[i] - 7)
#             start.setScale(1.4)
#             # Ending address of the segment
#             end = QGraphicsSimpleTextItem(str(starting_address[i] + segment_data[i][2]))
#             scene.addItem(end)
#             end.setPos(0, starting_address[i] + segment_data[i][2] - 7)
#             end.setScale(1.4)
#             # ٍ Segment size
#             seg_size = QGraphicsSimpleTextItem('Size: ' + str(segment_data[i][2]))
#             scene.addItem(seg_size)
#             seg_size.setPos(68, starting_address[i] + segment_data[i][2] / 2 + 7)
#             seg_size.setScale(1.4)
#
#         for i in range(len(holes)):
#             # Hole size
#             r = QtCore.QRectF(QtCore.QPointF(50, holes[i].address), QtCore.QSizeF(110, holes[i].size))
#             scene.addRect(r, pen, holes_color)
#             # Hole starting address
#             start = QGraphicsSimpleTextItem(str(holes[i].address))
#             scene.addItem(start)
#             start.setPos(0, holes[i].address - 7)
#             start.setScale(1.4)
#             # Hole ending address
#             end = QGraphicsSimpleTextItem(str(holes[i].address + holes[i].size))
#             scene.addItem(end)
#             end.setPos(0, holes[i].address + holes[i].size - 7)
#             end.setScale(1.4)
#             # Holes size
#             hole_size = QGraphicsSimpleTextItem('Size: ' + str(holes[i].size))
#             scene.addItem(hole_size)
#             hole_size.setPos(68, holes[i].address + holes[i].size / 2 - 10)
#             hole_size.setScale(1.4)
#
#
# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Form = QtWidgets.QWidget()
#     ui = Ui_memory_Form()
#     ui.setupUi(Form)
#     Form.show()
#     sys.exit(app.exec_())
#
# obj1 = Ui_memory_Form()
# obj1.draw({"Data": 50, "Size": 200}, 200, 2000)
#
#


#     self.submit_hole_btn.clicked.connect(self.submit_hole_clicked)
#
#
#     def submit_hole_clicked(self):
#         self.starting_address_entry.clear()
#         self.size_entry.clear()
#
# # u1=Ui_memory_Form()
# Ui_memory_Form.draw(u1,{"data": 50}, [300, 200], 2000)

# # import these before using the method
# from PyQt5.QtGui import *
# from PyQt5.QtWidgets import *
# from PyQt5.QtCore import *
# from PyQt5.uic import loadUiType
# from PyQt5 import QtCore, QtGui, QtWidgets
# import sys


#
# def draw(self, pro_segment, holes, memory_size):
#     starting_address = []
#     segment_data = []
#
#     for key in pro_segment.keys():
#         starting_address.append(key)
#     for value in pro_segment.values():
#         segment_data.append(value)
#
#     scene = QtWidgets.QGraphicsScene()
#     self.graphicsView.setScene(scene)
#     pen = QtGui.QPen(QtCore.Qt.black, 3)
#     memory_color = QtGui.QBrush(QtCore.Qt.black)
#     holes_color = QtGui.QBrush(QtCore.Qt.darkGray)
#     segments_color = QtGui.QBrush(QtCore.Qt.white)
#     r = QtCore.QRectF(QtCore.QPointF(50, 0), QtCore.QSizeF(110, memory_size))
#     scene.addRect(r, pen, memory_color)
#     mem_start = QGraphicsSimpleTextItem('0')
#     scene.addItem(mem_start)
#     mem_start.setPos(0, -7)
#     mem_start.setScale(1.4)
#     mem_end = QGraphicsSimpleTextItem(str(memory_size))
#     scene.addItem(mem_end)
#     mem_end.setPos(0, memory_size - 7)
#     mem_end.setScale(1.4)
#
#     for i in range(len(starting_address)):
#         # Segment size
#         r = QtCore.QRectF(QtCore.QPointF(50, starting_address[i]), QtCore.QSizeF(110, segment_data[i][2]))
#         scene.addRect(r, pen, segments_color)
#         # Segment name
#         seg_name = QGraphicsSimpleTextItem(segment_data[i][1])
#         scene.addItem(seg_name)
#         seg_name.setPos(68, starting_address[i] + segment_data[i][2] / 2 - 10)
#         seg_name.setScale(1.4)
#         # Parent process of the segment
#         pro_name = QGraphicsSimpleTextItem(segment_data[i][0])
#         scene.addItem(pro_name)
#         pro_name.setPos(68, starting_address[i] + segment_data[i][2] / 2 - 25)
#         pro_name.setScale(1.4)
#         # Starting address of the segment
#         start = QGraphicsSimpleTextItem(str(starting_address[i]))
#         scene.addItem(start)
#         start.setPos(0, starting_address[i] - 7)
#         start.setScale(1.4)
#         # Ending address of the segment
#         end = QGraphicsSimpleTextItem(str(starting_address[i] + segment_data[i][2]))
#         scene.addItem(end)
#         end.setPos(0, starting_address[i] + segment_data[i][2] - 7)
#         end.setScale(1.4)
#         # ٍ Segment size
#         seg_size = QGraphicsSimpleTextItem('Size: ' + str(segment_data[i][2]))
#         scene.addItem(seg_size)
#         seg_size.setPos(68, starting_address[i] + segment_data[i][2] / 2 + 7)
#         seg_size.setScale(1.4)
#
#     for i in range(len(holes)):
#         # Hole size
#         r = QtCore.QRectF(QtCore.QPointF(50, holes[i].address), QtCore.QSizeF(110, holes[i].size))
#         scene.addRect(r, pen, holes_color)
#         # Hole starting address
#         start = QGraphicsSimpleTextItem(str(holes[i].address))
#         scene.addItem(start)
#         start.setPos(0, holes[i].address - 7)
#         start.setScale(1.4)
#         # Hole ending address
#         end = QGraphicsSimpleTextItem(str(holes[i].address + holes[i].size))
#         scene.addItem(end)
#         end.setPos(0, holes[i].address + holes[i].size - 7)
#         end.setScale(1.4)
#         # Holes size
#         hole_size = QGraphicsSimpleTextItem('Size: ' + str(holes[i].size))
#         scene.addItem(hole_size)
#         hole_size.setPos(68, holes[i].address + holes[i].size / 2 - 10)
#         hole_size.setScale(1.4)
from copy import deepcopy

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.uic import loadUiType
import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from test import Ui_MainWindow
from holes_window import Ui_holes_Form


class Hole:
    def __init__(self, address=None, size=None):
        self.address = address
        self.size = size

    def __str__(self) -> str:  # For Printing a Single Object
        return str(self.address) + " : " + str(self.size)

    def __repr__(self) -> str:  # For Printing List (Collection) of Objects
        return str(self.address) + " : " + str(self.size)


class Main(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.setWindowTitle('Memory Management')
        self.pro=deepcopy(Ui_holes_Form.processes_list)
        self.pro_list = deepcopy(self.pro)
        self.ori_holes = []
        self.holes = []
        self.x = {}
        self.size = Ui_holes_Form.total_memory_for_holes_window.Size
        self.AL = 0
        self.init = False
        # self.SHOW()

    def single_draw(self, pro_segment, holes, memory_size):
        starting_address = []
        segment_data = []

        for key in pro_segment.keys():
            starting_address.append(key)
        for value in pro_segment.values():
            segment_data.append(value)

        scene = QtWidgets.QGraphicsScene()
        self.graphicsView.setScene(scene)
        pen = QtGui.QPen(QtCore.Qt.black, 3)
        memory_color = QtGui.QBrush(QtCore.Qt.black)
        holes_color = QtGui.QBrush(QtCore.Qt.darkGray)
        segments_color = QtGui.QBrush(QtCore.Qt.white)
        r = QtCore.QRectF(QtCore.QPointF(50, 0), QtCore.QSizeF(110, memory_size))
        scene.addRect(r, pen, memory_color)

        mem_start = QGraphicsSimpleTextItem('0')
        scene.addItem(mem_start)
        mem_start.setPos(0, -7)
        mem_start.setScale(1.4)
        mem_end = QGraphicsSimpleTextItem(str(memory_size))
        scene.addItem(mem_end)
        mem_end.setPos(0, memory_size - 7)
        mem_end.setScale(1.4)
        for i in range(len(starting_address)):
            # Segment size
            r = QtCore.QRectF(QtCore.QPointF(50, starting_address[i]), QtCore.QSizeF(110, segment_data[i]['Size']))
            scene.addRect(r, pen, segments_color)
            # Segment name
            seg_name = QGraphicsSimpleTextItem('segment:' + segment_data[i]['Name'])
            scene.addItem(seg_name)
            seg_name.setPos(58, starting_address[i] + segment_data[i]["Size"] / 2 - 10)
            seg_name.setScale(1.4)
            # Parent process of the segment
            pro_name = QGraphicsSimpleTextItem('process: ' + segment_data[i]["Process"])
            scene.addItem(pro_name)
            pro_name.setPos(68, starting_address[i] + segment_data[i]["Size"] / 2 - 25)
            pro_name.setScale(1.4)
            # Starting address of the segment
            start = QGraphicsSimpleTextItem(str(starting_address[i]))
            scene.addItem(start)
            start.setPos(0, starting_address[i] - 7)
            start.setScale(1.4)
            # Ending address of the segment
            end = QGraphicsSimpleTextItem(str(starting_address[i] + segment_data[i]["Size"]))
            scene.addItem(end)
            end.setPos(0, starting_address[i] + segment_data[i]["Size"] - 7)
            end.setScale(1.4)
            # ٍ Segment size
            seg_size = QGraphicsSimpleTextItem('Size: ' + str(segment_data[i]["Size"]))
            scene.addItem(seg_size)
            seg_size.setPos(68, starting_address[i] + segment_data[i]["Size"] / 2 + 7)
            seg_size.setScale(1.4)

        for i in range(len(holes)):
            # Hole size
            r = QtCore.QRectF(QtCore.QPointF(50, holes[i].address), QtCore.QSizeF(110, holes[i].size))
            scene.addRect(r, pen, holes_color)
            # Hole starting address
            start = QGraphicsSimpleTextItem(str(holes[i].address))
            scene.addItem(start)
            start.setPos(0, holes[i].address - 7)
            start.setScale(1.4)
            # Hole ending address
            end = QGraphicsSimpleTextItem(str(holes[i].address + holes[i].size))
            scene.addItem(end)
            end.setPos(0, holes[i].address + holes[i].size - 7)
            end.setScale(1.4)
            # Holes size
            hole_size = QGraphicsSimpleTextItem('HoleSize: ' + str(holes[i].size))
            scene.addItem(hole_size)
            hole_size.setPos(58, holes[i].address + holes[i].size / 2 - 10)
            hole_size.setScale(1.4)

    def show_segments_table(self):
        self.segment_table.setRowCount(0)
        pro_segment = Ui_holes_Form.total_memory_for_holes_window.Pro_Seg
        index = 0
        for i in pro_segment:
            temp = ''
            if pro_segment[i]["Process"] == str(self.pro_choose.currentText()):
                self.segment_table.insertRow(index)
                self.segment_table.setItem(index, 0, QTableWidgetItem(str(pro_segment[i]["Name"])))
                self.segment_table.setItem(index, 1, QTableWidgetItem(str(i)))
                self.segment_table.setItem(index, 2, QTableWidgetItem(str(pro_segment[i]["Size"])))
                index += 1
        self.segment_table.resizeRowsToContents()

    def SHOW(self):
        self.holes = deepcopy(Ui_holes_Form.total_memory_for_holes_window.Holes)
        self.single_draw(self.x, self.holes, self.size)
        # self.show_segments_table(x)

    def reserve(self):
        print("button Clicked")
        try:
            hole = Hole(int(self.res_start.text()), int(self.res_size.text()))
            if Ui_holes_Form.total_memory_for_holes_window.Add_Hole(hole,
                                                                    Ui_holes_Form.total_memory_for_holes_window.Pro_Seg):
                self.pro_list = deepcopy(self.pro)
                self.SHOW()
            else:
                error_msg = QtWidgets.QMessageBox()
                error_msg.setWindowTitle("Hole Error")
                error_msg.setText("This Hole Cannot be Allocated")
                error_msg.setIcon(QtWidgets.QMessageBox.Critical)
                error_msg.exec_()
            self.res_start.clear()
            self.res_size.clear()
        except:
            error_msg = QtWidgets.QMessageBox()
            error_msg.setWindowTitle("Deallocate Error")
            error_msg.setText("Please Enter Valid Reserved Data")
            error_msg.setIcon(QtWidgets.QMessageBox.Critical)
            error_msg.exec_()

    def alloc_btn(self):
        if not self.init:
            self.pro_choose.clear()
            self.segment_table.setRowCount(0)
            self.init = True
        if self.best_fit_radiobtn.isChecked():
            self.AL = 1
        elif self.first_fit_radiobtn.isChecked():
            self.AL = 0
        else:
            error_msg = QtWidgets.QMessageBox()
            error_msg.setWindowTitle("Allocation Error")
            error_msg.setText("Please Select Algorithm first")
            error_msg.setIcon(QtWidgets.QMessageBox.Critical)
            error_msg.exec_()
            return
        if len(self.pro_list) != 0:
            temp = list(self.pro_list[0].Segments.keys())
            t2 = Ui_holes_Form.total_memory_for_holes_window.Allocate_Segment(self.pro_list[0].Name, temp[0],
                                                                         self.pro_list[0].Segments[temp[0]], self.AL)
            if t2:
                t = list(Ui_holes_Form.total_memory_for_holes_window.Pro_Seg.keys())[
                    list(Ui_holes_Form.total_memory_for_holes_window.Pro_Seg.values()).
                        index({"Process": self.pro_list[0].Name, "Name": temp[0], "Size": self.pro_list[0].Segments[temp[0]]})]
                self.x[t] = {"Process": self.pro_list[0].Name, "Name": temp[0], "Size": self.pro_list[0].Segments[temp[0]]}
                self.SHOW()
                self.pro_list[0].Segments.pop(temp[0])
                if not self.pro_list[0].Segments:
                    Ui_holes_Form.total_memory_for_holes_window.Processes.append(self.pro_list[0].Name)
                    self.pro_choose.addItem(self.pro_list[0].Name)
                    self.pro_choose.setCurrentIndex(-1)
                    self.pro_list.pop(0)

            else:
                self.SHOW()
                error_msg = QtWidgets.QMessageBox()
                error_msg.setWindowTitle("No fit")
                error_msg.setText("The Segment: " + temp[0] + "\nof Size: " + str(
                    self.pro_list[0].Segments[temp[0]]) + "\n,from Process: " + self.pro_list[
                                      0].Name + "\nCannot be Allocated")
                error_msg.setIcon(QtWidgets.QMessageBox.Critical)
                error_msg.exec_()
                self.pro_list.pop(0)

    def allocate_process_clicked(self):
        if not (self.first_fit_radiobtn.isChecked() or self.best_fit_radiobtn.isChecked()):
            error_msg = QtWidgets.QMessageBox()
            error_msg.setWindowTitle("Allocation Error")
            error_msg.setText("Please Select Algorithm first")
            error_msg.setIcon(QtWidgets.QMessageBox.Critical)
            error_msg.exec_()
            return
        for p in self.pro:
            if self.first_fit_radiobtn.isChecked():
                Ui_holes_Form.total_memory_for_holes_window.Allocate_Process(p, 0)
                self.AL = 0
            elif self.best_fit_radiobtn.isChecked():
                Ui_holes_Form.total_memory_for_holes_window.Allocate_Process(p, 1)
                self.AL = 1
        self.pro_list = deepcopy(self.pro)
        self.pro_choose.clear()
        self.pro_choose.addItems(Ui_holes_Form.total_memory_for_holes_window.Processes)
        self.pro_choose.setCurrentIndex(-1)
        self.init = False

    def deallocate_process(self):
        t = self.pro_choose.currentText()
        Ui_holes_Form.total_memory_for_holes_window.DeAllocate(t)
        self.pro_choose.clear()
        self.pro_choose.addItems(Ui_holes_Form.total_memory_for_holes_window.Processes)
        self.pro_choose.setCurrentIndex(-1)
        self.segment_table.setRowCount(0)
        self.x = deepcopy(Ui_holes_Form.total_memory_for_holes_window.Pro_Seg)
        for i in self.pro:
            if i.Name == t:
                self.pro.remove(i)
                break
        self.pro_list = deepcopy(self.pro)
        self.SHOW()



def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
