class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hm={}
        for j in range(len(nums)):
            if nums[j] in hm:
                return(True)
            hm[nums[j]]='Yes'
        return(False)