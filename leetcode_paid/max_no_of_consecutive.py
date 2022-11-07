# Question:
# Given a binary array nums, return the maximum number of consecutive 1's in the array.

# Constraints:

# 1 <= nums.length <= 10^5
# nums[i] is either 0 or 1.

# example of expected result
# Example 1:

# Input: nums = [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.


# Solution

# The constraints for this problem make it easy
# to understand that it can be done in one iteration.

# The length of input array is a positive integer and will not exceed 10,000

# class Solution:
#     def findMaxConsecutiveOnes(self, data: list[int])-> int:
#         # declare default 0 value for max_count and count
#         count = max_count = 0

#         for num in data:
#             if num == 1:
#                 count += 1
#             else:
#                 max_count = max(max_count, count)
#                 count = 0
#         return max(max_count, count)


# Complexity Analysis

# Time Complexity: O(N), where N is the number of elements in the array.

# Space Complexity: O(1). We do not use any extra space.

 ###second answer
# import itertools
# class Solution:
#     def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
#         return max((sum(t[1]) for t in itertools.groupby(nums) if t[0]), default=0)

#third solution
class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        res, s = [], 0
        nums.append(0)
        for i in range(0,len(nums)):
            if nums[i] == 1:
                s+=1
            else:
                res.append(s)
                print(res,'haha')
                s=0
        return max(res)

nums =  [1,1,1,0,1,1,1,1]
res = Solution()

resp = res.findMaxConsecutiveOnes(nums)
print(resp)