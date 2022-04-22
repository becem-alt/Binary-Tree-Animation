class Node:
    def __init__(self,data,left=None,right=None) -> None:
        self.data=data
        self.left=left
        self.right=right
    
    def insert(self,x):
        if x>self.data:
            if(self.right is None):
                self.right=Node(x)
            else:
                self.right.insert(x)
        else:
            if(self.left is None):
                self.left=Node(x)
            else:
                self.left.insert(x)
                
    def display(self):
        if(self.left is not  None):
            self.left.display()
        print(self.data)
        if(self.right is not None):
            self.right.display() 
        
            
                