# _*_ coding: utf-8 _*_

from generator import Generator
from preprocessor import MidiTool
import glob
import os
import numpy as np
"""
다중으로 가르치려면 어떻게 할까?
->generator가 살아 있어야함 
-> 여러 파일의 테이블을 하나로 하는 것으로 해결 
-> 하지만 각각은 input이 작아서 문제 발생 
-> 각 파일에 대하여 원핫엔코딩을해서 그렇다.
-> 테이블 하나 만들어서 그걸로 다쓰고 해야 할듯 
처음에 generator를 살리고 모든것을 저장하는 테이블이 있으면 끝날텐데 ....

max_length이름은 직관적이지 않다. batch_size같은게 맞지 않나?
abcdef -> g 에서 len(abcdef)이니까
"""
class Bard():
	def __init__(self, input_file_dir, output_file_dir):
		self.input_file_dir = input_file_dir
		#self.input_file = input_file_dir.split('/')[-1]
		#self.input_file_name = self.input_file.split('.')[0]
		self.output_file_dir = output_file_dir
		self.max_length = 16
		self.step = 1
		self.midi_tool = MidiTool(self.step, self.max_length)

	def parse_midi(self):
		sheets = []
		headers = []
		#폴더에 있는 midi파일들의 이름을 가져와서 각각 parsing
		if(os.path.exists(self.input_file_dir)):
			midifile_list = glob.glob(self.input_file_dir + "*.mid")
			midifile_list = midifile_list + glob.glob(self.input_file_dir + "*.midi")
			#파일이 없으면 종료 하는 루틴이 필요 할 듯
			for midifile in midifile_list:
				sheet, header = self.midi_tool.parseMidi(midifile)
				sheets.append(sheet)
				headers.append(header)
			return sheets, headers
		else:
			#없으면 종료
			print("dir is noting")
	
	def make_tables(self, sheets):
		"""
		안으로 넣을수는 없을까?
		"""
		tables = []
		for sheet in sheets:
			table = list(set(sheet))
			tables += table
		
		self.tables = sorted(list(set(tables)))
		self.tables_indices = dict((t, i) for i, t in enumerate(tables))
		self.indices_tables = dict((i, t) for i, t in enumerate(tables))	

	def mappingData(self, sheet):
		"""
		학습할 x(sentences) y(next_values)를 정한다.
		이걸 뽑아 내다니 ㅠㅠ
		"""
		values = sorted(list(set(sheet)))
		self.sentences = []
		self.next_values = []
		for i in range(0, len(values) - self.max_length, self.step):
			self.sentences.append(sheet[i : i + self.max_length])
			self.next_values.append(sheet[i + self.max_length])

		x = np.zeros((len(self.sentences), self.max_length, len(self.tables)), dtype = np.bool)
		y = np.zeros((len(self.sentences), len(self.tables)), dtype = np.bool)

		for number, sentence in enumerate(self.sentences):
			for index, value in enumerate(sentence):
				x[number, index, self.tables_indices[value]] = 1
			y[number, self.tables_indices[self.next_values[number]]] = 1

		return x, y	

	def preprocess(self, sheets):
		x_list = []
		y_list = []

		self.make_tables(sheets)

		for sheet in sheets:
			x, y = self.mappingData(sheet)
			x_list.append(x)
			y_list.append(y)

		return x_list, y_list
	
	def init_generator(self, table):
		self.generator = Generator(self.max_length, table)

	def train(self, x, y):
		self.generator.train(x, y)

	def save_weights(self, filename="./weight.hdf5"):
		self.generator.saveWeights(filename)

	def load_weights(self, filename="./weight.hdf5"):
		self.generator.loadWeights(filename)

if __name__ == "__main__":
	input_file_dir = "./input_files/"
	output_file_dir = "./output_files/"

	bard = Bard(input_file_dir, input_file_dir)
	sheets, headers = bard.parse_midi()
	x_list, y_list= bard.preprocess(sheets)
	bard.init_generator(bard.tables)

	bard.train(x_list[1], y_list[1])
		
		
	

