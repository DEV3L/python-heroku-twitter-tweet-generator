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

    def join_dicts(self):

        pass

#
# mapping = {}
# tempMapping = {}
#
# starts = []
#
#
# # Building and normalizing the mapping.
# def buildMapping(wordlist, markovLength):
#     global tempMapping
#     starts.append(wordlist[0])
#     for i in range(1, len(wordlist) - 1):
#         if i <= markovLength:
#             history = wordlist[: i + 1]
#         else:
#             history = wordlist[i - markovLength + 1: i + 1]
#         follow = wordlist[i + 1]
#         # if the last elt was a period, add the next word to the start list
#         if history[-1] == "." and follow not in ".,!?;":
#             starts.append(follow)
#         addItemToTempMapping(history, follow)
#     # Normalize the values in tempMapping, put them into mapping
#     for first, followset in tempMapping.items():
#         total = sum(followset.values())
#         # Normalizing here:
#         mapping[first] = dict([(k, v / total) for k, v in followset.items()])
