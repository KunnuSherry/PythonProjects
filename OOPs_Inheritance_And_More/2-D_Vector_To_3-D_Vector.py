# Create a class (2-D vector) and use it to create another class representing a 3-D vector.

class twoDVector:
    def __init__(self, i, j):
        self.i = i
        self.j = j
class threeDVector(twoDVector):
    def __init__(self,i,j, k):
        super().__init__(i, j)
        self.k = k
    def show(self):
        return f'The Vector is: {self.i}i, {self.j}j, {self.k}k'
    
e = threeDVector(2,3,4)
print(e.show())


