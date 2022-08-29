#################################################################################
##
##
##################################################################################

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList():
     
    def __init__(self):
        self.head = None

    def add_node(self, data):
        new_node = Node(data)
        
        if not self.head: #if listedlist is empty
            self.head = new_node
        else:
            last_node = self.head
            while last_node.next is not None:
                last_node = last_node.next
            last_node.next = new_node
   
    @staticmethod
    def reverse_linkedlist(head):
        
        if head is None or head.next is None:
            return head
        
        new_head = linkedlist.reverse_linkedlist(head.next)
        next_head = head.next
        next_head.next = head
        head.next = None
        return new_head
        
    
    def display_linkedlist(self):
        if not self.head:
            print('Linkedlist is empty')
        else:
            next_node = self.head
            while next_node:
                if next_node.next is None:
                    print(f'{next_node.data} -> NULL')
                else:
                    print(f'{next_node.data} ->', end = ' ')
                next_node = next_node.next
    
linkedlist = LinkedList()
linkedlist.display_linkedlist()
linkedlist.add_node(10)
linkedlist.add_node(20)
linkedlist.add_node(30)
linkedlist.add_node(40)
linkedlist.add_node(50)
linkedlist.display_linkedlist()
linkedlist.head = linkedlist.reverse_linkedlist(linkedlist.head)
linkedlist.display_linkedlist()