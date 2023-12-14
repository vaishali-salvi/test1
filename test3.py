"""Create a class that accepts two numbers. Create another class that fetches the last digit of those two numbers. Create a third class that multiplayer that last two digits.
Example: Class A: Accept two numbers.
		    Class B: Fetches the last digits of the numbers
		    Class C: Multiplay the last two digits.
"""


class A:
    def __init__(self, n1, n2):
        self.n1=str(n1)
        self.n2=str(n2)

    def disp(self):
        n11=str(self.n1)
        n12=str(self.n2)
        print(n11[-1])
        print(n12[-1])

class B(A):
    def __init__(self):
        super.__init__(45,56)

    def dispb(self):
        print(self.n1)
        print(self.n2)    


#a=A(23,34)
b=B()
b.dispb()






