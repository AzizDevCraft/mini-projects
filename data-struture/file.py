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
    
    def enqueue (self, value : int) : 
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
    
    def peek (self) -> Union [int, None] : 
        pass 
    
    def is_empty (self) -> bool :
        pass
    
if __name__ == "__main__" : 
    
    file = Queue ()
    file.enqueue (5)
    file.enqueue (15)
    print(file)
    print (file.dequeue ().value)
    print (file.dequeue ().value)
    print (file)