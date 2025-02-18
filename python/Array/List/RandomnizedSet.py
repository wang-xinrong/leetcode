import random

class RandomizedSet:

    def __init__(self):
        self.list, self.dict = [], {}
        
    def insert(self, val: int) -> bool:
        if val in self.dict:
            return False
        else:
            self.list.append(val)
            self.dict[val] = len(self.list) - 1
            return True

    def remove(self, val: int) -> bool:
        if val in self.dict:
            index = self.dict.pop(val)
            value = self.list.pop()
            if index != len(self.list):
                self.list[index] = value
                self.dict[value] = index
            return True
        else:
            return False
        
    def getRandom(self) -> int:
        return random.choice(self.list)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()