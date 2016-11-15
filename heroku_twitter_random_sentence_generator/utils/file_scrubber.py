import random
import re

from ordered_set import OrderedSet


class FileScrubber():
    min_string_token_count = 2

    def __init__(self, file_name):
        self.file_name = file_name

    def scrub_file(self):
        lines_set = OrderedSet()
        with open(self.file_name, 'r') as file_handler:
            for line in file_handler:
                scrubbed_line = re.sub('\[.*?\]', '', re.sub('\{.*?\}', '', line)).strip(' ')
                scrubbed_line = re.sub(':', '', scrubbed_line)
                scrubbed_line = re.sub(';', '', scrubbed_line)
                scrubbed_line = scrubbed_line.strip()
                scrubbed_line = scrubbed_line.rstrip(',')

                if not scrubbed_line or len(scrubbed_line.split()) < self.min_string_token_count:
                    continue

                lines_set.add(scrubbed_line)

        merged_lines = []
        line_modulo_count, line_count, merged_line = self.reset_modulo_count_line()

        for line in lines_set:
            _line = line
            if merged_line and _line[0] != 'I':
                _line = _line[0].lower() + _line[1:]

            merged_line += _line

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

        if not merged_line:
            merged_lines.append(merged_line)

        with open('../../resources/scrubbed_file.txt', 'w') as file_handler:
            for line in merged_lines:
                file_handler.write(line)

    @staticmethod
    def reset_modulo_count_line():
        return random.randint(1, 3), 0, ''

if __name__ == "__main__":
    # iconv -f utf-8 -t ascii//TRANSLIT <file>
    file_scrubber = FileScrubber('../../resources/taylorswift.txt')
    file_scrubber.scrub_file()
