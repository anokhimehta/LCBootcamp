########STRING TO INTEGER

class Solution:
    def myAtoi(self, s: str) -> int:

        #remove leading whitespace
        s = s.strip()
        if not s:
            return 0

        index = 0
        #check sign
        sign = 1
        if (s[index] == '-'):
            sign = -1
            index+=1
        elif (s[index] == '+'):
            index+=1

        #conversion
        total_int = 0
        while (index < len(s) and s[index].isdigit()):
            total_int = (total_int * 10) + int(s[index])

            if(sign * total_int > 2**31 - 1):
                return 2**31 - 1
            if(sign * total_int < -2**31):
                return -2**31

            index+=1

        return sign * total_int
