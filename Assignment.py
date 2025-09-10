# Task 1

a = [int(i) for i in input("Enter first list: ").split()]
b = [int(i) for i in input("Enter second list: ").split()]

c = a + b
c.sort()
print("Sorted merged list:", c)

# Task 2

print("Smallest:", min(c))
print("Largest:", max(c))

# Task 3

birthdays = {
    "Usman": "2002",
    "Waleed": "2003",
    "Nouman": "2004"
}

print("\nWelcome to the birthday dictionary. We know the birthdays of:")
for i in birthdays:
    print(i)

name = input("Who's birthday do you want to look up? ")
if name in birthdays:
    print(name, "was born in", birthdays[name])
else:
    print("Not found in dictionary.")

# Task 4

sample_dict = {
    "name": "Usman",
    "age": 22,
    "salary": 45000,
    "city": "Attock"
}

keys = ["name", "salary"]
newdict = {}
for k in keys:
    newdict[k] = sample_dict[k]

print("New dictionary:", newdict)
