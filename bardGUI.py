# _*_ coding: utf-8 _*_
import sys
from PyQt4.QtGui import *

import GUI 
from bard import Bard
class MainDialog(QDialog, GUI.Ui_Dialog):
    def __init__(self):
        QDialog.__init__(self)
        
        # 다이얼 로그 설정
        self.setupUi(self)
        
        # 이벤트 설정
        self.input_pushButton.clicked.connect(self.getInputFile)
        self.output_pushButton.clicked.connect(self.setOutputFolder)
        self.generate_pushButton.clicked.connect(self.generate)

        # 경로
        self.input_file_dir = ""
        self.output_file_dir = ""

    def getInputFile(self):
        self.input_file_dir = QFileDialog.getOpenFileName(self, 
        	u'파일을 선택해주세요', 'c:\\',"midi files (*.midi *.mid)")
        self.input_lineEdit.setText(self.input_file_dir)

    def setOutputFolder(self):
    	self.output_file_dir = QFileDialog.getExistingDirectory(self,
    		u'출력 디렉토리를 지정해 주세요', 'c:\\')
    	self.output_lineEdit.setText(self.output_file_dir)
    
    def generate(self):
    	if self.input_file_dir == "" or self.output_file_dir == "":
    		QMessageBox.information(self, u"경로 없음", u"경로를 지정해 주세요")
        bard = Bard(str(self.input_file_dir), str(self.output_file_dir)+"\\")
        bard = bard.main(10)
        QMessageBox.information(self, u"생성 완료", u"파일 생성 완료")

    
app = QApplication(sys.argv)
dlg = MainDialog()
dlg.show()
app.exec_()