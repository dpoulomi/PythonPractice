import sys


def best_price(price_list, rod_length):
    best_price_for_length = [0] * rod_length
    best_price_for_length[0] = price_list[0]
    #best_price_for_length[1] = max(price_list[0] * 2, price_list[1])

    for i in range(1, rod_length):
        max_value = - sys.maxsize - 1
        for k in range(0, i):
            max_value = max(max_value, price_list[k] + best_price_for_length[i - k - 1])
        best_price_for_length[i] = max_value

    return best_price_for_length



if __name__ == '__main__':
    arr = [3 ,  5,   8,   9,  10,  17,  17,  20]
    rod_length = len(arr)
    price = best_price(arr, rod_length)
    print(price[rod_length - 1])


    # best_price_for_length[i] = (i + 1)-th best price
# rod_length = 1, best_price_for_length = 3
# rod_length = 2, best_price_for_length = max(6, 5) = 6
# rod_length = 3, best_price_for_length = (1,1,1), (1,2), (2,1), (3)
    #
