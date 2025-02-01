# stack 
from dataclasses import dataclass

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
        pass
    
    def pop (self) -> "Node" : 
        pass
    
    def peek (self) -> "Node" : 
        pass  