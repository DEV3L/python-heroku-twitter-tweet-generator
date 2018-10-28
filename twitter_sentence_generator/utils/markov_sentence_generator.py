# https://github.com/hrs/markov-sentence-generator
# !/usr/bin/python

import random
import sys

from twitter_sentence_generator.builders.mapping_builder import MappingBuilder
from twitter_sentence_generator.extractors.file_words_extractor import FileWordsExtractor
from twitter_sentence_generator.transformers.list_transformer import ListTransformer

# These mappings can get fairly large -- they're stored globally to save copying time.

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
def build_mapping(word_list, markov_length):
    global tempMapping
    starts.append(word_list[0])

    tempMapping = MappingBuilder(mapping=mapping, temp_mapping=tempMapping, starts=starts).add_item_to_temp_mapping(
        [word_list[0]], word_list[1])

    for i in range(1, len(word_list) - 1):
        if i <= markov_length:
            history = word_list[: i + 1]
        else:
            history = word_list[i - markov_length + 1: i + 1]
        follow = word_list[i + 1]
        # if the last elt was a period, add the next word to the start list
        if history[-1] == "." and follow not in ".,!?;":
            starts.append(follow)
        tempMapping = MappingBuilder(mapping=mapping, temp_mapping=tempMapping, starts=starts).add_item_to_temp_mapping(
            history, follow)
    # Normalize the values in tempMapping, put them into mapping
    for first, follow_set in tempMapping.items():
        total = sum(follow_set.values())
        # Normalizing here:
        mapping[first] = dict([(k, v / total) for k, v in follow_set.items()])


# Returns the next word in the sentence (chosen randomly),
# given the previous ones.
def get_next_word(previous_list):
    total_sum = 0.0
    next_word = ''
    index = random.random()

    # Shorten prevList until it's in mapping
    _mapping = mapping
    hash_key = ListTransformer(previous_list).tuple

    while hash_key not in mapping:
        previous_list.pop(0)

    # Get a random word from the mapping, given prevList
    for key, value in mapping[ListTransformer(previous_list).tuple].items():
        total_sum += value
        if total_sum >= index and next_word == "":
            next_word = key

    return next_word


def build_sentence(markov_length):
    # Start with a random "starting word"
    current_word = random.choice(starts)

    sentence = current_word.capitalize()
    previous_list = [current_word]

    # Keep adding words until we hit a punctuation mark
    while current_word not in ".!?":
        current_word = get_next_word(previous_list)
        previous_list.append(current_word)

        # if the prevList has gotten too long, trim it
        if len(previous_list) > markov_length:
            previous_list.pop(0)

        if current_word not in ".,!?;":
            sentence += " "  # Add spaces between words (but not punctuation)

        sentence += current_word

    return sentence


def main():
    if len(sys.argv) < 2:
        sys.stderr.write('Usage: ' + sys.argv[0] + ' text_source [chain_length=1]\n')
        sys.exit(1)

    filename = sys.argv[1]
    markov_length = 1
    if len(sys.argv) == 3:
        markov_length = int(sys.argv[2])

    file_words_extractor = FileWordsExtractor(filename)
    words = file_words_extractor.extract_words()

    build_mapping(words, markov_length)

    print(build_sentence(markov_length))


if __name__ == "__main__":
    main()
