# _*_ coding: utf-8 _*_
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.layers import LSTM
from keras.optimizers import RMSprop
from keras.utils.data_utils import get_file
import numpy as np
import random
import sys

import musicUtil 

class preprocessor(object):
	""" 클래스 너무 개판 애매한 객체지향 보다는 걍 모듈로 빼는게 나을지도 모르겠다. 매개변수 터지지만"""
	def __init__(self, sheet, maxlen = 5):
		"""set으로 중복없애고 리스트 만들어 정렬(chord단위)
		이렇게 되면 맨뒤에 의문사나 .같은게 문제가됨 ?같은거 없애봐라 -> 코드는 상관없징
		chords는 나중에 는 전체 코드 구성으로 바꺼야 됨 
		"""
		split_sheet = sheet.split(' ')
		self.chords = sorted(list(set(split_sheet)))
		self.chord_indices = dict((w, i) for i, w in enumerate(self.chords))
		self.indices_chord = dict((i, w) for i, w in enumerate(self.chords))
		
		self.maxlen = maxlen
		step = 2
		self.sentences = []
		self.next_chords = []
		for i in range(0, len(self.chords) - self.maxlen, step):
			self.sentences.append(split_sheet[i:i + self.maxlen])
			self.next_chords.append(split_sheet[i  +self.maxlen])
		
	def onehotEncodig(self):
		"""
		다음의 형태로 만들어 줍니다.
		x = 데이터의 수 * input_shape(연속 되는 데이터 수 (maxlen = 4라면 (ex A B C D)) * 코드의 종류 수)
		y = 데이터의 수 * 출력(코드의 종류 수(코드의 종류마다 1비트씩 사용함))

		"""
		x = np.zeros((len(self.sentences), self.maxlen, len(self.chords)), dtype=np.bool)
		y = np.zeros((len(self.sentences), len(self.chords)), dtype=np.bool)
		
		for number, sentence in enumerate(self.sentences):
			for index, chord in enumerate(sentence):
				x[number, index, self.chord_indices[chord]] = 1
			y[number, self.chord_indices[self.next_chords[number]]] = 1

		return x,y

def generateSheet(arg, generated, sentence, model):
	"""학습된 model에 의해서 chord를 생성"""
	x = np.zeros((1,arg.maxlen, len(arg.chords)))
	for t, chord in enumerate(sentence):
		x[0, t, arg.chord_indices[chord]] = 1

	preds = model.predict(x, verbose=0)[0]
	next_index = sample(preds, 1.0)
	next_chord = arg.indices_chord[next_index]
	generated += next_chord

	sentence = sentence[1:] #첫번쨰 요소를 제거 	
	sentence.append(next_chord)#새로운 단어를 추가한다.

	#full_sentence.append(next_chord)#버그 보소 
	
	sys.stdout.write(next_chord + ' ')
	sys.stdout.flush()

	return next_chord

	

def buildModel(maxlen, chords):
    print('Build model...')
    model = Sequential()
    model.add(LSTM(128, input_shape=(maxlen, len(chords))))
    model.add(Dense(len(chords)))
    model.add(Activation('softmax'))

    optimizer = RMSprop(lr=0.01)
    model.compile(loss='categorical_crossentropy', optimizer=optimizer)

    return model

def sample(preds, temperature=1.0):
    # 이해 필요
    preds = np.asarray(preds).astype('float64')
    preds = np.log(preds) / temperature
    exp_preds = np.exp(preds)
    preds = exp_preds / np.sum(exp_preds)
    probas = np.random.multinomial(1, preds, 1)
    return np.argmax(probas)

if __name__ == "__main__":
	
	sheet, head = musicUtil.parse_midi("sample.mid")
	#sheet = "G G B B G G B B G G B B G G B B G G B B G G B B A B B B A B B B G G B B A A D D G G B B E E B B G G G G G G G G G G B B G G B B A B B B A B B D G G B B A A D D G G B B E E B B G B A B G B A B G G G G G G G G G G B B A A D D G G B B E E B B G G B B G G B B"
	#pp = preprocessor()
	print sheet
	pp = preprocessor(sheet)
	x,y = pp.onehotEncodig()

	model = buildModel(pp.maxlen, pp.chords)

	sheet_split = sheet.split(' ')

	for iteration in range(1,2):
		print()
		print("Iteration",iteration)

		model.fit(x,y,verbose=0)

		#이부분은 함수화 하는게 좋을거 같다.
		start_index = random.randint(0, len(sheet_split) - pp.maxlen -1)
		generated = ""
		sentence = sheet_split[start_index :start_index + pp.maxlen]
		for chord in sentence:
			generated += (chord + ' ')
		sys.stdout.write(generated)

		chords = generated
		for i in range(100):#일단 반복은 sheet의 
			next_chord = generateSheet(pp, generated, sentence, model)
			chords += (next_chord + ' ')
	print()


	print chords.split(' ')[:-1]#마지막은 똥이 붙어서 빼야됨
	musicUtil.out_midi("test.midi", head, chords.split(' ')[:-1])






