# לייצג רשימה מקושרת



class Node:
    # next, num
    def __init__(self, num, nxt=None):
        self.num = num
        self.nxt = nxt

    def __str__(self):
        return "->" + str(self.num)

# בנ משורשרת יית רשימה מ ar
def Build(ar):
    head = None
    for x in ar:
        el = Node(x, head)
        head = el
    return head

#הדפסת רשימה משורשרת
def PrintL(head):
    pos = head
    print()
    while(pos is not None):
        print(pos, end = "")
        pos = pos.nxt
    print("-||")
    
#החזרת סכום רשימה משורשרת (ממוצע)
def Avrg(head):
    sm =0; cnt =0
    pos = head
    while(pos is not None):
        sm += pos.num
        cnt += 1
        pos = pos.nxt
    return sm / cnt

# searches for 'num' if found delete it, otherwise print "not found"
def DeleteNum(head, num):
    # if empty
    if(head is None):
        print("Empty linked list")
        return None
    # if first element yo be deleted
    if(head.num == num):
        return head.nxt
    # search in loop while checking the next value
    pos = head
    while(pos.nxt != None):
        if(pos.nxt.num == num):
            pos.nxt = pos.nxt.nxt
            return head
        pos = pos.nxt
    print(num, "Not Found")
    return head
            
# add num to end of linked list (starts with head)
def AddNumLast(head, num):
    el = Node(num)
    # empty list: 
    if head == None:
        return el
    pos = head
    while(pos.nxt != None):
        pos = pos.nxt
    pos.nxt = el;
    return head
    

def Concatenate(head1, head2):
    if head2 is None:
        return head1
    if head1 is None:
        return head2
    pos = head1
    while(pos.nxt is not None):
        pos = pos.nxt
    # pos stands on tail of head2
    pos.nxt = head2
    return head1
    
    



    
    
lst3 = [10,20,30,40,50,60,70]
h3 = Build(lst3) ; PrintL(h3)

        
