"""You just found a bigger dinner table, so now more space is
available. Think of three more guests to invite to dinner.
• Start with your program from Exercise 3-4 or Exercise 3-5. Add a print()
call to the end of your program informing people that you found a bigger
dinner table.
• Use insert() to add one new guest to the beginning of your list.
• Use insert() to add one new guest to the middle of your list.
• Use append() to add one new guest to the end of your list.
• Print a new set of invitation messages, one for each person in your list."""

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
