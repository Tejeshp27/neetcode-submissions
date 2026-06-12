class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        

        for num in nums:
            if num not in count:
                count[num] = 0
            count[num]+=1

            
        for x in count:
            if count[x] > len(nums)/2:
                return x


        
    