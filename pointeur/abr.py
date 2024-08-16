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
        current = self.racine
        while current != None and current.valeur != item : 
            if item < current.valeur : 
                current = current.gauche
            else : 
                current = current.droite 
        return current 

    def __contains__ (self, item) :
        resultat = self.find (item)
        if type (resultat) == cellule : 
            return True 
        return False 
    
    def maxi (self, noeud) : 
        current = noeud 
        while current.droite != None : 
            current = current.droite 
        return current 
    
    def mini (self, noeud) : 
        current = noeud 
        while current.gauche != None :
            current = current.gauche 
        return current 
    
    def sucesseur (self, noeud) : 
        if noeud.droite != None : 
            return self.mini(noeud.droite)
        else : 
            current = noeud 
            while current.pere.valeur < noeud.valeur : 
                current = current.pere
            return current.pere 
    
    def supression (self) : 
        pass 
    
    def mirroir (self, noeud) : 
        if noeud != None : 
            self.mirroir (noeud.gauche)
            self.mirroir (noeud.droite)
            noeud.gauche, noeud.droite = noeud.droite, noeud.gauche
    
    def sum_feuille (self, noeud) : 
        if noeud == None : 
            return 0 
        elif noeud.gauche == None and noeud.droite == None :
            return noeud.valeur 
        return self.sum_feuille (noeud.gauche) + self.sum_feuille (noeud.droite)          
    
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
    arbre.mirroir (arbre.racine)
    print (arbre.afficher (arbre.racine))
    print (arbre.sum_feuille (arbre.racine))