'''
Task:
Input Format

The <i>insert function</i> has parameters: a pointer to a Node named <i>head</i>, and an integer value,<i>data</i>.
The constructor for Node has 1 parameter: an integer value for the <i>data </i>field.
You do not need to read anything from stdin.

Output Format

Your <i>insert function</i> should return a reference to the node of the linked list. 
'''


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Solution:
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            print ()
            current = current.next

    def insert(self, head, data):
        # 3 cases: if list is empty, if list contains 1 Nose and else
        if head == None:
            head = Node(data)
            head.next = None
        elif head.next == None:
            head.next = Node(data)
        else:
            runner = head
            while runner.next != None:
                runner = runner.next
            #now last node is in runner
            runner.next = Node(data)
        return head

#fuction cuoutns lenght of tail and summs       
def get_lenght(head):
    if head is None:
        return 0
    else:
        tailLength = get_lenght(head.next)
        length = tailLength + 1
        return length



mylist= Solution()  #stores the sequence of nodes
T=int(input())
head=None           #initially head points to None, because the list is empty
for i in range(T):
    data=int(input()) #data field in a current Node
    head=mylist.insert(head,data)
mylist.display(head);

print (get_lenght(head))
