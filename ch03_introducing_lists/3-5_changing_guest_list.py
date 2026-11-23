"""You just heard that one of your guests can't make the
dinner, so you need to send out a new set of invitations. You'll have to think of
someone else to invite.
• Start with your program from Exercise 3-4. Add a print() call at the end
of your program stating the name of the guest who can't make it.
• Modify your list, replacing the name of the guest who can't make it with
the name of the new person you are inviting.
• Print a second set of invitation messages, one for each person who is still
in your list."""

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
