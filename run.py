from PyQt5 import QtWidgets
from imageprocess import Ui_MainWindow
#from PyQt5.QtWidgets import QFileDialog
from imageedit import imageedit_self
from bottombutton import button_self
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class mywindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def  __init__ (self):
        super(mywindow, self).__init__()
        self.setupUi(self)
        self.open.triggered.connect(self.read_file)#打开
        self.save.triggered.connect(self.save_file)#保存
        #编辑
        self.zoomin.triggered.connect(self.zoomin_file)#放大
        self.zoomout.triggered.connect(self.zoomout_file)#缩小
        self.gray.triggered.connect(self.gray_file)#灰度
        self.light.triggered.connect(self.light_file)#亮度
        self.rotate.triggered.connect(self.rotate_file)#旋转
        self.screenshots.triggered.connect(self.screenshots_file)#截图
        #按钮功能
        #浏览
        self.Scan.clicked.connect(self.scan_file)


    def read_file(self):
        #选取文件
        filename, filetype =QFileDialog.getOpenFileName(self, "打开文件", "D:/imagetest", "All Files(*);;Text Files(*.png)")
        print(filename, filetype)
        self.lineEdit.setText(filename)
        self.label_pic.setPixmap(QPixmap(filename))

    def save_file(self):
        #获取文件路径
        file_path = self.lineEdit.text()
        if file_path=='':
            self.showMessageBox()
        else:
            # 用全局变量保存所有需要保存的变量在内存中的值。
            file_name = QFileDialog.getSaveFileName(self,"文件保存","D:/imagetest/save","All Files (*);;Text Files (*.png)")
            print(file_name[0])
            btn=button_self()
            btn.file_save(file_path,file_name[0])

    def zoomin_file(self):#放大
        file_path = self.lineEdit.text()
        if file_path=='':
            self.showMessageBox()
        else:
            imageedit_self.imagemagnification(file_path)

    def zoomout_file(self):#缩小
        file_path = self.lineEdit.text()
        if file_path=='':
            self.showMessageBox()
        else:
            imageedit_self.imagereduction(file_path)

    def gray_file(self):#灰度
        file_path = self.lineEdit.text()
        if file_path=='':
            self.showMessageBox()
        else:
            imageedit_self.imagegray(file_path)

    def light_file(self):#亮度
        file_path = self.lineEdit.text()
        if file_path=='':
            self.showMessageBox()
        else:
            imageedit_self.imagebrightness(file_path,1.3,3)

    def rotate_file(self):#旋转
        file_path = self.lineEdit.text()
        if file_path=='':
            self.showMessageBox()
        else:
            imageedit_self.imagerotate(file_path)

    def screenshots_file(self):#截图
        file_path = self.lineEdit.text()
        if file_path=='':
            self.showMessageBox()
        else:
            imageedit_self.imagegrab(file_path)
    #按钮功能
    #浏览
    def scan_file(self):
        file_path = self.lineEdit.text()
        if file_path=='':
            self.showMessageBox()
        else:
            btn=button_self()
            btn.scan_pic(file_path)#

    def showMessageBox(self):
       res_3 = QMessageBox.warning(self, "警告", "请选择文件，再执行该操作！", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

if __name__=="__main__":
    import sys
    app=QtWidgets.QApplication(sys.argv)
    ui = mywindow()    
    ui.show()
    sys.exit(app.exec_())
