"""
    Stock Buy And Sell
"""

def stock(nums):
    max_profit = 0
    
    for i in range(0, len(nums)-1):
        max_difference= 0
        for j in range(i+1, len(nums)):
            if max_difference < nums[j] - nums[i] :
                max_difference = nums[j] - nums[i]
                if max_profit < max_difference:
                    max_profit = max_difference
    
    return max_profit

if __name__ == "__main__":
    prices = [7,6,4,3,1]
    print(stock(prices))