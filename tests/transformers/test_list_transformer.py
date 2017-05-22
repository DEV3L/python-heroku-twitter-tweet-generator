def test_list_transformer():
    from twitter_sentence_generator.transformers.list_transformer import ListTransformer

    list_transformer = ListTransformer(['test'])
    assert ('test',) == list_transformer.tuple

    list_transformer = ListTransformer(['test', 'test'])
    assert ('test', 'test') == list_transformer.tuple
