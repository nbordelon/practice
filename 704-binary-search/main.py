# https://leetcode.com/problems/binary-search/

# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

# You must write an algorithm with O(log n) runtime complexity.

class Solution:
    def search(self, nums: list[int], target: int) -> int:

        value = -1
        
        half = 0
        left = 0
        right = (len(nums)-1)

        while(left<=right):

                # Find middle indice
                half = (right+left)//2

                # Search right of half
                if  target > nums[half]:
                    left = half+1
                    
                # Search left of half 
                elif target < nums[half]:
                    right = half-1

                else:
                    value = half
                    break

        return value

if __name__ == '__main__':
    # Please separate inputs with an empty space. (1 2 3)
    usrInpt0 = list(map(int,(input("Enter your test case: ").strip().split())))
    usrInpt1 = (int(input("Enter your test case: ")))
    print(Solution().search(usrInpt0,usrInpt1))