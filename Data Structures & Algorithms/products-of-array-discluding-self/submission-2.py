class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product=1
        sproduct=1
        prefix=[]
        suffix=[]
        res=[]
        for i in nums:
            prefix.append(product)
            product=product*i
        for j in range(len(nums)-1,-1,-1):
            suffix.append(sproduct)
            sproduct=sproduct*nums[j]
        suffix.reverse()
        for m in range(len(nums)):
            res.append(prefix[m]*suffix[m])
        return res
       


        

