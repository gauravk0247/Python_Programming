# Q.7 Override the __len__() method on Vector of problem 5 to display the dimension of the Vector.
# Q.5 Write a class vetor representing a vector of n dimension. Overload the + and * operator which calculates the sun and the dot product of them.
class Vector:
    def __init__(self, vec):
        self.vec = vec

    def __str__(self):
        str1 = ""
        index = 0
        for i in self.vec:
            str1 += f" {i}a{index} +"
            index +=1
        return str1[:-1]

    def __add__(self, vec2):
        newList = []
        for i in range(len(self.vec)):
           newList.append(self.vec[i] + vec2.vec[i])
        return Vector(newList)

    def __mul__(self, vec2):
        sum = 0
        for i in range(len(self.vec)):
           sum += self.vec[i] * vec2.vec[i]
        return sum

    def __len__(self):
        return len(self.vec)

v1 =  Vector([1, 4, 6, 6])
v2 =  Vector([1, 6, 9])
print(len(v1))
print(len(v2))