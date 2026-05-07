class Solution:
    #Rehan I Baig gitHub: @raaayhaan
    def findErrorNums(self, nums: List[int]) -> List[int]:
        duplicate = 0
        missing = 0
        freq = [0] * (len(nums) + 1)
        for num in nums:
            freq[num] += 1
        for i in range (1, len(freq)):
            if freq[i] == 2 :
                duplicate = i
            elif freq[i] == 0 :
                missing = i
        return [duplicate , missing]