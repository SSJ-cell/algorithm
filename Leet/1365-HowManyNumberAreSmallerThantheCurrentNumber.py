#https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        result = []
        for i in range(len(nums)) :
            count = 0
            for j in range(len(nums)) :
                if nums[i] > nums[j] :
                    count += 1
            result.append(count)
        return result