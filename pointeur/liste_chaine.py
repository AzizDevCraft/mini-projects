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
    pass

if __name__ == "__main__" : 
    chaine = Noeud (5)
    print (chaine)