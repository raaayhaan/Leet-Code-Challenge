class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # freq = [0] *(len (nums) + 1)
        for n in nums :
            index = abs(n) - 1
            if nums[index] > 0 :
                nums[index] = -nums[index]        
        missing = []
        for i in range (len(nums)):
            if (nums[i] > 0):
                missing.append(i+1)
                
        return missing

        