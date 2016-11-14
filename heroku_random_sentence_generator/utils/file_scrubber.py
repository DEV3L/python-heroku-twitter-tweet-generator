import re

from ordered_set import OrderedSet


class FileScrubber():
    min_string_token_count = 2

    def __init__(self, file_name):
        self.file_name = file_name
        self.lines_set = OrderedSet()

    def scrub_file(self):
        with open(self.file_name, 'r') as file_handler:
            for line in file_handler:
                scrubbed_line = re.sub('\[.*?\]', '', re.sub('\{.*?\}', '', line)).strip(' ')
                scrubbed_line = scrubbed_line.strip()
                scrubbed_line = scrubbed_line.rstrip(',')

                if not scrubbed_line or len(scrubbed_line.split()) < self.min_string_token_count:
                    continue

                self.lines_set.add(scrubbed_line + '\n')

        with open('../../resources/scrubbed_file.txt', 'w') as file_handler:
            for item in self.lines_set:
                file_handler.write('{}'.format(item))


if __name__ == "__main__":
    # iconv -f utf-8 -t ascii//TRANSLIT <file>
    file_scrubber = FileScrubber('../../resources/taylorswift.txt')
    file_scrubber.scrub_file()
