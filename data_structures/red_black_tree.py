#-----------------------------------------------------
# fullname      :   s.m.mehrabul islam
# roll          :   sh-86
# email         :   smmehrabul-2017614964@cs.du.ac.bd
# institute     :   university of dhaka, bangladesh
# session       :   2017-2018
#-----------------------------------------------------

RED = 1
BLACK = 0

class Node():
    def __init__(self, value):
        self.value = value                            
        self.parent = None                      
        self.left = None                                
        self.right = None                     
        self.color = RED                        

class RedBlackTree():
    def __init__(self):
        self.NULL = Node(0)
        self.NULL.color = BLACK
        self.NULL.left = None
        self.NULL.right = None
        self.root = self.NULL

    def search_node(self, key):
        number_of_inspection = 0
        node = self.root
        while(node != self.NULL):
            number_of_inspection += 1
            if(node.value == key):
                return (node.value, number_of_inspection)
            elif(key < node.value):
                node = node.left
            else:
                node = node.right
        return (-1, -1)

    def insert_node(self, key):
        number_of_inspection = 0

        node = Node(key)
        node.parent = None
        node.value = key
        node.left = self.NULL
        node.right = self.NULL
        node.color = RED

        current = self.root
        parent = None
        while(current != self.NULL):       
            number_of_inspection += 1                
            parent = current
            if node.value < current.value :
                current = current.left
            else :
                current = current.right

        node.parent = parent                                 
        if(parent == None):                                   
            self.root = node
        elif(node.value < parent.value):                    
            parent.left = node
        else:
            parent.right = node

        if(node.parent == None):
            node.color = BLACK
            return (key, number_of_inspection)

        if(node.parent.parent == None):                
            return (key, number_of_inspection)

        number_of_inspection += self.balance_insertion(node)
        return (key, number_of_inspection)

    def balance_insertion(self, node):
        number_of_inspection = 0
        while node.parent.color == RED:                             # while parent red
            number_of_inspection += 1
            if node.parent == node.parent.parent.right:             # parent is right child
                u = node.parent.parent.left                    
                if u.color == RED:                                  # uncle node is red
                    u.color = BLACK                         
                    node.parent.color = BLACK
                    node.parent.parent.color = RED             
                    node = node.parent.parent                     
                else:                                               # uncle node is black
                    if node == node.parent.left:                  
                        node = node.parent
                        self.right_rotate(node)                
                    node.parent.color = BLACK
                    node.parent.parent.color = RED
                    self.left_rotate(node.parent.parent)
            else:                                                   # parent is left child
                u = node.parent.parent.right                   
                if u.color == RED:                                  # uncle node is red
                    u.color = BLACK                         
                    node.parent.color = BLACK
                    node.parent.parent.color = RED             
                    node = node.parent.parent                     
                else:                                               # uncle node is black
                    if node == node.parent.right:                 
                        node = node.parent
                        self.left_rotate(node)                 
                    node.parent.color = BLACK
                    node.parent.parent.color = RED
                    self.right_rotate(node.parent.parent)     
            if node == self.root:                                   # break on node == root 
                break
        self.root.color = BLACK
        return number_of_inspection                             


    def left_rotate(self, node):
        node_right = node.right                                      
        node.right = node_right.left                                 
        if(node_right.left != self.NULL):
            node_right.left.parent = node

        node_right.parent = node.parent                              
        if(node.parent == None):                          
            self.root = node_right                      
        elif node == node.parent.left:
            node.parent.left = node_right
        else :
            node.parent.right = node_right

        node_right.left = node
        node.parent = node_right

    def right_rotate(self, node):
        node_left = node.left                                     
        node.left = node_left.right                                
        if(node_left.right != self.NULL):
            node_left.right.parent = node

        node_left.parent = node.parent                       
        if(node.parent == None):                          
            self.root = node_left                                
        elif(node == node.parent.right):
            node.parent.right = node_left
        else:
            node.parent.left = node_left
        
        node_left.right = node
        node.parent = node_left

    def __print_helper(self, node, indent, last):
        if(node != self.NULL):
            print(indent, end=' ')
            if last:
                print ("R---", end= ' ')
                indent += "     "
            else:
                print("L---", end=' ')
                indent += "|    "
            s_color = "RED" if node.color == RED else "BLACK"
            print (str(node.value) + "(" + s_color + ")")
            self.__print_helper(node.left, indent, False)
            self.__print_helper(node.right, indent, True)

    def print_tree(self):
        self.__print_helper(self.root, "" , True)