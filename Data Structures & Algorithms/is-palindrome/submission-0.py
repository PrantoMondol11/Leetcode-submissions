class Solution:
    def isPalindrome(self, s: str) -> bool:
        r=""
        for i in s:
            if 'a' <= i <= 'z' or 'A' <= i <= 'Z' or '0'<=i<='9' :
                r+=i
        r=r.lower()
        i=0
        j=len(r)-1
        while(i<j):
            if r[i]!=r[j]:
                return False
            i+=1
            j-=1
        return True 
        