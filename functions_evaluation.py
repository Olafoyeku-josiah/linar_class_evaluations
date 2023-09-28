#program to calculate volume of a rectangle
length=input(" enter the length value: ")
breadth=input(" enter the breadth value: ")
height=input(" enter the height value: ")
def volume(length,breadth,height):
    """this function calculates the volume of a rectangle,
    it takes three parameters
    length=int , breadth=int and height=int"""
    volume=int(length) * int(breadth) * int(height)
    print("The volume of the rectangle is {}cm".format(volume))
volume(length,breadth,height)