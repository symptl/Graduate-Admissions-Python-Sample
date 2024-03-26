import sys


# LINKED LIST
# Defines a Linked List class and a Node class as a building block
# Included methods are append, print, delete, and reverse
# Need to add linear search
class NodeList:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        
        # Create head if linked list is empty
        if not self.head:
            self.head = NodeList(data)
            return

        # Cycle through list until it gets to the end and add element
        last = self.head
        while last.next:
            last = last.next
        last.next = NodeList(data)

    def traverse_list(self):
        # Print all list elements sequentially from the beginning and count size in memory
        current_node = self.head
        size = 0
        while current_node:
            #   print(current_node.data) This line prints all list elements, disabled for speed
            size += sys.getsizeof(current_node)
            current_node = current_node.next
        return size

    def delete_node(self, key):
        # Delete first node that contains the specified data
        current_node = self.head

        if current_node and current_node.data == key:
            self.head = current_node.next
            current_node = None
            return

        prev = None
        while current_node and current_node.data != key:
            prev = current_node
            current_node = current_node.next

        # If the node wasn't found, then return with no action
        if current_node is None:
            return

        # If it was found then node will get unlinked (previous and next nodes get new link)
        prev.next = current_node.next
        current_node = None

    def reverse(self):
        # Sets initial conditions
        prev = None
        current_node = self.head
        while current_node:
            next_node = current_node.next  # Remember the next node to change
            current_node.next = prev  # Reverse direction, will start at "None" (it's the end of the final list)
            prev = current_node  # Remember the destination for the next node
            current_node = next_node  # Move to the next node to repeat process
        self.head = prev  # Sets final element as head (uses prev because current is "None")

    def linear_search(self, value):   # Should theoretically by O(n)
        current_node = self.head
        while current_node:
            if current_node.data == value:
                return current_node
            current_node = current_node.next
        return None


# AVL TREE
# A binary search tree that self-balances with each insertion or deletion to minimize height
# Values on the left branch of any node are all lower than the node and vice versa for the right branch
# Included methods are insert, delete, search, and in-order traversal
# Methods included but not necessarily intended to be directly called are left/right rotate, get min value node,
# get height, get balance

class TreeNode:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def insert(self, root, value):
        # Perform the normal BST insertion by searching through tree
        if not root:
            return TreeNode(value)
        elif value < root.data:
            root.left = self.insert(root.left, value)
        else:
            root.right = self.insert(root.right, value)

        #  Update the height of the ancestor node
        root.height = 1 + max(self.get_height(root.left),
                              self.get_height(root.right))

        # Get the balance factor
        balance = self.get_balance(root)

        #  If the node is unbalanced, then try one of the four rotations

        # Case 1: Left Left
        if balance > 1 and value < root.left.data:
            return self.right_rotate(root)

        # Case 2: Right Right
        if balance < -1 and value > root.right.data:
            return self.left_rotate(root)

        # Case 3: Left Right
        if balance > 1 and value > root.left.data:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Case 4: Right Left
        if balance < -1 and value < root.right.data:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def delete(self, root, value):
        # Perform standard BST delete by searching through tree
        if not root:
            return root

        elif value < root.key:
            root.left = self.delete(root.left, value)

        elif value > root.key:
            root.right = self.delete(root.right, value)

        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp

            elif root.right is None:
                temp = root.left
                root = None
                return temp

            temp = self.get_min_value_node(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)

        # If the tree had only one node then return
        if root is None:
            return root

        # Update the height of the current node
        root.height = 1 + max(self.get_height(root.left),
                              self.get_height(root.right))

        # Get the balance factor
        balance = self.get_balance(root)

        # If the node is unbalanced, then try one of the four cases

        # Left Left
        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.right_rotate(root)

        # Left Right
        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Right Right
        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.left_rotate(root)

        # Right Left
        if balance < -1 and self.get_balance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def get_min_value_node(self, node):
        if node is None or node.left is None:
            return node
        return self.get_min_value_node(node.left)

    def left_rotate(self, z):
        y = z.right
        T2 = y.left

        # Perform rotation
        y.left = z
        z.right = T2

        # Update heights
        z.height = 1 + max(self.get_height(z.left),
                           self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left),
                           self.get_height(y.right))

        # Return the new root
        return y

    def right_rotate(self, y):
        x = y.left
        T2 = x.right

        # Perform rotation
        x.right = y
        y.left = T2

        # Update heights
        y.height = 1 + max(self.get_height(y.left),
                           self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left),
                           self.get_height(x.right))

        # Return the new root
        return x

    def get_height(self, root):
        if not root:
            return 0
        return root.height

    def get_balance(self, root):
        if not root:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)

    # Inorder Traversal
    def inorder_traversal(self, root):
        size = 0
        if root is not None:
            size += self.inorder_traversal(root.left)
            # print("{0} ".format(root.data), end="") #This line prints out value during traversal, disabled for speed
            size += self.inorder_traversal(root.right)
        return sys.getsizeof(root) + size  # Returns memory size of current node and child nodes

    def search(self, root, value):   # Should theoretically be O(log(n))
        # Base Cases: root is null or value is present at root
        if root is None or root.data == value:
            return root

        # Value is greater than root's value
        if root.data < value:
            return self.search(root.right, value)

        # Value is smaller than root's value
        return self.search(root.left, value)
