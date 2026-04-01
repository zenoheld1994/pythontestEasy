 
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

