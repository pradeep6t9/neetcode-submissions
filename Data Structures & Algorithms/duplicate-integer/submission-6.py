class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hm={}
        for i in range(len(nums)):
            if nums[i] in hm:
                hm[nums[i]]+=1
            else:
                hm[nums[i]]=1
        if any(value > 1 for value in hm.values()):
            return True
        else:
            return False

            