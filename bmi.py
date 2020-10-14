import sys
print(" BMI: Body Mass Index Calculator v0.1 beta gamma")
userWeight = input("Enter your weight in pounds: ")
userHeight = input("Enter your height: ")

BMI = (703 *float(userWeight)) / (float(userHeight) *  float(userWeight))
print("Your body mass index (BMI) is " + str(BMI) + "%")
