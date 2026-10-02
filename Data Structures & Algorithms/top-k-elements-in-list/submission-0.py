class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm={}
        for s in nums:
            if s in hm:
                hm[s]+=1
            else:
                hm[s]=1
        res= sorted(hm.items(),key = lambda x:x[1], reverse = True)
        return [x[0] for x in res[:k]]