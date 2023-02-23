def find_current_maximum(elements, w):
    n = len(elements)
    start = 0
    result = []
    maximum = 0
    for i in range(n):
        temp = elements[start]
        if i >= w - 1:
            if temp > maximum:
                maximum = temp
                result.append(maximum)
                start = start + 1
            else:
                start = start + 1
    print(result)


if __name__ == '__main__':
    arr = [-4, 5, 4, -4, 4, 6, 7]
    find_current_maximum(arr, 3)
