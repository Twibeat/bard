#_*_ coding: utf-8 _*_
from core.preprocessor import MidiTool
from core.generator import Generator
from music21 import converter, note, stream, midi
import glob
import os
import numpy as np
import pickle

class Bard():
    def __init__(self, max_length=16, step=1):
        self.max_length = max_length
        self.step = step
        self.midi_tool = MidiTool(self.step, self.max_length)

    def preprocess(self, input_file_dir):

        self.sheet, self.header = self.midi_tool.parse_midi(input_file_dir)
        x, y, table = self.midi_tool.preprocess(self.sheet)
        self.generator = Generator(self.max_length, table)
        return x, y

    def train(self, x, y):
        self.generator.train(x, y)

    def generate(self, output_file_dir, filename):
        values = self.generator.generateValue(self.sheet)#원래는 임의로 입력을 주어야함
        output_file_name = output_file_dir + filename + '.mid'
        self.midi_tool.out_midi(output_file_name, self.header, values)

    def save_weights(self, filename="./weight.hdf5"):
        self.generator.saveWeights(filename)

    def load_weights(self, filename="/weight.hdf5"):
        self.generator.loadWeights(filename)

    '''
    to DO
    multi bard내용 이쪽으로 그리고 bard를 이용해서구현
    
    '''

    def parse_midi(self, input_file_dir, output_file_dir):
        self.input_file_dir = input_file_dir
        self.output_file_dir = output_file_dir
        sheets = []
        headers = []

        # 폴더에 있는 midi파일들의 이름을 가져와서 각각 parsing

        try:
            if not os.path.exists(self.input_file_dir):
                raise IOError
            midifile_list = glob.glob(self.input_file_dir + "*.mid")
            midifile_list = midifile_list + glob.glob(self.input_file_dir + "*.midi")
            print(midifile_list)
            # 파일이 없으면 종료 하는 루틴이 필요 할 듯
            for midifile in midifile_list:
                sheet, header = self.midi_tool.parse_midi(midifile)
                sheets.append(sheet)
                headers.append(header)
            return sheets, headers
        except IOError:
            """
            확인이 필요
            """
            print("dir " + self.input_file_dir + " is nothing")
            exit()
            return [], []
            # 없으면 종료
            # raise IOError


    def make_tables(self, sheets):
        """
        안으로 넣을수는 없을까?
        """
        tables = []
        for sheet in sheets:
            table = list(set(sheet))
            tables += table

        self.tables = sorted(list(set(tables)))
        self.tables_indices = dict((t, i) for i, t in enumerate(self.tables))
        self.indices_tables = dict((i, t) for i, t in enumerate(self.tables))


    def mapping_data(self, sheet):
        """
        학습할 x(sentences) y(next_values)를 정한다.
        이걸 뽑아 내다니 ㅠㅠ
        """
        values = sorted(list(set(sheet)))
        self.sentences = []
        self.next_values = []
        for i in range(0, len(values) - self.max_length, self.step):
            self.sentences.append(sheet[i: i + self.max_length])
            self.next_values.append(sheet[i + self.max_length])

        # 테이블이 작아서 len(self.indices_tables)로 함
        x = np.zeros((len(self.sentences), self.max_length, len(self.tables)), dtype=np.bool)
        y = np.zeros((len(self.sentences), len(self.tables)), dtype=np.bool)

        for number, sentence in enumerate(self.sentences):

            for index, value in enumerate(sentence):
                x[number, index, self.tables_indices[value]] = 1
            y[number, self.tables_indices[self.next_values[number]]] = 1

        return x, y


    def multi_preprocess(self, sheets):
        x_list = []
        y_list = []

        self.make_tables(sheets)

        for sheet in sheets:
            x, y = self.mapping_data(sheet)
            x_list.append(x)
            y_list.append(y)

        return x_list, y_list


    def init_generator(self):
        self.generator = Generator(self.max_length, self.tables)


    def multi_train(self, x, y):
        self.generator.train(x, y)

    def generate_midi(self, header, sheet, output_file_name="output.mid"):
        output_values = self.generator.generateValue(sheet)
        self.midi_tool.out_midi(output_file_name, header, output_values)


    def multi_train_iterate(self, sheets, x_list, y_list, max_iteration=10):
        """
        왜 안되지 ... 일단 밖으로 뺌
        """
        for iteration in range(1, max_iteration + 1):
            print("Iteration", iteration)
            for index in range(len(sheets)):
                print("train", index)
                self.multi_train(x_list[index], y_list[index])


    def save_tables(self, filename="table.txt"):
        with open(filename, 'wb') as save_data:
            pickle.dump(self.tables, save_data)


    def load_tables(self, filename="table.txt"):
        with open(filename, 'rb') as load_data:
            self.tables = pickle.load(load_data)
