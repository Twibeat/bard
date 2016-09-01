# _*_ coding: utf-8 _*_

import random
from chord_lstm import *

if __name__ == "__main__":
	
	sheet, head = musicUtil.parse_midi("twice_cheerup.mid")
	
	print sheet
	pp = preprocessor(sheet)
	x,y = pp.onehotEncodig()

	model = buildModel(pp.maxlen, pp.chords)

	sheet_split = sheet.split(' ')

	for iteration in range(1,2):
		print()
		print("Iteration",iteration)

		model.fit(x,y,verbose=0)

		"""이부분은 함수화 하는게 좋을거 같다.
		그리고 랜덤으로 시작위치를 정하니까 좀 그런듯 
		"""
		start_index = random.randint(0, len(sheet_split) - pp.maxlen -1)
		generated = ""
		sentence = sheet_split[start_index :start_index + pp.maxlen]
		for chord in sentence:
			generated += (chord + ' ')
		sys.stdout.write(generated)

		chords = generated
		for i in range(len(sheet_split)):#일단 반복은 sheet의 
			next_chord = generateSheet(pp, generated, sentence, model)
			chords += (next_chord + ' ')
	print()


	print chords.split(' ')[:-1]#마지막은 똥이 붙어서 빼야됨
	musicUtil.out_midi("test_1.midi", head, chords.split(' ')[:-1])






