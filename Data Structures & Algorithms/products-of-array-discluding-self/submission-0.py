class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[]
        
        for i in range(len(nums)):
            j=0
            product=1
            while(j<len(nums)):
                if j==i:
                    j+=1
                    continue
                else:
                    product=product*nums[j]
                j+=1
            res.append(product)
        return res