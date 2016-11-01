# _*_ coding: utf-8 _*_

from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.layers import LSTM
from keras.optimizers import RMSprop
from keras.utils.data_utils import get_file
import numpy as np

class Generator():
	def __init__(self, max_length, values, lstm_dim = 2):
		self.max_length = max_length
		self.values_length = len(values)
		self.values_indices = dict((v, i) for i, v in enumerate(values)) 
		self.indices_values = dict((i, v) for i, v in enumerate(values))
		""" 
		lstm의 차원은 최소 2차원이 되어야 한다. 입력이 2차원이기 때문 [max_length, values_length]형태로 들어감
		"""
		if lstm_dim < 2:
			lstm_dim = 2

		self.model = Sequential()
		self.model.add(LSTM(lstm_dim, input_shape=(max_length, self.values_length), return_sequences=True))
		self.model.add(LSTM(lstm_dim, return_sequences=False))
		self.model.add(Dense(self.values_length))	
		self.model.add(Activation('softmax'))

		optimizer = RMSprop(lr=0.01)
		self.model.compile(loss='categorical_crossentropy', optimizer=optimizer)
	
	def sample(self, preds, temperature=1.0):
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
	    # 가장 큰 값을 반환 한다.
	    return np.argmax(probas)
	    
	def train(self, x, y):
		self.model.fit(x, y, verbose=0)

	def train_generation(self, x, y, sheet):
		# 학습시킨다. 안되면 verbose=0으로 하면 되는 경우가 있음(데이터가 너무 작으면 에러 발생.)
		self.train(x, y)
		values = self.generateValue(sheet)
		return values

	def generateValue(self, sheet):
		print "generate values..."
		"""
		preprocessed라는 매개변수는 조금 그렇다.
		랜덤으로 시작위치를 정하니까 좀 그런듯 
		-> 현재는 시작 위치를 기준으로 만든다.
		"""
		#start_index = random.randint(0, len(sheet) - preprocessed.maxlen -1)
		#generated = sheet[start_index :start_index + preprocessed.maxlen]
		generated = sheet[0:self.max_length]
		
		#첫번째 멜로디를 넣을 것인가 여부 
		#values = generated # 일단 안넣는다.
		values = []
		for i in range(len(sheet)):#일단 반복은 sheet의 크기로
			generated, next_value = self.generateNextValue(generated)
			values.append(next_value)
		#print values
		return values

	def generateNextValue(self, generated):
		"""학습된 model에 의해서 value를 생성"""
		x = np.zeros((1, self.max_length, self.values_length))
		for t, value in enumerate(generated):
			x[0, t, self.values_indices[value]] = 1

		preds = self.model.predict(x, verbose=0)[0]
		next_index = self.sample(preds)
		next_value = self.indices_values[next_index]

		generated.append(next_value)#새로운 단어를 추가한다.
		#첫번쨰 요소를 제거 
		return generated[1:], next_value

	def saveWeights(self,filename):
		self.model.save_weights(filename)

	def loadWeights(self,filename):
		self.model.load_weights(filename)