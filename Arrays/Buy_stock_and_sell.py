def buy_and_sell_stock(prices):
    min_p = float('inf')
    max_p = 0
    for i in prices:
        min_p = min(min_p,i)
        max_p = max(max_p,i-min_p)
    return max_p
print(buy_and_sell_stock(prices=[6,3,4,8,2,7,9]))