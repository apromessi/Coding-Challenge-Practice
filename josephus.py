class Node(object):
    """Doubly-linked node."""

    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

    def remove(self):
        self.prev.next = self.next
        self.next.prev = self.prev

    def __repr__(self):
        return "<Node prev=%s data=%s next=%s>" % (self.prev.data, self.data, self.next.data)


def find_survivor(num_people, kill_every):
    # """Given num_people in a circle, kill everyone [kill_every]th person, return survivor.

    #     >>> find_survivor(4, 2)
    #     1

    #     >>> find_survivor(41, 3)
    #     31

    # As a sanity case, if never skip anyone, the last person will be our survivor:

    #     >>> find_survivor(10, 1)
    #     10
    # """

    head = Node(1)
    prev = head
    for num in range(1, num_people+1):
        new_node = Node(num, prev)
        print new_node, "new_node"
        prev.next = new_node
        prev = new_node
    head.prev = prev

    current = head
    while current.next or current.prev:
        for i in range(kill_every):
            current = current.next
            print current, "current"
        kill = current
        print kill, "kill"
        current = current.next
        kill.remove()
        
    return current

find_survivor(10, 3)
# find_survivor(41, 3)



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TEST PASSED. W00T!\n"
