class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        done = 0
        tmp = 0
        i = 0
        number = 0
        while not done:
            try:
                zero = nums.index(0)
            except:
                break
            if tmp == zero:
                number += 1
            else:
                number = 0
            tmp = zero
            nums.pop(zero)
            nums.append(0)
            i += 1
            try:
                if number > 5 and nums[-i] == tmp:
                    break
            except:
                break
            
            