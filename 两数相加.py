'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''

#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1_listNodeNum =[]
        l2_listNodeNum =[]
        sum_listNode =[]
        l1_listNum = self.ListNodeNumList(l1, l1_listNodeNum)
        l2_listNum = self.ListNodeNumList(l2, l2_listNodeNum)
        maxLenList, max_NumListLen, min_NumListLen = self.compareTwoList(l1_listNum, l2_listNum)
        for i in range(max_NumListLen):
            if i <= min_NumListLen-1:
                sum_listNode.append(l1_listNum[i]+l2_listNum[i])
            else:
                sum_listNode.append(maxLenList[i])
        for k in range(max_NumListLen):
            if k !=max_NumListLen-1 and sum_listNode[k]>=10:
                sum_listNode[k]=sum_listNode[k]%10
                sum_listNode[k+1]=sum_listNode[k+1]+1
            if k==max_NumListLen-1 and sum_listNode[k]>=10:
                sum_listNode[k]=sum_listNode[k]%10
                sum_listNode.append(1)
        return sum_listNode

    def compareTwoList(self, list1, list2):
        max_NumListLen = max(len(list1), len(list2))
        min_NumListLen = min(len(list1), len(list2))
        if len(list1) > len(list2):
            return list1, max_NumListLen,min_NumListLen
        return list2,max_NumListLen,min_NumListLen
    
    # def listToListNode(self,list):
    #     listLen = len(list)
    #     outListNode = ListNode(list[0])
    #     outListNode2 = outListNode
    #     for i in range(1, len(list),1):
    #         outListNode.next=ListNode(list[i])
    #         outListNode = outListNode.next
    #     return outListNode2
    
    def ListNodeNumList(self, listNode, listNodeNum):
        listNodeNum.append(listNode.val)
        while(listNode.next != None):
            temp = listNode.val
            if temp ==0 and listNode.next ==None:
                return "链表定义有误，该链表不能是以数字0开头的非零数字,如 3->4->0,表示034"
            listNode = listNode.next
            listNodeNum.append(listNode.val)
        return listNodeNum
      
# 感觉这个还是有问题的，要求的输出的ListNode，但是我最后返回的是一个列表啊！！！后面再慢慢研究吧
