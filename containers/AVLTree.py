'''
This file implements the AVL Tree data structure.
The functions in this file are considerably harder than the
functions in the BinaryTree and BST files,
but there are fewer of them.
'''

from containers.BinaryTree import BinaryTree, Node
from containers.BST import BST


class AVLTree(BST):
    '''
    FIXME:
    AVLTree is currently not a subclass of BST.
    You should make the necessary changes in the class declaration line above
    and in the constructor below.
    '''

    def __init__(self, xs=None):
        '''
        FIXME:
        Implement this function.
        '''
        super().__init__(xs)

    def balance_factor(self):
        '''
        Returns the balance factor of a tree.
        '''
        return AVLTree._balance_factor(self.root)

    @staticmethod
    def _balance_factor(node):
        '''
        Returns the balance factor of a node.
        '''
        if node is None:
            return 0
        return BinaryTree._height(node.left) - BinaryTree._height(node.right)

    def is_avl_satisfied(self):
        '''
        Returns True if the avl tree satisfies that all nodes have
        a balance factor in [-1,0,1].
        '''
        return AVLTree._is_avl_satisfied(self.root)

    @staticmethod
    def _is_avl_satisfied(node):
        '''
        FIXME:
        Implement this function.
        '''
        if node is None:
            return True

        bal_fact = AVLTree._balance_factor(node)

        if bal_fact not in [-1, 0, 1]:
            return False

        left_subtree_satisfied = AVLTree._is_avl_satisfied(node.left)
        right_subtree_satisfied = AVLTree._is_avl_satisfied(node.right)

        return left_subtree_satisfied and right_subtree_satisfied

    @staticmethod
    def _left_rotate(node):
        '''
        FIXME:
        Implement this function.

        The lecture videos provide a high-level overview of tree rotations,
        and the textbook provides full python code.
        The textbook's class hierarchy for their AVL tree code is fairly
        different from our class hierarchy,
        however, so you will have to adapt their code.
        '''
        if node.right:
            new_root = Node(node.right.value)
            new_root.left = Node(node.value, node.left, node.right.left)
            new_root.right = node.right.right
            return new_root
        else:
            return node

    @staticmethod
    def _right_rotate(node):
        '''
        FIXME:
        Implement this function.

        The lecture videos provide a high-level overview of tree rotations,
        and the textbook provides full python code.
        The textbook's class hierarchy for their AVL tree code is fairly
        different from our class hierarchy,
        however, so you will have to adapt their code.
        '''
        if node.left:
            old_root = Node(node.value, right=node.right)
            old_root.left = node.left.right
            i = node.left.value
            new_root = Node(i, left=node.left.left, right=old_root)
            return new_root
        else:
            return node

    def insert(self, value):
        '''
        FIXME:
        Implement this function.

        The lecture videos provide a high-level overview of how to insert
        into an AVL tree,
        and the textbook provides full python code.
        The textbook's class hierarchy for their AVL tree code is fairly
        different from our class hierarchy,
        however, so you will have to adapt their code.

        HINT:
        It is okay to add @staticmethod helper functions for this code.
        The code should look very similar to the code for your
        insert function for the BST,
        but it will also call the left and right rebalancing functions.
        '''
        if self.root:
            self.root = AVLTree._insert(self.root, value)
        else:
            self.root = Node(value)

    def insert_list(self, xs):

        for x in xs:
            if self.root:
                self.root = AVLTree._insert(self.root, x)
            else:
                self.root = Node(x)

    @staticmethod
    def _insert(node, value):
        if not node:
            return Node(value)
        elif value < node.value:
            node.left = AVLTree._insert(node.left, value)
        else:
            node.right = AVLTree._insert(node.right, value)

        balance_factor = AVLTree._balance_factor(node)
        if balance_factor > 1 and value < node.left.value:
            return AVLTree._right_rotate(node)
        elif balance_factor < -1 and value > node.right.value:
            return AVLTree._left_rotate(node)
        elif balance_factor > 1 and value > node.left.value:
            node.left = AVLTree._left_rotate(node.left)
            return AVLTree._right_rotate(node)
        elif balance_factor < -1 and value < node.right.value:
            node.right = AVLTree._right_rotate(node.right)
            return AVLTree._left_rotate(node)
        else:
            return node

    @staticmethod
    def _rebalance(node):
        '''
        There are no test cases for the rebalance function,
        so you do not technically have to implement it.
        But both the insert function needs the rebalancing code,
        so I recommend including that code here.
        '''
