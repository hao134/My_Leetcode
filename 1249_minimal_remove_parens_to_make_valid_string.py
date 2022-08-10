s_test = "a)b(c)d"
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        s = [*s]
        for index, element in enumerate(s):
            if element == "(":
                stack.append(index)
            elif not stack and element == ")":
                s[index] = " "
            elif element == ")":
                stack.pop()
        
        if len(stack) >0:
            for i in stack:
                s[i] = " "
        
        new_string = ""
        for i in s:
            if i == " ":
                continue
            new_string+=i

        return new_string

print(Solution().minRemoveToMakeValid(s=s_test))
