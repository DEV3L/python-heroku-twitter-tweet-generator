from twitter_sentence_generator.transformers.list_transformer import ListTransformer


class MappingBuilder():
    def __init__(self, mapping=None, temp_mapping=None, starts=None):
        self.mapping = mapping or {}
        self.temp_mapping = temp_mapping or {}
        self.starts = starts or []

    def add_item_to_temp_mapping(self, history, word):
        """
        Adds "word" to the "temp_mapping" dict under "history".
        Match each word to a weighted list of possible next words.

        add_item_to_temp_mapping(["rain", "in"], "Spain")
        result : {('in',): {'Spain': 1.0}, ('rain', 'in'): {'Spain': 1.0}}

        :param history:
        :param word:
        :return:
        """
        while history:
            first = ListTransformer(history).tuple

            # this could be shortened up with a default dict
            if first in self.temp_mapping:
                if word in self.temp_mapping[first]:
                    self.temp_mapping[first][word] += 1.0
                else:
                    self.temp_mapping[first][word] = 1.0
            else:
                self.temp_mapping[first] = {}
                self.temp_mapping[first][word] = 1.0
            history = history[1:]

        return self.temp_mapping
