

class Solution:
    def contain_duplicate(self, nums):
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False


nums = [2, 3, 4, 5, 6, 7]
news = Solution()
hodl = news.contain_duplicate(nums)
print(hodl)
