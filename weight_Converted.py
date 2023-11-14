weight = int(input("Weight: "))
unit = input ("(K)g or (L)bs ")
if unit.upper == "l":
    converted = weight * 0.45
    print("Your weight in Kilograms is " + str(converted))
else:
    converted = weight / 0.45
    print("Your weight in Pounds is " + str(converted))
    