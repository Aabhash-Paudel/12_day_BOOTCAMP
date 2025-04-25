class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def pop(self, data):
        current = self.head

        if current and current.data == data:
            self.head = current.next
            return

        prev = None
        while current and current.data != data:
            prev = current
            current = current.next

        if current is None:
            return

        prev.next = current.next

    def add(self, data, position):
        new_node = Node(data)

        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        current_position = 0

        while current and current_position < position - 1:
            current = current.next
            current_position += 1

        if current is None:
            self.append(data)
            return

        new_node.next = current.next
        current.next = new_node


if __name__ == "__main__":
    ll = LinkedList()

    ll.push(1)
    ll.push(2)
    ll.push(3)
    ll.push(4)
    ll.push(5)
    ll.push(6)
    ll.push(7)

    ll.display()
    ll.pop(3)
    ll.display()
    ll.add(2, 3)
    ll.display()
