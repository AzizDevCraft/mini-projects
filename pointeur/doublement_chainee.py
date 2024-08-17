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
            while current != None : 
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
    
    def __add__ (self, plus) : 
        if type(plus) == ListDoublementChainee and plus.tete != None: 
            if self.tete != None : 
                self.queue.suivant = plus.tete
                plus.tete.prec = self.queue
                self.queue = plus.queue
            else : 
                self.tete = plus.tete
                self.queue = plus.queue 
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
    
    def __setitem__ (self, index, new) : 
        if type (index) != int : 
            raise TypeError ("Erreur : TypeError (l'indice doit etre un entier)")  
        if not (-len(self) <= index < len (self)) : 
            raise IndexError ("Error : index out of range !")
        if index < 0 : 
            index += len (self) 
        current = self.tete
        for i in range (len (self)) : 
            if current.valeur == self [index] : 
                current.valeur = new
                break
            current = current.suivant
    
    def __delitem__ (self, index) : 
        if type (index) != int : 
            raise TypeError ("Erreur : TypeError (l'indice doit etre un entier)")  
        if not (-len(self) <= index < len (self)) : 
            raise IndexError ("Error : index out of range !")
        if index < 0 : 
            index += len (self) 
        if index == 0 : 
            self.tete = self.tete.suivant 
        elif index == len(self) - 1 :
            self.queue = self.queue.prec
            self.queue.suivant = None 
        else : 
            current = self.tete 
            while current.suivant != None and current.suivant.valeur != self [index] : 
                current = current.suivant 
            current.suivant = current.suivant.suivant 
            current.suivant.prec = current  
    
    def ajouter (self, value) : 
        ele = Noeud (value)
        if self.tete == None : 
            self.tete = ele
            self.queue = ele
        else : 
            self.queue.suivant = ele
            ele.prec = self.queue
            self.queue = ele

    def insertion (self, item, index = 0) : 
        ele = Noeud (item)
        if self.tete != None :
            if not (-len(self) -1 <= index <= len (self)) : 
                raise IndexError ("Error : index out of range !")
            if index < 0 : 
                index += (len (self) + 1)
            if index == 0 :
                ele.suivant  = self.tete
                self.tete.prec = ele 
                self.tete = ele
            elif index == len(self) : 
                self.ajouter (item)
            else : 
                current = self.tete 
                compteur = 1
                while current.suivant != None or compteur != index :
                    if compteur == index : 
                        ele.suivant  = current.suivant 
                        current.suivant.prec = ele
                        ele.prec = current
                        current.suivant = ele
                        break
                    current = current.suivant 
                    compteur += 1
        else : 
            self.tete = ele 
            self.queue = ele             
    
    def find (self, item) : 
        if self.tete == None or item not in self : 
            return repr (None)
        index = 0 
        for i in self : 
            if i == item : 
                return index
            index += 1 
    
    def reverse (self) : 
        new = ListDoublementChainee ()
        for i in range (len(self)-1, -1, -1) :
            new.ajouter (self[i])
        self.tete = new.tete
        self.queue = new.queue 
        return self 
    
if __name__ == "__main__" : 
    """cette espace est reserve au essai !"""
    chaine = ListDoublementChainee ()
    chaine.ajouter(5)
    chaine.ajouter(4)
    chaine.ajouter(3)
    chaine.ajouter(2)
    chaine.ajouter(1)
    chainette = ListDoublementChainee ()
    chainette.ajouter (6)
    chainette.ajouter (7)
    chainette.ajouter (8)
    chaine + chainette
    print (chaine)
    
    del chaine [3]
    print (chaine)
    
    
    
    