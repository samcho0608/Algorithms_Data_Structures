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

# Complete the mergeLists function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def mergeLists(head1, head2):
    sys.setrecursionlimit(1000000)
    if not (head1 and head2):
        if head1:
            head1.next = mergeLists(head1.next, head2)
            return head1
        if head2:
            head2.next = mergeLists(head1, head2.next)
            return head2
        else:
            return None
    
    if head1.data < head2.data:
        head1.next = mergeLists(head1.next, head2)
        return head1
    else:
        head2.next = mergeLists(head1, head2.next)
        return head2
    # NON-RECURSIVE METHOD
    # # head of merged list
    # if head1.data < head2.data:
    #     merged = head1
    #     head1 = head1.next
    # else:
    #     merged = head2
    #     head2 = head2.next
        
    # head = merged
    # while head1 or head2:
    #     # if either of them are None
    #     if (not head1) ^ (not head2):
    #         smaller = head1 if head1 is not None else head2
    #     else:
    #         smaller = head1 if head1.data < head2.data else head2
    #     if smaller is head1:
    #         head1 = head1.next
    #     else:
    #         head2 = head2.next
        
    #     smaller.next = None
    #     merged.next = smaller
    #     merged = merged.next
        
    # return head
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    tests = int(input())

    for tests_itr in range(tests):
        llist1_count = int(input())

        llist1 = SinglyLinkedList()

        for _ in range(llist1_count):
            llist1_item = int(input())
            llist1.insert_node(llist1_item)
            
        llist2_count = int(input())

        llist2 = SinglyLinkedList()

        for _ in range(llist2_count):
            llist2_item = int(input())
            llist2.insert_node(llist2_item)

        llist3 = mergeLists(llist1.head, llist2.head)

        print_singly_linked_list(llist3, ' ', fptr)
        fptr.write('\n')

    fptr.close()
