import re

# two pointers from outside
def isPalindrome(s):
    s = re.sub('[^0-9a-zA-Z]+', '', s).lower()
    if len(s)<=1:
        return True
    l, r = 0, len(s) -1
    while l < r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True



# two pointers from inside
def isPalindrome2(s):
    s = re.sub('[^0-9a-zA-Z]+', '', s).lower()
    if len(s) <= 1:
        return True
    if len(s) % 2 ==0:
        l = int(len(s)/2) - 1
        r = int(len(s)/2)
        while r < len(s):
            if s[l]!=s[r]:
                return False
            l -= 1
            r += 1
        return True
            
    else:
        l = int(len(s)/2) - 1
        r = int(len(s)/2) + 1
        while r < len(s):
            if s[l]!=s[r]:
                return False
            l -= 1
            r += 1
        return True

print(isPalindrome2(s = "accdcfa"))

# Almost a palindrome
# drop most one letter let the string be palindrome
class Solution:
    def validPalindrome(self, s):
        s = re.sub('[^0-9a-zA-Z]+', '', s).lower()
        if len(s) <=1:
            return True
        l, r = 0, len(s)-1
        while l < r:
            if s[l] != s[r]:
                return self.isPalindrome(s, l+1, r) or self.isPalindrome(s, l, r-1)
            l += 1
            r -= 1
        return True


    @staticmethod
    def isPalindrome(s, left, right):
        while left < right:
            if s[left]!=s[right]:
                return False
            l += 1
            r -= 1
        return True
