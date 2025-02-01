# file = Queue 
from dataclasses import dataclass 
from typing import Union 

@dataclass
class Node : 
    value : int
    next : "Node" = None
    
@dataclass 
class Queue : 
    tete : "Node" = None
    queue : "Node" = None
    size : int = 0
    
    def __len__ (self) -> int : 
        return self.size
    
    def enqueue (self, value) : 
        pass 
    
    def dequeue (self) -> "Node" : 
        pass
    
    def peek (self) -> Union [int, None] : 
        pass 
    
    def is_empty (self) -> bool :
        pass