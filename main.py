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
    print("!" in my_list)
    my_list.sort()
    print(my_list)

def tuple_demo():
    person = ("Alex", 16, "Roosevelt Island")
    name, age, neighborhood = person
    print(person)

def set_demo():
    my_set = set()
    my_set = {1,2,3,4,6,5,7,8,9,10, 2}
    my_set.add(7)
    my_set.remove(4)
    print(my_set)
    my_set.add(4)
    other_set = {2,4,6,8,10,12}
    print(my_set.union(other_set))
    print(my_set.intersection(other_set))
    print(my_set.difference(other_set))

def dict_demo():
    print("dict demo")

def main():
    list_demo()
    tuple_demo()
    set_demo()
    dict_demo()

if __name__ == "__main__":
    main()