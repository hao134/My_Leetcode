class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0: return True
        parens = {
            '(':')',
            '[':']',
            '{':'}'
        }
        stack = []
        for item in s:
            if item in parens:
                stack.append(item)
            else:
                if stack:
                    leftBracket = stack.pop()
                    correctBracket = parens[leftBracket]
                    if item != correctBracket: return False
            
        return stack == []