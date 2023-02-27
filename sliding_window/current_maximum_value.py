def find_current_maximum(elements, w):
    n = len(elements)
    maximumElements = []
    maximum = 0
    start = 0
    for i in range(n):
        temp = arr[i]
        if temp > arr[start]:
            maximumElements.append(temp)
        if i >= w - 1:
            start = start + 1
    return maximumElements


if __name__ == '__main__':
    arr = [-4, 2, -5, 3, 6]
    result = find_current_maximum(arr, 3)
    print(result)
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = find_current_maximum(arr, 4)
    print(result)
    arr = [1, 2, 3, 4, 5, 6]
    result = find_current_maximum(arr, 6)
    print(result)
    arr = [-4, 5, 4, -4, 4, 6, 7]
    result = find_current_maximum(arr, 2)
    print(result)

