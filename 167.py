class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in numbers:
            try:
                tmp = numbers.index(target-i)
                break
            except:
                pass
        if numbers.index(i) == tmp:
            tmp += 1
        ret = [numbers.index(i)+1,tmp+1]
        ret.sort()
        return ret