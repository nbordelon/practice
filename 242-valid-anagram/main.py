# https://leetcode.com/problems/valid-anagram/

# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

class Solution(object):
    def isAnagram(self, s: str, t: str) -> bool:
        """
        :type s: str
        :rtype: bool
        """

        a = sorted(s)
        b = sorted(t)
        
        return a == b

if __name__ == '__main__':
    usrInpt0 = (input("Enter your test case: "))
    usrInpt1 = (input("Enter your test case: "))
    print(Solution().isAnagram(usrInpt0, usrInpt1))