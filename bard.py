from generator import Generator
from preprocessor import MidiTool

if __name__ == "__main__":
	midi_util = MidiTool()

	sheet, header = midi_util.parseMidi("twice_cheerup.mid")#("twice_cheerup.mid")

	x, y, value_length = midi_util.preprocess(sheet)#(sheet)

	generator = Generator(midi_util.maxlen, value_length)

	generator.train_generation_iterate(x, y, header, sheet, 1)