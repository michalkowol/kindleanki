import csv
import os
from dataclasses import dataclass
from typing import List, Optional, Set


@dataclass
class AnkiCard:
    id: str
    original_word: str
    original_usage: str
    phonetic: Optional[str]
    audio: Optional[str]
    translated_word: str
    translated_usage: str

    def format(self):
        phonetic_html = f' <i style="color: #D3D3D3">{self.phonetic}</i>' if self.phonetic else ''
        audio_html = f'<br/><audio controls autoplay><source src="{self.audio}" type="audio/mpeg"></audio>' if self.audio else ''
        return {
            'front': f'<p><b>{self.original_word}</b>{phonetic_html}{audio_html}</p><p>{self.original_usage}</p>',
            'back': f'<p><b>{self.translated_word}</b></p><p>{self.translated_usage}</p>',
            'id': self.id
        }


@dataclass
class AnkiCards:
    cards: List[AnkiCard]

    def __init__(self):
        self.cards = []

    def add(self, card: AnkiCard):
        self.cards.append(card)

    def save_as_csv(self, output_file: str):
        with open(output_file, 'a') as f:
            writer = csv.DictWriter(f, fieldnames=['front', 'back', 'id'])
            for card in self.cards:
                writer.writerow(card.format())

    @staticmethod
    def read_ids(output_file: str) -> Set[str]:
        if os.path.exists(output_file):
            with open(output_file, 'r') as f:
                reader = csv.DictReader(f, fieldnames=['front', 'back', 'id'])
                return set([row.get('id') for row in reader])
        else:
            return set()
