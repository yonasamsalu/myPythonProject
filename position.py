def welcome(f_name, l_name):
    print(f_name, l_name)
    print()
    print(f'Welcome to here {f_name} {l_name}')
welcome(l_name= "Amsalu", f_name="Meron") # we can change the position of arguments by assigning with parameters.
print()


welcome("Yonas", l_name="Amsalu")  # "Yonas" is positional argument and "Amsalu" is keyword argument.
    # positional arguments always come first.
#   welcome(f_name="Yonas", "Amsalu")  .This is invalid and shows an error
