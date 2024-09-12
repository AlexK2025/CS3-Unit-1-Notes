def bake_cookie(ingredients, instructions, temperature, cutter="heart",  for_sarslols=True, name="haley"):
    print("ingredirents")
    for ingredient in ingredients:
        print(ingredient)
    print("insterucshins", end="\n")
    print(instructions)
    print(f"The oven is at {temperature} degreez")
    print(f"Shape: {cutter}")   
        
def main():
    ingredients = ["flour", "sugar", "eggs", "butter", "chocolate chips", "cinnamon"]
    instructions = "mix and bake"
    temp = 300
    bake_cookie(ingredients, instructions, temp, "omar")
    

if __name__ == "__main__":
    main()