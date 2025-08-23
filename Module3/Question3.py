# ask user for biological SEX, which is not the same as GENDER and also does not account for intersex people or people who have undergone hormone replacement therapy
sex = input("Enter biological gender (male/female): ")
sex = sex.lower()

# ask user for hemoglobin value
hemVal = float(input("Enter hemoglobin value (g/l): "))

# evaluate hemoglobin if sex is set to female
if sex == "female":
    if hemVal < 117:
        print("Your hemoglobin is low.")
    elif hemVal > 155:
        print("Your hemoglobin is high.")
    else:
        print("Your hemoglobin is normal.")

# evaluate hemoglobin if sex is set to male
if sex == "male":
    if hemVal < 134:
        print("Your hemoglobin is low.")
    elif hemVal > 167:
        print("Your hemoglobin is high.")
    else:
        print("Your hemoglobin is normal.")

# return error if user said neither male nor female
if (sex != "male") & (sex != "female"):
    print("Invalid gender.")