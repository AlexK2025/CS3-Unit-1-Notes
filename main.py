def calculate(x, y, operation="add"):
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

def list_iteration(other_list):
    new_list = []
    for item in other_list:
        new_list.append(item*2)
    print(new_list)

    other_list = [item * 2 for item in other_list]
    print(other_list)

def main():
    print(calculate(2, 3))
    print(calculate(2, 3, "subtract"))
    print(calculate(2, 3, operation="subtract"))

    list_iteration([5, 2, 3, 4])

if __name__ == "__main__":
    main()