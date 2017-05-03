# _*_ coding: utf-8 _*_
from core import new_bard
from core import preprocessor

input_file_dir = "/Users/changmin/Desktop/temp/"
output_file_dir  = "/User/changmin/Desktop/"
# bard = new_bard.Bard()
# s1 , s2 = bard.multi_preprocess(input_file_dir)
# bard.multi_train(s1[1:], s2[1:])
# bard.multi_generate()
multibard = new_bard.Bard()
sheets, headers = multibard.parse_midi(input_file_dir, output_file_dir)
x_list, y_list = multibard.multi_preprocess(sheets)
multibard.init_generator()
multibard.multi_train_iterate(sheets, x_list, y_list, 10)

#multibard.save_weights(output_file_dir + 'weights.hdf5')
#multibard.save_tables(output_file_dir + 'tables.table')
