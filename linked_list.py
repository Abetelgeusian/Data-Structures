
# Example of Linked list and how to traverse them

class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

a = Node('A')
b = Node('B') 
c = Node('C')
d = Node('D')
e = Node('E')

a.next = b
b.next = c
c.next = d
d.next = e

# non recursively
def print_list(head):
    current = head
    while current is not None:
        print(current.val)
        current = current.next

# recursively

def print_rec(head):
    if head is None:
        return
    print(head.val)
    print_rec(head.next)

print_list(a)
print("\n")
print_rec(a)

# Problem 1
# Instead of pritning each node, return a list with all the nodes
# non recursive
def linked_list_values(head):
    list = []
    while head is not None:
      list.append(head.val)
      head = head.next
    # print(list)  
    return list

linked_list_values(b)

# Recursive

# def linked_list_rec(head):
#     list_r=[]
#     if head is None:
#         return
#     list_r.append(head.val)
#     print(list_r)
#     linked_list_rec(head.next)
    

# linked_list_rec(a)

## The above approach wont work. Each time the function is called list is reinitilized. Thus you need to fucntions.

def linked_list_rec(head):
    list_r = []
    _linked_list_rec(head,list_r)
    # return list_r
    print(list_r)

def _linked_list_rec(head,values):
    if head is None:
        return
    values.append(head.val)
    _linked_list_rec(head.next, values)

linked_list_rec(a)