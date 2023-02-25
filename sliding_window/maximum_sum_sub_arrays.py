# input
# arr = [1,5,-1,6,3,2] and k = 3
# output 11

def sliding_window_method(arr, k):
    n = len(arr)
    start = 0
    max_sum = 0
    temp = 0
    for i in range(n):
        temp = temp + arr[i]
        if i >= k - 1:
            if temp > max_sum:
                max_sum = temp
            temp = temp - arr[start]
            start = start + 1
    return max_sum


if __name__ == '__main__':
    arr = [1, 5, -1, 6, 3, 2]
    k = 3
    result = sliding_window_method(arr, k)
    print(result)
    arr = [4, 1, 3, 5, 1]
    k = 2
    result = sliding_window_method(arr, k)
    print(result)
    arr = [23, 10, 5, 12, 3, 89, -10]
    k = 3
    result = sliding_window_method(arr, k)
    print(result)
