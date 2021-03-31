def numberOfWays(coins, total , count):
    if(total == 0):
        return 1
    if(total < 0):
        return 0
    if(total >= 1 and count <= 0):
        return 0
    return numberOfWays(coins, total , count - 1) + numberOfWays(coins, total - coins[count - 1] , count)


if __name__ == '__main__':
    coins = [2,5,3 ,6]
    total = 10
    count = len(coins)
    print(numberOfWays(coins, total, count))


#1 , 2, 3
#4   1 , 1 , 1, 1
    # 2 , 2
    #2 , 1 , 1
    #3 , 1

#5 {1 , 2, 3}
#  1, 1, 1 , 1 , 1
# 2, 2, 1
#
#
#



