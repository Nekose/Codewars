import numpy

class Vector:
    def __init__(self,x=0,y=0,z=0):
        if type(x) is list or type(x) is numpy.ndarray:
            self.x,self.y,self.z = x
        else:
            self.x = x
            self.y = y
            self.z = z

        self.magnitude = numpy.linalg.norm([self.x,self.y,self.z])

    def to_tuple(self):
        return (self.x,self.y,self.z)

    def __str__(self):
        return f"<{self.x}, {self.y}, {self.z}>"

    def __eq__(self, o: "Vector") -> bool:
        if type(o) is Vector:
            if self.magnitude == o.magnitude and self.to_tuple() == o.to_tuple():
                return True
            else:
                return False
        else:
            if self.magnitude == o:
                return True
            else:
                return False

    def __add__(self, other: "Vector"):
        return Vector(self.x + other.x,self.y + other.y, self.z + other.z)


    def __sub__(self, other: "Vector"):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def cross(self,other: "Vector"):
        return Vector(numpy.cross(self.to_tuple(),other.to_tuple()))

    def dot(self,other: "Vector"):
        return numpy.dot(self.to_tuple(),other.to_tuple())

test1 = Vector(1,2,3)
test2 = Vector(1,2,3)

print(test1.dot(test2))
print(test1.magnitude)