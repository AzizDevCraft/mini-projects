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
            return repr(None)
        current = self.tete
        ch = f"{current.valeur} -> "
        while current.suivant != None : 
            current = current.suivant
            ch += f"{current.valeur} -> "
        return ch [:-4]
    
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
        if type(plus) == ListeChainee and plus.tete != None: 
            if self.tete != None : 
                current = self.tete 
                while current.suivant != None : 
                    current = current.suivant
                current.suivant = plus.tete
            else : 
                self.tete = plus.tete
        else : 
            self.ajouter (plus)    
        return self 
    
    def __radd__ (self, plus) : 
        self.insertion (plus)   
        return self  
    
    def __getitem__ (self, index) : 
        pass     
             
    def ajouter (self, valeur) : 
        ele = Noeud (valeur)
        if self.tete == None : 
            self.tete = ele
        else : 
            current = self.tete 
            while current.suivant != None : 
                current = current.suivant     
            current.suivant = ele 
    
    def insertion (self, item, index = 0) :
        ele = Noeud (item)
        if self.tete != None :
            if not (-len(self) < index <= len (self)) : 
                raise IndexError ("Error : index out of range !")
            if index < 0 : 
                index += len (self) 
            if index == 0 : 
                ele.suivant, self.tete = self.tete, ele
            current = self.tete 
            compteur = 1
            while current.suivant != None and compteur != index : 
                current = current.suivant 
                compteur += 1
                if compteur == index : 
                    ele.suivant, current.suivant = current.suivant, ele
        else : 
            self.tete = ele 
    
    def supprimer (self, item) : 
        pass 
    
    def find (self, item) : 
        pass 
    
    def reverse (self) : 
        pass 
    
    def sort (self) : 
        pass
   
if __name__ == "__main__" :
    chaine = ListeChainee (Noeud (1, Noeud (2, Noeud (4, Noeud (5)))))
    chainette = ListeChainee (Noeud(0, Noeud(-1, Noeud(-2))))
    print ([1,2,3,4,55] + chaine)
    