def find_current_maximum(elements, w):
    n = len(elements)
    maximumElements = []
    maximum = 0
    for i in range(n):
        temp = arr[i]
        if temp > maximum:
            maximum = temp
        if i >= w - 1:
            maximumElements.append(maximum)
    return maximumElements


if __name__ == '__main__':
    arr = [-4, 2, -5, 3, 6]
    result = find_current_maximum(arr, 3)
    print(result)
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = find_current_maximum(arr, 4)
    print(result)
