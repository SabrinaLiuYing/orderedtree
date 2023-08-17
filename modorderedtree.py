from os import access
from turtle import end_fill
from treenode import *

class ModOrderedTree:

    ## ModOrderedTree() produces an empty ordered tree.
    ## __init__: -> ModOrderedTree
    def __init__(self):
        self._root = None

    ## self.is_empty() produces True if the tree is empty 
    ##     and False otherwise.
    ## is_empty: ModOrderedTree -> Bool
    def is_empty(self):
        if self._root == None:
            return True
        else:
            return False

    ## self.root() produces the root of self.
    ## root: ModOrderedTree -> TreeNode
    ## Requires: self is not empty
    def root(self):
        return self._root


    ## self.value(node) produces the value of node.
    ## value: ModOrderedTree TreeNode -> Any
    ## Requires: node is a TreeNode in self
    def value(self, node):
        return node.access_value()
    
    ## self.parent(node) produces the TreeNode that is the parent
    ##     of node, if any, and otherwise None.
    ## parent: ModOrderedTree TreeNode -> (anyof TreeNode None)
    ## Requires: node is a TreeNode in self
    def parent(self, node):
        prev = node.access_prev()
        # if the node is the root the parent is itself
        if prev == None:
            return prev
        else: 
            while (prev.access_first() != node):
                prev = prev.access_prev()
            return prev

        


    ## self.left_leaf(node) produces the leftmost leaf
    ##     in the subtree rooted at node.
    ## left_leaf: ModOrderedTree TreeNode -> TreeNode
    ## Requires: node is a TreeNode in self
    def left_leaf(self, node):
        return node.access_left()

    ## self.one_child(node, index) produces the index
    ##     child of node.
    ## one_child: ModOrderedTree TreeNode Int -> TreeNode
    ## Requires: node is a TreeNode in self that is not a leaf
    ##           index is in the range from 0 to the
    ##               number of children of node - 1
    def one_child(self, node, index):
        child = node.access_first()
        ii = 0
        while (ii != index):
            child = child.access_next()
            ii += 1
        return child

    ## self.set_value(node, new_value) changes the
    ##     value of node to new_value.
    ## Effects: Mutates self by changing the value
    ##     of node to new_value.
    ## set_value: ModOrderedTree TreeNode Any -> None
    ## Requires: node is a TreeNode in self
    def set_value(self, node, new_value):
        node.store_value(new_value)



    ## self.add_leaf(parent, pos, value) adds a new leaf storing
    ##     value as a child of parent in position pos, where the
    ##     first position is 0; if parent is None then the new node
    ##     is the root replacing the entire tree (if any).
    ## add_leaf: ModOrderedTree (anyof TreeNode None) Int Any
    ##     -> TreeNode
    ## Requires: parent is either none or a TreeNode in self
    ##           pos <= the number of children of parent
    def add_leaf(self, parent, pos, value):
        node = TreeNode(value, None, None, None, None)
        node.link_left(node)
        if parent == None :
            self._root = node
        elif pos == 0 :
            node.link_prev(parent)
            node.link_left(node)
            if parent.access_first() != None:
                node.link_next(parent.access_first())
                parent.access_first().link_prev(node)
            parent.link_first(node)
            parent.link_next(node)
            parent_prev = node
            while (parent_prev.access_prev() != None and 
            parent_prev.access_prev().access_first()==parent_prev):
                parent_prev.access_prev().link_left(node)
                parent_prev = parent_prev.access_prev()
        else:
            child_prev = parent.access_first()
            ii = 0
            while (ii != pos-1):
                child_prev = child_prev.access_next()
                ii += 1
            node.link_prev(child_prev)
            child_next = child_prev.access_next()
            if (child_next != None):
                child_next.link_prev(node)
                node.link_next(child_next)
            child_prev.link_next(node)
        return node





    
    ## self.delete_leaf(node) deletes node from self.
    ## delete_leaf: ModOrderedTree TreeNode -> None
    ## Requires: node is a leaf in self
    def delete_leaf(self, node):
        # if the self is empty
        if self._root == None:
            return
        # if the node is the root
        elif node == self._root:
            self._root = None
        else:
            node_next = node.access_next()
            node_prev = node.access_prev()
            # if the node is the first child of its parent
            if node_prev.access_first() == node :
                node_prev.link_left(node_next)
                node_prev.link_next(node_next)
                parent_prev = node_prev
                while (parent_prev.access_prev() != None and 
                    parent_prev.access_prev().access_first()==parent_prev):
                    parent_prev.access_prev().link_left(node_prev)
                    parent_prev = parent_prev.access_prev()
                if node_next == None :
                    node_prev.link_left(node_prev)
                    node_prev.link_first(None)
                else:
                    node_prev.link_left(node_next.access_left())
                    node_prev.link_first(node_next)
                    node_next.link_prev(node_prev)
            else:
                node_prev.link_next(node_next)
                node_next.link_prev(node_prev)






