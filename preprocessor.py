# _*_ coding: utf-8 _*_
"""
재구성하기위함 아직 사용은 하지 않는다.
"""
from music21 import note, stream, converter, midi
from fractions import Fraction
import numpy as np

class MidiTool:
	def __init__(self, step = 1, maxlen=16):
		"""
		maxlen을 크게 하고 step의 수룰 줄이면 한음만 반복되는 현상이 줄어 들지만 학습이 느려진다.
		maxlen이라는 이름은 좀 그렇다. 한번에 학습시킬 멜로디의 수를 나타내는건데...
		"""
		self.maxlen = maxlen
		self.step = step

	def parseMidi(self, filename):
		"""
		http://web.mit.edu/music21/doc/usersGuide/usersGuide_17_derivations.html	
		sample.mid는 불러오면 Sore이고 여러개의 Part로 구성된다. Part는 Voice로 구성되어 있다.
		midi파일에서 최초의 Voice를 찾는다. 
		=> 문제의 여지가 있다. 항상 Voice에서 피아노 멜로디가 있는게 아니라서 
		"""
		print "parse midi file..."
		score = converter.parse(filename)
		for part in score:
			for voice in part:
				if isinstance(voice, stream.Voice):
					print "length: ", len(voice)
					return self.makeList(voice)

	def parseMidi2(self, filename):
		"""
		여러개를 학습 시키기 위한 연구 중	
		"""
		header_list = []
		melody_list = []

		print "parse midi file..."
		score = converter.parse(filename)
		for part in score:
			for voice in part:
				if isinstance(voice, stream.Voice):					
					melody, header = self.makeList(voice)
					header_list.append(header)
					melody_list.append(melody)

		print "number of melody:", len(melody_list)
		return melody_list, header_list	

	def makeList(self, stream):
		"""
		voice는 note의 스트림임
		"""
		header_size = 3 #header가 3개가 아닐수도 
		stream_to_list = []

		for each_item in stream[header_size : ]:
			if isinstance(each_item, note.Note):
				stream_to_list.append(each_item.name + str(each_item.octave) + '/' + str(each_item.duration.quarterLength))
			elif isinstance(each_item, note.Rest):
				stream_to_list.append(each_item.name + '/' + str(each_item.duration.quarterLength))

		return stream_to_list, stream[0:header_size]

	def preprocess(self, sheet):
		self.mappingData(sheet)
		x,y = self.onehotEncoding()
		return x, y, self.values;

	def mappingData(self, sheet):
		self.values = sorted(list(set(sheet)))
		self.values_indices = dict((v, i) for i, v in enumerate(self.values))
		self.indices_values = dict((i, v) for i, v in enumerate(self.values))
		
		self.sentences = []
		self.next_values = []
		for i in range(0, len(self.values) - self.maxlen, self.step):
			self.sentences.append(sheet[i : i + self.maxlen])
			self.next_values.append(sheet[i + self.maxlen])
	
	def onehotEncoding(self):
		x = np.zeros((len(self.sentences), self.maxlen, len(self.values)), dtype = np.bool)
		y = np.zeros((len(self.sentences), len(self.values)), dtype = np.bool)

		for number, sentence in enumerate(self.sentences):
			for index, value in enumerate(sentence):
				x[number, index, self.values_indices[value]] = 1
			y[number, self.values_indices[self.next_values[number]]] = 1

		return x, y

	def out_midi(self, dir, head, chords):
		"""생성된 char형태의 코드를 midi로 만들어줌"""
		streams = stream.Stream()
		for h in head:
			streams.append(h)

		for chord in chords:
			# 현재는 (음과 옥타브 / 음길이) 형태로 구분한다. 나누어 준다.
			chord = chord.split('/', 1)
			if chord[0] == "rest":
				n = note.Rest(chord[0])
				n = self.set_duration(n, chord[1])
				streams.append(n)
			else:
				n = note.Note(chord[0])
				n = self.set_duration(n, chord[1])
				streams.append(n)

		self.write_stream(dir, streams)

	def write_stream(self, dir, streams):
		"""stream을 저장한다."""
		print "write stream..."
		mf = midi.translate.streamToMidiFile(streams)
		mf.open(dir,'wb')
		mf.write()
		mf.close()

	def set_duration(self, note, duration):
		"""
		무한 소수 같은건 (1/12) 분수로 표현되어서 이에 대한 처리를 해준다. python3쓰면 상관이 없긴한데 ...
		기본 모듈 중 하나인 Fraction(from fractions import Fration) 이용
		"""
		if duration.find('/') is not -1:
			splited = duration.split('/')
			note.duration.quarterLength = Fraction(int(splited[0]), int(splited[1]))
		else:
			note.duration.quarterLength = float(duration) 
		return note

