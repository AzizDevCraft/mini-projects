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
    
    def pop (self) -> "Node" : 
        if self.top is None :
            raise ValueError ("Stack is empty") 
        poped_node = self.top
        self.top = self.top.next
        self.size -= 1 
        return poped_node
        
    def peek (self) -> Union [int, None] : 
        if self.top is not None : 
            return self.top.value
        return self.top
    
if __name__ == "__main__" : 
    pile = Stack ()
    
    print (pile.is_empty())
    pile.push (5)
    pile.push (10)
    pile.push (1)
    print (pile)
    print (pile.peek ())
    print (pile.pop ().value)
    print (pile.pop ().value)
    print (pile)
    print (pile.pop ().value)
    print (pile)