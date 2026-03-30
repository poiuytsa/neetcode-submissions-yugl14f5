class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)-1):
            needed=target-numbers[i]
            for j in range(len(numbers)):
                if needed==numbers[j]:
                    return [i+1,j+1]