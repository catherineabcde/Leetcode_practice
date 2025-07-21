class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
            seen = {}

            for i, num in enumerate(nums): # {value: key}
                complement = target - num
                if complement in seen:
                    return [seen[complement], i]
                seen[num] = i

            return []


#class Solution:
#    def twoSum(self, nums: List[int], target: int) -> List[int]:
#        for i in range(len(nums)):
#            for j in range(i+1, len(nums)):
#                if nums[i] + nums[j] == target:
#                    return [i, j] 

