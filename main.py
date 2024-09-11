import os

#Task 4
def add(x, y):
    return x + y

#Task 5
def calculate(x, y, operation="equal"):
    if (operation == "add"):
        return x + y
    elif (operation == "subtract"):
        return x - y
    elif (operation == "multiply"):
        return x * y
    elif (operation == "divide"):
        return x / y
    elif (operation == "equal"):
        return x == y
    else:
        return "No operation"

def main():
    print(__name__)
    print("hello world")
    
    #Task 1
    x = 42
    y = 3/4
    z = int('7')
    a = float(5)
    name = "Alex"
    print(type(x), '\n', type(y), '\n', type(z), '\n', type(a), '\n', type(name))

    #Task 2
    rent = 480
    per_day = rent/30
    print(per_day)

    #Task 3
    print("Hello world")
    print(f"My name is {name}")

    #Task 4
    print(add(x, x))

    #Task 5
    print(calculate(x, y, "equal"))

    num = 5
    number = open("number.txt", 'w')
    if (os.stat("number.txt").st_size == 0):
        number.write("5")
    number = open("number.txt", 'r')
    val = int(number.read())
    number = open("number.txt", 'w')
    number.write(str(val + num))
    number.close()

if __name__ == "__main__":
    main()