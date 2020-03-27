import sys
sys.path.append('../queue_and_stack')
# from dll_queue import Queue
# from dll_stack import Stack



class BinarySearchTree:
    def __init__(self, value):
        self.value = ''
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if self.value == '':
            BinarySearchTree(value)
        # Root node will always have value as it is part of constructor
        # If the value of node being added is less than its parent,
        # we go left.
        if value == self.value:
            return value
        if value < self.value:
            # If there is no left value from the current node, we recursively call
            # BinarySearchTree() adding a new node.
            if self.left is None:
                self.left = BinarySearchTree(value)
            # If there is a left node, we continue down to that node and start again
            else:
                self.left.insert(value)

        else: # Value is greater than or equal to
# Repeat as above with right nodes
            if self.right is None:
                self.right = BinarySearchTree(value)

            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # Recursively move down tree going left when searching for something
        # lower than current node, right when greater than current node
        if self.value == target:
            return True
        if target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)



    # Return the maximum value found in the tree
    def get_max(self):
        if self.right:
            return self.right.get_max()
        else:
            return self.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)

        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)



    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
