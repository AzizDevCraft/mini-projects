def Max_heap(T, n, i): 
    
    largest = i 
    l = 2 * i + 1     
    r = 2 * i + 2     
  
    if l < n and T[i] < T[l]: 
        largest = l  
    if r < n and T[largest] < T[r]: 
        largest = r 
    if largest != i:  
        T[i],T[largest] = T[largest],T[i]   
        Max_heap(T, n, largest) 

def heap_sort(l): 
    n = len(l) 
    for i in range(n, -1, -1): 
        Max_heap(l, n, i) 
    for i in range(n-1, 0, -1): 
        l[i], l[0] = l[0], l[i]   
        Max_heap(l, i, 0) 

    return l

print (heap_sort ([3,2,5,0,1,8,7,6,9,4]))

