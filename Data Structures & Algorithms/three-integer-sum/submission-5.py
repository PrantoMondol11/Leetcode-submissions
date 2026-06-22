class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums=sorted(nums)
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            k=i+1
            j=len(nums)-1
            while(k<j):
                
                if nums[i]+nums[j]+nums[k]==0:
                    res.append([nums[i],nums[k],nums[j]])
                    j-=1
                    k+=1
                    while(k<j and nums[j]==nums[j+1]):
                            j-=1
                    while(k<j and nums[k]==nums[k-1]):
                            k+=1

                  
                elif nums[i]+nums[j]+nums[k]>0:
                    j-=1
                else:
                    k+=1
        return res
        