class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if not prices: return 0
        min_price = prices[0]
        max_profit = 0
        # Start from day 2 (index 1) to ensure we sell AFTER buying
        for i in range(1, len(prices)):
            # 1. Check if selling today at prices[i] gives better profit
            max_profit = max(max_profit, prices[i] - min_price)
            # 2. Then check if today is a better day to buy for the future
            min_price = min(min_price, prices[i])
        return max_profit


if __name__ == "__main__":
    # Indexes represent the day and values represents the price
    print(Solution().maxProfit([7,1,5,3,6,4]))