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
        pass 
    
    def __contains__ (self, value) : 
        pass 
    
    def __len__ (self) : 
        pass 
    
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
    
    def ajouter (self, valeur) : 
        pass
    
    def insertion (self, index, valeur) : 
        pass 
    
    def find (self, item) : 
        pass 
    
    def reverse (self) : 
        pass 