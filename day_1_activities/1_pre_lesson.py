# this is what we will use for the video intro to dictionaries
# dictionary = a collection of {key;value} pair
                # ordered and changeable. No duplicates

capitals = {"USA": "Washington D.C",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}
# print(dir(capitals))
# print(help(capitals))
# print(capitals.get("USA"))
# if capitals.get("Japan"):
#     print("That capital exists")
# else:
#     print("That Capital doesn't exist")
# capitals.update({"Germany": "Berlin"})
# capitals.update({"Usa": "Detroit"})
# capitals.pop("China")
# capitals.popitem()
# capitals.clear()
# key = capitals.keys()

# for key in capitals.keys():
#     print(key)

# values = capitals.values()
# for value in capitals.values():
#     print(value)

items = capitals.items()
for key, value in capitals.values():
    print(f"{key}: {value}")