class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=defaultdict(list)
        for i in strs:
            h1=[0]*26
            for j in i:
                h1[ord(j)-ord('a')]+=1
            res[tuple(h1)].append(i)
        return list(res.values())
                
                
            
        