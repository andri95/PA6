# Exception classes
class NotFoundException(Exception):
    pass

class ItemExistsException(Exception):
    pass

# bucketNode class has key, data and next pointer
class bucketNode:
    def __init__(self, key = None, data = None, next = None):
        self.key = key
        self.data = data
        self.next = next

class Bucket:
    def __init__(self):
        self.head = None
        self.tail = None
        self.curr = None
        self.size = 0

    # adds new node to back of list
    def insert(self, key, data):
        node = bucketNode(key, data)
        if self.head == None:
            self.head = node
            self.tail = node
            self.size += 1
            self.curr = self.head
        
        else:
            # if equal key is not found, add node
            # raises ItemExistsException if equal key is found
            try:
                self.find(key)
                raise ItemExistsException
            except NotFoundException:
                self.tail.next = node
                self.tail = node
                self.size += 1

    # O(n) removal, finds equal key and removes
    # raises ItemNotFoundException if corresponding key is not found
    def remove(self, key):

        if self.size == 0:
            raise NotFoundException

        if self.head.key == key:
            self.head = self.head.next
            self.size -= 1
            return True
        else:
            curr = self.head
            while curr.next != None:
                if curr.next.key == key:
                    curr.next = curr.next.next
                    self.size -= 1
                    return True
                else:
                    curr = curr.next
            raise NotFoundException

    # finds node with equal key, raises NotFoundException if eq key is not found
    def find(self, key):
        if self.size == 0:
            raise NotFoundException
            
        if self.head.key == key:
            return self.head
        else:
            curr = self.head
            while curr.next != None:
                if curr.next.key == key:
                    return curr.next
                else:
                    curr = curr.next
            raise NotFoundException

    # if equal key is found, update corresponding data
    # raises NotFoundException if eq key is not found
    def update(self, key, data):
        if self.size == 0:
            raise NotFoundException
            
        if self.head.key == key:
            self.head.data = data
            return
        else:
            curr = self.head
            while curr.next != None:
                if curr.next.key == key:
                    curr.next.data = data
                    return
                else:
                    curr = curr.next
            raise NotFoundException

    # checks if list contains node with input key
    def contains(self, key):
        try:
            self.find(key)
            return True
        except NotFoundException:
            return False

    # helper classes for rebuild() in HashMap
    def get_next(self):
        self.curr = self.curr.next

    def get_node(self):
        return self.curr

    def set_curr(self):
        self.curr = self.head

    def __len__(self):
        return self.size