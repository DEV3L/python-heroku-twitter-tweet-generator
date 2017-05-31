def test_mapping_builder():
    from twitter_sentence_generator.builders.mapping_builder import MappingBuilder

    mapping_builder = MappingBuilder()

    assert {} == mapping_builder.mapping
    assert {} == mapping_builder.temp_mapping
    assert [] == mapping_builder.starts


def test_add_item_to_temp_mapping():
    from twitter_sentence_generator.builders.mapping_builder import MappingBuilder
    expected_value = {('eat',): {'tacos': 1.0}, ('I', 'eat'): {'tacos': 1.0}}

    mapping_builder = MappingBuilder()
    mapping_builder.add_item_to_temp_mapping(["I", "eat"], 'tacos')

    assert expected_value == mapping_builder.temp_mapping

    expected_value = {('eat',): {'tacos': 1.0}, ('teach',): {'tacos': 1.0}, ('I', 'teach'): {'tacos': 1.0},
                      ('I', 'eat'): {'tacos': 1.0}}
    mapping_builder.add_item_to_temp_mapping(["I", "teach"], 'tacos')

    assert expected_value == mapping_builder.temp_mapping

    expected_value = {('eat',): {'tacos': 2.0}, ('teach',): {'tacos': 1.0}, ('I', 'teach'): {'tacos': 1.0},
                      ('I', 'eat'): {'tacos': 1.0}}
    mapping_builder.add_item_to_temp_mapping(["eat"], 'tacos')

    assert expected_value == mapping_builder.temp_mapping
