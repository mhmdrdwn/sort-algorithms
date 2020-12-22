def insertion_sort(A): 
    """
    The algorithm works from second element where it 
    assign the key as it iterates through the elements 
    where j is the preceding element of the key. If the 
    key is greater than the preceding element, swap 
    the key and preceding element. This is repeated 
    untill j reaches -1 as j is decremented each loop 
    by 1 untill the while loop breaks where j is -1.

    Parameters
    ----------
    A: array or list
        unsorted List of input A

    Returns:
    --------
    A: array or list
        sorted A list in place
    """

    for i in range(1, len(A)): 
        key = A[i] 
        j = i-1
        while j >=0 and key < A[j] : 
            A[j+1] = A[j] 
            j -= 1
        A[j+1] = key 
    return A


def bubble_sort(A):
    """
    The algorithm here works from left the elements and swap them
    if they are not sorted. through the first run, the algorithm
    managed to push the greatest element to the left. So, in the 
    next run the algorithm will iterate over all elements except 
    last one and swap elements if needed and so on.
    The algorithm is in place sorting algorithm and performance 
    of This algorithm at worst case is O(n^2)
    
    Parameters
    ----------
    A: array or list
        unsorted List of input data

    Returns:
    --------
    A: list
        sorted list in place
    """
    for i in range(len(A)):
        for j in range(len(A) - 1):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
    return A

def merge_sort(A):
    """
    Parameters
    ----------
    A: array or list
        unsorted List of input data

    Returns:
    --------
    A: list
        sorted A list in place
    """

    if len(A) > 1:
        middle_item = len(A)//2
        right_split = A[middle_item:]
        left_split = A[:middle_item]
        merge_sort(left_split)
        merge_sort(right_split)
        A = merge(A, left_split, right_split)        
    return A


def quick_sort(A):
    """

    Parameters
    ----------
    A: array or list
        unsorted List of input data

    Returns:
    --------
    A: list
        sorted A list in place
    """
    
    left_part = []
    equal_part = []
    right_part = []
    

    if len(A) > 1:
        pivot = A[len(A)//2]
        for element in A:
            if element < pivot:
                left_part.append(element)
            elif element == pivot:
                equal_part.append(element)
            elif element > pivot:
                right_part.append(element)
        A = quick_sort(left_part)+equal_part+quick_sort(right_part)
    
    return A


def partition(interval_list, A):
    low, high = interval_list.pop()
    if high - low < 2:
        return
    pivot_element = A[(low + high) // 2]
    high += 1;

    left_arr, right_arr, pivots = [], [], 0
    for item in A[low:high]:
        if item > pivot_element:
            right_arr.append(item)
        elif item < pivot_element:
            left_arr.append(item)
        else:
            pivots += 1
    A[low:high] = left_arr + ([pivot_element] * pivots) + right_arr
    offset = len(left_arr) - 1
    interval_list.add( (low, low + offset) )
    interval_list.add( (low + offset + pivots, high - 1))


def lamport_sort(A):
    interval_list = set([(0, len(A)-1)])
    while len(interval_list) > 0:
        partition(interval_list, A)
    return A


def binary_insertion_sort(A,left, right):
    for i in range(left+1, right+1):
        temp = A[i]
        pos = binary_search(A, temp, left, i) + 1
        for k in range(i, pos, -1):
            A[k] = A[k - 1]
        A[pos] = temp


def binary_search(A, key, left, right):
    if right - left <= 1:
        if key < A[left]:
            return left - 1 
        else:
            return left 
    mid = (left + right)//2
    if A[mid] < key:
        return binary_search(A, key, mid, right)
    elif A[mid] > key:
        return binary_search(A, key, left, mid)
    else:
        return mid


def merge(A, left_split, right_split, start=0):   
    """ 
    Parameters
    ----------
    A: array or list
        unsorted List of input A
    left_split: list
    right_split: list   
    start: int
        beginning index of the left split

    Returns:
    --------
    A: list
        sorted list in place
    """
    i, j, k = 0, 0, start
      
    while i < len(left_split) and j < len(right_split): 
        if left_split[i] <= right_split[j]: 
            A[k] = left_split[i] 
            i += 1
  
        else: 
            A[k] = right_split[j] 
            j += 1
  
        k += 1
  
    while i < len(left_split): 
        A[k] = left_split[i] 
        k += 1
        i += 1
  
    while j < len(right_split): 
        A[k] = right_split[j] 
        k += 1
        j += 1


def combined_sort(A):
    n = len(A)
    run = cal_run(n)
    for start in range(0, n, run): 
        end = min(start + run - 1, n - 1) 
        binary_insertion_sort(A, start, end) 
        
    size = run
    while size < n:    
        for start in range(0, n , 2 * size):
            mid = min(n-1, start + size - 1)
            end = min(n-1, start+2*size-1)
            left_split = A[start:mid+1]
            right_split = A[mid+1:end+1]
            merge(A, left_split, right_split, start)
        size *= 2
    return A


def cal_run(n):
    """
    calculate the length of the run

    Parameters:
    -----------
    n: length of the array or list
        int

    Returns:
    -------
    run_len: length of run
        int
    """
    minrun = 32
    r, l = 0, n
    while l >= minrun:
        r = r | (l&1)
        l = l >> 1
    return r+l
