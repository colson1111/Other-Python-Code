import numpy as np
import time

lst = np.random.randint(low = 1, high = 100, size = 10000).tolist()

lst1 = lst

# bubble sort
def bubble_sort(lst):
    
    for i in range(len(lst)-1,0,-1):
        for j in range(i):
            if lst[j] > lst[j + 1]:
                c = lst[j]
                lst[j] = lst[j + 1]
                lst[j + 1] = c
    
    return lst

a = time.time()
bubble_sort(lst1)
bubble_time = time.time() - a

            