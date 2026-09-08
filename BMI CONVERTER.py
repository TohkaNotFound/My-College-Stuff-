weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in centimeters: "))

BMI = weight / (height * height / 10000)

print("Your BMI is: {:.2f}".format(BMI))