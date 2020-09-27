class Node():
    def __init__(self,value, nxt = None,freq = None):
        self.value = value
        self.freq = freq
        self.next = nxt
    
    def __repr__(self):
        return (f'{self.value}')

    def __hash__(self):
        return hash([self.value,self.next])

multi_nodes = []
branches = []
class LinkedList():
    def __init__(self,startingValue):
        self.start = Node(startingValue)
        self.isCircular = False
    
    def makeCircular(self):
        node = self.start
        while True:
            if node.next is None or node.next is self.start:
                node.next = self.start
                self.isCircular = True
                return True
            node = node.next

    def indexOf(self,value,el = None):
        node =self.start
        i = 0
        if el is None:
            while True:
                if node is None or node.next is self.start:
                    return -1
                if node.value == value:
                    return i
                i+=1
                node = node.next
        else:
            while True:
                if node is None or node.next is self.start :
                    return -1
                if node.value is el:
                    return i
                i+=1
                node = node.next

    def get(self,index):
        node = self.start
        i = 0
        while True:
            if node is None:
                return False
            if i==index:
                return node
            i+=1
            node = node.next

    def append(self,value):
        node = self.start
        while True:
            if node.next is None or node.next is self.start:
                node.next = Node(value)
                break
            else:
                node = node.next
    
    def leng(self):
        node = self.start
        leng = 0
        while True:
            leng+=1
            if node.next is None or node.next is self.start:
                break
            node = node.next
        return leng
    def print1(self):
        node = self.start
        while True:
            if node.next is None or node.next is self.start:
                
                print(node.value,end=' ')
                break
            print(node.value,end=' ')
            node = node.next
        print()
    
    def insert(self,x,y,z=None):
        node = self.start
        if z is None:
            while True:
                if node is None:
                    return False
                    
                elif node.value == y:
                    node.next = Node(x,node.next)
                    break
                elif node.next.value == x:
                    node.next = Node(y,node.next)
                    break
            
                node = node.next
        else:
            y = self.indexOf(y)
            z = self.indexOf(z)
            #print(y,z)
            i = int((y+z)/2)
            node = self.get(i)
            node.next = Node(x,node.next)

    def shorten(self,element,p):
        index = self.indexOf(element)
        node = self.get(index)
        branches.append(node.next)
        if isinstance(self.get(index+p),bool):
            self.makeCircular()
        node.next = self.get(index+p)
        
    def reduceBranch(self,branches):
        for node in branches:
            while True:
                if node is None or node is self.start:
                    break
                if node.next in branches:
                    branches.remove(node.next)
                node = node.next
            
operations = []
num_operations = int(input())

for i in range(num_operations):
    line = input().split()
    operations.append(line)

x = LinkedList(int(operations[0][-1]))
for operation in operations[1:]:
    if operation[0] == 'I':
        if operation[1] == '0':
                x.append(int(operation[2]))

        if operation[1] == '1':
            x.insert(int(operation[3]),int(operation[2]))

        if operation[1] == '2':
            x.insert(int(operation[4]),int(operation[3]),int(operation[2]))

    if operation[0] == 'U':
        x.shorten(int(operation[1]),int(operation[2]))
'''
x = LinkedList(1)
x.append(7)
x.insert(7,6)
x.insert(2,1)
x.insert(3,7,1)
x.insert(5,6,3)
x.insert(4,7,1)
'''
x.reduceBranch(branches)
for branch in branches:
    node = branch
    while True:
        if x.indexOf(node.value) != -1:
            if node not in multi_nodes:
                node.freq = 1
                multi_nodes.append(node)
            if node in multi_nodes:
                multi_nodes[multi_nodes.index(node)].freq +=1
            break
        node = node.next
print(1 if x.isCircular else 0)
print(len(multi_nodes))
if len(multi_nodes) == 0:
    x.print1()
else:
    print(*multi_nodes)
    print(*[node.freq for node in multi_nodes])
