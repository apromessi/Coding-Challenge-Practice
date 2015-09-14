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
# print "Print forwards list"
# linked.print_ll()
linked.reverse()
# print "Print reversed list"
# linked.print_ll()

# Merge sort with linked lists
# - given 1 linked list with two sorted parts
# - should be a constant space solution

two_in_one = LinkedList()
two_in_one.create_ll([1, 3, 4, 5, 2, 4, 7])

def merge(linked_list):
    # traverse until you find data that is lower than previous item
    a_head = linked_list.head
    current = a_head
    while current.data < current.next.data:
        current = current.next
    b_head = current.next
    
    # call it the new head
    # traverse both sections of the list at once and change pointers to order data

merge(two_in_one)
