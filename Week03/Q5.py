contacts = {
    "Alice" : "555-1234",
    "Bob" : "555-5678",
    "Charlie" : "555-9999"
}

print(f"Alice's number: {contacts["Alice"]}")

contacts["Diana"] = "555-4321"

print(f"Contacts after adding Diana: {contacts}")

contacts["Bob"] = "555-0000"
print(f"Contacts after updating Bob's number: {contacts}")

del contacts["Charlie"]
print(f"Contacts after deleting Charlie: {contacts}")

# .keys() returns a view object that displays a list of all the keys in a dictionary
print(f"All names {contacts.keys()}")

# .values() returns a view object that displays a list of all the values in a dictionary
print(f"All numbers {contacts.values()}")

# len() didplays the length of a dictionary 
print(f"Total contacts {len(contacts)}")


# Dictionary = Built-in, mutable, and ordered collection data structure that stores data in unique key-value pairs