
#####Palindrome Linked List
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        #base case
        if not head or not head.next:
            return True

        #get to middle of list
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        #slow is now at the middle of linked list
        #reverse second half
        prev, curr = None, slow
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        #compare halves
        first, second = head, prev
        while second:
            if first.val != second.val:
                return False
            first = first.next
            second = second.next

        return True
        
####Reorder List
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        #get fast to end
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        #reverse second half
        second = slow.next
        slow.next = None
        node = None

        while second:
            temp = second.next
            second.next = node
            node = second
            second = temp

        #merge two halves
        first = head
        second = node

        while second:
            temp1, temp2 = first.next, second.next
            first.next, second.next, = second, temp1
            first, second = temp1, temp2
        
