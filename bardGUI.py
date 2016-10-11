# _*_ coding: utf-8 _*_
import sys
import os
from PyQt4.QtGui import *
from PyQt4 import QtCore

import GUI 
from bard import Bard
"""
추가적인 파라미터 필요
"""
class MainDialog(QDialog, GUI.Ui_Dialog):
    def __init__(self, parent=None):
        super(MainDialog, self).__init__(parent)
        
        # 다이얼 로그 설정
        self.setupUi(self)
        
        # 이벤트 설정
        self.input_pushButton.clicked.connect(self.getInputFile)
        self.output_pushButton.clicked.connect(self.setOutputDir)
        self.generate_pushButton.clicked.connect(self.setGenerate)

        # 경로
        self.input_file_dir = ""
        self.output_file_dir = ""

        # 백그라운드 작업
        self.backgroundProcess = BackgroundThread()
        self.backgroundProcess.backgroundDone.connect(self.finished)

    def getInputFile(self):
        input_file_dir = QFileDialog.getOpenFileName(self, 
        	u'파일을 선택해주세요', 'c:\\',"midi files (*.midi *.mid)")
        self.input_lineEdit.setText(input_file_dir)

    def setOutputDir(self):
    	output_file_dir = QFileDialog.getExistingDirectory(self,
    		u'출력 디렉토리를 지정해 주세요', 'c:\\')
    	self.output_lineEdit.setText(output_file_dir + '\\')
    
    def setGenerate(self):
        self.input_file_dir = str(self.input_lineEdit.text())
        self.output_file_dir = str(self.output_lineEdit.text())

    	if not os.path.exists(self.input_file_dir) or not os.path.exists(self.output_file_dir):
    		QMessageBox.information(self, u"경로 없음", u"잘못된 경로 입니다. 올바른 경로를 지정해 주세요");return
        #bard = Bard(str(self.input_file_dir), str(self.output_file_dir)+"\\")
        #bard = bard.main(10)
        self.backgroundProcess.setDir(self.input_file_dir, self.output_file_dir)
        self.backgroundProcess.start()
        QMessageBox.information(self, u"파일 생성", u"파일 생성을 생성합니다.")
        #QMessageBox.information(self, u"생성 완료", u"파일 생성 완료")

    def finished(self):
        QMessageBox.information(self, u"파일 생성 완료", u"파일이 생성되었습니다.")

class BackgroundThread(QtCore.QThread):
    backgroundDone = QtCore.pyqtSignal(bool)
    def setDir(self, input_file_dir, output_file_dir):
        self.input_file_dir = input_file_dir
        self.output_file_dir = output_file_dir

    def run(self):
        """
        오버라이딩 함수 start로 실행 main은 함수 분리할 필요가 있음

        """
        bard = Bard(self.input_file_dir, self.output_file_dir)
        bard = bard.main(10)
        self.backgroundDone.emit(True)
        

app = QApplication(sys.argv)
dialog = MainDialog()
dialog.show()
app.exec_()