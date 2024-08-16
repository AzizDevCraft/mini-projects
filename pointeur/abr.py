class cellule : 
    def __init__ (self, valeur) : 
        self.valeur = valeur
        self.gauche = None 
        self.droite = None 
        self.pere = None 
        
class Abr : 
    
    def __init__ (self, racine = None) : 
        self.racine = racine
    
    def afficher (self, n) :
        if n == None : 
            return ""
        return self.afficher (n.gauche) + str (n.valeur) + " " + self.afficher (n.droite)
    
    def __iter__ (self) : 
        """parcourt infixe"""
    
    
    def ajouter (self, valeur) : 
        ele = cellule (valeur)
        if self.racine == None : 
            self.racine = ele
        else : 
            current = self.racine
            InsertionCheck = False 
            while not (InsertionCheck) : 
                if current.valeur < valeur : 
                    if current.droite == None : 
                        current.droite = ele
                        ele.pere = current 
                        InsertionCheck = True 
                    else : 
                        current = current.droite 
                else : 
                    if current.gauche == None : 
                        current.gauche = ele
                        ele.pere = current 
                        InsertionCheck = True
                    else : 
                        current = current.gauche
    
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
    
if __name__ == "__main__" : 
    arbre = Abr ()
    arbre.ajouter (6)
    arbre.ajouter (4)
    arbre.ajouter (2)
    arbre.ajouter (5)
    arbre.ajouter (9)
    arbre.ajouter (3)
    print (arbre.afficher (arbre.racine))