n = 5
test_array = [2,3,5,4,1]


def bubbleSwap(array):
    for step in range(n-1,0, -1):
        for item in range(step):
            if array[item] > array[item+1]:
                array[item], array[item+1] = array[item+1], array[item] #I love Python
            else:
                pass
    return array


print (bubbleSwap(test_array))

def bubbleSwapBetter(array):
    count = n-1
    exchange = True
    swaps = 0
    while exchange and count > 0: #This includes reqiurement for exchange = True
        exchange = False
        for item in range(count):
            if array[item] > array[item+1]:
                array[item], array[item+1] = array[item+1], array[item]
                exchange = True
                swaps += 1

            else:
                pass
        count = count - 1

    return swaps, array

def print_result(array):
    result = [
        'Array is sorted in {:d} swaps.'.format(bubbleSwapBetter(array)[0]),
        'First Element: {:d}'.format(bubbleSwapBetter(array)[1][0]),
        'Last Element: {:d}'.format(bubbleSwapBetter(array)[1][-1]),
    ]

    return '\n'.join(result)

print (print_result(test_array))

