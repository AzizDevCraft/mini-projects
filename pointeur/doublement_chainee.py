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
    
    def __add__ (self, plus) : 
        if type(plus) == ListDoublementChainee and plus.tete != None: 
            if self.tete != None : 
                self.queue.suivant = plus.tete
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
        pass 
    
    def ajouter (self, value) : 
        ele = Noeud (value)
        if self.tete == None : 
            self.tete = ele
            self.queue = ele
        else : 
            self.queue.suivant = ele
            self.queue = ele
    
    def insertion (self, item, index = 0) : 
        ele = Noeud (item)
        if self.tete != None :
            if not (-len(self) -1 <= index <= len (self)) : 
                raise IndexError ("Error : index out of range !")
            if index < 0 : 
                index += (len (self) + 1)
            if index == 0 :
                ele.suivant, self.tete = self.tete, ele
            elif index == len(self) : 
                self.queue.suivant = ele
                self.queue = ele 
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
        pass 
    
if __name__ == "__main__" : 
    chaine = ListDoublementChainee ()
    chaine.ajouter(5)
    chaine.ajouter(4)
    chaine.ajouter(3)
    chaine.ajouter(2)
    chaine.ajouter(1)
    print (chaine)
    chainette = ListDoublementChainee ()
    chainette.ajouter (6)
    chainette.ajouter (7)
    chainette.ajouter (8)
    print (chainette)
    print (chaine + chainette)
    
    