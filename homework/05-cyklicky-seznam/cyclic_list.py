class CyclicList:
    def __init__(self, data):
        if not len(data):
            raise Exception("The CyclicList must have at least 1 element.")
        self._data = data

    def __len__(self):
        return len(self._data)

    def __repr__(self):
        return str([i for i in range(len(self._data))])

    def __iter__(self):
        for i in range(len(self._data)):
            yield i

    def __getitem__(self, key):
        if isinstance(key, slice):
            result = []
            for i in self._data[
                   (None if key.start is None else key.start % len(self._data)):
                   (None if key.stop is None else key.stop % len(self._data)):
                   (None if key.step is None else key.step)
                   ]:
                result.append(i)
            return result
        elif isinstance(key, int):
            return self._data[key % len(self._data)]
        else:
            raise Exception("Invalid argument type.")
