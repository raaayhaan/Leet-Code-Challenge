class Solution {
    //Rehan Baig (gitHub:@raaay_haan)
    public int[] getConcatenation(int[] nums) {
        int [] ans = new int[2 * nums.length];
        for(int i = 0; i < nums.length; i++){
            ans[i] = nums[i];
            int size = i + nums.length;
            ans[size] = nums[i];
        }
        return ans;
    }
}