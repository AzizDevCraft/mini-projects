"""Une liste chaînée est une structure de données 
    où chaque élément (appelé "nœud") 
        contient des données et une référence (ou un lien) 
            vers le nœud suivant. """
            
class Noeud : 
    
    def __init__ (self, valeur, suivant = None) : 
        self.valeur = valeur 
        self.suivant = suivant 
    
    def __str__ (self) : 
        return repr ((self.valeur, self.suivant))

class ListeChainee : 
    
    def __init__ (self, tete = None) : 
        self.tete = tete
    
    def __str__ (self) : 
        if self.tete == None :
            return None 
        current = self.tete
        ch = f"{current.valeur} -> "
        while current.suivant != None : 
            current = current.suivant
            ch += f"{current.valeur} -> "
        return ch [:-4]
                    
    def ajouter (self, valeur) : 
        pass
    
    def __iter__ (self) : 
        pass
    
    def __contains__ (self, value) :
        pass 
    
    def __del__ (self, cellule) : 
        pass 

    def __len__ (self) : 
        pass 
    
    def __add__ (self, plus) : 
        pass 
    
    def reverse (self) : 
        pass 
    
    def sort (self) : 
        pass
   
if __name__ == "__main__" :
    chaine = ListeChainee (Noeud (5, Noeud (4, Noeud (3, Noeud (2)))))
    print (chaine)
    for i in chaine : 
        print (i)
    
    