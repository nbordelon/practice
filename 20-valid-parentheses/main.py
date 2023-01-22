# https://leetcode.com/problems/valid-parentheses/

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        pFlag = 0
        sFlag = 0
        bFlag = 0

        next = s

        output = 0
        
        if len(s) > 1:
            for x in range(len(s)):

                if (s[x] == "("):
                    pFlag += 1
                    next += "p"
                if (s[x] == "{"):
                    sFlag += 1
                    next += "s"
                if (s[x] == "["):
                    bFlag += 1
                    next += "b"

                if (s[x] == ")"):
                    if next[-1] != "p":
                        output = 0
                        break
                    if (pFlag > 0):
                        pFlag -= 1
                        output+=1
                        next = next[:-1]

                if (s[x] == "}"):
                    if next[-1] != "s":
                        output = 0
                        break
                    if (sFlag > 0):
                        sFlag -= 1
                        output+=1
                        next = next[:-1]

                if(s[x] == "]"):
                    if next[-1] != "b":
                        output = 0
                        break
                    if (bFlag > 0):
                        bFlag -= 1
                        output+=1
                        next = next[:-1]
        
        if(pFlag or sFlag or bFlag):
            output = 0

        if (len(next) != len(s)):
            output = 0

        return (output > 0)


if __name__ == '__main__':
    print(Solution().isValid(input("Enter your test case: ")))