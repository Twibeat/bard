# _*_ coding: utf-8 _*_
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.layers import LSTM
from keras.optimizers import RMSprop
from keras.utils.data_utils import get_file
import numpy as np

import musicUtil 

class preprocessor(object):
	""" 클래스 너무 개판 애매한 객체지향 보다는 걍 모듈로 빼는게 나을지도 모르겠다. 매개변수 터지지만
		=>매개변수 터지는건 너무도 큰 고통임
	"""
	def __init__(self, sheet, maxlen = 16):
		
		self.preprocess(sheet)
		"""
		이부분도 함수로 만들것 
		"""
		self.maxlen = maxlen #너무작으면 결과가 이상하게(FFFFFFFFFF같은, 같은거만 나온다면 늘려야됨)
		step = 4 # 시작위치 넘어 갈 순서
		self.sentences = []
		self.next_chords = []
		for i in range(0, len(self.chords) - self.maxlen, step):
			self.sentences.append(sheet[i:i + self.maxlen])        
			self.next_chords.append(sheet[i + self.maxlen])

	def preprocess(self,sheet):
		"""set으로 중복없애고 리스트 만들어 정렬(chord단위)
		이렇게 되면 맨뒤에 의문사나 .같은게 문제가됨 ?같은거 없애봐라 -> 코드는 상관없징
		chords는 나중에 는 전체 코드 구성으로 바꺼야 됨 
		"""
		self.chords = sorted(list(set(sheet)))#list(np.unique(np.array(sheet)))#
		self.chord_indices = dict((w, i) for i, w in enumerate(self.chords))
		self.indices_chord = dict((i, w) for i, w in enumerate(self.chords))
		print self.chord_indices
		print self.indices_chord

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

		return x, y

def generateSheet(arg, generated, model):
	"""학습된 model에 의해서 chord를 생성"""
	x = np.zeros((1, arg.maxlen, len(arg.chords)))
	for t, chord in enumerate(generated):
		x[0, t, arg.chord_indices[chord]] = 1

	preds = model.predict(x, verbose=0)[0]
	next_index = sample(preds, 0.5)
	next_chord = arg.indices_chord[next_index]

	generated.append(next_chord)#새로운 단어를 추가한다.
	#첫번쨰 요소를 제거 
	return generated[1:], next_chord 

def buildModel(maxlen, chords):
    print('Build model...')
    model = Sequential()
    model.add(LSTM(128, input_shape=(maxlen, len(chords)),return_sequences=True))
    model.add(LSTM(128, return_sequences=False))#lstm을 하나 더 추가하니 많이 느려짐
    model.add(Dense(len(chords)))
    model.add(Activation('softmax'))

    optimizer = RMSprop(lr=0.01)
    model.compile(loss='categorical_crossentropy', optimizer=optimizer)

    return model

def sample(preds, temperature=1.0):
    """ 
    float의 범위가 작아서 double(여기서는 float64)로 바꿈 
	
    """
    preds = np.asarray(preds).astype('float64')
    preds = np.log(preds) / temperature
    # 지수평균을 구한다.
    exp_preds = np.exp(preds)
    preds = exp_preds / np.sum(exp_preds)
    # 다항 분포를 구한다.
    probas = np.random.multinomial(1, preds, 1)
    return np.argmax(probas)

