string1 = "abcbdca"
string2 = "abccbdt"
string3 = "abccabb"
string4 = "abcaefghroo"
string5 = "abcbda"

def test(string):
    p1 = 0
    p2 = len(string) - 1
    count1 = 0
    count2 = 0
    countList1 = []
    countList2 = []
    Maxcount = 0
 
    while p1 < p2:
        while string[p1] not in countList1:
            countList1.append(string[p1])
            count1 += 1
            p1 += 1
            if Maxcount < count1: Maxcount = count1
        p1 += 1
        count1 = 0
        while string[p2] not in countList2:
            countList2.append(string[p2])
            count2 += 1
            p2 -= 1
            if Maxcount < count2: Maxcount = count2
        p2 -= 1
        count2 = 0
    return Maxcount

# print(test(string = string1))
# print(test(string= string2))
# print(test(string=string3))
# print(test(string=string4))
# print(test(string=string5))

# above is my attempt way seems to have some wrongs
# below is the base way
def lengthOfLongestSubstring(string):
    p1 = 0
    p2 = 0
    seenLetter = []
    count = 0
    MaxCount = 0
    while p1 < len(string):
        try:
            while string[p2] not in seenLetter:
                seenLetter.append(string[p2])
                p2 += 1
                count += 1 
                #print(seenLetter)
                if MaxCount < count: MaxCount = count
            p1 += 1
            p2 = p1
            count = 0
            seenLetter = []
        except:
            break

    return MaxCount

print(lengthOfLongestSubstring(string = string1))
print(lengthOfLongestSubstring(string= string2))
print(lengthOfLongestSubstring(string=string3))
print(lengthOfLongestSubstring(string=string4))
print(lengthOfLongestSubstring(string=string5))
print(lengthOfLongestSubstring(string="cccccc"))
print(lengthOfLongestSubstring(string="abcdef"))
print("-----------------------")


# better way
# sliding window
string4 = "abcaefghroo"
def lengthOfLongestSubstring2(string):
    L = 0
    R = 0
    maxLen = 0
    letter = {}
    while R < len(string):
        currentChar = string[R]
        try:
            prevSeenChar = letter[currentChar];
        except:
            prevSeenChar = -1
        if prevSeenChar >= L:
            L = prevSeenChar + 1
        # print("in?",string[R] in letter)
        length = (R-L) + 1
        letter[string[R]] = R
        
        if maxLen < length: maxLen=length
        
        R += 1
    return maxLen

print(lengthOfLongestSubstring2(string=string1))
print(lengthOfLongestSubstring2(string= string2))
print(lengthOfLongestSubstring2(string=string3))
print(lengthOfLongestSubstring2(string=string4))
print(lengthOfLongestSubstring2(string=string5))
print(lengthOfLongestSubstring2(string="cccccc"))
print(lengthOfLongestSubstring2(string="abcdef"))


