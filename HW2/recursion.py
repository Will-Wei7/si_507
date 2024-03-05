import math

def change(amount, coins):
    """
    Finds the minimum number of coins needed to make up a given amount.
    
    Args:
    - amount (int): The target amount to achieve with the coins.
    - coins (list of int): Available denominations of coins.
    
    Returns:
    - int: The minimum number of coins needed to make up the amount, or math.inf if it's not possible.
    """
    if amount == 0:
        return 0
    if amount < 0 or not coins:
        return math.inf

    with_coin = change(amount - coins[0], coins) + 1
    without_coin = change(amount, coins[1:])
    return min(with_coin, without_coin)

def giveChange(amount, coins):
    """
    Finds the minimum number of coins and their denominations needed to make up a given amount.
    
    Args:
    - amount (int): The target amount to achieve with the coins.
    - coins (list of int): Available denominations of coins.
    
    Returns:
    - list: A list containing the minimum number of coins and a list of the coins used.
    """
    if amount == 0:
        return [0, []]
    if amount < 0 or not coins:
        return [math.inf, []]

    with_coin = giveChange(amount - coins[0], coins)
    with_coin[0] += 1
    with_coin[1] = with_coin[1] + [coins[0]]
    
    without_coin = giveChange(amount, coins[1:])

    if with_coin[0] < without_coin[0]:
        return with_coin
    else:
        return without_coin
    
if __name__ == "__main__":
    print(change(48, [1, 5, 10, 25, 50]))
    print(change(48, [1, 7, 24, 42]))    
    print(change(35, [1, 3, 16, 30, 50]))
    print(change(6, [4, 5, 9]))  
    print(giveChange(48, [1, 5, 10, 25, 50]))
    print(giveChange(48, [1, 7, 24, 42]))
    print(giveChange(35, [1, 3, 16, 30, 50]))
    print(giveChange(6, [4, 5, 9]))       