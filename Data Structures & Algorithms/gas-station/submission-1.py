class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        l,r,gasInTank=0,0,0
        n=len(gas)
        if sum(cost)>sum(gas):
            return -1
        while r-l<n:
            gasInTank+=gas[r%n]
            gasInTank-=cost[r%n]
            #print(f"{gasInTank=}")
            if gasInTank<0:
                l=r+1
                r=l
                gasInTank=0
            else:
                r+=1
            #print(f"{l=}{r=}")

        return l%n