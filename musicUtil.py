# _*_ coding: utf-8 _*_
from music21 import *
from fractions import Fraction

def parse_midi(filename):
	"""
	http://web.mit.edu/music21/doc/usersGuide/usersGuide_17_derivations.html	
	sample.mid는 불러오면 Sore이고 여러개의 Part로 구성된다. Part는 
	midi파일에서 최초의 Voice를 찾는다.
	"""
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

	return stream_to_list, stream[0:header_size]

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

	"""stream을 저장한다."""
	mf = midi.translate.streamToMidiFile(streams)
	mf.open(dir,'wb')
	mf.write()
	mf.close()

def set_duration(note, duration):
	"""
	무한 소수 같은건 (1/12) 분수로 표현되어서 이에 대한 처리를 해준다.
	기본 모듈 중 하나인 Fraction(from fractions import Fration) 이용
	"""
	if duration.find('/') is not -1:
		splited = duration.split('/')
		note.duration.quarterLength = Fraction(int(splited[0]), int(splited[1]))
	else:
		note.duration.quarterLength = float(duration) 
	return note
	