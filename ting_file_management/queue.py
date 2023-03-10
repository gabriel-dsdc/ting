from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def enqueue(self, value):
        self._data.append(value)
        return self._data[-1]

    def dequeue(self):
        return self._data.pop(0)

    def search(self, index):
        if index < 0 or index >= self.__len__():
            raise IndexError
        return self._data[index]
