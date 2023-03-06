from typing import Optional

import requests


class DikiApi:

    @staticmethod
    def audio_url(word: str) -> Optional[str]:
        url = f'https://www.diki.pl/images-common/en/mp3/{word}.mp3'
        response = requests.head(url=url)
        return url if response.status_code == 200 else None
