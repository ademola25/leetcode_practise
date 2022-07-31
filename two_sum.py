class Solution:
    def twoSum(self, nums, target):
        prev_map = {}  # val : index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prev_map:
                return [prev_map[diff], i]
            prev_map[n] = i
        return


nums = [2, 7, 11, 15]
target = 9
res = Solution()
result = res.twoSum(nums, target)
print(result)
