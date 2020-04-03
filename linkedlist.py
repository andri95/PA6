
# Node model class
class Node:

    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next
        self.reveal = False

class LinkedList:
    
    # head indicates start of list, tail indicates end of list
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # adds new node to back of list
    def push_back(self, data):

        node = Node(data)

        if self.head == None:
            self.head = node
        
        else:
            self.tail.next = node

        self.tail = node
        self.size += 1

    # adds new node at the front of list
    def push_front(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node

        else:
            node.next = self.head
            self.head = node

        self.size += 1

    # removes first node, returns node.data
    def pop_front(self):
        if self.size == 0:
            return None
        else:
            curr = self.head
            self.head = self.head.next
            curr.next = None
            self.size -= 1
            return curr.data

    # returns size of list
    def get_size(self):
        return self.size

    # returns contents of list in string format
    def __str__(self):
        curr = self.head
        ret_str = ''
        while curr != None:
            if curr.reveal == True:
                ret_str += str(curr.data) + ' '
            else:
                ret_str += '- ' 
            curr = curr.next
        return ret_str