try:
    number=int(input("enter your number:"))
    print("the number entered is",number)

except ValueError as ex:
    print("Exeption",ex)