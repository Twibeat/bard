# _*_ coding: utf-8 _*_
import sys
import os
from PyQt4.QtGui import *
from PyQt4 import QtCore

import multiGUI 
from bard import Bard
from multiBard import MultiBard
"""
추가적인 파라미터 필요
"""
class MainDialog(QDialog, multiGUI.Ui_Dialog):
    def __init__(self, parent=None):
        super(MainDialog, self).__init__(parent)
        
        # 다이얼 로그 설정
        self.setupUi(self)
        
        # 이벤트 설정
        self.input_pushButton.clicked.connect(self.getImproviseInputFile)
        self.output_pushButton.clicked.connect(self.setImproviseOutputDir)
        self.improvise_pushButton.clicked.connect(self.setImproviseGenerate)
        self.train_input_pushButton.clicked.connect(self.setTrainInputDir)
        self.train_output_pushButton.clicked.connect(self.setTrainOutputDir)
        self.train_pushButton.clicked.connect(self.multiTrain)
        self.generate_table_pushButton.clicked.connect(self.setGenerateTableFile)
        self.generate_weight_pushButton.clicked.connect(self.setGenerateWeightFile)
        self.generate_output_pushButton.clicked.connect(self.setGenerateOutputDir)
        self.generate_pushButton.clicked.connect(self.generateMidi)
        # 경로
        self.input_file_dir = ""
        self.output_file_dir = ""

        # 백그라운드 작업
        self.backgroundProcess = BackgroundThread()
        self.backgroundProcess.backgroundDone.connect(self.finishedGeneration)

        self.backgroundProcessTrain = BackgroundThreadTrain()
        self.backgroundProcessTrain.backgroundDone.connect(self.finishedTrain)

        self.backgroundProcessGenerate = BackgroundThreadGenerate()
        self.backgroundProcessGenerate.backgroundDone.connect(self.finishedGeneration)

    def getImproviseInputFile(self):
        input_file_dir = QFileDialog.getOpenFileName(self, 
        	u'파일을 선택해주세요', 'c:\\',"midi files (*.midi *.mid)")
        self.input_lineEdit.setText(input_file_dir)

    def setImproviseOutputDir(self):
    	output_file_dir = QFileDialog.getExistingDirectory(self,
    		u'출력 디렉토리를 지정해 주세요', 'c:\\')
    	self.output_lineEdit.setText(output_file_dir + '\\')
    
    def setImproviseGenerate(self):
        self.input_file_dir = str(self.input_lineEdit.text())
        self.output_file_dir = str(self.output_lineEdit.text())

    	if (not os.path.exists(self.input_file_dir)) or (not os.path.exists(self.output_file_dir)):
    		QMessageBox.information(self, u"경로 없음", u"잘못된 경로 입니다. 올바른 경로를 지정해 주세요");return

        iteraion = self.iteraion_spinBox.value()    
        self.backgroundProcess.setParameter(self.input_file_dir, self.output_file_dir, iteraion)
        self.backgroundProcess.start()
        QMessageBox.information(self, u"파일 생성", u"파일을 생성합니다.")

    def finishedGeneration(self):
        QMessageBox.information(self, u"파일 생성 완료", u"파일이 생성되었습니다.")

    def finishedTrain(self):
        QMessageBox.information(self, u"학습 완료", u"가중치파일과 테이블 파일이 생성되었습니다.")

    def setTrainInputDir(self):
        input_file_dir = QFileDialog.getExistingDirectory(self,u'미디 파일의 디렉토리를 선택해주세요', 'c:\\')
        self.train_input_lineEdit.setText(input_file_dir+'\\')

    def setTrainOutputDir(self):
        output_file_dir = QFileDialog.getExistingDirectory(self,u'출력 디렉토리를 지정해 주세요', 'c:\\')
        self.train_output_lineEdit.setText(output_file_dir+'\\')

    def multiTrain(self):
        input_file_dir = str(self.train_input_lineEdit.text())
        output_file_dir = str(self.train_output_lineEdit.text())

        if (not os.path.exists(input_file_dir)) or (not os.path.exists(output_file_dir)):
            QMessageBox.information(self, u"경로 없음", u"잘못된 경로 입니다. 올바른 경로를 지정해 주세요");return;
        
        iteraion = self.train_iteraion_spinBox.value()    
        self.backgroundProcessTrain.setParameter(input_file_dir, output_file_dir, iteraion)
        self.backgroundProcessTrain.start()
        QMessageBox.information(self, u"파일 생성", u"파일을 생성합니다.")
    
    def setGenerateTableFile(self):
        table_file_dir = QFileDialog.getOpenFileName(self, 
            u'파일을 선택해주세요', 'c:\\',"table files (*.table)")
        self.generation_table_lineEdit.setText(table_file_dir)

    def setGenerateWeightFile(self):
        weight_file_dir = QFileDialog.getOpenFileName(self, 
            u'파일을 선택해주세요', 'c:\\',"weight files (*.hdf5)")
        self.generation_weight_lineEdit.setText(weight_file_dir)
    
    def setGenerateOutputDir(self):
        output_file_dir = QFileDialog.getExistingDirectory(self,
            u'출력 디렉토리를 지정해 주세요', 'c:\\')
        self.generation_output_lineEdit.setText(output_file_dir + '\\')

    def generateMidi(self):
        table_file_dir = str(self.generation_table_lineEdit.text())
        weight_file_dir = str(self.generation_weight_lineEdit.text())
        output_file_dir = str(self.generation_output_lineEdit.text())

        if (not os.path.exists(table_file_dir)) or (not os.path.exists(weight_file_dir)) or (not os.path.exists(output_file_dir)):
            QMessageBox.information(self, u"경로 없음", u"잘못된 경로 입니다. 올바른 경로를 지정해 주세요");return;
           
        self.backgroundProcessGenerate.setParameter(table_file_dir, weight_file_dir, output_file_dir)
        self.backgroundProcessGenerate.start()
        QMessageBox.information(self, u"파일 생성", u"파일을 생성합니다.")

