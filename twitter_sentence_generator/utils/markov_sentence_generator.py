# https://github.com/hrs/markov-sentence-generator
# !/usr/bin/python

import random
import sys

from twitter_sentence_generator.builders.mapping_builder import MappingBuilder
from twitter_sentence_generator.extractors.file_words_extractor import FileWordsExtractor
from twitter_sentence_generator.transformers.list_transformer import ListTransformer

# These mappings can get fairly large -- they're stored globally to
# save copying time.

# (tuple of words) -> {dict: word -> number of times the word appears following the tuple}
# Example entry:
#    ('eyes', 'turned') => {'to': 2.0, 'from': 1.0}
# Used briefly while first constructing the normalized mapping
tempMapping = {}

# (tuple of words) -> {dict: word -> *normalized* number of times the word appears following the tuple}
# Example entry:
#    ('eyes', 'turned') => {'to': 0.66666666, 'from': 0.33333333}
mapping = {}

# Contains the set of words that can start sentences
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
        tempMapping = MappingBuilder(mapping=mapping, temp_mapping=tempMapping, starts=starts).add_item_to_temp_mapping(
            history, follow)
    # Normalize the values in tempMapping, put them into mapping
    for first, followset in tempMapping.items():
        total = sum(followset.values())
        # Normalizing here:
        mapping[first] = dict([(k, v / total) for k, v in followset.items()])


# Returns the next word in the sentence (chosen randomly),
# given the previous ones.
def next(prevList):
    sum = 0.0
    retval = ""
    index = random.random()
    # Shorten prevList until it's in mapping
    while ListTransformer(prevList).tuple not in mapping:
        prevList.pop(0)
    # Get a random word from the mapping, given prevList
    for k, v in mapping[ListTransformer(prevList).tuple].items():
        sum += v
        if sum >= index and retval == "":
            retval = k
    return retval


def genSentence(markovLength):
    # Start with a random "starting word"
    curr = random.choice(starts)
    sent = curr.capitalize()
    prevList = [curr]

    ## Keep adding words until we hit a period
    # while (curr not in ".\n"):

    # Keep adding words until we hit a punctuation mark
    while (curr not in ".!?"):
        curr = next(prevList)
        prevList.append(curr)
        # if the prevList has gotten too long, trim it
        if len(prevList) > markovLength:
            prevList.pop(0)
        if (curr not in ".,!?;"):
            sent += " "  # Add spaces between words (but not punctuation)
        sent += curr
    return sent


def main():
    if len(sys.argv) < 2:
        sys.stderr.write('Usage: ' + sys.argv[0] + ' text_source [chain_length=1]\n')
        sys.exit(1)

    filename = sys.argv[1]
    markovLength = 1
    if len(sys.argv) == 3:
        markovLength = int(sys.argv[2])

    file_words_extractor = FileWordsExtractor(filename)
    words = file_words_extractor.extract_words()

    buildMapping(words, markovLength)

    print(genSentence(markovLength))


if __name__ == "__main__":
    main()
