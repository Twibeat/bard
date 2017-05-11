# _*_ coding: utf-8 _*_
from core.bard import Bard
from core import preprocessor

input_file_dir = "/Users/changmin/Desktop/temp/"
output_file_dir  = "/Users/changmin/Desktop/"
test_file = "/Users/changmin/Desktop/test.mid"
test_file2 = "/Users/changmin/Desktop/temp/twice_like_ooh_ahh.midi"
sample_file = "/Users/changmin/Desktop/temp/for_elise.midi"

bard = Bard()
melody, next = bard.preprocess(sample_file)
for iteration in range(100):
    print("iteration : ", iteration)
    bard.train(melody, next)
bard.generate(output_file_dir, "test")

print("Single file success!!")

# multibard = Bard()
# sheets, headers = multibard.parse_midi(input_file_dir, output_file_dir)
# x_list, y_list = multibard.multi_preprocess(sheets)
# multibard.init_generator()
# multibard.multi_train_iterate(sheets, x_list, y_list, 10)
#
# multibard.save_weights(output_file_dir + 'weights.hdf5')
# multibard.save_tables(output_file_dir + 'tables.table')
#
# print("Multi file success")
