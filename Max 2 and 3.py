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

def max2(a, b):
    a = int(input("Enter a number: "))
    b = int(input("Enter a number: "))

    if a > b:
        return a
    
    if b > a:
        return b

result = max3(input, input, input)
print("The maximum is: ", result)

result = max2(input, input)
print("The maximum is: ", result)