def bubble_sort (liste) :
    PermutationOk = True 
    while PermutationOk : 
        PermutationOk = False
        for i in range (len (liste) - 1) : 
            if liste [i] > liste [i+1] : 
                liste[i], liste [i+1] = liste [i+1], liste [i]
                PermutationOk = True
    return liste 

if __name__ == "__main__" : 
    l = [4,5,3,1,2,8,0]
    print (bubble_sort(l))
