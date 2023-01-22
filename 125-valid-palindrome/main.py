# https://leetcode.com/problems/valid-palindrome/

# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        s = s.lower()

        j = 0
        forw = []
        back = []

        for i in range(len(s)):

            if s[i].isalpha() or s[i].isnumeric():
                forw.append(s[i])

            if s[j-1].isalpha() or s[j-1].isnumeric():
                back.append(s[j-1])
        
            j-=1

        return (back == forw)

if __name__ == '__main__':
    usrInpt = (input("Enter your test case: "))
    print(Solution().isPalindrome(usrInpt))