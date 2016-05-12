"""
Programed by: Sameul Mullins

Program: fraction_class

Description: This program creates a fraction and can either add or multiply fractions together.
"""

from fractions import gcd

class fraction(object):
    def __init__(self,n=None,d=None,w=None):
        self.numerator = n
        self.denominator = d
        self.wholenum = w

    def __str__(self):
        return "%s " " %s / %s" % (self.wholenum, self.numerator , self.denominator)

    def numerator(self,n):
        self.numerator = n 

    def denominator(self,d):
        self.denominator = d
        
    def __add__(self,rhs):
        w = self.denominator * rhs.denominator
        x = self.numerator * rhs.denominator
        y = rhs.numerator * self.denominator
        z = x + y
        a = int(z / w)
        return  fraction(z % w ,w,a)
        
       
        
    def __mul__(self,rhs):
        x = self.numerator * rhs.numerator
        y = self.denominator * rhs.denominator
        return fraction(x,y)

 if __name__ == '__main__':
     a = fraction(1,2)
     b = fraction(4,5)
     c = a * b
     print(c)

    
a = fraction(1,2)
b = fraction(4,5)
c = a + b
print(c)