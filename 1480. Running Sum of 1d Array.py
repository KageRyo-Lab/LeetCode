class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running_sum = []
        current_sum = 0
        for i in nums:
            current_sum += i
            running_sum.append(current_sum)
        return running_sum