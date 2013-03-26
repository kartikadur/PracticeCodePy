class Node():
    '''Node class that stores x and y coords or given point'''
    def __init__ (self, x, y):
        '''Contructor'''
        self.x = x
        self.y = y
    def chgOnX(self):
        '''Transform point by reflecting on X Axis'''
        self.y *= -1;
    def chgOnY(self):
        '''Transform point by reflecting on Y Axis'''
        self.x *= -1;
    def getQuad(self):
        '''Return the quadrant for point'''
        if(self.x): print(x)
        

N = int(input())
NodeList = [] 
for i in range(N):
    x, y = [int(i) for i in input().split(' ')]
    NodeList.append(Node(x, y))

Q = int(input())
for i in range(Q):
    c = input().split(' ')
    if(c[0]=='C'):
        for j in range(int(c[1]) - 1, int(c[2])):
            NodeList[j].getQuad()
    if(c[0]=='X'):
        for j in range(int(c[1]) - 1, int(c[2])):
            NodeList[j].chgOnX()
    if(c[0]=='Y'):
        for j in range(int(c[1]) - 1, int(c[2])):
            NodeList[j].chgOnY()
    