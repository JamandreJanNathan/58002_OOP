import math

class Circle:
  def __init__(attr, radius):
    attr.radius=radius
    attr.pi=math.pi

  def perimeter(attr):
    return 2*attr.pi*attr.radius

  def area(attr):
    return attr.pi*(attr.radius**2)

  def display(attr):
    print("perimeter =", attr.perimeter())
    print("Area =", attr.area())

samplecircle=Circle(float(input("Input radius: ")))
samplecircle.display()