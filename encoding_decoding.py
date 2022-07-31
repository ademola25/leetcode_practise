# Description
# Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

# Please implement encode and decode

# Contact me on wechat to get Amazon、Google requent Interview questions . (wechat id : jiuzhang0607)


# Example
# Example1

# Input: ["lint","code","love","you"]
# Output: ["lint","code","love","you"]
# Explanation:
# One possible encode method is: "lint:;code:;love:;you"


strs = ["lint","code","love","you"]
res = ''
for i in strs:
    res+= ''.join((str(len(i)),'#', i, ))
   
    print(res)

str = "4#lint4#code4#love3#you"
res, i = [], 0
while i < len(str):
    j = i
    while str[j] != "#":
        j+=1
    length = int(str[i:j])
    res.append(str[j + 1 : j + 1 + length])
    i = j + 1 + length
    print(res)
# count = 0
# strs = ["lint","code","love","you"]
# res = ''
# for s in strs:
#     res += str(len(s)) + '#' + s
#     print(res)

# def encod(strs):
#     res = ''
#     for i in strs:
#         res+= ''.join((str(len(i)),'#', i, ))
#     return res



# strs = ["lint","code","love","you"]
# encod(strs)