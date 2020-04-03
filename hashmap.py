from bucket import *

# key class used to hash/compare keys
class Key:
    def __init__(self, key):
        self.key = key

    def __hash__(self):
        return (self.key ^ 17) * 7

    def __eq__(self, other):
        return self.key == other.key

class HashMap:
    def __init__(self):
        self.capacity = 8
        self.max = 1.2
        self.arr = [Bucket() for _ in range(self.capacity)]
        self.size = 0

    # checks if items in array has reached 120% of bucket count
    def check_size(self):
        if self.size / self.capacity >= self.max:
            self.rebuild()

    # resizes array
    def rebuild(self):
        old_cap = self.capacity
        self.capacity = self.capacity * 2
        temp_arr = [Bucket() for _ in range(self.capacity)]

        # all items from self.arr copied to temp_arr,
        # keys re-hashed in relation to new capacity
        # get_node() and get_next() used to iterate through buckets
        for bucket in range(old_cap):
            while self.arr[bucket].get_node() != None:
                node = self.arr[bucket].get_node()
                compr = self.compress(hash(node.key))
                temp_arr[compr].insert(node.key, node.data)
                self.arr[bucket].get_next()
            self.arr[bucket].set_curr()
        self.arr = temp_arr

    # key is always hashed and compressed to insert/update/search
    # the right Bucket
    def insert(self, key, data):
        self.check_size()
        myKey = Key(key)
        compr = self.compress(hash(myKey))
        self.arr[compr].insert(myKey, data)
        self.size += 1            

    def find(self, key):
        myKey = Key(key)
        compr = self.compress(hash(myKey))
        return self.arr[compr].find(myKey)

    def remove(self, key):
        myKey = Key(key)
        compr = self.compress(hash(myKey))
        if self.arr[compr].remove(myKey) == True:
            self.size -= 1
        
    # compression helper function
    def compress(self, key):
        return key % self.capacity

    def __len__(self):
        return self.size