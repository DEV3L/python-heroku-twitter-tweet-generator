def test_mapping_builder():
    from twitter_sentence_generator.builders.mapping_builder import MappingBuilder

    mapping_builder = MappingBuilder()

    assert {} == mapping_builder.mapping
    assert {} == mapping_builder.temp_mapping
    assert [] == mapping_builder.starts


def test_add_item_to_temp_mapping():
    from twitter_sentence_generator.builders.mapping_builder import MappingBuilder
    expected_value = {('in',): {'Spain': 1.0}, ('rain', 'in'): {'Spain': 1.0}, ('the', 'rain', 'in'): {'Spain': 1.0}}

    mapping_builder = MappingBuilder()
    mapping_builder.add_item_to_temp_mapping(["the", "rain", "in"], 'Spain')

    assert expected_value == mapping_builder.temp_mapping

# # Self-explanatory -- adds "word" to the "tempMapping" dict under "history".
# # tempMapping (and mapping) both match each word to a list of possible next
# # words.
# # Given history = ["the", "rain", "in"] and word = "Spain", we add "Spain" to
# # the entries for ["the", "rain", "in"], ["rain", "in"], and ["in"].
# def add_item_to_temp_mapping(self, history, word):
#     while len(history) > 0:
#         first = ListTransformer(history).tuple
#         if first in self.temp_mapping:
#             if word in self.temp_mapping[first]:
#                 self.temp_mapping[first][word] += 1.0
#             else:
#                 self.temp_mapping[first][word] = 1.0
#         else:
#             self.temp_mapping[first] = {}
#             self.temp_mapping[first][word] = 1.0
#         history = history[1:]
