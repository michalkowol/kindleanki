import argparse


class Utils:

    @staticmethod
    def parse_arguments() -> argparse.Namespace:
        parser = argparse.ArgumentParser(description='Kindle to Anki exporter')
        parser.add_argument('--deepl-api-key', type=str, required=True, help='DeepL API Key')
        parser.add_argument('--input', type=str, required=True, help='input file (mostly vocab.db)')
        parser.add_argument('--output', type=str, required=True, help='output file (mostly vocab.csv)')
        parser.add_argument('--diff', type=str, required=False, help='diff file (mostly diff.txt)')
        return parser.parse_args()

    @staticmethod
    def str_between(text: str, start: str, end: str) -> str:
        start_pos = text.find(start) + len(start)
        end_pos = text.find(end)
        return text[start_pos:end_pos].strip()
