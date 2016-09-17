from preprocessor import MidiTool

input_file = "twice_like_ooh_ahh.midi"
input_file_folder = "./input_files/"
input_file_dir = input_file_folder + input_file
input_file_name = input_file.split('.')[0]

output_file_dir = "./output_files/"

if __name__ == "__main__":

	midi_util = MidiTool()

	sheet, header = midi_util.parseMidi2(input_file_dir)
	for index in range(0,len(sheet)):
		"""print len(sheet[index])
		for h in header[index]:
			print h"""
		midi_util.out_midi(output_file_dir + input_file_name + str(index) + "_input.midi", header[index], sheet[index])