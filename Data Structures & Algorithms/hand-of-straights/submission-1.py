class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize!=0:
            return False
        freq=Counter(hand)
        hand.sort()

        for n in hand:
            if freq[n]>0:
                for i in range(n,n+groupSize):
                    if not freq[i]:
                        return False
                    freq[i]-=1        
        return True