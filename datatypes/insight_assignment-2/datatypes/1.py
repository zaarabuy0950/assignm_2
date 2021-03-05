class Vehicle:
    color='red'
    door=5


    def change_color(self, color):
       self.color = color

class Car(Vehicle):
    def change_color(self,color):
        self.color = color
        super().change_color("ink")


class Bike(Vehicle):
    door = 0

v=Vehicle()
c = Car()
c.change_color("red")
print(c.color)


b=Bike()

print(b.door)



