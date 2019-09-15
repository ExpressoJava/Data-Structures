class Heap:
    def __init__(self):
        self.storage = []
        self.comparator = comparator

    def insert(self, value):
        self.storage.append(value)
        value_index = len(self.storage) - 1
        self._bubble_up(value_ndex)

    # store what's at the front
    # put the smallest value at the front then remove it from our storage
    # call sift down
    # return value
    def delete(self):
        pass

    def get_max(self):
        return self.storage[0]

    def get_size(self):
        pass

    # while index > 0
    # get the parent (index - 1 ) // 2
    # if child is greater than parent ---> comparator(child, parent)
    # swap them
    # if not then we're still inside the while, but we have nothing to do
    # break
    def _bubble_up(self, index):
        pass

    # while index < max index
    # look at both children, choose the biggest
    # left child: 2 * index, + 1
    # right child: 2 * index, + 2
    # swap with that child, if the chosen one is larger, update the index to the new location
    # otherwise break out of loop
    def _sift_down(self, index):
        pass
