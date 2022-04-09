class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        need = {}
        for i, num in enumerate(nums):
            if num in need:
                return [need[num], i] # if current number is a number need return index of number needed and current number
            else:
                need[target - num] = i # number need is at index = i




    #print(twoSum([2,1,4,5,22,7,8,9],24))