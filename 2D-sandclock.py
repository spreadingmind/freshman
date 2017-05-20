

#Bulding a 2d-array with all numbers
# arr = []
# for arr_i in range(6):
#    arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
#    arr.append(arr_t)

#Prebuilt example
#arr = [[1, 1, 1, 0, 0, 0],[0,1,0, 0, 0, 0],[1, 1, 1, 0, 0, 0],[0, 0, 0, 0, 0, 0],[0 ,0 ,0, 0, 0, 0],[0, 0, 0, 0, 0, 0]]
arr = [[1, 1, 1, 0, 0, 0],
[0, 1, 0, 0, 0, 0],
[1, 1, 1, 0, 0, 0],
[0, 0, 2, 4, 4, 0],
[0, 0, 0, 2, 0, 0],
[0, 0, 1, 2, 4, 0]]
hourglass_array = []

for i in range(4):
    for j in range(4):

        hourglass_array.append([arr[i][j:j+3],[arr[i+1][j+1]],arr[i+2][j:j+3]])


#Printing hourglasses beautifully
def print_hourglass(array):
    print (array[0],sep=' ')
    print ('  ',array[1],'  ')
    print (array[2],sep=' ')
    print ()

for hourglass in hourglass_array:
    print_hourglass(hourglass)

#Fingding the max summ of hourglass

def find_hourglass_sum(hourglass):
    top = sum(hourglass[0])
    middle = sum(hourglass[1])
    down = sum(hourglass[2])
    return  top + down + middle

def find_max_hourglass_sum(array):
    maximum_hourglass = find_hourglass_sum(array[0])
    for hourglass in array:
        if find_hourglass_sum(hourglass) > maximum_hourglass:
            maximum_hourglass = find_hourglass_sum(hourglass)
        else:
            continue
    return maximum_hourglass


print (find_max_hourglass_sum(hourglass_array))
