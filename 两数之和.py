'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in nums:
            if (target - i) in nums and (target - i) == i:
                try:
                    targetSubtractI = nums.index(target-i, nums.index(i)+1, len(nums))
                    return [nums.index(i), targetSubtractI]
                except:
                    continue
            if (target - i) in nums and (target - i) != i:
                return [nums.index(i), nums.index(target-i)]

if __name__ == "__main__":
    solution = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    print(solution.twoSum(nums, target))

