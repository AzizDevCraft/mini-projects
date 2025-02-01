# file = Queue 
from dataclasses import dataclass 
from typing import Union, Any

@dataclass
class Node : 
    value : Any
    next : "Node" = None
    
@dataclass 
class Queue : 
    tete : "Node" = None
    queue : "Node" = None
    size : int = 0
    
    def __len__ (self) -> int : 
        return self.size
    
    def enqueue (self, value : Any) : 
        new_node = Node (value)
        if self.tete is not None : 
            self.queue.next = self.queue = new_node
        else : 
            self.tete = self.queue = new_node
        self.size += 1 
    
    def dequeue (self) -> "Node" :
        if self.tete is None : 
            raise ValueError ("Queue is empty") 
        poped_node = self.tete
        self.tete = self.tete.next
        
        if self.tete is None : 
            self.queue = None 
        self.size -= 1 
        
        return poped_node
    
    def peek (self) -> Union [Any, None] : 
        if self.tete is None : 
            return None
        return self.tete.value
    
    def is_empty (self) -> bool :
        return self.tete is None 
    
if __name__ == "__main__" : 
    
    file = Queue ()
    file.enqueue (5)
    file.enqueue (15)
    print (file.peek ())
    print(file)
    print (file.dequeue ().value)
    print (file.dequeue ().value)
    print (file)