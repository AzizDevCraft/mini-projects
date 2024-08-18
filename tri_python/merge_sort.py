def fusion (l1,l2): 
    l = [None]*(len(l1)+len(l2))
    v,k = 0,0
    for i in range (len(l)) :
        if v == len(l1) : 
            l[i] = l2[k]
            k += 1 
        elif k == len(l2) :
            l[i] = l1[v]
            v += 1 
        elif l1[v] < l2 [k] : 
            l[i] = l1[v]
            v += 1 
        else : 
            l[i] = l2[k]
            k += 1 
    return l

def merge_sort (l) :
    if len(l) == 1 :
        return l
    else :
        l1 = merge_sort (l[:len(l)//2])
        l2 = merge_sort (l[len(l)//2 :])
        return fusion (l1,l2)
    
print (merge_sort([3,2,5,0,1,8,7,6,9,4]))