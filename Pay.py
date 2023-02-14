def computepay(hours, rate):
    hours = int(input("Enter the hours worked: "))
    rate = int(input("Enter the rate: "))

    if hours > 40:
        pay = 40 * rate + (hours-40)*(1.5*rate)

    else:
        pay = hours * rate

    return pay