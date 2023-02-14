def max3(x, y, z):
    x = int(input("Enter a number: "))
    y = int(input("Enter a number: "))
    z = int(input("Enter a number: "))

    if x > y and x > z:
        return x
    
    if y > x and y > z:
        return y
    
    if z > x and z > y:
        return z