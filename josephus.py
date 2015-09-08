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
        if self.prev and self and self.next:
            return "<Node prev=%s data=%s next=%s>" % (self.prev.data, self.data, self.next.data)
        elif self.prev and self:
            return "<Node prev=%s data=%s next=%s>" % (self.prev.data, self.data, "None")
        elif self and self.next:
            return "<Node prev=%s data=%s next=%s>" % ("None", self.data, self.next.data)
        elif self.prev and self.next:
            return "<Node prev=%s data=%s next=%s>" % (self.prev.data, "None", self.next.data)


def find_survivor(num_people, kill_every):
    """Given num_people in a circle, kill everyone [kill_every]th person, return survivor.

        >>> find_survivor(4, 2)
        1

        >>> find_survivor(41, 3)
        31

        >>> find_survivor(10, 3)
        4

    As a sanity case, if never skip anyone, the last person will be our survivor:

        >>> find_survivor(10, 1)
        10
    """

    head = Node(1)
    previous = head
    for num in range(2, num_people+1):
        new_node = Node(data=num, prev=previous, next=None)
        previous.next = new_node
        previous = new_node
    head.prev = previous
    head.prev.next = head

    current = head
    while current.next != current:
        for i in range(kill_every-1):
            # print current, "current"
            current = current.next
        kill = current
        # print kill, "kill"
        current = current.next
        kill.remove()
        
    return current.data


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TEST PASSED. W00T!\n"
