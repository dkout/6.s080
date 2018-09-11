class Rational:
    def __init__(self, n, d):
        self.n=n
        self.d=d
    def get_numerator(self):
        return int(self.n)
    def get_denominator(self):
        return int(self.d)
    def to_float(self):
        return float(self.get_numerator()/self.get_denominator())
    def reciprocal(self):
        return Rational(self.d, self.n)
    def reduce(self):
        n=self.get_numerator()
        d=self.get_denominator()
        x,y=n,d
        while y!=0:
            (x,y)=(y,x%y)
        return Rational(n/x,d/x)
    def __add__(self,other):
        if isinstance(other,int):
            return Rational(self.get_numerator()+other*self.get_denominator(), self.get_denominator())
        if isinstance(other, Rational):
            on=other.get_numerator()
            od=other.get_denominator()
            n=self.get_numerator()
            d=self.get_denominator()
            return (Rational(n*od+on*d, od*d))
        if isinstance(other, float):
            return other+self.to_float()
        else:
            return None
    def __mul__(self,other):
        if isinstance(other,int):
            return Rational(self.get_numerator()*other, self.get_denominator())
        if isinstance(other, Rational):
            on=other.get_numerator()
            od=other.get_denominator()
            n=self.get_numerator()
            d=self.get_denominator()
            return (Rational(n*on, od*d))
        if isinstance(other, float):
            return other*self.to_float()
        else:
            return None
    def __truediv__(self,other):
        if isinstance(other,int):
            return Rational(self.get_numerator(), self.get_denominator()*other)
        if isinstance(other, Rational):
            on=other.get_numerator()
            od=other.get_denominator()
            n=self.get_numerator()
            d=self.get_denominator()
            return (Rational(n*od, on*d))
        if isinstance(other, float):
            return self.to_float()/other
        else:
            return None
    def __sub__(self,other):
        if isinstance(other,int):
            return Rational(self.get_numerator()-other*self.get_denominator(), self.get_denominator())
        if isinstance(other, Rational):
            on=other.get_numerator()
            od=other.get_denominator()
            n=self.get_numerator()
            d=self.get_denominator()
            return (Rational(n*od-on*d, od*d))
        if isinstance(other, float):
            return self.to_float()-other
        else:
            return None
