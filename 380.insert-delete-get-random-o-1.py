import random

class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.values = []
        self.val_index = {}

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.val_index:
            return False
        self.values.append(val)
        self.val_index[val] = len(self.values) - 1
        return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.val_index:
            return False
        idx_to_del = self.val_index[val]
        last_idx, last_val = len(self.values) - 1, self.values[-1]
        # assign the slot to be deleted with value of the last element
        self.values[idx_to_del] = last_val
        self.val_index[last_val] = idx_to_del
        # delete val from dict and the last element of the list
        del self.val_index[val]
        self.values.pop()
        return True

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return random.choice(self.values)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()