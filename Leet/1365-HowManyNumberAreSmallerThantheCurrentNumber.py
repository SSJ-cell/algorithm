#https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        sorted_nums = sorted(nums)
        rank = {}

        for i, num in enumerate(sorted_nums) :
            if num not in rank :
                rank[num] = i

        return [rank[num] for num in nums]