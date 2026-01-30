monday_class = {"Alice", "Bob", "Charlie", "Diana"}
wednesday_class = {"Bob", "Diana", "Eve", "Frank"}
monday_class.add("Grace")
allStudents = monday_class | wednesday_class

# Monday class
print(f"Monday class: {monday_class}")

# Wednesday class
print(f"Wednesday class: {wednesday_class}")

# Both classes
print(f"Attended both classes: {monday_class & wednesday_class}")

# Either one of the two
print(f"Attended either class: {monday_class | wednesday_class}")

# Only monday
print(f"Only monday: {monday_class - wednesday_class}")

# Only one class
print(f"Only once class: {monday_class ^ wednesday_class}")

# is monday_class a subset of the variable allStudents? 
print(f"Is monday subset of all students" , monday_class <= allStudents)