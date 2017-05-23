from twitter_sentence_generator.transformers.list_transformer import ListTransformer


class MappingBuilder():
    def __init__(self):
        self.mapping = {}
        self.temp_mapping = {}
        self.starts = []

    # Self-explanatory -- adds "word" to the "tempMapping" dict under "history".
    # tempMapping (and mapping) both match each word to a list of possible next
    # words.
    # Given history = ["the", "rain", "in"] and word = "Spain", we add "Spain" to
    # the entries for ["the", "rain", "in"], ["rain", "in"], and ["in"].
    def add_item_to_temp_mapping(self, history, word):
        while len(history) > 0:
            first = ListTransformer(history).tuple
            if first in self.temp_mapping:
                if word in self.temp_mapping[first]:
                    self.temp_mapping[first][word] += 1.0
                else:
                    self.temp_mapping[first][word] = 1.0
            else:
                self.temp_mapping[first] = {}
                self.temp_mapping[first][word] = 1.0
            history = history[1:]


mapping = {}
tempMapping = {}

starts = []


# Building and normalizing the mapping.
def buildMapping(wordlist, markovLength):
    global tempMapping
    starts.append(wordlist[0])
    for i in range(1, len(wordlist) - 1):
        if i <= markovLength:
            history = wordlist[: i + 1]
        else:
            history = wordlist[i - markovLength + 1: i + 1]
        follow = wordlist[i + 1]
        # if the last elt was a period, add the next word to the start list
        if history[-1] == "." and follow not in ".,!?;":
            starts.append(follow)
        addItemToTempMapping(history, follow)
    # Normalize the values in tempMapping, put them into mapping
    for first, followset in tempMapping.items():
        total = sum(followset.values())
        # Normalizing here:
        mapping[first] = dict([(k, v / total) for k, v in followset.items()])


# Self-explanatory -- adds "word" to the "tempMapping" dict under "history".
# tempMapping (and mapping) both match each word to a list of possible next
# words.
# Given history = ["the", "rain", "in"] and word = "Spain", we add "Spain" to
# the entries for ["the", "rain", "in"], ["rain", "in"], and ["in"].
def addItemToTempMapping(history, word):
    global tempMapping
    while len(history) > 0:
        first = toHashKey(history)
        if first in tempMapping:
            if word in tempMapping[first]:
                tempMapping[first][word] += 1.0
            else:
                tempMapping[first][word] = 1.0
        else:
            tempMapping[first] = {}
            tempMapping[first][word] = 1.0
        history = history[1:]
