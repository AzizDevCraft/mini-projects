class Noeud : 
    
    def __init__ (self, valeur) : 
        self.valeur = valeur 
        self.suivant = None 
        self.prec = None 
        
class ListDoublementChainee : 
    
    def __init__ (self) :
        self.tete = None 
        self.queue = None  