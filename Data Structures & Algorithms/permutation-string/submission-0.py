class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count= {}
        count1={}
        for i in range(len(s1)):
            count[s1[i]]=count.get(s1[i],0)+1
        left=0
        for right in range(len(s2)):
            count1[s2[right]]=count1.get(s2[right],0)+1
            if right-left+1 > len(s1):
                count1[s2[left]]-=1
                if count1[s2[left]]==0:
                    del count1[s2[left]]
                left+=1
            if right - left +1== len(s1):
                if count1==count :
                    return True
        return False
