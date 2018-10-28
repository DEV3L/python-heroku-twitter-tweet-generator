import os
import random
import re

from ordered_set import OrderedSet


class FileScrubber:
    min_string_token_count = 3

    def __init__(self, file_name):
        self.file_name = file_name

    def scrub_file(self):
        # remove duplicate lines
        unique_lines_set = OrderedSet()
        with open(self.file_name, 'r') as file_handler:
            for line in file_handler:
                unique_lines_set.append(line)

        scrubbed_lines_set = OrderedSet()
        for line in unique_lines_set:
            scrubbed_line = re.sub('\[.*?\]', '', line).strip(' ')
            scrubbed_line = re.sub('\{.*?\}', '', scrubbed_line)
            scrubbed_line = re.sub('\(.*?\)', '', scrubbed_line)
            scrubbed_line = re.sub(':', '', scrubbed_line)
            scrubbed_line = re.sub(';', '', scrubbed_line)
            scrubbed_line = scrubbed_line.strip()
            scrubbed_line = scrubbed_line.rstrip(',')
            scrubbed_line = scrubbed_line.rstrip('.')

            if not scrubbed_line:
                continue

            scrubbed_lines_set.add(scrubbed_line)

        merged_lines = []
        line_modulo_count, line_count, merged_line = self.reset_modulo_count_line()

        for line in scrubbed_lines_set:
            _line = line
            if merged_line and _line[0] != 'I' and _line[1] != ' ':
                _line = _line[0].lower() + _line[1:]

            merged_line += _line

            if len(line.split()) < self.min_string_token_count:
                merged_line += ' '
                continue

            line_count += 1
            if line[-1:] in ".!?":
                merged_line += '\n'
            elif line_count % line_modulo_count == 0:
                merged_line += '.\n'
            else:
                merged_line += ' '
                continue
            merged_lines.append(merged_line)
            line_modulo_count, line_count, merged_line = self.reset_modulo_count_line()

        if merged_line:
            merged_lines.append(merged_line)

        with open(scrub_file, 'w') as file_handler:
            for line in merged_lines:
                file_handler.write(line)

    @staticmethod
    def reset_modulo_count_line():
        return random.randint(1, 2), 0, ''


# convert to utf-8 character set
# iconv -f utf-8 -t ascii//TRANSLIT <file>
source_file = os.environ.get('SOURCE_FILE', './resources/twentyonepilots.txt')
scrub_file = os.environ.get('SCRUBBED_FILE', './resources/twentyonepilots_scrubbed.txt')

if __name__ == "__main__":
    file_scrubber = FileScrubber(source_file)
    file_scrubber.scrub_file()
