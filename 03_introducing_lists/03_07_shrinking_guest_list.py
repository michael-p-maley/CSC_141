## Making a guest list.

guest_list = ['Kenny', 'Carter', 'Preston']

# Printing a message to the first name on the list.
message = f"I'm having a dinner later in the week and I would like you to be there {guest_list[0]}."
print(message)

# Printing a message to the second name on the list.
message = f"\nI'm having a dinner later in the week and I would like you to be there {guest_list[1]}."
print(message)

# Printing a message to the third name on the list.
message = f"\nI'm having a dinner later in the week and I would like you to be there {guest_list[2]}."
print(message)

## Adding elements to a list.

message = f"\n{guest_list[0]}, {guest_list[1]}, {guest_list[2]}, I found a bigger table for dinner later this week and will be having more people over."
print(message)

# Adding an element to the list using "insert()"
guest_list.insert(0, 'Tommy')
print(guest_list)

# Adding an element to the middle of the list using "insert()"
guest_list.insert(2, 'Blake')
print(guest_list)

# Adding an element to the end of the list using "append()"
guest_list.append('Danny')
print(guest_list)

# This will print the first name in the list.
message = f"\nYou are invited to my dinner later this week {guest_list[0]}."
print(message)

# This will print the second name in the list.
message = f"\nYou are invited to my dinner later this week {guest_list[1]}."
print(message)

# This will print the third name in the list.
message = f"\nYou are invited to my dinner later this week {guest_list[2]}."
print(message)

# This will print the fourth name in the list.
message = f"\nYou are invited to my dinner later this week {guest_list[3]}."
print(message)

# This will print the fifth name in the list.
message = f"\nYou are invited to my dinner later this week {guest_list[4]}."
print(message)

# This will print the last message in the list.
message = f"\nYou are invited to my dinner later this week {guest_list[-1]}."
print(message)

## Removing elements from a list.

message = f"\nI can only invite two people to my dinner now."
print(message)

'''
"pop()" removes the last element in the list.
"pop(0)" removes the first element in the list.
'''
popped_guests = guest_list.pop()
message = f"\nYou are no longer invited to my dinner {popped_guests}."
print(message)

popped_guests = guest_list.pop(0)
message = f"\nYou are no longer invited to my dinner {popped_guests}."
print(message)

popped_guests = guest_list.pop(1)
message = f"\nYou are no longer invited to my dinner {popped_guests}."
print(message)

popped_guests = guest_list.pop()
message = f"\nYou are no longer invited to my dinner {popped_guests}."
print(message)

message = f"\n{guest_list[0]}, you are still invited."
print(message)

message = f"\n{guest_list[1]}, you are still invited."
print(message)

# Removing elements from a list using "del".

del guest_list[0]
del guest_list[0]
print(guest_list)
