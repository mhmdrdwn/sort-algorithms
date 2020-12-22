def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key
    return arr


def bubble_sort(arr):
    n = len(arr) 
  
    # Traverse through all array elements 
    for i in range(n-1): 
    # range(n) also work but outer loop will repeat one time more than needed. 
  
        # Last i elements are already in place 
        for j in range(0, n-i-1): 
  
            # traverse the array from 0 to n-i-1 
            # Swap if the element found is greater 
            # than the next element 
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j] 
    return arr


def merge(data_list, left_split, right_split):
    i=j=k=0
        
    while i < len(left_split) and j < len(right_split):
        if left_split[i] < right_split[j]:
            data_list[k]=left_split[i]
            i+=1
        else:
            data_list[k]=right_split[j]
            j+=1
        k+=1

    while i < len(left_split):
        data_list[k]=left_split[i]
        i+=1
        k+=1

    while j < len(right_split):
        data_list[k]=right_split[j]
        j+=1
        k+=1

    return data_list


def merge_sort(data_list):
    if len(data_list)>1:
        middle_item = len(data_list)//2
        right_split = data_list[middle_item:]
        left_split = data_list[:middle_item]
        
        merge_sort(left_split)
        merge_sort(right_split)
        
        data_list = merge(data_list, left_split, right_split)
        
    return data_list


def quick_sort(data_list):
    left_part = []
    equal_part = []
    right_part = []

    if len(data_list) > 1:
        pivot = data_list[len(data_list)//2]

        for element in data_list:
            if element < pivot:
                left_part.append(element)
            elif element == pivot:
                equal_part.append(element)
            elif element > pivot:
                right_part.append(element)

        data_list = quick_sort(left_part)+equal_part+quick_sort(right_part)
        return data_list
    
    return data_list

def partition(interval_list, arr):
    low, high = interval_list.pop()
    if high - low < 2:
        return
    pivot_element = arr[(low + high) // 2]
    high += 1;

    left_arr, right_arr, pivots = [], [], 0
    for item in arr[low:high]:
        if item > pivot_element:
            right_arr.append(item)
        elif item < pivot_element:
            left_arr.append(item)
        else:
            pivots += 1
    arr[low:high] = left_arr + ([pivot_element] * pivots) + right_arr
    offset = len(left_arr) - 1
    interval_list.add( (low, low + offset) )
    interval_list.add( (low + offset + pivots, high - 1))

def lamport_sort(arr):
    interval_list = set([(0, len(arr) - 1)])
    while len(interval_list) > 0:
        partition(interval_list, arr)
    return arr


def combined_sort(data_list):
    threshold = 10
    if len(data_list) >= threshold:
        middle_item = len(data_list)//2
        right_split = data_list[middle_item:]
        left_split = data_list[:middle_item]
        combined_sort(left_split)
        combined_sort(right_split)
        data_list = merge(data_list, left_split, right_split)
    else:
        data_list = insertion_sort(data_list)

    return data_list


if __name__ == '__main__':
    print('hello')
    test_list = list(range(-25,25))
    quick_sort(test_list)
    print(test_list)

