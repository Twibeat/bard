'''
from core.bard import Bard

if __name__ == "__main__":
	bard = Bard("./input_files/twice_like_ooh_ahh.midi", "./output_files/")
	sheet, header, x, y, input_set = bard.preprocess()
	bard.generate(sheet, header, x, y, input_set, 10)
'''
'''
from core.multiBard import MultiBard 
if __name__ == "__main__":
	input_file_dir = "./input_files/"
	output_file_dir = "./output_files/"

	bard = MultiBard()
	sheets, headers = bard.parse_midi(input_file_dir, output_file_dir)
	x_list, y_list= bard.preprocess(sheets)
	
	bard.init_generator(bard.tables)
	
	bard.multi_train_iterate(sheets, x_list, y_list, 10)
'''
