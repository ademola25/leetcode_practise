# # print("Hello", end=" ")
# # print("World") # Hello World
# # print('words', 'with', 'commas', 'in', 'between', sep=', ')


# def isValid(password):
     
#     # for checking if password length
#     # is between 8 and 15
#     if (len(password) < 8 or len(password) > 15):
#         return False
 
#     # to check space
#     if (" " in password):
#         return False
 
#     if (True):
#         count = 0
 
#         # check digits from 0 to 9
#         arr = ['0', '1', '2', '3',
#         '4', '5', '6', '7', '8', '9']
 
#         for i in password:
#             if i in arr:
#                 count = 1
#                 break
 
#         if count == 0:
#             return False
 
#     # for special characters
#     if True:
#         count = 0
 
#         arr = ['@', '#','!','~','$','%','^',
#                 '&','*','(',',','-','+','/',
#                 ':','.',',','<','>','?','|']
 
#         for i in password:
#             if i in arr:
#                 count = 1
#                 break
#         if count == 0:
#             return False
 
#     if True:
#         count = 0
 
#         # checking capital letters
#         for i in range(65, 91):
 
#             if chr(i) in password:
#                 count = 1
 
#         if (count == 0):
#             return False
 
#     if (True):
#         count = 0
 
#         # checking small letters
#         for i in range(97, 123):
 
#             if chr(i) in password:
#                 count = 1
 
#         if (count == 0):
#             return False
 
#     # if all conditions fails
#     return True
 
# # Driver code
# password1 = "GeeksForGeeks"
 
# if (isValid([i for i in password1])):
#     print("Valid Password")
# else:
#     print("Invalid Password!!!")
 
# password2 = "Geek$ForGeeks7"
# if (isValid([i for i in password2])):
#     print("Valid Password")
# else:
#     print("Invalid Password!!!")


from nturl2path import url2pathname


list1=['uba666', 'uba122', 'uba111', 'uba000', 'uba555', 'uba333']
list2 =['uba666', 'uba122', 'uba111', 'uba000','uba343','uba900']

# for item in list1:
#     # print(item,'ete')
#     if item not in list2:
#         print(item,'inodey')
S1 = set(list1)
s2 = set(list2)
lol = S1.difference(s2)
for item in lol:
    print(item)
# check = [item in list1 for item in list2]


# print(check)



    

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

# conf_mixin_view = ConfigMixinView.as_view()



        







def check_parenthesis(self, string):
    hash_store = {
            ")":"(",
            "}":"{",
            "]":"["
        }
    stack_store = []
        
    for i in x:
        if i in hash_store:
            if stack_store and stack_store[-1] == hash_store[i]:
                stack_store.pop()
            else:
                return False
        else:
            stack_store.append(i)  
        return False if stack_store else True
