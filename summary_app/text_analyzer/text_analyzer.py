from typing import AnyStr, Dict

import spacy
from spacy.tokens import Doc


class TextAnalyzer:

    def __init__(self, tokenizer="en_core_web_sm"):
        self._nlp = spacy.load(tokenizer)

    def summarization(self, text: AnyStr) -> Doc:
        summarization = self._nlp(text)

        return summarization

    def summarization_as_dict(self, text: AnyStr) -> Dict:
        return self.summarization(text).to_json()


TextAnalyzerInstance = TextAnalyzer()
