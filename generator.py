# _*_ coding: utf-8 _*_
"""
재구성하기 위함 아직 사용은 하지 않는다.
"""
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.layers import LSTM
from keras.optimizers import RMSprop
from keras.utils.data_utils import get_file
import numpy as np

class Generator():
	def __init__(self, max_length, value_length):
		self.max_length = max_length
		self.value_length = value_length
		self.values_indices = 
		self.indices_values = dict((i, v) for i, v in enumerate(self.values))


		self.model = Sequential()
		self.model.add(LSTM(128, input_shape=(max_length, value_length), return_sequences=True))
		self.model.add(LSTM(128, return_sequences=False))
		self.model.add(Dense(value_length))	
		self.model.add(Activation('softmax'))

		optimizer = RMSprop(lr=0.01)
		self.model.compile(loss='categorical_crossentropy', optimizer=optimizer)
	
	def generateList(self):
		pass
	def generateNewNote(self):
		pass
	def sample(self):
		pass

	def train_generation_iterate(self, x, y, head, sheet, times=50):
		#학습 - 멜로디 생성을 반복합니다.
		#곡 1개 기준으로 50번 학습정도면 최소 loss에 도달함
		for iteration in range(0, times):
			print("Iteration",iteration)
			# 학습시킨다. 안되면 verbose=0으로 하면 되는 경우가 있음(데이터가 너무 작으면 에러 발생.)
			self.model.fit(x, y, verbose=1)

			values = self.generateValue(sheet)

			#10번에 한번씩 파일을 만든다.
			if (iteration % 10) == 0:
				print("Write file")
				output_file_name = "oop_test" + '_iter' + str(iteration) + '.midi'
				musicUtil.out_midi(output_file_name, head, values)
	
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
		for i in range(len(sheet)):#일단 반복은 sheet의 
			generated, next_value = generateSheet(generated)
			values.append(next_value)
		#print values
		return values

	def generateSheet(self, generated):
		"""학습된 model에 의해서 value를 생성"""
		x = np.zeros((1, self.max_length, self.value_length))
		for t, value in enumerate(generated):
			x[0, t, self.value_indices[value]] = 1

		preds = self.model.predict(x, verbose=0)[0]
		next_index = sample(preds, 0.5)
		next_value = self.indices_value[next_index]

		generated.append(next_value)#새로운 단어를 추가한다.
		#첫번쨰 요소를 제거 
		return generated[1:], next_value 

def buildModel(maxlen, values):
    print('Build model...')
    model = Sequential()
    model.add(LSTM(128, input_shape=(maxlen, len(values)), return_sequences=True))
    model.add(LSTM(128, return_sequences=False))#lstm을 하나 더 추가하니 많이 느려짐
    model.add(Dense(len(values)))
    model.add(Activation('softmax'))

    optimizer = RMSprop(lr=0.01)
    model.compile(loss='categorical_crossentropy', optimizer=optimizer)

    return model

def generatevalue(sheet, preprocessor):
	print "generate values..."
	"""
	preprocessed라는 매개변수는 조금 그렇다.
	랜덤으로 시작위치를 정하니까 좀 그런듯 
	-> 현재는 시작 위치를 기준으로 만든다.
	"""
	#start_index = random.randint(0, len(sheet) - preprocessed.maxlen -1)
	#generated = sheet[start_index :start_index + preprocessed.maxlen]
	generated = sheet[0:preprocessor.maxlen]
	
	#첫번째 멜로디를 넣을 것인가 여부 
	#values = generated # 일단 안넣는다.
	values = []
	for i in range(len(sheet)):#일단 반복은 sheet의 
		generated, next_value = generateSheet(preprocessor, generated, model)
		values.append(next_value)
	#print values
	return values

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