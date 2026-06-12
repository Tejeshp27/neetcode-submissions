class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        

        for num in nums:
           count[num] = count.get(num,0)+1

            
        for x in count:
            if count[x] > len(nums)/2:
                return x


        
    