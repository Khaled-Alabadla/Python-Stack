# Merge Two Sorted Linked Lists

## Overview

This project implements a solution to merge two sorted linked lists into a single sorted linked list. The algorithm efficiently combines the lists while maintaining the sorted order.

## Steps

1. **Initialize a dummy node**: Create a dummy node to serve as the start of the merged list.
2. **Compare and merge**: Iterate through both lists, comparing the current nodes' values and appending the smaller one to the merged list.
3. **Handle remaining nodes**: After one list is exhausted, append the remaining nodes from the other list.
4. **Return the result**: The merged list starts from the node after the dummy node.

## Usage

- Define linked lists using the `ListNode` class.
- Call `Solution().mergeTwoLists(list1, list2)` to merge two sorted lists.
