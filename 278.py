class Solution:
    def firstBadVersion(self, n):
        bv = 0
        k = 0
        tmp = n//4
        num = n//2
        while bv == 0:
            print(num)
            print(tmp)
            print("aaa")
            if isBadVersion(num-1) == 0 and isBadVersion(num) == 1 and isBadVersion(num+1) == 1:
                bv = 1
            elif isBadVersion(num) == 0:
                num += tmp
                tmp = tmp //2
                if tmp < 1:
                    tmp = 1
            elif isBadVersion(num) == 1:
                num -= tmp
                tmp = tmp //2
                if tmp < 1:
                    tmp = 1
        return num
            
                
        