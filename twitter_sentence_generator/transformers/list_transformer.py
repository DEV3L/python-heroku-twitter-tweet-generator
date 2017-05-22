class ListTransformer():
    def __init__(self, _list):
        self._list = _list

    @property
    def tuple(self):
        return tuple(self._list)
