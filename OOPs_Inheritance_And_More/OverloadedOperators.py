# . Write a class ‘Complex’ to represent complex numbers, along with overloaded operators ‘+’ and ‘*’ which adds and multiplies them.

class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    def __add__(self, c2):
        return f'{self.real + c2.real} + {self.imag + c2.imag}i'
    def __mul__(self,c2):
        return f'{self.real * c2.real} + {self.imag * c2.imag}i'
    def __str__(self):
        return f"{self.real} + {self.imag}i"
    
c1 = Complex(2,1)
c2 = Complex(3,2)
print(c1+c2)
print(c1*c2)

print(str(c1))