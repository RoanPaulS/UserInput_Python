age = int(input("Enter your age :"));

if age>5:
    nationality = input("Enter your Nationality :");
    #if (nationality == "indian" or nationality == "Indian" or nationality == "INDIAN" ):
    if(nationality.upper() == "INDIAN" or nationality.lower() == "indian"):
        print("Eligible for Aadhar Card");
    else:
        print("Not for other Nationalities");
else:
    print("Age must be Greater than 5");
