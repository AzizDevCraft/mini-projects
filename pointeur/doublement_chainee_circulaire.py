class Noeud : 
    
    def __init__ (self, valeur) : 
        self.valeur = valeur 
        self.suivant = None 
        self.prec = None 

class ListDoublementChaineeCirculaire : 
    
    def __init__ (self, tete = None) : 
        self.tete = None 
        self._lengh = 0
        
    def __str__ (self) : 
        if self.tete == None : 
            return repr (None)
        ch = ""
        for i in self : 
            ch += f"{i.valeur} -> "
        return ch [:-4]
                
    def __iter__ (self) : 
        current = self.tete
        i = 0 
        while i < self._lengh : 
            yield current
            current = current.suivant
            i += 1
    
    def __contains__ (self, item) : 
        for i in self : 
            if i.valeur == item : 
                return True
        return False  
    
    def __len__ (self) : 
        return self._lengh 
    
    def __add__ (self, plus) : 
        pass
    
    def _radd__ (self, plus) : 
        pass
    
    def __getitem__ (self, index) : 
        if type (index) != int : 
            raise TypeError ("Erreur : TypeError (l'indice doit etre un entier)")  
        if not (-len(self) <= index < len (self)) : 
            raise IndexError ("Error : index out of range !")
        if index < 0 : 
            index += len (self) 
        for item in self : 
            if self.find (item.valeur) == index : 
                return item.valeur 
    
    def __setitem__ (self, index, new) : 
        pass
    
    def __delitem__ (self, index) : 
        pass
    
    def ajouter (self, value) : 
        ele = Noeud (value)
        if self.tete == None :
            self.tete = ele
            ele.suivant = ele
            ele.prec = ele
        else : 
            self.tete.prec.suivant = ele
            ele.suivant = self.tete
            ele.prec = self.tete.prec
            self.tete.prec = ele
        self._lengh += 1 
    
    def insert (self, value, index = 0) : 
        pass
    
    def find (self, item) : 
        if self.tete == None or item not in self : 
            return repr (None)
        index = 0 
        for i in self : 
            if i.valeur == item : 
                return index
            index += 1 
    
    def reverse (self) : 
        pass 
    
if __name__ == "__main__" : 
    """espace reserve au testes !"""
    liste = ListDoublementChaineeCirculaire ()
    liste.ajouter (1)
    liste.ajouter (2)
    liste.ajouter (0)
    liste.ajouter (3)
    liste.ajouter (5) 
    print (liste)
    print (len(liste))
    print (0 in liste)
    print (4 in liste)
    print (liste[2])