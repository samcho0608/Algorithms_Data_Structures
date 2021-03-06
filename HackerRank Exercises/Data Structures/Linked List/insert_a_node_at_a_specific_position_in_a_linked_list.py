#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the insertNodeAtPosition function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def insertNodeAtPosition(head, data, position):
    if position < 2:
        tmp, head.next = head.next, SinglyLinkedListNode(data)
        head.next.next = tmp
    else:
        insertNodeAtPosition(head.next, data, position - 1)
    return head
    
    # NON-RECURSIVE VERSION
    # if not position:
    #     if head:
    #         next_node = head
    #         head = SinglyLinkedListNode(data)
    #         head.next = next_node
    #     else:
    #         head = SinglyLinkedListNode(data)
    #     return head
            
    # # didn't error check head
    # current = head
    # for n in range(position - 1):
    #     current = current.next
    # next_node = current.next
    # current.next = SinglyLinkedListNode(data)
    # current.next.next = next_node
    
    # return head

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    llist_count = int(input())

    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist.insert_node(llist_item)

    data = int(input())

    position = int(input())

    llist_head = insertNodeAtPosition(llist.head, data, position)

    print_singly_linked_list(llist_head, ' ', fptr)
    fptr.write('\n')

    fptr.close()
