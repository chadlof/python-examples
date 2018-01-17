import math
def quad():
    print("This program find the real solution to a quaddratic\n")

    try:
        a, b, c = eval(input("Enter the coefficeients (a, b, c):"))
        discRoot = math.sqrt(b * b - 4 * a * c)
        root1 = (-b + discRoot) / (2 * a)
        root2 = (-b - discRoot) / (2 * a)
        print("\nThe solutions are: ",root1, root2)
    except ValueError as excObj:
        if str(excObj) == "math domain error":
            print("No real Roots")
        else:
            print("You didn't give me the right number of cofficients.")
    except NameError:
        print("\nYou didn't enter three numbers")
    except TypeError:
        print("\nYour inputs were not all numbers")
    except SyntaxError:
        print("\nYour inputs were not in the correct form")
    except:
        print("\nSomething went wrong!")

quad()

