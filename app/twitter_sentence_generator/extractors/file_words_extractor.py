import re

WORDS_REGULAR_EXPRESSION = r"[\w']+|[.,!?;]"


class FileWordsExtractor():
    def __init__(self, file_name):
        self.file_name = file_name
        self._file_contents = None

    @property
    def file_contents(self):
        self._file_contents = self._file_contents if self._file_contents is not None else self._read_file()
        return self._file_contents

    @property
    def words(self):
        return re.findall(WORDS_REGULAR_EXPRESSION, self.file_contents)

    def wordlist(self, filename):
        wordlist = [self.fixCaps(w) for w in re.findall(r"[\w']+|[.,!?;]", self.file_contents)]
        return wordlist

    def fixCaps(self, w):
        return ''

    def _read_file(self):
        with open(self.file_name, 'r') as file:
            file_contents = file.read()
        self._file_contents = file_contents
