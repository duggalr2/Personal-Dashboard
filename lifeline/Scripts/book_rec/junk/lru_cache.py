##TODO:
# Typically LRU cache is implemented using a doubly linked list and a hash map.
# Doubly Linked List is used to store list of pages with most recently used page at the start of the list.
# So, as more pages are added to the list, least recently used pages are moved to the end of the list with page
# at tail being the least recently used page in the list.
# Hash Map (key: page number, value: page) is used for O(1) access to pages in cache
#
# When a page is accessed, there can be 2 cases:
# 1. Page is present in the cache - If the page is already present in the cache, we move the page to the start of the list.
# 2. Page is not present in the cache - If the page is not present in the cache, we add the page to the list.
# How to add a page to the list:
#    a. If the cache is not full, add the new page to the start of the list.
#    b. If the cache is full, remove the last node of the linked list and move the new page to the start of the list.

class Node(object):

    def __init__(self, init_data):
        self.data = init_data
        self.next = None
        self.previous = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def get_prev(self):
        return self.previous

    def set_prev(self, data):
        self.previous = data

    def set_data(self, data):
        self.data = data

    def set_next(self, data):
        self.next = data

class DoubleLinkedList(object):

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get_self_head(self):
        return self.head

    def get_size(self):
        return self.size

    def add(self, item):
        if self.size == 60:
            return 'Cache is full'

        current = self.head
        while True:
            if current == None:
                temp = Node(item)
                temp.set_next(self.tail)
                temp.set_prev(self.head)
                self.head = temp
                self.size += 1
                break

            elif current.get_next() == None:
                temp = Node(item)
                temp.set_prev(self.head.get_prev())
                self.head.set_prev(temp)
                temp.set_next(self.head)
                self.head = temp
                self.size += 1
                break

            current = current.get_next()

    def __str__(self):
        current = self.head
        x = ''
        while current != None:
            x += str(current.get_data()) + ' '
            current = current.get_next()
        print(x.split())


class HashTable(object):

    def __init__(self): ##TODO: Set on final size;
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, data):
        hash_value = self.hash_function(key, len(self.slots))

        if self.slots[hash_value] == None:
            self.slots[hash_value] = key
            self.data[hash_value] = data
        else:
            if self.slots[hash_value] == key:
                self.data[hash_value] = data
            else:
                next_slot = self.rehash(hash_value, len(self.slots))
                while self.slots[next_slot] != None and self.slots[next_slot] != key:
                    next_slot = self.rehash(next_slot, len(self.slots))

                if self.slots[next_slot] == None:
                    self.slots[next_slot] = key
                    self.data[next_slot] = data
                else:
                    self.data[next_slot] = data

    def hash_function(self, key, size):
        return key % size

    def rehash(self, old_hash, size):
        return (old_hash + 1) % size

    def get(self, key):
        start_slot = self.hash_function(key, len(self.slots))
        data = None
        stop = False
        found = False
        position = start_slot

        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.slots))
                if position == start_slot:
                    stop = True
        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)

    def __in__(self, key):
        value = self.hash_function(key, self.size)
        if self.slots[value] == key:
            return True
        current = value + 1
        while current != value:
            if current == (self.size - 1):
                current = 0
                continue
            elif self.slots[current] == key:
                return True
            current += 1
        return False

    def delete(self, key):
        value = self.hash_function(key, self.size)
        if self.slots[value] == key:
            self.slots[value] = None
            self.data[value] = None
            return True
        current = value + 1
        while current != value:
            if self.slots[value] == key:
                self.slots[value] = None
                self.data[value] = None
                break
            elif current == (self.size - 1):
                current = 0
                continue
            elif self.slots[current] == key:
                self.slots[current] = None
                self.data[current] = None
                break
            current += 1

from functools import lru_cache

@lru_cache(maxsize=100)
def fac(x):
    return x**x

print(fac(5000))





