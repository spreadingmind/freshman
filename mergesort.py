#sort an array of n elements
'''
1 Split into halfes
2 Call mergesort on left side
3 Call mersort on right
4 Merge sorted halves
5 Repeat
'''

def mergesort(arr):
    if len(arr) > 1:

        middle = len(arr) // 2
        left = arr[:middle]
        right = arr[middle:]
        mergesort(left)
        mergesort(right)

        left_pointer, right_pointer, arr_pointer = 0,0,0

        while left_pointer < len(left) and right_pointer < len(right):
            if left[left_pointer]  < right[right_pointer]:
                arr[arr_pointer] = left[left_pointer]
                left_pointer += 1
                arr_pointer += 1
            else:
                arr[arr_pointer] = right[right_pointer]
                arr_pointer += 1
                right_pointer += 1

        while left_pointer < len(left):
            arr[arr_pointer] = left[left_pointer]
            arr_pointer += 1
            left_pointer += 1
        while right_pointer < len(right):
            arr[arr_pointer] = right[right_pointer]
            arr_pointer += 1
            right_pointer += 1
        return arr


print (mergesort([5,6,2,1,4,5,6,25,6]))