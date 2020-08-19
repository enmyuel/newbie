# studied from Youtube "Joe James" channel

class Node:
    def __init__(self, data, node=None):
        self.data = data
        self.next_node = node
    def get_next_node(self):
        return self.next_node
    def set_next_node(self, node):
        self.next_node = node
    def get_data(self):
        return self.data
    def set_data(self, data):
        self.data = data

class LinkedList():
    def __init__(self, root=None):
        self.root = root
        self.size = 0
    def get_size(self):
        return self.size
    def add(self, data):
        new_node = Node(data, self.root)
        self.root = new_node
        self.size += 1
    def remove(self, data):
        this_node = self.root
        prev_node = None
        while this_node:
            if this_node.get_data() == data:
                if prev_node:
                    prev_node.set_next_node(this_node.get_next_node())
                else:
                    self.root = this_node.get_next_node()
                self.size -= 1
                return True
            else:
                prev_node = this_node
                this_node = this_node.get_next_node()
        return False
    def find(self, data):
        this_node = self.root
        while this_node:
            if this_node.get_data() == data:
                return True
            else:
                this_node = this_node.get_next_node()
        return None
    def print(self):
        this_node = self.root
        while this_node:
            print(this_node.get_data())
            this_node = this_node.get_next_node()


myList = LinkedList()
myList.add(10)
myList.add(20)
myList.add(40)
myList.add(30)

myList.print()
print(myList.find(10))
print(myList.find(15))
myList.remove(20)

myList.print()