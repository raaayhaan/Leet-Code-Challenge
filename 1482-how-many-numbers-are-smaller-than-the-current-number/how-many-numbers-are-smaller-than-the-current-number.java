class Solution {
    //Rehan I Baig, gitHub:@raaayhaan
    public int[] smallerNumbersThanCurrent(int[] nums) {
        int[] freq = new int[nums.length];
        for(int i = 0; i < nums.length; i++){
            for (int j = 0; j < nums.length; j++){
                if(nums[i] > nums[j]){
                    freq[i]++;
                }
            }
        }
        return freq;
    }
}