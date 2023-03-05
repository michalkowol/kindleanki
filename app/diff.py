import os
from dataclasses import dataclass
from typing import Set, Optional

from app import AnkiCards


@dataclass
class Diff:
    diff_file: Optional[str]
    ids: Set[str]

    @staticmethod
    def from_file(diff_file: Optional[str]):
        ids = Diff._get_already_processed_ids(diff_file)
        return Diff(diff_file=diff_file, ids=ids)

    def is_absent(self, id: str) -> bool:
        return id not in self.ids

    @staticmethod
    def _get_already_processed_ids(diff_file: Optional[str]) -> Set[str]:
        if diff_file and os.path.exists(diff_file):
            with open(diff_file, 'r') as f:
                return set([line.strip() for line in f.readlines()])
        else:
            return set()

    def update_file_with_new_cards(self, deck: AnkiCards):
        new_ids = set(self.ids)
        new_ids.update([card.id for card in deck.cards])
        with open(self.diff_file, 'w') as f:
            for id in new_ids:
                f.write(id + '\n')
