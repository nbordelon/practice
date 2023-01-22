# https://leetcode.com/problems/contains-duplicate/

# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        return_val = True

        init_tot = len(nums)
        uniq_tot = len(set(nums))

        if init_tot == uniq_tot:
            return_val = False

        return return_val

if __name__ == '__main__':
    # Please separate inputs with an empty space. (1 2 3)
    usrInpt = list(map(int,(input("Enter your test case: ").strip().split())))
    print(Solution().containsDuplicate(usrInpt))