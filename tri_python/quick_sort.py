def quick_sort(l):
    if len(l)<=1: 
        return l
    
    pivot=l.pop() 
    s=[]  
    b=[] 
    for i in l:
        if i<pivot:
            s.append(i) 
        else :
            b.append(i) 
    return quick_sort(s)+[pivot]+quick_sort(b) 

print(quick_sort([3,2,5,0,1,8,7,6,9,4]))