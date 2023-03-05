from alive_progress import alive_bar

from app.ankicards import AnkiCards, AnkiCard
from app.dictionaryapi_webclient import DictionaryApi
from app.diff import Diff
from app.translator import Translator
from app.utils import Utils
from app.vocab import Vocab


def main():
    arguments = Utils.parse_arguments()
    vocab_db = Vocab(arguments.input)
    words_with_usage = vocab_db.read_all()
    cards = AnkiCards()
    deepl_translator = Translator(arguments.deepl_api_key)
    cards_diff = Diff.from_file(arguments.diff)
    with alive_bar(len(words_with_usage)) as bar:
        for word_with_usage in words_with_usage:
            if cards_diff.is_absent(word_with_usage.id):
                definition = DictionaryApi.get(word_with_usage.word)
                translation = deepl_translator.translate(word_with_usage.word, word_with_usage.usage)
                card = AnkiCard(
                    id=word_with_usage.id,
                    original_word=word_with_usage.word.lower(),
                    original_usage=word_with_usage.usage_with_bold_word(),
                    phonetic=definition.phonetic if definition else None,
                    audio=definition.audio if definition else None,
                    translated_word=translation.word.lower(),
                    translated_usage=translation.text,
                )
                cards.add(card)
            bar()
    cards.save_as_csv(arguments.output)
    cards_diff.update_file_with_new_cards(cards)
