age = int(input("Enter your age :"));


if age>5:
    nationality = input("Enter your Nationality :");
    if (nationality == "indian"):
        print("Eligible for Aadhar Card");
    else:
        print("Not for other Nationalities");
else:
    print("Age must be Greater than 5");
