class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        first={}
        second={}
        for i in range(len(s)):
            if s[i] in first:
                first[s[i]]+=1
            else:
                first[s[i]]=1
        for j in range(len(t)):
            if t[j] in second:
                second[t[j]]+=1
            else:
                second[t[j]]=1
        if first == second:
            return True
        else:
            return False

        