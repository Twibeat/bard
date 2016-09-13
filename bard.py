from generator import Generator
from preprocessor import MidiTool

if __name__ == "__main__":
	midi_util = MidiTool()

	midi_util.parseMidi("twice_cheerup.mid")#("twice_cheerup.mid")

	midi_util.preprocess()#(sheet)

	generator = Generator()

	generator.buildModel()

	generator.iterate()