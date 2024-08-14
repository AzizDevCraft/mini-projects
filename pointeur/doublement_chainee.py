class Noeud : 
    
    def __init__ (self, valeur) : 
        self.valeur = valeur 
        self.suivant = None 
        self.prec = None 
        
class ListDoublementChainee : 
    
    def __init__ (self) :
        self.tete = None 
        self.queue = None 
        
    def __str__ (self) : 
        if self.tete == None :
            return repr(None)
        ch = ''
        for i in self : 
            ch += f"{i} -> "
        return ch [:-4] 
    
    def __iter__ (self) : 
        if self.tete != None : 
            current = self.tete 
            while current != self.queue.suivant : 
                yield current.valeur
                current = current.suivant  
    
    def __contains__ (self, value) : 
        if self.tete != None : 
            if self.tete.valeur == value  or self.queue.valeur == value: 
                return True
            for item in self : 
                if item == value : 
                    return True 
        return False 
    
    def __len__ (self) : 
        compteur = 0
        for i in self : 
            compteur += 1
        return compteur 
    
    def __add__ (self) : 
        pass
    
    def __radd__ (self) : 
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
            self.queue = ele
        else : 
            self.queue.suivant = ele
            self.queue = ele
    
    def insertion (self, index, valeur) : 
        pass 
    
    def find (self, item) : 
        pass 
    
    def reverse (self) : 
        pass 
    
if __name__ == "__main__" : 
    chaine = ListDoublementChainee ()
    chaine.ajouter(5)
    chaine.ajouter(4)
    chaine.ajouter(3)
    chaine.ajouter(2)
    chaine.ajouter(1)
    print (chaine)
    for i in chaine : 
        print (i)