import sqlite3
from dataclasses import dataclass

from attr import define


@dataclass
class WordWithUsage:
    id: str
    word: str
    usage: str

    def usage_with_bold_word(self) -> str:
        return self.usage.replace(self.word, f'<b>{self.word}</b>')


@define
class Vocab:
    vacab_file: str

    def read_all(self) -> list[WordWithUsage]:
        with sqlite3.connect(self.vacab_file) as con:
            words_with_usage = []
            for word, usage, lookup_id in con.execute('SELECT w.word, l.usage, l.id FROM words w JOIN lookups l ON w.id = l.word_key'):
                words_with_usage.append(WordWithUsage(id=lookup_id, word=word, usage=usage))
            return words_with_usage
