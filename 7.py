class Solution:
    def reverse(self, x: int) -> int:
        negative = False
        if x < 0:
            negative = True

        if negative:
            x = int(str(x)[1:][::-1])
            if x > 2**31 or x < -2**31:
                return 0
            return int("-" + str(x))
        else:
            x = int(str(x)[::-1])
            if x > 2**31 or x < -2**31:
                return 0
            return int(x)