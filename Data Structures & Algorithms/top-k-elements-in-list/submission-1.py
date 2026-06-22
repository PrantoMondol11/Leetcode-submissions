class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res=[]
        hash=defaultdict(int)

        for i in nums:
            hash[i]+=1
        
        sorted_items=sorted(hash.items(),key=lambda x : x[1],reverse=True)

        for j in sorted_items:
            if k>0:
                res.append(j[0])
                k-=1
        return res
            