import random

class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.keys = []
        self.dict = {}

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.dict:
            return False
        self.keys.append(val)
        self.dict[val] = len(self.keys) - 1
        return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.dict:
            return False
        idx_to_del = self.dict[val]
        last_idx, last_val = len(self.keys) - 1, self.keys[-1]
        # assign the slot to be deleted with value of the last element
        self.keys[idx_to_del] = last_val
        self.dict[last_val] = idx_to_del
        # delete val from dict and the last element of the list
        del self.dict[val]
        self.keys.pop()
        return True

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return random.choice(self.keys)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()