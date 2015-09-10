class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def create_ll(self, data_points=[]):
        self.head = Node(data_points[0])
        current = self.head
        for data in data_points[1:]:
            current.next = Node(data)
            current = current.next # may get attribute error



    def print_ll(self):
        current = self.head
        while current.next:
            print current.data
            current = current.next

    def reverse(self):
        current = self.head
        previous = None
        while current.next:
            previous = current
            current = current.next
            current.next = previous
        self.head = current

