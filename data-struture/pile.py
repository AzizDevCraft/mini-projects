# pile = stack 
from dataclasses import dataclass
from typing import Union

@dataclass
class Node : 
    value : int
    next : "Node" = None 
    
@dataclass
class Stack : 
    top : "Node" = None 
    size : int = 0
    
    def __len__ (self) -> int : 
        return self.size
    
    def is_empty (self) -> bool : 
        return self.top is None
    
    def push (self, value : int) :
        node = Node (value)
        if self.top is not None : 
            self.top, self.top.next = node, self.top 
        else : 
            self.top = node    
        self.size += 1
    
    def pop (self) -> Union ["Node", None] : 
        if self.top is not None : 
            poped_node = self.top
            if self.size > 1 : 
                self.top, self.top.next = self.top.next, self.top.next.next
            else : 
                self.top = None 
            self.size -= 1 
            return poped_node
        return None
    
    def peek (self) -> "Node" : 
        pass  
    
if __name__ == "__main__" : 
    pile = Stack ()
    
    print (pile.is_empty())
    pile.push (5)
    pile.push (10)
    pile.push (1)
    print (pile)
    print (pile.pop ().value)
    print (pile.pop ().value)
    print (pile)
    print (pile.pop ().value)
    print (pile)
    print (pile.pop ())