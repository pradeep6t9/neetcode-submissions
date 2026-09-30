class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm={}
        for i in range(len(nums)):
            hm[nums[i]]=i
        for j in range(len(nums)):
            res=target-nums[j]
            if res in hm and hm[res] != j:
                return([j,hm[res]])
        return([j,hm[res]])
        