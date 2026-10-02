class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm={}
        for i in strs:
            key = ''.join(sorted(i))
            if key in hm:
                hm[key].append(i)
            else:
                hm[key]=[i]
        return list(hm.values())