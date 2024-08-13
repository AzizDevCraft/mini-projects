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
        ele = Noeud (valeur)
        if self.tete == None : 
            self.tete = ele
        else : 
            current = self.tete 
            while current.suivant != None : 
                current = current.suivant     
            current.suivant = ele
    
    def __iter__ (self) : 
        if self.tete != None :  
            current = self.tete
            while current != None : 
                yield current.valeur
                current = current.suivant 
           
    def __contains__ (self, value) :
        if self.tete != None : 
            if self.tete.valeur == value : 
                return True
            current = self.tete
            while current.suivant != None : 
                current = current.suivant
                if current.valeur == value : 
                    return True
        return False 

    def __len__ (self) : 
        compteur = 0
        for i in self : 
            compteur += 1
        return compteur 
    
    def __add__ (self, plus) : 
        pass 
    
    def reverse (self) : 
        pass 
    
    def sort (self) : 
        pass
   
if __name__ == "__main__" :
    chaine = ListeChainee (Noeud (5, Noeud (4, Noeud (3, Noeud (2)))))
    print (chaine)
    chaine.ajouter (1)
    print (chaine)
    for i in chaine : 
        print (i) 
    print (5 in chaine)
    print (9 in chaine)
    print (1 in chaine)
    print (len(chaine))