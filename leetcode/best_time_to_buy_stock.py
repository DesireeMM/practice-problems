# you are given an array where array[i] is the price of a given stock on the ith day
# you want to maximize your profit by choosing a single day to buy one stock
# and choosing a different day in the future to sell that stock
# return the maximum profit you can achieve from this transaction
# if you cannot achieve any profit, return 0

# pseudocode
# find the max and min values for the array
# if the max index is greater than the min index
# return max-min values
# if the max index is less than the min index
# iterate through the list
# find the difference between the index +1 and index
# keep track of the max difference we see
# return that max difference

def find_max_profit(stock_list):
    """Take in an array of stock prices and return the maximum profit"""

    sell_value = max(stock_list)
    sell_index = stock_list.index(sell_value)

    buy_value = min(stock_list)
    buy_index = stock_list.index(buy_value)

    if buy_index < sell_index:
        return sell_value - buy_value
    
    else:
        max_diff_so_far = 0
        for i in range(len(stock_list)):
            for j in range(i, len(stock_list)):
                diff = stock_list[j] - stock_list[i]
                if diff > max_diff_so_far:
                    max_diff_so_far = diff

        return max_diff_so_far

# need a faster solution
# consider popping the last price
# check other prices against popped price

def faster_max_profit(stock_list, max_diff=0):
    
    last_day = stock_list.pop()

    if not stock_list:
        return max_diff

    for item in stock_list:
        diff = last_day - item
        if diff > max_diff:
            max_diff = diff
        
    return faster_max_profit(stock_list, max_diff)

# alternative

def max_profit(stock_list):
    left_index = 0
    right_index = 1
    max_profit = 0

    while right_index < len(stock_list):
        current_profit = stock_list[right_index] - stock_list[left_index]
        if stock_list[left_index] < stock_list[right_index]:
            max_profit = max(current_profit, max_profit)
        else:
            left_index = right_index
        right_index += 1
    
    return max_profit