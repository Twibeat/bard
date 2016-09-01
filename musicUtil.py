# _*_ coding: utf-8 _*_
from music21 import *
import nester

def parse_midi(filename):
	"""
	http://web.mit.edu/music21/doc/usersGuide/usersGuide_17_derivations.html	
	sample.mid는 불러오면 Sore이고 이는 Part의 크기 2리스트 가됨
	Part를 스트림으로 가져와서 출력이 가능 
	옥타브가 필요
	"""
	mid = converter.parse(filename)
	stream1 = mid[0].stream()
	stream2 = mid[0].stream()#다른 스트림에 대한 처리 필요

	header_size = 3 #header가 3개가 아닐수도 
	stream_to_char =''

	"""
	Note, Rest둘다 duration이 있다. 처리 필요 
	"""
	for each_item in stream1[header_size:]:
		if isinstance(each_item, note.Note):
			stream_to_char += (each_item.name + ' ')#.name올 바꾸면 샵,플랫되는데 rest만 나온다...
			print each_item.duration.type# 길이
		elif isinstance(each_item, note.Rest):
			stream_to_char += (each_item.name + ' ')
			print each_item.duration.type# 길이
			
	return stream_to_char, stream1[0:header_size]

def out_midi(dir, head, chords):
	"""생성된 char형태의 코드를 midi로 만들어줌"""
	streams = stream.Stream()
	for h in head:
		streams.append(h)

	for chord in chords:
		if chord == "rest":
			n = note.Rest(chord)
			n.duration.type = "eighth"
			streams.append(n)
		elif chord is not '':# 추후에 버그 수정후 없앨것
			n = note.Note(chord)
			n.duration.type = "eighth"
			streams.append(n)

	"""stream을 저장한다."""
	mf = midi.translate.streamToMidiFile(streams)
	mf.open(dir,'wb')
	mf.write()
	mf.close()

def test_check_midi(filename):
	midi = converter.parse(filename)
	for part in midi:
		nester.print_lol(part)

def test_check_hierarchy(filename):
	mid = converter.parse(filename)
	streams = mid[0].stream()
	
	header_size = 3
	stream_to_char = ""

	for s in streams[header_size:10]:
		if isinstance(s, note.Note):
			print "note: ", s.fullName
		if isinstance(s, pitch.Pitch):
			print "pitch: ",s.name

if __name__ == "__main__":
	char, st = parse_midi("twice_cheerup.mid")
	#print char.split(' ')
	#test_check_midi("twice_cheerup.mid")
	#test_check_hierarchy("twice_cheerup.mid")