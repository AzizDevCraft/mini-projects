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
        pass 
    
    def __len__ (self) : 
        return self._lengh 
    
    def __add__ (self, plus) : 
        pass
    
    def _radd__ (self, plus) : 
        pass
    
    def __getitem__ (self, index) : 
        pass
    
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
    
    def find (self, value) : 
        pass 
    
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
    for i in liste : 
        print (i.valeur)
        
    print (liste)