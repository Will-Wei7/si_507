import math

def change(amount, coins):
    if amount == 0:
        return 0
    if amount < 0 or not coins:
        return math.inf

    with_coin = change(amount - coins[0], coins) + 1
    
    without_coin = change(amount, coins[1:])
    
    return min(with_coin, without_coin)

if __name__ == "__main__":
    print(change(48, [1, 5, 10, 25, 50]))
    print(change(48, [1, 7, 24, 42]))    
    print(change(35, [1, 3, 16, 30, 50]))
    print(change(6, [4, 5, 9]))         