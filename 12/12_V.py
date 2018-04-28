# 12_V1
print('cdcdd'[int(input())-1])

# 12_V2
class Circle:
    def __init__(self, index, x, y, r):
        self.index = index
        self.x = x
        self.y = y
        self.r = r
    def touch(self, other):
        d = distance(self.x, self.y, other.x, other.y)
        if d < self.r + other.r:
            return 'Overlap'
        elif d == self.r + other.r:
            return 'Touch'
        return 'Free'
def distance(x1, y1, x2, y2):
    return ((x1-x2)**2+(y1-y2)**2)**0.5
n = int(input().strip())
circles = []
for i in range(n):
    circle_input = [int(e) for e in input().strip().split()]
    circle = Circle(*circle_input)
    circles.append(circle)
output = []
for i in range(n):
    flag = True
    for j in range(n):
        if i == j:      continue
        if circles[i].touch(circles[j]) != 'Free':
            flag = False
            break
    if flag:    output.append(circles[i].index)
if len(output) == 0:
    print('Not Found')
else:
    print(' '.join([str(e) for e in output]))

# 12_V3
class Circle:
    def __init__(self,index,x,y,r):
        self.index = index
        self.x = x
        self.y = y
        self.r = r
    def line_intersection(self,line):
        if line.x1 != line.x2:
            M = (line.y2-line.y1)/(line.x2-line.x1)
            B = line.y1-M * line.x1
            a = M**2+1
            b = -2*self.x + 2*M*(B-self.y)
            c = self.x**2+(B-self.y)**2-self.r**2
            if b**2 > 4*a*c:
                ans1 = (-b + math.sqrt(b**2-4*a*c))/2/a
                ans2 = (-b - math.sqrt(b**2-4*a*c))/2/a
                return (2,(ans1,M*ans1+B),(ans2,M*ans2+B))
            elif b**2 == 4*a*c:
                return (1,(-b/2/a,M*(-b/2/a)+B))
            else:
                return (0,)
        else:
            if self.r**2 == (line.x1-self.x)**2:
                return (1,(line.x1,self.y))
            elif self.r**2 > (line.x1-self.x)**2:
                rr = math.sqrt(self.r**2 - (line.x1-self.x)**2)
                ans1 = rr+self.y
                ans2 = rr-self.y
                return (2,(line.x1,ans1),(line.x2,ans2))
            else:
                return (0,)
    def contain_point(self,px,py):
        if distance(self.x,self.y,px,py) <= self.r:
            return True
        return False
    def line_in_circle(self,line):
        if self.contain_point(line.x1, line.y1) or self.contain_point(line.x2, line.y2):
            return True
        ret = self.line_intersection(line)
        if ret[0] == 0:
            return False
        if ret[0] == 1:
            return line.contain_point(*ret[1])
        if ret[0] == 2:
            return line.contain_point(*ret[1]) or line.contain_point(*ret[2])
def distance(x1,y1,x2,y2):
    return ((x1-x2)**2+(y1-y2)**2)**0.5
class Line:
    def __init__(self,x1,y1,x2,y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
    def contain_point(self,px,py):
        if not (min(self.y1,self.y2) <= py <= max(self.y1,self.y2)):
            return False
        if self.x1 == self.x2:
            return px == self.x1
        else:
            return abs((self.y1-py)*(self.x2-self.x1)-(self.y2-self.y1)*(self.x1-px))<1e-5
n = int(input().strip())
line_input = [int(e) for e in input().strip().split()]
line = Line(*line_input)
output = []
for i in range(n):
    circle_input = [int(e) for e in input().strip().split()]
    circle = Circle(*circle_input)
    if circle.line_in_circle(line):
        output.append(circle.index)
if len(output) == 0:
    print('Not Found')
else:
    print(' '.join([str(e) for e in output]))

# 12_V4
from math import pi
class Circle:
    def __init__(self, x, y, r=0, c=0):
        self.x = x
        self.y = y
        self.r = r
        self.c = c
    def contain_point(self, px, py):
        return distance(self.x, self.y, px, py) <= self.r
    def touch(self, other):
        d = distance(self.x, self.y, other.x, other.y)
        if d < self.r + other.r:
            return 'Overlap'
        elif d == self.r + other.r:
            return 'Touch'
        return 'Free'
    def area(self):
        return pi * self.r**2
def distance(x1, y1, x2, y2):
    return ((x1-x2)**2+(y1-y2)**2)**0.5
n = int(input())
p = Circle(*map(float, input().split()))
grp = []
for _ in range(n):
    cr = Circle(*map(float, input().split()))
    inc, exc = [[cr]], []
    for ls in grp:
        if any(cr.touch(x) != 'Free' for x in ls):
            inc.append(ls)
        else:   exc.append(ls)
    grp = exc + [[x for ls in inc for x in ls]]
for ls in grp:
    if any(p.touch(x) != 'Free' for x in ls):
        print( sum(x.area()*x.c for x in ls) / sum(x.area() for x in ls) )
        break
else:       print(1.0)

