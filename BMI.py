def calculate_bmi(weight, height):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    bmi = weight/(height * height)
    print("Your BMI is "+ str(bmi))

    if bmi > 25.0:
        print("You are Overweight")
    elif bmi < 18.5:
        print("You are UnderWeight")
    else:
        print("You are Normal")


calculate_bmi(weight=57, height=1.73)