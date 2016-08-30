# _*_ coding: utf-8 _*_
from music21 import *

def parse_midi(filename):
	"""
	http://web.mit.edu/music21/doc/usersGuide/usersGuide_17_derivations.html	
	sample.mid는 불러오면 Sore이고 이는 Part의 크기 2리스트 가됨
	2개의 Part를 스트림으로 가져와서 출력이 가능 """

	mid = converter.parse(filename)
	stream1 = mid[0].stream()
	stream2 = mid[0].stream()

	stream_to_char =''
	for i in stream1[3:]:
		stream_to_char += (i.step + ' ')

	return stream_to_char, stream1[0:3]

def out_midi(dir,head,chords):
	"""생성된 char형태의 코드를 midi로 만들어줌"""
	streams = stream.Stream()
	for h in head:
		streams.append(h)

	for chord in chords:
		if chord is not '':# 추후에 버그 수정후 없앨것
			n = note.Note(chord)
			streams.append(n)

	"""stream을 저장한다."""
	mf = midi.translate.streamToMidiFile(streams)
	mf.open(dir,'wb')
	mf.write()
	mf.close()

def check_midi(filename):
	midi = converter.parse(filename)