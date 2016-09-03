# _*_ coding: utf-8 _*_

import random
from chord_lstm import *

if __name__ == "__main__":
	
	sheet, head = musicUtil.parse_midi("twice_cheerup.mid")
	
	print sheet
	pp = preprocessor(sheet)
	x,y = pp.onehotEncodig()

	model = buildModel(pp.maxlen, pp.chords)

	for iteration in range(1,2):
		print("Iteration",iteration)

		model.fit(x,y,verbose=0)

		"""랜덤으로 시작위치를 정하니까 좀 그런듯 
		"""
		start_index = random.randint(0, len(sheet) - pp.maxlen -1)
		generated = sheet[start_index :start_index + pp.maxlen]
		
		chords = generated
		for i in range(len(sheet)):#일단 반복은 sheet의 
			generated, next_chord = generateSheet(pp, generated, model)
			chords.append(next_chord)
		print chords
	musicUtil.out_midi("test_1.midi", head, chords)






