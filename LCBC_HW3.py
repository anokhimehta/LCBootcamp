
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
        
