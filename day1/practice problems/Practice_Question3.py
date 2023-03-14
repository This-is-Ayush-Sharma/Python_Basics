adult_price = 37550.0
child_price = adult_price / 3

no_adult = int(input())
no_child = int(input())

total = (adult_price*no_adult) + (child_price*no_child)
service = total * 0.07
total2 = total + service
print("Service ",total2)
print("After 10% off", total2*0.90)