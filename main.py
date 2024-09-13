def calculate(x, y, operation="equals"):
    if (operation=="add"):
        return x+y
    elif (operation=="subtract"):
        return x-y
    elif (operation=="multiply"):
        return x*y
    elif (operation=="divide"):
        return x/y
    elif (operation=="equals"):
        return x==y
    else:
        return "Invalid operation"

def main():
    print(calculate(5, 5))

if __name__ == "__main__":
    main()