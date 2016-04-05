import numpy as np

# merge sort algorithm
lst = np.random.randint(low = 1, high = 10000, size = 100).tolist()

def mergesort(lst):
    if len(lst) == 1:
        return lst
    
    l1 = lst[:len(lst) / 2]
    l2 = lst[len(lst) / 2:]
    
    l1 = mergesort(l1)
    l2 = mergesort(l2)
    
    return merge(l1, l2)

def merge(lst1, lst2):
    
    lst3 = []
    
    while len(lst1) > 0 and len(lst2) > 0:
        if lst1[0] > lst2[0]:
            lst3.append(lst2.pop(0))
        else:
            lst3.append(lst1.pop(0))
            
    while len(lst1) > 0:
        lst3.append(lst1.pop(0))
    while len(lst2) > 0:
        lst3.append(lst2.pop(0))
    
    return lst3

mergesort(lst)
