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
        if type (index) != int : 
            raise TypeError ("Erreur : TypeError (l'indice doit etre un entier)")  
        if not (-len(self) <= index < len (self)) : 
                raise IndexError ("Error : index out of range !")
        if index < 0 : 
                index += len (self) 
        for item in self : 
            if self.find (item) == index : 
                return item
             
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
            if not (-len(self) -1 <= index <= len (self)) : 
                raise IndexError ("Error : index out of range !")
            if index < 0 : 
                index += (len (self) + 1) 
            if index == 0 : 
                ele.suivant, self.tete = self.tete, ele
            elif index == len(self): 
                pointeur = self.tete 
                for i in range (len (self)-1) : 
                    pointeur = pointeur.suivant 
                pointeur.suivant = ele
            else : 
                current = self.tete 
                compteur = 1
                while current.suivant != None or compteur != index :
                    if compteur == index : 
                        ele.suivant, current.suivant = current.suivant, ele 
                        break
                    current = current.suivant 
                    compteur += 1
                    
        else : 
            self.tete = ele 
    
    def supprimer (self, item) : 
        try : 
            assert self.tete != None and item in self 
        except AssertionError : 
            print ("Erreur : l'element que vous voulez supprimez n'existe pas !") 
        else : 
            if self.tete.valeur == item : 
                self.tete = self.tete.suivant 
            else :
                current = self.tete 
                while current.suivant != None and current.suivant.valeur != item : 
                    current = current.suivant 
                current.suivant = current.suivant.suivant 
                    
    
    def find (self, item) : 
        if self.tete == None or item not in self : 
            return repr (None)
        index = 0 
        for i in self : 
            if i == item : 
                return index
            index += 1
    
    def reverse (self) : 
        new = ListeChainee ()
        for i in range (len(self)-1, -1, -1) :
            new.ajouter (self[i])
        return new 
            

if __name__ == "__main__" :
    """cette espace est réserver pour les testes"""
    chaine = ListeChainee (Noeud (1, Noeud (2, Noeud (4, Noeud (5)))))
    chainette = ListeChainee (Noeud(0, Noeud(-1, Noeud(-2))))
    chaine + chainette
    print (chaine)
    print (chaine.reverse ())
    print ([1,2,3] + chaine)
    
    