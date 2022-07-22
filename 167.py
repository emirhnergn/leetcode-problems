class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        tmp2 = -99999999999999
        for i in numbers:
            if tmp2 != i:
                try:
                    tmp = numbers.index(target-i)
                    tmp2 = i
                    break
                except:
                    tmp2 = i
                    pass
            else:
                pass
        if numbers.index(i) == tmp:
            tmp += 1
        ret = [numbers.index(i)+1,tmp+1]
        ret.sort()
        return ret