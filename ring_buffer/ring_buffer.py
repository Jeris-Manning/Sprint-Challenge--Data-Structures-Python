from doubly_linked_list import DoublyLinkedList
from doubly_linked_list import ListNode


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.storage.length < self.capacity:
            self.storage.add_to_tail(item)
            return
        if self.current == None:
            self.storage.remove_from_head()
            self.storage.add_to_head(item)
            self.current = self.storage.head
            return

        if self.current == None:
            self.current = self.storage.head
        if self.current.next == None:
            self.current = self.storage.head
        else:
            self.current = self.current.next

        self.current.value = item



    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        print_entry = self.storage.head
        # TODO: Your code here
        for i in range(0, self.storage.length):
            list_buffer_contents.append(print_entry.value)
            print_entry = print_entry.next

        print(list_buffer_contents)
        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
