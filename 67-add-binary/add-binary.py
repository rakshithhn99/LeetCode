class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = []
        carry = 0
        i=len(a)-1; j=len(b)-1
        while i>=0 and j>=0:
            intr_result = carry + int(a[i]) + int(b[j])
            result.append(intr_result % 2)
            carry = intr_result // 2
            i-=1 
            j-=1
        
        while i>=0:
            intr_result = carry+int(a[i])
            result.append(intr_result % 2)
            carry = intr_result // 2
            i-=1

        while j>=0:
            intr_result = carry+int(b[j])
            result.append(intr_result % 2)
            carry = intr_result // 2
            j-=1

        if carry:
            result.append(carry)

        result.reverse()
        return ''.join(str(i) for i in result)
        
        
        