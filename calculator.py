#Calculator.py takes in two ints and outputs basic calculator functions (+, -, *, /)

#Alexis Matheson

def main():
    #Create a test year variable and get input from the user by the input function
    num = input("Enter the first number: ")
    num2 = input("Enter a second number: ")

    try:
        int(num)
        is_num = True
        try:
            int(num2)
            is_num2 = True
            add = calcAdd(num, num2)
            sub = calcSub(num, num2)
            mult = calcMult(num, num2)
            div = calcDiv(num, num2)
        except:
            is_num2 = False
            print("The second input entered is not valid.")
    except:
        is_num = False
        print("The first input entered is not valid.")

def calcAdd(num, num2):
    result = int(num) + int(num2)
    print(str(num) + ' + ' + str(num2) + ' = ' + str(result))

def calcSub(num, num2):
    result = int(num) - int(num2)
    print(str(num) + ' - ' + str(num2) + ' = ' + str(result))

def calcMult(num, num2):
    result = int(num) * int(num2)
    print(str(num) + ' * ' + str(num2) + ' = ' + str(result))

def calcDiv(num, num2):
    result = int(num) / int(num2)
    print(str(num) + ' / ' + str(num2) + ' = ' + str(result))

if __name__ == "__main__":
    main()