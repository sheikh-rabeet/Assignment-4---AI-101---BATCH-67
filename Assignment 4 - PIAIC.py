# Exercise 3-1: Names
names = ['Haris', 'Mujtaba', 'Ahmed', 'Umer']

# I will print each person's name by accessing each element in the list
for name in names:
    print(name)


# Exercise 3-2: Greetings
names = ['Haris', 'Mujtaba', 'Ahmed', 'Umer']

# I will print personalized greeting messages
for name in names:
    print(f"Hello, {name}! How are you today?")


# Exercise 3-3: Your Own List
transportation = ['Honda motorcycle', 'Tesla car', 'Boeing 747 airplane', 'Harley Davidson motorcycle']

# I will print statements about these transportation items
for item in transportation:
    print(f"I would like to own a {item}.")

# Exercise 3-4: Guest List
guests = ['Haris', 'Mujtaba', 'Ahmed']

# I will print invitation messages
for guest in guests:
    print(f"Hello {guest}, I would like to invite you to dinner!")


# Exercise 3-5: Changing Guest List
guests = ['Haris', 'Mujtaba', 'Ahmed']
unavailable_guest = 'Mujtaba'

# I will print who can't make it
print(f"\nUnfortunately, {unavailable_guest} can't make it to dinner.")

# I will replace the unavailable guest with a new guest
guests.remove(unavailable_guest)
guests.append('Umer')

# I will print new invitations
for guest in guests:
    print(f"Hello {guest}, I would like to invite you to dinner!")

# Exercise 3-6: More Guests
guests = ['Haris', 'Mujtaba', 'Ahmed']

# I will inform that you found a bigger table
print("\nGood news! I found a bigger table and can invite more people.")

# I will insert new guests into the list
guests.insert(0, 'Sarah')      # At the beginning
guests.insert(2, 'Ali')        # In the middle
guests.append('Zara')          # At the end

# I will print new invitations
for guest in guests:
    print(f"Hello {guest}, I would like to invite you to dinner!")


# Exercise 3-7: Shrinking Guest List
guests = ['Haris', 'Mujtaba', 'Ahmed', 'Umer', 'Sarah', 'Ali', 'Zara']

# I will inform that only two people can be invited
print("\nDue to space limitations, I can invite only two people for dinner.")

# I will remove guests one by one
while len(guests) > 2:
    removed_guest = guests.pop()
    print(f"Sorry {removed_guest}, I can't invite you to dinner.")

# I wll print messages to the two remaining guests
for guest in guests:
    print(f"{guest}, you are still invited to dinner!")

# I will clear the list
guests.clear()

# I will print empty list to ensure it's empty
print("\nFinal guest list:", guests)

# Exercise 3-8: Seeing the World
places = ['Paris', 'Tokyo', 'New York', 'Sydney', 'Cape Town']

# i will print original list
print("Original list of places:")
print(places)

# I will print in alphabetical order without modifying the list
print("\nAlphabetical order:")
print(sorted(places))

# I will show original list is still unchanged
print("\nOriginal list (unchanged):")
print(places)

# I will print in reverse-alphabetical order without modifying the list
print("\nReverse alphabetical order:")
print(sorted(places, reverse=True))

# I will show original list is still unchanged
print("\nOriginal list (unchanged again):")
print(places)

# I will reverse the list and print
places.reverse()
print("\nReversed list:")
print(places)

# I will reverse it back and print
places.reverse()
print("\nReversed back to original list:")
print(places)

# I will sort the list alphabetically and print
places.sort()
print("\nSorted list alphabetically:")
print(places)

# I will sort the list in reverse alphabetical order and print
places.sort(reverse=True)
print("\nSorted list in reverse alphabetical order:")
print(places)

# Exercise 3-9: Dinner Guests
guests = ['Haris', 'Mujtaba', 'Ahmed']

# I will print the number of people invited
print(f"\nI am inviting {len(guests)} people to dinner.")

# Exercise 3-10: Every Function
items = ['mountains', 'rivers', 'countries', 'cities', 'languages']

# I will print the list
print("Original list:", items)

# I will use len() to find number of items
print("\nNumber of items in the list:", len(items))

# I will use sorted() to print the list in alphabetical order
print("\nSorted list (alphabetical):", sorted(items))

# I will use reverse() to reverse the list
items.reverse()
print("\nReversed list:", items)

# I will use sort() to sort the list in alphabetical order
items.sort()
print("\nSorted list (in place, alphabetical):", items)

# I will use sort() to sort the list in reverse order
items.sort(reverse=True)
print("\nSorted list (in place, reverse alphabetical):", items)


# Exercise 3-11: Intentional Error
names = ['Haris', 'Mujtaba', 'Ahmed']

# I will try to access an index out of range
try:
    print(names[5])
except IndexError:
    print("\nError: Index out of range!")

# I will correct the error by using an index within the range
print(names[2])  # This will work correctly most probably.

# END OF TASKS