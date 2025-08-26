from typing import List

# Solution 1 - Double Loop(O(n^2))
class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)): # i+1 起始是因為要避免重複計算相同的組合
                if nums[i]+nums[j] == target:
                    return[i,j]

# Solution 2 - One Pass Hash Table(O(n))
class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        for i, num in enumerate(nums):  # enumerate 是用來取得這個 Hash Table(Dict型態) 的 key->i 和 value->num
            complement = target - num   # 計算 target 減去 value 還差多少
            if complement in num_dict:  # 查表有沒有符合的數，如果有就回傳
                return [num_dict[complement], i]
            # 如果沒有符合的數就把目前的數放進 Hash Table 裡面，再繼續下一個數
            num_dict[num] = i
        # 都沒有符合的數就回傳空陣列
        return []