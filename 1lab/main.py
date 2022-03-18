from tkinter import *


class Color:
    def __init__(self, name, r, g, b):
        self.name = name
        self.r = r
        self.g = g
        self.b = b

    def __str__(self):
        # return ("Color {" +
        #         " name = " + str(self.name) +
        #         ", r = " + str(self.r) +
        #         ", g = " + str(self.g) +
        #         ", b = " + str(self.b) + "}")
        return f"Color {{name = {self.name}, r = {self.r}, g = {self.g}, b = {self.b}}}"

    def __eq__(self, other):
        if isinstance(other, Color):
            return (self.r == other.r and
                    self.g == other.g and
                    self.b == other.b)
        return NotImplemented


class Rectangle:
    x1 = 100
    y1 = 100

    def __init__(self, x2, y2):
        self.x2 = x2
        self.y2 = y2


def main():
    red = Color("Красный", 255, 0, 0)
    green = Color("Зеленый", 0, 255, 0)
    otherRed = Color("Другой красный", 255, 0, 0)
    print(otherRed)
    print(red)
    print(green)
    print(red == green)
    print(red == otherRed)
    root = Tk()
    root.title("Графические примитивы")
    root.minsize(width=500, height=400)

    canv = Canvas(root, width=500, height=400, bg="grey")
    rect = Rectangle(200, 200)

    canv.create_rectangle(rect.x1, rect.y1, rect.x2, rect.y2, fill="white", outline="blue")

    canv.pack()
    canv.mainloop()


main()
