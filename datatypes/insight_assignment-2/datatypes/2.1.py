# class Vehicle:
#     door = 4
#     def __init__(self, color, mileage):
#         self.color = color
#         self.mileage = mileage
#
#     def new_color(self):
#         self.color='blue'
#
#     def new_door(self):
#             self.door = 12
#
#     def get_info(self):
#         return f"{self.color} vehicle has mileage{self.mileage}"
#
# vehicle1 = Vehicle('red', 24)
#
#
#
# print(vehicle1.door)
# vehicle1.new_color()
# print(vehicle1.color)
# vehicle1.get_info()
# print(vehicle1.get_info())
#
# vehicle1.new_door()
# print(vehicle1.door)
#
#
#
#
# def decorator_function(main_function):
#     def inner_function(*args,**kwargs):
#         print('i m a developer')
#         return main_function(*args,**kwargs)
#     return inner_function
#
# # @decorator_function
# def display(msg):
#     print(msg)
#
#
# display=decorator_function(display)
# display('hello,whats up')
#
#
#
# class Vehicle:
#     color='red'
#     door=5
#
#
#     def change_color(self, color):
#        self.color = color
#
# class Car(Vehicle):
#     def change_color(self,color):
#         self.color = color
#         super().change_color("ink")
#
#
# class Bike(Vehicle):
#     door = 0
#
# v=Vehicle()
# c = Car()
# c.change_color("red")
# print(c.color)
#
#
# b=Bike()
#
# print(b.door)
#
#
#
