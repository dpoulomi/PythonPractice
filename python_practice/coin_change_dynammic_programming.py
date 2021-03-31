def getNumberOfWays(coins , total, count):
    table = [0] * (total + 1)
    # total is 1
    # table[0][0] = 1
    # #total is 2
    # table[0][1] = 1
    # for i in range(total):
    #     for j in range(len(coins)):
    #         table[i][j] = table[i - 1][]
    table[0] = 1
    for i in range(len(coins)):
        for j in range(total + 1):
            if coins[i] <= j:
                table[j] = table[j] + table[j - coins[i]]
    return table[total]



if __name__ == '__main__':
    coins = [1 , 2 , 3]
    total = 4
    count = len(coins)
    print(getNumberOfWays(coins, total, count))




#     1 2 3 4
#   1 1 1 1 1
#   2 1 2 2
#   3
#



#1 , 2, 3 -- coins
#4 -- total
# 1 , 1 , 1, 1
# 2 , 2
#2 , 1 , 1
#3 , 1
