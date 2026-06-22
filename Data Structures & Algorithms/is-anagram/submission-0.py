class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        h1=[0]*26
        h2=[0]*26
        for i in range(len(s)):
            h1[ord(s[i])-ord('a')]+=1
        for j in range(len(t)):
            h2[ord(t[j])-ord('a')]+=1
        for k in range(26):
            if h1[k]!=h2[k]:
                return False
        return True