# _*_ coding: utf-8 _*_

import random
from chord_lstm import *

def generate_chord(sheet, preprocessor):
	print "generate chords..."
	"""
	preprocessed라는 매개변수는 조금 그렇다.
	랜덤으로 시작위치를 정하니까 좀 그런듯 
	-> 현재는 시작 위치를 기준으로 만든다.
	"""
	#start_index = random.randint(0, len(sheet) - preprocessed.maxlen -1)
	#generated = sheet[start_index :start_index + preprocessed.maxlen]
	generated = sheet[0:preprocessor.maxlen]
	
	#첫번째 멜로디를 넣을 것인가 여부 
	#chords = generated # 일단 안넣는다.
	chords = []
	for i in range(len(sheet)):#일단 반복은 sheet의 
		generated, next_chord = generateSheet(preprocessor, generated, model)
		chords.append(next_chord)
	#print chords
	return chords

def train_generation_iterate(x, y, model, head, sheet, times=50):
	#학습 - 멜로디 생성을 반복합니다.
	#곡 1개 기준으로 50번 학습정도면 최소 loss에 도달함
	for iteration in range(0, times):
		print("Iteration",iteration)
		# 학습시킨다. 안되면 verbose=0으로 하면 되는 경우가 있음(데이터가 너무 작으면 에러 발생.)
		model.fit(x,y,verbose=1)

		chords = generate_chord(sheet,preprocessed)

		#10번에 한번씩 파일을 만든다.
		if (iteration % 10) == 0:
			print("Write file")
			output_file_name = input_file_name + '_iter' + str(iteration) + '.midi'
			musicUtil.out_midi(output_file_name, head, chords)

if __name__ == "__main__":
	# midi에서 멜로디를 추출합니다.
	input_file_dir = "twice_cheerup.mid"
	input_file_name = input_file_dir.split('.')[0]
	sheet, head = musicUtil.parse_midi(input_file_dir)
	
	#추출한 멜로디를 파일로 만들어 저장합니다.(스트림중 하나만 고르기 때문에 생성된것과 비교를 위함)
	musicUtil.out_midi(input_file_name + "_input.midi", head, sheet)

	#멜로디에서 특징을 뽑아내고 학습에 적절한 형태로 만듭니다.
	print sheet
	preprocessed = preprocessor(sheet)
	x,y = preprocessed.onehotEncodig()

	#데이터에 맞는 모델을 만듭니다.
	model = buildModel(preprocessed.maxlen, preprocessed.chords)

	iterate(x, y model, head, sheet, 11)
	





