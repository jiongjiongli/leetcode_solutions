"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        # Store original random pointers so we can restore them later.
        randoms = []
        randoms.append(head.random)

        # Create copy of the head.
        # The copy's next and random fields initially point to the same nodes
        # as the original head.
        copy_head = Node(head.val, head.next, head.random)

        # Use the original node's random field as a mapping:
        # original node -> copied node
        head.random = copy_head

        # Create copies of the remaining nodes.
        # Each copy's next and random fields initially point to the same nodes
        # as the original head.
        next_node = head.next
        copy_node = copy_head

        while next_node:
            # Save original random pointer for later restoration.
            randoms.append(next_node.random)

            copy_node.next = Node(next_node.val, next_node.next, next_node.random)

            copy_node = copy_node.next

            # Use the original node's random field as a mapping:
            # original node -> copied node
            next_node.random = copy_node

            next_node = next_node.next

        # Fix random pointers in copied list.
        copy_node = copy_head

        while copy_node:
            if copy_node.random:
                # Before this step:
                # copy_node.random points to an original node.
                # That original node's random field has been repurposed
                # to point to its corresponding copy.
                copy_node.random = copy_node.random.random

            copy_node = copy_node.next

        # Restore original random pointers.
        node = head
        idx = 0

        while node:
            node.random = randoms[idx]
            node = node.next
            idx += 1

        return copy_head
