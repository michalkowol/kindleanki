from dataclasses import dataclass
from typing import Optional, List

import requests
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class PhoneticDto:
    audio: str


@dataclass_json
@dataclass
class DefinitionDto:
    word: str
    phonetic: Optional[str]
    phonetics: List[PhoneticDto]


@dataclass
class Definition:
    word: str
    phonetic: Optional[str]
    audio: Optional[str]


class DictionaryApi:

    @staticmethod
    def get(word: str) -> Optional[Definition]:
        response = requests.get(url=f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}')
        if response.status_code == 200:
            definition_dto = DefinitionDto.from_dict(response.json()[0], infer_missing=True)
            audio = definition_dto.phonetics[0].audio if definition_dto.phonetics else None
            return Definition(word=definition_dto.word, phonetic=definition_dto.phonetic, audio=audio)
        else:
            return None
