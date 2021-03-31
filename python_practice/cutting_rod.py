import sys


def max(one, two):
    if one > two:
        return one
    else:
        return two


def best_price(price_list, rod_length):
    if rod_length <= 0:
        return 0
    max_val = -sys.maxsize - 1
    for i in range(0, rod_length):
        max_val = max(int(max_val), int(price_list[i]) + int(best_price(price_list, rod_length - i - 1)))

    return max_val


if __name__ == '__main__':
    arr = [1, 5, 8, 9, 10, 17, 17, 20]
    price = best_price(arr, len(arr))
    print(price)



