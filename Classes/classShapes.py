class Shapes:
    def __init__(self):
        self.geometric = input("Choose, if u want Square, Circle, Rectangle, Triangle: ")
    
    def choose(self):
        if self.geometric == "Square":
            print("Square has 4 vertical and 4 straight")
        elif self.geometric == "Circle":
            print("Circle has 0 vertical HAHAHA")
        elif self.geometric == "Rectangle":
            print("Rectangle has 4 vertical and 4 straight")
        elif self.geometric == "Triangle":
            print("Triangle has 3 vertical and 3 straight")

geo = Shapes()
geo.choose()