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
    model.add(LSTM(128, input_shape=(maxlen, len(chords)), return_sequences=True))
    model.add(LSTM(128, return_sequences=False))#lstm을 하나 더 추가하니 많이 느려짐
    model.add(Dense(len(chords)))
    model.add(Activation('softmax'))

    optimizer = RMSprop(lr=0.01)
    model.compile(loss='categorical_crossentropy', optimizer=optimizer)

    return model

def generateChord(sheet, preprocessor):
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