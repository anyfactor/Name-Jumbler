# Inpus the name as list
first_name = list(input("First Name: "))
last_name = list(input("Last Name: "))


# Sets actual copy of the lists
first_name1 = first_name.copy()
last_name1 = last_name.copy()

# Jumbles the letters of the name
first_name1[0] = last_name[0]
last_name1[0] = first_name[0]

# Converts list to string
first_name1 = ''.join(first_name1)
last_name1 = ''.join(last_name1)

# Prints the modified name
print("Your stupid name {} {}" .format(first_name1 , last_name1))
