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
            current = current.next

    def print_ll(self):
        current = self.head
        while current:
            print current.data
            current = current.next

    def reverse(self):
        previous = self.head
        current = previous.next
        previous.next = None
        next = current.next
        while next:
            current.next = previous
            previous = current
            current = next
            next = current.next
        current.next = previous
        self.head = current
        
linked = LinkedList()
linked.create_ll([1, 2, 3, 4, 5, 6, 7])
print "Print forwards list"
linked.print_ll()
linked.reverse()
print "Print reversed list"
linked.print_ll()