class BackgroundThread(QtCore.QThread):
    backgroundDone = QtCore.pyqtSignal(bool)
    def setParameter(self, input_file_dir, output_file_dir, iteraion = 10):
        self.input_file_dir = input_file_dir
        self.output_file_dir = output_file_dir
        self.iteraion = iteraion
    def run(self):
        """
        오버라이딩 함수 start로 실행 main은 함수 분리할 필요가 있음

        """
        bard = Bard(self.input_file_dir, self.output_file_dir)
        sheet, header, x, y, input_set = bard.preprocess()
        bard.generate(sheet, header, x, y, input_set, self.iteraion)
        
        self.backgroundDone.emit(True)

class BackgroundThreadTrain(QtCore.QThread):
    backgroundDone = QtCore.pyqtSignal(bool)
    def setParameter(self, input_file_dir, output_file_dir, iteraion = 10):
        self.input_file_dir = input_file_dir
        self.output_file_dir = output_file_dir
        self.iteraion = iteraion

    def run(self):
        multibard = MultiBard()
        sheets, headers = multibard.parse_midi(self.input_file_dir, self.output_file_dir)
        x_list, y_list = multibard.preprocess(sheets)
        multibard.init_generator(multibard.tables)
        multibard.multi_train_iterate(sheets, x_list, y_list, self.iteraion)

        multibard.save_weights(self.output_file_dir+'weights.hdf5')
        multibard.save_table(self.output_file_dir+'tables.table')

        self.backgroundDone.emit(True)

class BackgroundThreadGenerate(QtCore.QThread):
    backgroundDone = QtCore.pyqtSignal(bool)
    def setParameter(self, table_file_dir, weight_file_dir, output_file_dir):
        self.table_file_dir = table_file_dir
        self.weight_file_dir = weight_file_dir
        self.output_file_dir = output_file_dir

    def run(self):
        multiBard = MultiBard()
        multiBard.load_tables(self.table_file_dir)
        multiBard.init_generator(multiBard.tables)
        multiBard.load_weights(self.weight_file_dir)

        """
        sample 입력 받아서 테스트 하면됨
        """
        self.backgroundDone.emit(True)
app = QApplication(sys.argv)
dialog = MainDialog()
dialog.show()
app.exec_()