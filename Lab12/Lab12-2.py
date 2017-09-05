
def myFunc():
    try:
        x = int(input("Please enter a number."))
        y = int(input("Please enter another number."))
        print(x/y)
    except ValueError:
        print("Input must be a number!")
    except ZeroDivisionError:
        print("Infinity.") 

myFunc()
