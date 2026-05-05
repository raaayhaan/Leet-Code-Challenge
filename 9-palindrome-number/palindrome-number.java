class Solution {
    public boolean isPalindrome(int x) {
        int rev = 0;
        int y = x;
        if (x < 0){
            return false;
        }
        else{
            while (x != 0){
                int lastDigit = x % 10;
                rev = rev * 10 + lastDigit;
                x /= 10;
            }
            if (rev == y) return true;
            else return false;
        }
    }
}