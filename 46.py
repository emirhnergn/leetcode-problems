import itertools
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer = []
        perms = list(itertools.permutations(nums))
        for i in perms:
            answer.append(list(i))
        return answer