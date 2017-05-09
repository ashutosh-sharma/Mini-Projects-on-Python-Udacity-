class Parent():
    def __init__(self,last,color):
        self.lastName=last
        self.eyeColor=color

class Child(Parent):
    def __init__(self,last,color,toys):
        Parent.__init__(self,last,color)
        self.noOfToys=toys


myley_cyrus=Child("Cyrus","Blue",5)
print(myley_cyrus.lastName)
print(myley_cyrus.noOfToys)
