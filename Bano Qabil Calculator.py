print ( "Bano Qabil Calculator")

num1 = float(input("Enter First Number Here: "))
num2 = float(input("Enter Second Number Here: "))

print("press 1 for Addition \npress 2 for Subtraction \npress 3 for Multiplication \npress 4 for Division")

choice = int(input("enter your choice form 1-4 "))

if choice == 1:
    print ("The Addition of two given number is",num1 + num2)
elif choice == 2:
    print ("The Subtraction of two given number is",num1 - num2)
elif choice == 3:
    print ("The multiplication of two given number is",num1 * num2)
elif choice == 4:
    print ("The Division of two given number is",num1 / num2)

else:
    print ("invalid input")