# num1 = float(input("enter number 1 :"))
# num2 = float(input("enter number 2 :"))

# choice = input("Enter operation :")   # * , - , / , +

# if choice == "+":                     # addition  
#     print("Result :" , num1 + num2)
# elif choice == "-":                   # subtraction  
#     print("Result :" , num1 - num2)
# elif choice == "*" :                  # multiplication  
#     print("Result :" , num1 * num2)
# elif choice == "/":                    # division
#     if num2 !=0:
#         print("Result :" , num1/num2)
#     else:
#         print("cannot divide by 0")






#  CALCULATOR
num1 = float(input("enter number 1 :"))
num2 = float(input("enter number 2 :"))

print("choose any number form 1 to 4 \n1. addition\n2. subtraction\n3. multiplication\n4. division")

choose_number = int(input( "enter number :" ))
if choose_number == 1:                     # addition  
    print("Result :" , num1 + num2)
elif choose_number ==2:                   # subtraction  
    print("Result :" , num1 - num2)
elif choose_number  == 3 :                  # multiplication  
    print("Result :" , num1 * num2)
elif choose_number == 4:                    # division
    if num2 !=0:
        print("Result :" , num1/num2)
    else:
        print("cannot divide by 0")

