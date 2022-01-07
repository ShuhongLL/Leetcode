import random

class RandomizedSet:
    # note:
    # when delete from an array
    # the runtime is O(n):
    #   1. find the element
    #   2. delete the element
    #   3. move the rest elements to fill the vacant slot in the array
    
    # hence to do remove in O(1):
    #   1. use map to find the index of the target to delete
    #   2. swap the target with the last element in the array
    #   3. delete the last index of the array
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.vals = []
        self.valToIndex = {}

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.valToIndex:
            return False
        self.vals.append(val)
        self.valToIndex[val] = len(self.vals) - 1
        return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.valToIndex:
            return False
        # swap target and the last element of the vals
        idx_to_del = self.valToIndex[val]
        last_val = self.vals[-1]
        self.vals[idx_to_del], self.vals[-1] = self.vals[-1], self.vals[idx_to_del]
        self.valToIndex[last_val] = idx_to_del
        # remove val
        del self.valToIndex[val]
        self.vals.pop()
        return True

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return random.choice(self.vals)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()