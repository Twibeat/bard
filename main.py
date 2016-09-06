# _*_ coding: utf-8 _*_

import random
from chord_lstm import *

if __name__ == "__main__":
	
	sheet, head = musicUtil.parse_midi("original.midi")
	
	print sheet
	pp = preprocessor(sheet)
	x,y = pp.onehotEncodig()

	model = buildModel(pp.maxlen, pp.chords)

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
		if (iteration % 10) == 0:
			filename = 'test_iter' + str(iteration) + '.midi'
			musicUtil.out_midi(filename, head, chords)






