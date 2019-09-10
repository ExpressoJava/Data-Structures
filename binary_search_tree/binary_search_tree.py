class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        new_node = BinarySearchTree(value)
        # If value is less than self.value
        # check if left is None
        # if so, set left to be this node
        # if not, call the left node's insert with this value

        # if value is greater than or equal self.value
        # check if right is none
        # if it is none, set right to be a node
        # if it has a node, call self.right.insert with this value
        if value < self.value:
            if not self.left:
                self.left = new_node
            else:
                self.left.insert(value)

        elif value >= self.value:
            if not self.right:
                self.right = new_node
            else:
                self.right.insert(value)

    """
    - if self.value is the target,
    - return True
    - if the target is less than self.value,
    - check if we have a left
    - if so return left.contains on the target
    - if not return False
    - otherwise the target must be greater than self.value
    - check if we have a right
    - if so, return self.right.contains on the target
    - if not, return False
    """

    def contains(self, target):
        if target == self.value:
            return True
        elif target < self.value:
            if self.left == None:
                return False
            return self.left.contains(target)
        elif target > self.value:
            if self.right == None:
                return False
            return self.right.contains(target)
    """
    - if we have a right
    - return right's get max
    - otherwise return self.value
    """

    def get_max(self):
        target = self
        max_value = None
        while target:
            max_value = target.value
            target = target.right
        return max_value

    # call the callback on the self's value
    def for_each(self, cb):
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)


bst = BinarySearchTree(25)

bst.insert(3)
bst.insert(11)
bst.insert(50)
bst.insert(23)
bst.insert(7)
bst.insert(21)

print(bst.contains(11))
print(bst.contains(23))
