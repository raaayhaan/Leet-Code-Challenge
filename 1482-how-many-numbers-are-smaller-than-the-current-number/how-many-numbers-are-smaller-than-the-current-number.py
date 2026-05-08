class Solution:
    #Rehan I Baig, gitHub:@raaayhaan
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        freq = [0] * len(nums)
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] > nums [j]:
                    freq[i] += 1
        return freq
        