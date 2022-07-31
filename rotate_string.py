# class Rotate:

#     def rotate_string(self, target, goal):
#         if len(target) == len(goal):

#             for i in target:
#                 target = target.replace(i, "", 1)
#                 target = target + i
#                 if target == goal:
#                     return True
#             return False
#         print("ayee")


# resp = Rotate()
# target = "abcde"
# goal = "bcdea"
# result = resp.rotate_string(target, goal)
# print(result)


class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        result = s + s
        if len(s) == len(goal):
            if len(goal) and goal in result:
                return True
            return False

# class Solution(object):
#     def rotateString(self, A, B):
#         return len(A) == len(B) and B in A+A


resp = Solution()
s = "abcde"
goal = "bcdef"
result = resp.rotateString(s, goal)
print(result)
