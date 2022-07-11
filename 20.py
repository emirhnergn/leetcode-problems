class Solution:
    def isValid(self, s: str) -> bool:
        liste = [0]
        dictin = {r"(":r")",r"[":r"]",r"{":r"}",
                 r")":r"(",r"]":r"[",r"}":r"{"}
        dictin2 = {r")":r"(",r"]":r"[",r"}":r"{"}
                 
        for i in s:
            try:
                if liste[-1] != dictin[i] and liste[-1] not in dictin2:
                    liste.append(i)
                elif liste[-1] == dictin2[i]:
                    liste.pop()
            except:
                pass
        if liste == [0]:
            return 1
        else:
            return 0 