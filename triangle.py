import math as m

class Triangle:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
        self.ablengh=m.sqrt(m.pow(b[0]-a[0],2)+m.pow(b[1]-a[1],2))
        self.aclengh=m.sqrt(m.pow(c[0]-a[0],2)+m.pow(c[1]-a[1],2))
        self.bclengh=m.sqrt(m.pow(c[0]-b[0],2)+m.pow(c[1]-b[1],2))

    def area(self):
        halfp=self.perimeter()/2
        self.s=round(m.sqrt(halfp*(halfp-self.ablengh)*(halfp-self.aclengh)*(halfp-self.bclengh)),2)
        
    def perimeter(self):
        self.p=round(self.ablengh+self.aclengh+self.bclengh,2)
        return self.p

    def is_exixt(self):
        if self.a[0]==self.b[0] or self.a[1]==self.b[1] or self.b[0]==self.c[0] or self.b[1]==self.c[1] or self.a[0]==self.c[0] or self.a[1]==self.c[1]:
            return False
        else:
            return True
        
#test_triangle=Triangle([-5,6],[7,8],[16,9])
#test_triangle.area()
#test_triangle.perimeter()
#print(test_triangle.p, test_triangle.s, test_triangle.is_exixt())

