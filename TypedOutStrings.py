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

print(CompareBackspace(["a","b","#","z"],["a","z","#","z"]).backSpaceCompare())
S = ["a","b","c","#","d"]
T = ["a","c","c","#","c"]
print(CompareBackspace(Sstring=S,Tstring=T).backSpaceCompare())