def binary_search(input_array, value):
    length = len(input_array)
    mid = length/2
    new_array = input_array
    idx = 0
    while (mid != 0):
        if new_array[mid] < value:
            idx += (mid+1)
            new_array = new_array[(mid+1):]
            mid = len(new_array)/2
        else:
            new_array = new_array[:mid]
            mid = len(new_array)/2
        if new_array[mid] == value:
            return idx
    return -1
