
class node(object):
    def __init__(self, prev,element,next):
        self.element = element
        self.next = next
        self.prev = prev

class bralist(object):
    head = node(None,None,None)
    tail = node(None,None,None)
    
    def __init__(self):
        self.head.next = self.tail 
        self.tail.prev = self.head

    def push(self,element):
        new_node = node(None,element,None)
        if self.head.next == self.tail:
            new_node.prev = self.head
            new_node.next = self.tail
            self.head.next = new_node
            self.tail.prev = new_node
        else:
            new_node.prev = self.tail.prev
            new_node.next = self.tail
            self.tail.prev.next = new_node
            self.tail.prev = new_node

    def top(self):
        return self.tail.prev.element
    
    def pop(self):
        self.tail.prev = self.tail.prev.prev
        self.tail.prev.prev.next = self.tail

    def print(self):
        i = self.head.next
        while i is not self.tail:
            print(i.element)
            i = i.next
    def isEmpty(self):
        if self.head.next == self.tail:
            return True
        else:
            return False

bracketList = bralist()   
befoList = []

def addBrackets(i):
    if i == '{':
        befoList.append('{')
    if i == '}':
        befoList.append('}')
    if i == '[':
        befoList.append('[')
    if i == ']':
        befoList.append(']')
    if i == '(':
        befoList.append('(')
    if i == ')':
        befoList.append(')')

def eofCheck(lst):
    for i in lst:
        if i == '{' or '[' or '(':
            bracketList.push(i)
        elif i == '}' or ']' or ')':
            if bracketList.isEmpty():
                print("warning: bracket was not closed")
            if i != bracketList.top():
                print("warning: wrong closing symbol")
            if i == bracketList.top():
                bracketList.pop()
    if bracketList.isEmpty():
        return True
    else:
        print("warning: bracket(s) left unclosed")
            

finput = open('C:\\Users\\100488516\\Desktop\\PythonProgram\\brackets\\bracketText.txt',"r")
for i in finput.read():
    addBrackets(i)
eofCheck(befoList)


