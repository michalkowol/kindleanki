from alive_progress import alive_bar

from app.ankicards import AnkiCards, AnkiCard
from app.dictionaryapi_webclient import DictionaryApi
from app.diki_webclient import DikiApi
from app.translator import Translator
from app.utils import Utils
from app.vocab import Vocab


def main():
    arguments = Utils.parse_arguments()
    vocab_db = Vocab(arguments.input)
    words_with_usage = vocab_db.read_all()
    cards = AnkiCards()
    deepl_translator = Translator.create(arguments.deepl_api_key)
    ids = AnkiCards.read_ids(output_file=arguments.output)
    with alive_bar(len(words_with_usage)) as bar:
        for word_with_usage in words_with_usage:
            if word_with_usage.id not in ids:
                definition = DictionaryApi.get(word_with_usage.word)
                audio_url = DikiApi.audio_url(word_with_usage.word.lower())
                translation = deepl_translator.translate(word_with_usage.word, word_with_usage.usage)
                card = AnkiCard(
                    id=word_with_usage.id,
                    original_word=word_with_usage.word.lower(),
                    original_usage=word_with_usage.usage_with_bold_word(),
                    phonetic=definition.phonetic if definition else None,
                    audio=audio_url if audio_url else definition.audio if definition else None,
                    translated_word=translation.word.lower(),
                    translated_usage=translation.text,
                )
                cards.add(card)
            bar()
    cards.save_as_csv(arguments.output)
