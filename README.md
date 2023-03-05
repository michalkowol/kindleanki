# Kindle to Anki

Kindle to Anki exporter

## Installation

```bash
brew install poetry
```

```bash
poetry install
```

## Usage

```bash
# with diff file
poetry run app --deepl-api-key YOUR_DEEPL_API_KEY --input vocab.db --output vocab.csv --diff diff.txt
```

```bash
# process all
poetry run app --deepl-api-key YOUR_DEEPL_API_KEY --input vocab.db --output vocab.csv
```
