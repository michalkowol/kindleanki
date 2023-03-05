from dataclasses import dataclass

import deepl

from app.utils import Utils


@dataclass
class Translation:
    word: str
    text: str


class Translator:
    deepl_translator: deepl.Translator

    def __init__(self, api_key: str):
        self.deepl_translator = deepl.Translator(api_key)

    def translate(self, word: str, text: str) -> Translation:
        text_with_bold_word = text.replace(word, f'<b>{word}</b>')
        result = self.deepl_translator.translate_text(text=text_with_bold_word, source_lang='EN', target_lang='PL', tag_handling='html')
        translated_word = Utils.str_between(result.text, '<b>', '</b>')
        return Translation(translated_word, result.text)
