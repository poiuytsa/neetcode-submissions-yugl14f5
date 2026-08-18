from collections import defaultdict 
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        events=defaultdict(int)
        for p,f,t in trips:
            events[f]+=p
            events[t]-=p

        #cant do dicts.sort(), only sorted(dicts) - returns keys sorted as a lis 
        curr_load=0
        for k in sorted(events):
            curr_load+=events[k]
            if curr_load>capacity:
                return False
        
        return True