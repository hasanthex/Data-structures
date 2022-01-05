class Node:
    def __init__(self, item):
        self.item = item
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None


if __name__ == '__main__':
    linked_list = LinkedList()

    # Assign item values
    linked_list.head = Node(10)
    second = Node(20)
    third = Node(30)

    # Connect nodes
    linked_list.head.next = second
    second.next = third

    # get linked list value
    print(linked_list.head.item, linked_list.head.next)
    print(second.item, second.next)
    print(third.item, third.next)

    # get linked list value throw loop
    while linked_list.head != None:
        print(linked_list.head.item)
        linked_list.head = linked_list.head.next
