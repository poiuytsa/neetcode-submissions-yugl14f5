import random 

class RandomizedSet:
    def __init__(self):
        #index->val
        self.nums=[]
        #val->index
        self.numMap={}

    def insert(self, val: int) -> bool:
        if val in self.numMap:
            return False
        
        self.nums.append(val)
        self.numMap[val]=len(self.nums)-1               #len(nums) is O(1)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.numMap:
            return False

        i=self.numMap[val]
        last=self.nums[-1]
        #for O(1) deletion in list, swap with last element and pop()
        self.nums[i],self.nums[-1]=self.nums[-1],self.nums[i]
        self.nums.pop()
        self.numMap[last]=i
        del self.numMap[val]
        return True 

    def getRandom(self) -> int:
        return random.choice(self.nums)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()