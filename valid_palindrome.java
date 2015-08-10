# https://leetcode.com/problems/valid-palindrome/

public class Solution {
    public boolean isPalindrome(String s) {
        s = s.replaceAll("[\\W\\_]","");
        s = s.toLowerCase();
        int len = s.length();
        for(int i=0; i<len/2; i++){
            if(s.charAt(i) != s.charAt(len-i-1))
                return false;
        }
        return true;
    }
}