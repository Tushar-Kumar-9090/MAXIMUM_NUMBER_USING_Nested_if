

## WAP to find maximum among 5 number using nested




num1=int(input("Enter The 1st Number: "))
num2=int(input("Enter The 2nd Number: "))
num3=int(input("Enter The 3rd Number: "))
num4=int(input("Enter The 4th Number: "))
num5=int(input("Enter The 5th Number: "))
if num1>num2:
    if num1>num3:
        if num1>num4:
            if num1>num5:
                print("num1 is maximum")
            else:
                print("num5 is maximum")
        else:
            if num4>num5:
                print("num4 is maximum")
            else:
                print("num5 is maximum")
    else:
        if num3>num4:
            if num3>num5:
                print("num3 is maximum")
            else:
                print("num5 is maximum")
        else:
            if num4>num5:
                print("num4 is maximum")
            else:
                print("num5 is maximum")
else:
    if num2>num3:
        if num2>num4:
            if num2>num5:
                print("num2 is maximum")
            else:
                print("num5 is maximum")
        else:
            if num4>num5:
                print("num4 is maximum")
            else:
                print("num5 is maximum")
    else:
        if num3>num4:
            if num3>num5:
                print("num3 is maximum")
            else:
                print("num5 is maximum")
        else:
            if num4>num5:
                print("num4 is maximum")
            else:
                print("num5 is maximum")