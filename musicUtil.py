# _*_ coding: utf-8 _*_
from music21 import *
import nester
def parse_midi(filename):
	"""
	http://web.mit.edu/music21/doc/usersGuide/usersGuide_17_derivations.html	
	sample.mid는 불러오면 Sore이고 이는 Part의 크기 2리스트 가됨
	2개의 Part를 스트림으로 가져와서 출력이 가능 
	#이나 -(플랫) 적용이 필요
	"""

	mid = converter.parse(filename)
	stream1 = mid[0].stream()
	stream2 = mid[0].stream()#다른 스트림에 대한 처리

	header_size = 3 #header가 3개가 아닐수도 
	stream_to_char =''

	for each_item in stream1[header_size:]:#
		if isinstance(each_item, note.Note):
			stream_to_char += (each_item.step + ' ')
		elif isinstance(each_item, note.Rest):
			stream_to_char += (each_item.name + ' ')
			
	return stream_to_char, stream1[0:header_size]

def out_midi(dir, head, chords):
	"""생성된 char형태의 코드를 midi로 만들어줌"""
	streams = stream.Stream()
	for h in head:
		streams.append(h)

	for chord in chords:
		if chord == "rest":
			n = note.Rest(chord)
			streams.append(n)
		elif chord is not '':# 추후에 버그 수정후 없앨것
			n = note.Note(chord)
			streams.append(n)

	"""stream을 저장한다."""
	mf = midi.translate.streamToMidiFile(streams)
	mf.open(dir,'wb')
	mf.write()
	mf.close()

def check_midi(filename):
	midi = converter.parse(filename)
	for part in midi:
		nester.print_lol(part)

if __name__ == "__main__":
	char, st = parse_midi("twice_cheerup.mid")
	#check_midi("twice_cheerup.mid")