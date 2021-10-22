import json


class Hanzi(object):
    def __init__(self):
        data_file = open("../data/data.json", 'r', encoding='utf-8')
        self.data = json.load(data_file)

    def get_full_infomation(self, input_char):
        if input_char in self.data:
            bujian, pinyin, bihua = self.data[input_char]
        else:
            bujian, pinyin, bihua = None, None, None

        return bujian, pinyin, bihua

    def get_bujian(self, input_char):
        bujian, pinyin, bihua = self.get_full_infomation(input_char)

        return bujian

    def get_pinyin(self, input_char):
        bujian, pinyin, bihua = self.get_full_infomation(input_char)

        return pinyin

    def get_bihua(self, input_char):
        bujian, pinyin, bihua = self.get_full_infomation(input_char)

        return bihua
