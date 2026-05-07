class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        freq = [0] *(len (nums) + 1)
        for n in nums :
            freq[n] += 1
        missing = []
        for i in range (1, len(freq)):
            if (freq[i] == 0):
                missing.append(i)
        return missing

        