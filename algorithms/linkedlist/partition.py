"""
Write code to partition a linked list around a value x, such that all nodes less
than x come before all nodes greater than or equal to x.  If x is contained
within the list, the values of x only need to be after the elements less than x.
The partition element x can appear anywhere in the "right partition";
it does not need to appear between the left and right partitions.

3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition=5]
3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8

We assume the values of all linked list nodes are int and that x in an int.
"""


class Node():
    def __init__(self, val=None):
        self.val = int(val)
        self.next = None


def print_linked_list(head):
    string = ""
    while head.next:
        string += str(head.val) + " -> "
        head = head.next
    string += str(head.val)
    print(string)


def partition(head, x):
    left = None
    right = None
    prev = None
    current = head
    while current:
        if int(current.val) >= x:
            if not right:
                right = current
        else:
            if not left:
                left = current
            else:
                prev.next = current.next
                left.next = current
                left = current
                left.next = right
        if prev and prev.next is None:
            break
        # cache previous value in case it needs to be pointed elsewhere
        prev = current
        current = current.next


def test():
    node_1 = Node("3")
    node_2 = Node("5")
    node_3 = Node("8")
    node_4 = Node("5")
    node_5 = Node("10")
    node_6 = Node("2")
    node_7 = Node("1")

    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_4
    node_4.next = node_5
    node_5.next = node_6
    node_6.next = node_7

    print_linked_list(node_1)
    partition(node_1, 5)
    print_linked_list(node_1)


if __name__ == '__main__':
    test()
