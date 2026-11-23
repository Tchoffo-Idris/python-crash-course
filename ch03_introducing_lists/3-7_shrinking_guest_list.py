"""You just found out that your new dinner table won't
arrive in time for the dinner, and you have space for only two guests.
• Start with your program from Exercise 3-6. Add a new line that prints a
message saying that you can invite only two people for dinner.
• Use pop() to remove guests from your list one at a time until only two
names remain in your list. Each time you pop a name from your list, print
a message to that person letting them know you're sorry you can't invite
them to dinner.
• Print a message to each of the two people still on your list, letting them
know they're still invited.
• Use del to remove the last two names from your list, so you have an empty
list. Print your list to make sure you actually have an empty list at the end
of your program."""

# Store living or deceased names of people
names = ["Micheal Jaskson", "Janet Jackson", "Albeit Einstein"]

# Prints and invitation message to names
print(f"Hello {names[0]}, You are invited to the dinner party")
print(f"Hello {names[1]}, You are invited to the dinner party")
print(f"Hello {names[2]}, You are invited to the dinner party")

# Prints does who can't attend the party
print("\nThe following people will not be able to attend the dinner party")
print(f"\t {names[1]}")
print(f"\t {names[2]}")

# This replaces the names of people who cannot attend the party
names[1] = "Sameul Jackson"
names[2] = "Emily Tracy"

# Prints all those who are now attending the party
print("\nThese are the final people who have been invited:")
print(f"Hello {names[0]}, You are invited to the dinner party")
print(f"Hello {names[1]}, You are invited to the dinner party")
print(f"Hello {names[2]}, You are invited to the dinner party")

print(f"\n I have found a bigger dinner table so more guest can come.")

# Inserts guest names at the beginning and at the middle of the list
names.insert(0, "Papa Jackson")
names.insert(2, "50 Cent")

# Appends a guest to the end of the list
names.append("Ice Cube")

# Prints all those who are now attending the party.
print("\nThese are the final people who have been invited:")
print(f"Hello {names[0]}, You are invited to the dinner party")
print(f"Hello {names[1]}, You are invited to the dinner party")
print(f"Hello {names[2]}, You are invited to the dinner party")
print(f"Hello {names[3]}, You are invited to the dinner party")
print(f"Hello {names[4]}, You are invited to the dinner party")
print(f"Hello {names[5]}, You are invited to the dinner party")

print("\n The dinner table won't arrive on time. So only two people will be able to come for the dinner")

# Pop names from the list and prints the popped names
popped_name = names.pop()
print(f"We are sorry {popped_name}, you have been removed from the list!")

popped_name = names.pop()
print(f"We are sorry {popped_name}, you have been removed from the list!")

popped_name = names.pop()
print(f"We are sorry {popped_name}, you have been removed from the list!")

popped_name = names.pop()
print(f"We are sorry {popped_name}, you have been removed from the list!")

# List of People still invited
print("\n Invited Guest")
print(f"Hello, {names[0]}, you are still invited")
print(f"Hello, {names[1]}, you are still invited")

# Using del statement to remove all the names on the list
print("\n An emtyp list")
del names[1]
del names[0]
print(names)