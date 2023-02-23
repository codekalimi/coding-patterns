# sliding window patterns for printing the fum of sub arrays

def sum_of_sub_arrays(arr, k):
    n = len(arr)
    total = 0
    start = 0
    for i in range(n):
        total = total + arr[i]
        if i >= k - 1:
            print(total, end=" ")
            total = total - arr[start]
            start = start + 1


if __name__ == "__main__":
    arr = [2, 4, 5, 6, 2, 6, 7, 6, 2, 7]
    sum_of_sub_arrays(arr, 3)
