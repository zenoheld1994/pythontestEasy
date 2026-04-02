x = "hello world"
# print(x[2:])
# print("o" in x)
# lista=[1,2]
# print(lista is lista)
mySeq = [20, 88, 40, 99, 60, 11, 100]


forbidden_chars= ["x", "y"]
pwd = "paswordx"
if any(char in forbidden_chars for char in pwd):
    print("forbidden!")
else:
    print("this is valid")
for i in range(len(forbidden_chars)):
    if(forbidden_chars[i]  in pwd):
       print("no mames")
    # if(pwd.find(forbidden_chars[i])):
    #     print("your pwd has forbidden shit!")
    

# for i in range(0, len(mySeq)):
#     print(mySeq[i])
'''
class Solution:
    def twoSum(self, nums: list[int], target: int)->list[int]:
        seen = set()
        solve = []

        

        for index,number in enumerate(nums):
            complement = target - number
            if complement in seen:
                solve.append(nums.index(complement))
                solve.append(index)
            seen.add(number)


        return solve 
 
    def __init__(self,targ: int,result: list[int]):
        listadenums =[3,3]
        self.targ = targ
        self.result = self.twoSum(listadenums,targ)
sol = Solution(6,[1,2])
print(sol.result)
'''

