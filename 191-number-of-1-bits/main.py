# https://leetcode.com/problems/number-of-1-bits/description/

# Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

# Note:

# Note that in some languages, such as Java, there is no unsigned integer type. In this case, the input will be given as a signed integer type. It should not affect your implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.
# In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 3, the input represents the signed integer. -3.

class Solution:
    def hammingWeight(self, n: int) -> int:
        """
        :type n: int
        :rtype: int
        """

        div = n
        count = 0

        while(div>0):

            if div%2==1:
                count+=1

            div = div//2

        return count

if __name__ == '__main__':
    usrInpt = (int(input("Enter your test case: ")))
    print(Solution().hammingWeight(usrInpt))