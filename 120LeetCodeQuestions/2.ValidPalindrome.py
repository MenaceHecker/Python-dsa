## A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and 
# removing all non-alphanumeric characters, it reads the same forward and backward. 
# Alphanumeric characters include letters and numbers.
##Given a string s, return true if it is a palindrome, or false otherwise.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = ""
        for i in s:
            if i.isnumeric() == True or i.isalpha() == True:
                s1 += i
        s1 = s1.lower()
        s2 = s1[::-1]
        if s1 == s2:
            return True
        return False
        