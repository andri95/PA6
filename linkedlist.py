
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

    def find(self, data):
        flag = False
        curr = self.head
        while curr != None:
            if curr.data == data:
                curr.reveal = True
                flag = True
            curr = curr.next
        return flag

    def reveal_status(self):
        curr = self.head
        while curr != None:
            if curr.reveal == False:
                return False
            curr = curr.next
        return True

    def reveal_all(self):
        curr = self.head
        while curr != None:
            curr.reveal = True
            curr = curr.next

    # returns size of list
    def get_size(self):
        return self.size

    # returns contents of list in string format
    def __str__(self):
        curr = self.head
        ret_str = ''
        while curr != None:
            if curr.reveal == True:
                ret_str += str(curr.data)
            else:
                ret_str += '-' 
            curr = curr.next
        return ret_str