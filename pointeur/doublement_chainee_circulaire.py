class Noeud : 
    
    def __init__ (self, valeur) : 
        self.valeur = valeur 
        self.suivant = None 
        self.prec = None 

class ListDoublementChaineeCirculaire : 
    
    def __init__ (self, tete = None) : 
        self.tete = None 
        self._lengh = 0
        
    def __str__ (self) : 
        if self.tete == None : 
            return repr (None)
        ch = ""
        for i in self : 
            ch += f"{i.valeur} -> "
        return ch [:-4]
                
    def __iter__ (self) : 
        current = self.tete
        i = 0 
        while i < self._lengh : 
            yield current
            current = current.suivant
            i += 1
    
    def __contains__ (self, item) : 
        for i in self : 
            if i.valeur == item : 
                return True
        return False  
    
    def __len__ (self) : 
        return self._lengh 
    
    def __add__ (self, plus) : 
        if type(plus) == ListDoublementChaineeCirculaire and plus.tete != None: 
            if self.tete != None : 
                self._lengh += len(plus)
                self.tete.prec.suivant = plus.tete
                plus.tete.prec.prec = self.tete 
                plus.tete.prec = self.tete.prec
            else : 
                self.tete = plus.tete
        else : 
            self.ajouter (plus)    
        return self
    
    def _radd__ (self, plus) : 
        self.insert (plus)   
        return self 
    
    def __getitem__ (self, index) : 
        if type (index) != int : 
            raise TypeError ("Erreur : TypeError (l'indice doit etre un entier)")  
        if not (-len(self) <= index < len (self)) : 
            raise IndexError ("Error : index out of range !")
        if index < 0 : 
            index += len (self) 
        for item in self : 
            if self.find (item.valeur) == index : 
                return item.valeur 
    
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
            self.tete.suivant.prec = self.tete.prec
            self.tete = self.tete.suivant
            self._lengh -= 1
        elif index == len(self) - 1 :
            self.tete.prec = self.tete.prec.prec
            self.tete.prec.suivant = self.tete 
            self._lengh -= 1
        else : 
            current = self.tete 
            while current.suivant != None and current.suivant.valeur != self [index] : 
                current = current.suivant 
            current.suivant = current.suivant.suivant
            current.suivant.prec = current  
            self._lengh -= 1        
    
    def ajouter (self, value) : 
        ele = Noeud (value)
        if self.tete == None :
            self.tete = ele
            ele.suivant = ele
            ele.prec = ele
        else : 
            self.tete.prec.suivant = ele
            ele.suivant = self.tete
            ele.prec = self.tete.prec
            self.tete.prec = ele
        self._lengh += 1 
    
    def insert (self, item, index = 0) : 
        ele = Noeud (item)
        if self.tete != None :
            if not (-len(self) -1 <= index <= len (self)) : 
                raise IndexError ("Error : index out of range !")
            if index < 0 : 
                index += (len (self) + 1)
            if index == 0 :
                ele.suivant  = self.tete
                ele.prec = self.tete.prec
                self.tete.prec = ele 
                self.tete = ele
            elif index == len(self) : 
                self.ajouter (item)
                self._lengh -= 1
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
            ele.suivant = ele
            ele.prec = ele
        self._lengh += 1
    
    def find (self, item) : 
        if self.tete == None or item not in self : 
            return repr (None)
        index = 0 
        for i in self : 
            if i.valeur == item : 
                return index
            index += 1 
    
    def reverse (self) : 
        new = ListDoublementChaineeCirculaire ()
        for i in range (len(self)-1, -1, -1) :
            new.ajouter (self[i])
        self.tete = new.tete
        return self  
    
if __name__ == "__main__" : 
    """espace reserve au testes !"""
    liste = ListDoublementChaineeCirculaire ()
    liste.ajouter (1)
    liste.ajouter (2)
    liste.ajouter (0)
    liste.ajouter (3)
    liste.ajouter (5) 
    chaine = ListDoublementChaineeCirculaire ()
    chaine.ajouter (6)
    chaine.ajouter (7)
    chaine.ajouter (8)
    liste + chaine
    print (liste)
    for i in liste : 
        print (i.valeur)