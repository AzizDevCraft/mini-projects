def tri_selection (liste) : 
    for i in range (len (liste)-1) : 
        mini = min (liste[i+1:])
        if mini < liste [i] : 
            pos = liste.index (mini)
            liste [i], liste [pos] = liste [pos], liste [i]
            
    return liste

if __name__ == "__main__" : 
    l = [4,5,3,1,2,8,0]
    print (tri_selection(l))