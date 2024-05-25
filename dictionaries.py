customer= {
    "name": "Yonas",    #name, age and is_certified are key words in the dictionary and have attribites.
    "age": 24,
    "age": 30,
    "is_verified" : True
}
print(customer['name'])
print()

 # print(customer[birthday])  shows an error since birthday is not included in the dictionary.
print(customer.get('birthday'))  # we use get method to remove the above error then the program will run without
                                 #       an error and shows 'None' value.
print()

print(customer.get("Birthdate", "january 13 2000"))  # to supply the defualt value.
print()

customer["name"] = " Abi Amsalu"    # tu update the name.
print(customer["name"])
print()

customer["job"] = "computer science student"   # to add a newu key value pair.
print(customer["job"])