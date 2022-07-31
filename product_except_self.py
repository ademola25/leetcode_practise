# Array and Hash
class Solution:
    def product_except(self, arr):
        res = [1] * (len(arr))
        prefix = 1
        for i in range(len(arr)):
            res[i] = prefix
            prefix *= arr[i]
        postfix = 1
        for i in range(len(arr) - 1, -1, -1):
            res[i] *= postfix
            postfix *= arr[i]
        return res


arr = [1, 2, 3, 4]
product = Solution()
result = product.product_except(arr)
print(result)


# Product of Array except Self  (Medium level)

# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.


# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
