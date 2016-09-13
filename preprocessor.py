# _*_ coding: utf-8 _*_
"""
재구성하기위함 아직 사용은 하지 않는다.
"""

from music21 import note
from fractions import Fraction
class MidiTool:
	def __init__(self, maxlen=16):
		"""
		maxlen이라는 이름은 좀 그렇다. 한번에 학습시킬 멜로디의 수를 나타내는건데...
		"""
		self.maxlen = maxlen

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
					return make_list(voice)
	def makeList(self, stream):
		"""
		voice는 note의 스트림임
		"""
		header_size = 3 #header가 3개가 아닐수도 
		stream_to_list = []

		for each_item in stream[header_size:]:
			if isinstance(each_item, note.Note):
				stream_to_list.append(each_item.name + str(each_item.octave) + '/' + str(each_item.duration.quarterLength))
			elif isinstance(each_item, note.Rest):
				stream_to_list.append(each_item.name + '/' + str(each_item.duration.quarterLength))

		return stream_to_list, stream[0:header_size]

	def preprocess(self):
		pass
	def outMidi(self):
		pass

class preprocessor(object):
	""" 
	사실 이건 데이터 전처리 하고는 약간 거리가 있네
	"""
	def __init__(self, sheet, maxlen = 16):
		
		self.mappingData(sheet)
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

	def mappingData(self, sheet):
		"""set으로 중복없애고 리스트 만들어 정렬(chord단위)
		이렇게 되면 맨뒤에 의문사나 .같은게 문제가됨 ?같은거 없애봐라 -> 코드는 상관없징
		chords는 특정 음악파일이 아닌 나중에 는 전체 코드 구성으로 바꺼야 됨 
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

def parse_midi(filename):
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
				return make_list(voice)

def make_list(stream):
	"""
	voice는 note의 스트림임
	"""
	header_size = 3 #header가 3개가 아닐수도 
	stream_to_list = []

	for each_item in stream[header_size:]:
		if isinstance(each_item, note.Note):
			stream_to_list.append(each_item.name + str(each_item.octave) + '/' + str(each_item.duration.quarterLength))
		elif isinstance(each_item, note.Rest):
			stream_to_list.append(each_item.name + '/' + str(each_item.duration.quarterLength))

	header = stream[0:header_size]
	return stream_to_list, header

def out_midi(dir, head, chords):
	"""생성된 char형태의 코드를 midi로 만들어줌"""
	streams = stream.Stream()

	for h in head:
		streams.append(h)

	for chord in chords:
		# 현재는 (음과 옥타브 / 음길이) 형태로 구분한다. 나누어 준다.
		chord = chord.split('/', 1)
		if chord[0] == "rest":
			n = note.Rest(chord[0])
			n = set_duration(n, chord[1])
			streams.append(n)
		else:
			n = note.Note(chord[0])
			n = set_duration(n, chord[1])
			streams.append(n)

	write_stream(dir, streams)

def write_stream(dir, streams):
	"""stream을 저장한다."""
	print "write stream..."
	mf = midi.translate.streamToMidiFile(streams)
	mf.open(dir,'wb')
	mf.write()
	mf.close()

def set_duration(note, duration):
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