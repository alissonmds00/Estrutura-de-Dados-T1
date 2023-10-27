class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SortedLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)

        if self.head is None or data < self.head.data:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next is not None and current.next.data < data:
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def search(self, data):
        current = self.head
        while current is not None:
            if current.data == data:
                return True
            current = current.next
        return False

    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Exemplo de uso:
linked_list = SortedLinkedList()
linked_list.insert("banana")
linked_list.insert("apple")
linked_list.insert("cherry")
linked_list.insert("date")
linked_list.insert("Alisson")

linked_list.display() 
