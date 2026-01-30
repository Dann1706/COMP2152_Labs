cart = ["Apple", "Banana", "Milk", "Bread", "Apple", "Eggs"]

appleCount = cart.count("Apple")
print(f"Number of Apples: {appleCount}")

milkPossition = cart.index("Milk")
print(f"Milk index is: {milkPossition}")

cart.remove("Apple") 
removedItem = cart.pop() # Delete the last item of the list

print (f"Removed items using pop: {removedItem}")
print ("Is Banana in the list? " , "Banana" in cart)

