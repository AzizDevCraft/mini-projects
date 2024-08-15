class cellule : 
    def __init__ (self, valeur) : 
        self.valeur = valeur
        self.gauche = None 
        self.droite = None 
        self.pere = None 
        
class Abr : 
    
    def __init__ (self, racine = None) : 
        self.racine = racine
        
    def __str__ (self) : 
        pass 
    
    def __iter__ (self) : 
        """parcourt infixe"""
    
    
    def find (self, item) :
        pass 
    
    def __contains__ (self, item) :
        pass
    
    def maxi (self, noeud) : 
        pass
    
    def mini (self, noeud) : 
        pass 
    
    def sucesseur (self) : 
        pass 
    
    def supression (self) : 
        pass 
    
    def mirroir (self) : 
        pass 
    
    def sum_feuille (self) : 
        pass 
    
    def sum_noeud (self) : 
        pass 
    
    def is_abr (self) : 
        pass 