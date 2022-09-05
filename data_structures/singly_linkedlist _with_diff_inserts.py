#################################################################################
## Category: LinkedList
## Tile: Implement different type of add opeation (add first/last/middle after certion element or index position) in singly linked list
##################################################################################

#CREATE NODE
class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None

        
#Create LINKED LIST TO CREATE/DELETE/MODIFY MUTIPLE NODES
class LinkedList:
    def __init__(self):
        self.head = None
    
    #Add new node at the beginning of the linkedlist
    def add_begin(self, data):
        
        """
          Step1: Create a new node with data value and ref is none
          Step2: Update new node ref address to head(first) node address
          Step3: Update head(first) node address to new node address
        """
        
        new_node = Node(data) 
        new_node.ref = self.head
        self.head = new_node
        
        
    #Add new node at the end of the linkedlist  
    def add_end(self, data):

        """
          Step1: Create a new node with data value and ref is none
          Step2: Check If linked list is empty then new node will be only one/fisrt node in linked list.
          Step3: Else need to capture the address of the last node
          step4: Update last node ref address to newly created node address 
        """
        
        new_node = Node(data) 
        
        if self.head is None:
            self.head = new_node
        else:
            pointer_node =  self.head 
            while pointer_node.ref is not None:
                pointer_node = pointer_node.ref
            pointer_node.ref = new_node
            
            
    #Insert new node between two nodes which is right after a node and find the node by value in linkedlist  
    def add_after_node_find_by_value(self, data, x):
        
        """
             Step1: Need to find the node address wich hold the x value
             Step2: If x value not present in linkedlist that need to inform to print not found
             Step3: If x value present then create new node with data value and ref address null
             Step4: Update new node ref address to next node address
             Step5: Update previous node ref address to new node address
        """
        pointer_node = self.head
        while pointer_node is not None:
            if pointer_node.data == x:
                break
            pointer_node = pointer_node.ref
        if pointer_node is None: 
            print("Unable to find the x value in list of nodes")
        else:
            new_node = Node(data) 
            new_node.ref = pointer_node.ref
            pointer_node.ref = new_node
    
    
    #Insert new node between two nodes which is right before a node and find the node by value in linkedlist  
    def add_before_node_find_by_value(self, data, x):
        
        """
            Step1: While adding new node before first node that case head address need to point to new node
            Step2: While adding new node before between two nodes(rest positions) that case logic will be different
            Step3: Need to capture the previous node address if next node value equal to x
            Step4: Update new node ref address to next node address
            steop5: Update previous node ref address to new node address
        """

        if self.head is None:
            print('Linked list is empty')
            return
        
        if self.head.data == x:
            self.add_begin(data)
            
        else:
            pointer_node = self.head
            while pointer_node.ref is not None:
                if pointer_node.ref.data == x:
                    break
                pointer_node = pointer_node.ref
            if pointer_node.ref is None:
                print('Unable to find x value in linkedlist')
            else:
                new_node = Node(data)
                new_node.ref = pointer_node.ref
                pointer_node.ref = new_node
            
            
    #Insert new node between two nodes which is right after a node and find the node by position in linkedlist  
    def add_after_node_find_by_position(self, data, position): #considering head node position starting from 1
        
        """
             Step1: Need to find the node address wich hold the x value
             Step2: If x value not present in linkedlist that need to inform to print not found
             Step3: If x value present then create new node with data value and ref address null
             Step4: Update new node ref address to next node address
             Step5: Update previous node ref address to new node address
        """
        current_position = 1
        pointer_node = self.head
        while pointer_node is not None:
            if current_position == position:
                break
            pointer_node = pointer_node.ref
            current_position += 1
        if pointer_node is None: 
            print(f"Unable to find the position {position} in list of nodes")
        else:
            new_node = Node(data) 
            new_node.ref = pointer_node.ref
            pointer_node.ref = new_node
         
        
    #Insert new node between two nodes which is right before a node and find the node by position in linkedlist  
    def add_before_node_find_by_position(self, data, position): #considering head node position starting from 1
        
        """
            Step1: While adding new node before first node that case head address need to point to new node
            Step2: While adding new node before between two nodes(rest positions) that case logic will be different
            Step3: Need to capture the previous node address if next node value equal to x
            Step4: Update new node ref address to next node address
            steop5: Update previous node ref address to new node address
        """

        if self.head is None:
            print('Linked list is empty')
            return
        
        if position == 1:
            self.add_begin(data)
            
        else:
            pointer_node = self.head
            current_position = 2
            while pointer_node.ref is not None:
                if current_position == position:
                    break
                pointer_node = pointer_node.ref
                current_position += 1
            if pointer_node.ref is None:
                print('Unable to find position {position} in linkedlist')
            else:
                new_node = Node(data)
                new_node.ref = pointer_node.ref
                pointer_node.ref = new_node
            
     
    #Insert new node to empty linkedlist else not
    def insert_if_empty(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print('Linkedlist is not empty!')
    
    
    #method to traverse the linked list
    def display_linkedlist(self):
        
        """
          Step1: Check if Linked is empty
          Step2: Else Linkedlist is not empty
          Step3: Print the data from first node and check if next node is not null 
        """
        
        pointer_node =  self.head
        if pointer_node is None: #if linked list is emepty
            print('Linked list is empty')
        else: #if linked list is not empty
            while pointer_node is not None:
                print(pointer_node.data, "--->", end = ' ')
                pointer_node = pointer_node.ref
  
        
linked_list = LinkedList()
linked_list.add_begin(10)
# linked_list.add_end(100)
# linked_list.add_begin(10)
# linked_list.add_before_node_find_by_value(20, 10)
# linked_list.add_before_node_find_by_value(30, 10)
# linked_list.add_before_node_find_by_value(30, 100)
# linked_list.add_after_node_find_by_position(100, 1)
# linked_list.add_before_node_find_by_position(200, 2)
linked_list.add_before_node_find_by_value(20,10)
linked_list.add_before_node_find_by_value(30,10)

linked_list.display_linkedlist()
