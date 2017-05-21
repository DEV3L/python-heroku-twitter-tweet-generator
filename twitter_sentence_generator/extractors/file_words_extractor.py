import re

WORDS_REGULAR_EXPRESSION = r"[\w']+|[.,!?;]"


class FileWordsExtractor():
    def __init__(self, file_name):
        self.file_name = file_name
        self._file_contents = None

    def extract_words(self):
        return [word for word in self._normalize_words()]

    @property
    def file_contents(self):
        # cache
        if self._file_contents is None:
            self._read_file()
        return self._file_contents

    @property
    def words(self):
        return re.findall(WORDS_REGULAR_EXPRESSION, self.file_contents)

    def _normalize_words(self):
        _words = []
        for word in self.words:
            if word.isupper() and word != "I":
                word = word.lower()
            elif word[0].isupper():
                word = word.lower().capitalize()
            else:
                word = word.lower()
            _words.append(word)
        return _words

    def _read_file(self):
        with open(self.file_name, 'r') as file:
            file_contents = file.read()
        self._file_contents = file_contents
