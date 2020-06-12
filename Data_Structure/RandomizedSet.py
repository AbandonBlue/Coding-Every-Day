import random

# Version 1
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = {}    # use dict(hash table concept) to implement

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        time: O(1)
        """
        if val not in self.data:
            self.data[val] = 1
            return True
        else:
            return False
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        time: O(1)
        """
        if val not in self.data:
            return False
        else:
            del self.data[val]
            return True
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        time: O(1)
        """
        return random.choice(list(self.data.keys()))   # without list will fail



# Verson 2
class RandomizedSet2:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = {}
        self.rdata = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.data:
            self.data[val] = 1
            self.rdata.append(val)
            return True
        else:
            return False
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.data:
            return False
        else:
            del self.data[val]
            self.rdata.remove(val)
            return True
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.rdata)   