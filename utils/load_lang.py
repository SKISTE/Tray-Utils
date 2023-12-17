import os
from utils.exceptions import *

class Language():
    def __init__(self, lang) -> None:

        self.lang = lang
        self.lang_dict = self.load_from_txt()

    def load_from_txt(self):
        try:
            with open(f'utils/langs/{self.lang}.txt', 'r', encoding='utf-8') as lang_file:
                text = lang_file.read()
                text = text.split('\n')
                lang_dict = {}
                for x in text:
                    key = x.split('=')[0]
                    value = x.split('=')[1]
                    if key != '' or value != '':
                        lang_dict.update({key:value})
                return lang_dict
        except FileNotFoundError:
            raise LanguageNotFinded(self.lang)
        pass