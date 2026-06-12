class Solution:
    def sortColors(self, nums: List[int]) -> None:
        
        count = {}

        for num in nums:
            count[num] = count.get(num,0) +1

            zero = count.get(0,0)
            one = count.get(1,0)
            two = count.get(2,0)

            for i in range(zero):
                nums[i] = 0
            for i in range(zero, zero + one):
                nums[i] = 1
            for i in range(one+zero,+zero + one + two):
                nums[i] = 2 

        

            
                
        