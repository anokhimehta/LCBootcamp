####Implement Queue using Stacks

class MyQueue:

    def __init__(self):
        self.in_stack = []
        self.out_stack = [] 

    def push(self, x: int) -> None:
        self.in_stack.append(x)

    def pop(self) -> int:
        if (len(self.out_stack) != 0):
            return self.out_stack.pop()
        else:
            while (len(self.in_stack) != 0):
                val = self.in_stack.pop()
                self.out_stack.append(val)
            return self.out_stack.pop()

    def peek(self) -> int:
        if (len(self.out_stack) != 0):
            return self.out_stack[-1]
        else:
            while (len(self.in_stack) != 0):
                val = self.in_stack.pop()
                self.out_stack.append(val)
            return self.out_stack[-1]
        

    def empty(self) -> bool:
        if (len(self.in_stack)==0 and len(self.out_stack)==0):
            return True
        return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()



#####PEOPLE AWARE OF SECRET
class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        
        MOD = 10**9 + 7
        #dp array is the array of new people who learned secret on day i
        dp = [0] * (n+1)
        #base case
        dp[1] = 1

        share = 0
        #loop through rest of the days
        for i in range(2, n+1):
            #if delay period has passed they can share
            if i - delay > 0:
                share = (share + dp[i-delay]) % MOD

            #remove people who forgot secret
            if i - forget > 0:
                share = (share - dp[i-forget]) % MOD

            dp[i] = share

        total = 0
        #sum people in last forget days
        for i in range(n - forget + 1, n+1):
            total = (total + dp[i]) % MOD

        return total
            


####DAILY TEMPERATURES
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        #setup array
        arr = [0] * len(temperatures)

        #stack will contain tuples (temp, index)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                stack_temp, stack_index = stack.pop()
                arr[stack_index] = i - stack_index

            stack.append((t, i))

        return arr

        
