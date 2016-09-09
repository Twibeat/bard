# _*_ coding: utf-8 _*_

import random
from chord_lstm import *

if __name__ == "__main__":
	# midi에서 멜로디를 추출합니다.
	input_file_dir = "twice_cheerup.mid"
	input_file_name = input_file_dir.split('.')[0]
	sheet, head = musicUtil.parse_midi(input_file_dir)
	
	#추출한 멜로디 파일로 만들어 저장합니다.
	musicUtil.out_midi(input_file_name + "_first_voice.midi", head, sheet)

	#멜로디에서 특징을 뽑아내고 학습에 적절한 형태로 만듭니다.
	print sheet
	pp = preprocessor(sheet)
	x,y = pp.onehotEncodig()

	#데이터에 맞는 모델을 만듭니다.
	model = buildModel(pp.maxlen, pp.chords)

	#학습 - 멜로디 생성을 반복합니다.
	for iteration in range(0,101):
		print("Iteration",iteration)

		model.fit(x,y,verbose=0)

		"""
		랜덤으로 시작위치를 정하니까 좀 그런듯 - 현재는 시작 위치를 기준으로 만든다.
		"""
		start_index = random.randint(0, len(sheet) - pp.maxlen -1)
		#generated = sheet[start_index :start_index + pp.maxlen]
		generated = sheet[0:pp.maxlen]
		#chords = generated
		chords = []
		for i in range(len(sheet)):#일단 반복은 sheet의 
			generated, next_chord = generateSheet(pp, generated, model)
			chords.append(next_chord)
		#print chords

		#10번에 한번씩 
		if (iteration % 10) == 0:
			print("Write file")
			output_file_name = input_file_name + '_iter' + str(iteration) + '.midi'
			musicUtil.out_midi(output_file_name, head, chords)






