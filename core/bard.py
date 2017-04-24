# _*_ coding: utf-8 _*_

from core.generator import Generator
from core.preprocessor import MidiTool
"""
multi는 복잡하니까 단분한 버전도 남김 - 아니지 재사용할수 있어야지!!
"""
class Bard():
	def __init__(self, input_file_dir, output_file_dir):
		self.input_file_dir = input_file_dir
		self.input_file = input_file_dir.split('/')[-1]
		self.input_file_name = self.input_file.split('.')[0]

		self.output_file_dir = output_file_dir

	def preprocess(self, step = 1, maxlen = 16):
		self.maxlen = maxlen
		self.step = step

		self.midi_tool = MidiTool(step, maxlen)

		sheet, header = self.midi_tool.parseMidi(self.input_file_dir)

		x, y , input_set = self.midi_tool.preprocess(sheet)

		return sheet, header, x, y, input_set

	def generate(self, sheet, header, x, y, input_set, n_iteration = 10):
		self.generator = Generator(self.maxlen, input_set)

		self.iterate_train_generation(x, y, header, sheet, n_iteration)

	def iterate_train_generation(self, x, y, header, sheet, times = 30):
		#학습 - 멜로디 생성을 반복합니다.
		#곡 1개 기준으로 30번 학습정도면 최소 loss에 도달
		for iteration in range(1, times + 1):
			print("Iteration",iteration)
			output_values = self.generator.train_generation(x, y, sheet)

			#10번에 한번씩 파일을 만든다.
			if (iteration % 10) == 0:
				print("Write file")
				output_file_name = self.output_file_dir + self.input_file_name + '_iter' + str(iteration) + '.mid'
				self.midi_tool.out_midi(output_file_name, header, output_values)
		print("iteration finished")

	def save_weights(self, filename="./weight.hdf5"):
		self.generator.saveWeights(filename)

	def load_weights(self, filename="./weight.hdf5"):
		self.generator.loadWeights(filename)

