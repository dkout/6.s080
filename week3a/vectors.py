class Vector:
    def __init__(self, coords):
        self.coords=coords
    def as_list(self):
        return self.coords
    def size(self):
        return len(self.coords)
    def magnitude(self):
        s=0
        for i in self.as_list():
            s+=i**2
        return s**0.5
    def euclidean_distance(self,other):
        s=0
        v1=self.as_list()
        v2=other.as_list()
        for i in range(self.size()):
            s+=(v1[i]-v2[i])**2
        return s**0.5
    def normalized(self):
        m=self.magnitude()
        newvec=[]
        for i in self.as_list():
            newvec.append(i/m)
        return Vector(newvec)
    def cosine_similarity(self, other):
        p=0
        v1=self.as_list()
        v2=other.as_list()
        for i in range(self.size()):
            p+=v1[i]*v2[i]
        return p/(self.magnitude()*other.magnitude())
    def __add__ (self,other):
        if isinstance(other, Vector) and other.size()==self.size():
            v=[]
            v1=self.as_list()
            v2=other.as_list()
            for i in range(self.size()):
                v.append(v1[i]+v2[i])
            return Vector(v)
        else:
            return None
    def __sub__ (self,other):
        if isinstance(other, Vector) and other.size()==self.size():
            v=[]
            v1=self.as_list()
            v2=other.as_list()
            for i in range(self.size()):
                v.append(v1[i]-v2[i])
            return Vector(v)
        else:
            return None
    def __mul__(self,other):
        if isinstance(other, Vector):
            if self.size()==other.size():
                p=0
                v1=self.as_list()
                v2=other.as_list()
                for i in range(self.size()):
                    p+=v1[i]*v2[i]
                return p
            else:
                return None
        elif isinstance(other, int) or isinstance(other,float):
            v=[]
            for i in self.as_list():
                v.append(i*other)
            return Vector(v)
        else:
            return None
    def __truediv__(self,other):
        if isinstance(other, int) or isinstance(other, float):
            v=[]
            for i in self.as_list():
                v.append(i/other)
            return Vector(v)
        else:
            return None
