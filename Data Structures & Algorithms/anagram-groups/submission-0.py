class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm={}
        for i in range(len(strs)):
            key = ''.join(sorted(strs[i]))
            if key in hm:
                hm[key].append(strs[i])
            else:
                hm[key]=[strs[i]]
        return list(hm.values())