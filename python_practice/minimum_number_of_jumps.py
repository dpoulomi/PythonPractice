import sys


def get_min_jump(arr , n):
    max_val = sys.maxsize - 1
    steps =   [int(max_val)] * n
    # stepTracker = []
    steps[0] = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if(i > j and (arr[j] + j) >= i):
                if((steps[j] + 1) < steps[i]):
                    steps[i] = steps[j] + 1

    return steps[n - 1]


if __name__ == '__main__':
    # arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    arr = [1, 4, 3, 2, 6, 7]
    n = len(arr)
    print(get_min_jump(arr, n))