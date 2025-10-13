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

########FIND ALL ANAGRAMS IN STRING
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        answer = []
        #create dict of p
        p_letters = {}
        for c in p:
            if c not in p_letters:
                p_letters[c] = 1
            else:
                p_letters[c] += 1

        window = len(p)

        #create initial window dictionary
        substr = s[0: window]
        s_letters = {}
        for c in substr:
            if c not in s_letters:
                s_letters[c] = 1
            else:
                s_letters[c] += 1
        
        if (p_letters == s_letters):
            answer.append(0)

        for i in range(1, len(s) - window + 1):
            #1. remove the first letter of the previous window
            first_letter = s[i - 1]
            s_letters[first_letter] -= 1
            if s_letters[first_letter] == 0:
                del s_letters[first_letter]
            #2. add the new letter to the window
            new_letter = s[i + window - 1]
            if new_letter not in s_letters:
                s_letters[new_letter] = 1
            else:
                s_letters[new_letter] += 1

            if (p_letters == s_letters):
                answer.append(i)

        return answer


        
