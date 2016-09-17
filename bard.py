# _*_ coding: utf-8 _*_

from generator import Generator
from preprocessor import MidiTool


input_file = "twice_like_ooh_ahh.midi"
input_file_folder = "./input_files/"
input_file_dir = input_file_folder + input_file
input_file_name = input_file.split('.')[0]

output_file_dir = "./output_files/"

def iterate_train_generation(x, y, header, sheet, times=30):
	#학습 - 멜로디 생성을 반복합니다.
	#곡 1개 기준으로 30번 학습정도면 최소 loss에 도달
	for iteration in range(1, times+1):
		print("Iteration",iteration)
		output_values = generator.train_generation(x, y, sheet)

		#10번에 한번씩 파일을 만든다.
		if (iteration % 10) == 0:
			print("Write file")
			output_file_name = output_file_dir + input_file_name + '_iter' + str(iteration) + '.midi'
			midi_util.out_midi(output_file_name, header, output_values)

if __name__ == "__main__":

	midi_util = MidiTool()

	sheet, header = midi_util.parseMidi(input_file_dir)

	#추출한 멜로디를 파일로 만들어 저장합니다.(스트림중 하나만 고르기 때문에 생성된것과 비교를 위함)
	midi_util.out_midi(output_file_dir + input_file_name + "_input.midi", header, sheet)

	x, y, input_set = midi_util.preprocess(sheet)#(sheet)

	generator = Generator(midi_util.maxlen, input_set)

	iterate_train_generation(x, y, header, sheet, 50)
