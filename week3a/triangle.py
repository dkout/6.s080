import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to_origin(self):
        return (self.x**2 + self.y**2)**0.5

    def euclidean_distance(self, other):
        return ((self.x - other.x)**2 + (self.y - other.y)**2)**0.5

    def manhattan_distance(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y)

    def angle_between(self, other):
        vert = other.y - self.y
        horiz = other.x - self.x
        return math.atan2(vert, horiz)

class Triangle:
    def __init__(self,p1,p2,p3):
        self.p1=p1
        self.p2=p2
        self.p3=p3
    def side_lengths(self):
        return (self.p1.euclidean_distance(p2), self.p1.euclidean_distance(p3), self.p2.euclidean_distance(p3))
    def angles(self):
        import math
        (l1,l2,l3)=self.side_lengths()
        a1=math.acos((l1**2+l2**2-l3**2)/(2*l1*l2))
        a2=math.acos((l2**2+l3**2-l1**2)/(2*l2*l3))
        a3=math.acos((l3**2+l1**2-l2**2)/(2*l1*l3))
        return (a1,a2,a3)
    def side_classification(self):
        (l1,l2,l3)=self.side_lengths()
        if abs(l1-l2)<10**-6 and abs(l2-l3)<10**-6:
            return "equilateral"
        elif abs(l1-l2)<10**-6 or abs(l2-l3)<10**-6 or abs(l3-l1)<10**-6:
            return "isosceles"
        else:
            return "scalene"
    def angle_classification(self):
        import math
        (a1,a2,a3)=self.angles()
        if abs(a1-a2)<10**-6 and abs(a1-a3)<10**-6:
            return "equiangular"
        if abs(a1-math.pi/2)<10**(-6) or abs(a2-math.pi/2)<10**(-6) or abs(a3-math.pi/2)<10**(-6) :
            return "right"
    
        if max(a1,a2,a3)>math.pi/2:
            return "obtuse"
       
        else:
            return "acute"
    def is_right(self):
        (a1,a2,a3)=self.angles()
        if  abs(a1-math.pi/2)<10**(-6) or abs(a2-math.pi/2)<10**(-6) or abs(a3-math.pi/2)<10**(-6) :
            return True
        else:
            return False
    def area(self):
        return 0.5*(self.p1.x*(self.p2.y-self.p3.y)+self.p2.x*(self.p3.y-self.p1.y)+self.p3.x*(self.p1.y-self.p2.y))
    def perimeter(self):
        p=0
        for i in self.side_lengths():
            p+=i
        return p

