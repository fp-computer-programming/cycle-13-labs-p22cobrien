# Author: CMOB 3/4/2022

def build_vehicle(p1,p2,p3,p4):
    wheels = p1
    axels = p2
    doors = p3
    color = p4
    print("The car has {0} wheels, {1} axels, {2} doors, and is {3}".format(wheels,axels,doors,color))


wheels = input("How many wheels are there? ")
axels = input("How many axels are there? ")
doors = input("How many doors are there? ")
color = input("What color is the car? ")

build_vehicle(wheels,axels,doors,color)
