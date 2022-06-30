class CompareBackspace:
    def __init__(self, Sstring, Tstring):
        self.Sstring = Sstring
        self.Tstring = Tstring

    @staticmethod
    def buildString(StringArray):
        builtArray = []
        for elem in StringArray:
            if elem == "#" and builtArray!=[]:
                builtArray.pop()
            elif elem == '#' and builtArray == []:
                pass
            else:
                builtArray.append(elem)
        return builtArray

    def backSpaceCompare(self):
        S = self.buildString(self.Sstring)
        T = self.buildString(self.Tstring)
        if S == T:
            return True
        return False

# print(CompareBackspace(["a","b","#","z"],["a","z","#","z"]).backSpaceCompare())
# S = ["a","b","c","#","d"]
# T = ["a","c","c","#","c"]
# print(CompareBackspace(Sstring=S,Tstring=T).backSpaceCompare())

def compareBackspace(S,T):
    p1 = len(S) - 1
    p2 = len(T) - 1
    while p1 >= 0 or p2 >= 0:
        if S[p1] == "#" or T[p2] == "#":
            if S[p1] == "#":
                backCount = 2

                while backCount > 0:
                    p1 -= 1
                    backCount -= 1

                    if S[p1] == "#":
                        backCount += 2
    
            if T[p2] == "#":
                backCount = 2

                while backCount > 0:
                    p2 -= 1
                    backCount -= 1
                    
                    if T[p2] == "#":
                        backCount += 2
        
        else:
            if S[p1] != T[p2]:
                return False
            else:
                p1 -= 1
                p2 -= 1
    return True
print(compareBackspace(["a","b","#","z"],["a","z","#","z"]))
print(compareBackspace(["a","b","c","#","d"],["a","c","c","#","c"]))