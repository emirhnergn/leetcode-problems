class Solution:
    def reverseWords(self, s: str) -> str:
        tmp = s.split(" ")
        for i in range(len(tmp)):
            tmp[i] = tmp[i][::-1]
        return " ".join(tmp)