def egaux(nb, taille):
    nb = str(nb)
    nb = "0" * (taille-len(nb)) + nb
    return nb

def fusion(l):
    new = []
    for i in l:
        new.extend(i)
    return new

def bucket_sort(l):
    maxi = len(str(max(l))) 
    liste = list(map(lambda x: egaux(x, maxi), l)) 
    
    for i in range(maxi): 
        bucket = [[] for _ in range(10)]  
        for j in liste:
            bucket[int(j[maxi-i-1])].append(j)
        liste = fusion(bucket)
    liste = list(map(int, liste)) 
    return liste

print(bucket_sort([231, 10, 121, 43, 112, 7, 170, 199, 119, 645]))