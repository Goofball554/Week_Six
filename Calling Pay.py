import Pay
import Tax

paybeforetax = Pay.computepay(input, input)
print("Your pay before tax is: ", paybeforetax)
print("Your pay after tax is: ", Tax.computetax(paybeforetax))