class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        #if odd
        if sum(nums)%2:
            return False

        dp = set()
        dp.add(0)

        target = sum(nums)//2
        
        for i in range(len(nums)-1, -1, -1):
            next_dp = set()
            for t in dp:
                next_dp.add(t+nums[i])
                next_dp.add(t)
            dp = next_dp

        return True if target in dp else False



class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        coins.sort()
        dp = [0] * (amount + 1)

        for i in range(1, amount+1):
            minn = float('inf')
            for coin in coins:
                diff = i - coin
                if diff < 0:
                    break
                minn = min(minn, dp[diff] + 1)
            dp[i] = minn

        if dp[amount] < float('inf'):
            return dp[amount]
        else:
            return -1





class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = float('-inf')
        currentSum = 0
        for num in nums:
            currentSum += num

            if currentSum > maxSum:
                maxSum = currentSum

            if currentSum < 0:
                currentSum = 0

        return maxSum
