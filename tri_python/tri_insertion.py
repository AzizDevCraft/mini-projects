def tri_insertion (liste) : 
    for i in range (1, len (liste)) : 
        x = liste [i]
        j = i
        while j>0 and x < liste [j-1] : 
            liste [j] = liste[j-1]
            j -= 1
        liste [j] = x
    return liste 

if __name__ == "__main__" : 
    l = [4,5,3,1,2,8,0]
    print (tri_insertion (l))