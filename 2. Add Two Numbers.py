from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Solution
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0)  # 建立一個虛擬的節點當作 Linked List(output) 的 head
        current = head      # 將目前的節點設為 head
        carry = 0           # carry 變數用來儲存進位的值
        
        while l1 or l2 or carry:    # 執行到 l1, l2 都為 None 且 carry 為 0 為止
            val1 = l1.val if l1 else 0 # 如果 l1 有值就取出，沒有就設為 0
            val2 = l2.val if l2 else 0 # 如果 l2 有值就取出，沒有就設為 0

            # divmod 會同時回傳商和餘數，例如這裡 carry 拿到的就是商(也就是進位的值)，out 拿到的就是餘數(也就是目前位數的值)
            carry, out = divmod(val1 + val2 + carry, 10)
            # total = val1 + val2 + carry
            # out = total % 10
            # carry = total // 10
            current.next = ListNode(out)    # 將下一個節點設為 out(目前位數的值)
            current = current.next          # 進入下一個節點

            if l1:  # 如果 l1 還有值就往下一個節點走
                l1 = l1.next
            if l2:  # 如果 l2 還有值就往下一個節點走
                l2 = l2.next

        # 如果 l1, l2 都為 None 且 carry 為 0 就會跳出 while 迴圈，回傳 head 的下一個節點(因為 head 是虛擬節點)
        # 這裡回傳的 head.next 就是 Linked List(output) 的 head
        return head.next