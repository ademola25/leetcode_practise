# Question
# Given an array nums of integers, return how many of them contain an even number of digits.

 

# Example 1:

# Input: nums = [12,345,2,6,7896]
# Output: 2
# Explanation: 
# 12 contains 2 digits (even number of digits). 
# 345 contains 3 digits (odd number of digits). 
# 2 contains 1 digit (odd number of digits). 
# 6 contains 1 digit (odd number of digits). 
# 7896 contains 4 digits (even number of digits). 
# Therefore only 12 and 7896 contain an even number of digits.

# VALIDATe with below constraints
# Constraints:

# 1 <= nums.length <= 500
# 1 <= nums[i] <= 105

# Solution
# class Solution:
#     def findNumbers(self, nums: list[int]) -> int:
#         res= []
#         for num in nums:
#             # convert num to string then fint the lenght
#             ans = sum(len(str(num))) % 2 == 0
#         return ans

class Solution:
    def findNumbers(self, nums: list[int]) -> int:
            return sum(len(str(n)) % 2 == 0 for n in nums) 

nums =  [12,345,2,6,7896]
res = Solution()

resp = res.findNumbers(nums)
print(resp)


