from typing import List
class Solution():
    def addBinary(self,a:str,b:str):
        result, carry, val = '', 0, 0
        for i in range(max(len(a),len(b))):
            val = carry
            if i < len(a):
                val += int(a[-(i+1)])
            if i < len(b):
                val += int(b[-(i+1)])
            carry, val = val //2, val%2
            result += str(val)
        if carry:
            result += str(1)
        return result[::-1]


"""
ex:
a = '11', b = '1'
(1) i = 0
val = 1, val = 2
carry = 1, val = 0
result = "0"

(2) i = 1
val = 2
carry = 1, val = 0
result = "00"

final:
carry  = 1
result = "001"
return result = "100"
"""