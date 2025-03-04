# perimeter and area of a square and rectange

shape = input("Enter shape (square/rectangle): ").lower()


if shape == "square":
    side = float(input("Enter side length: "))
    print("Area:", side * side)
    print("Perimeter:", 4 * side)

elif shape == "rectangle":
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))
    print("Area:", length * width)
    print("Perimeter:", 2 * (length + width))

else:
    print("Invalid shape!")
