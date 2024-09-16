def list_demo():
    my_list = ["H", "e", "l", "l", "o"]
    my_list.append("!")
    for item in my_list:
        print(item, end='')
    print('')
    print(f"length: {len(my_list)}")
    print(my_list[0:6])
    print(my_list[4:])
    print(my_list[-3:])
    my_list.remove('l')
    my_list.insert(4, 'l')
    print(my_list)

def tuple_demo():
    print("tuple demo")

def set_demo():
    print("set demo")

def dict_demo():
    print("dict demo")

def main():
    list_demo()
    tuple_demo()
    set_demo()
    dict_demo()

if __name__ == "__main__":
    main()