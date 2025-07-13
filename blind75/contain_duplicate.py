# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.


# Example 1:

# Input: nums = [1,2,3,1]
# Output: true
# Example 2:

# Input: nums = [1,2,3,4]
# Output: false
# Example 3:

# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true
from typing import List


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for i in nums:
            if i in hashset:
                return True
            hashset.add(i)
        return False

nums = [1, 2, 3, 1]
news = Solution()
hodl = news.hasDuplicate(nums)
print(hodl)


s = "racecar"
t = "carrace"
countS, countT = {}, {}
for n in range(len(s)):
    countS[s[n]] = 1 + countS.get(s[n], 1)
    countT[t[n]] = 1 + countT.get(t[n], 0)
    print(countS)
    print("-------")
    print(countT)