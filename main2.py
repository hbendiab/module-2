# Module 2 : Data structure manipulation 
# TODO: Create a list of your favorite fruits

fruits = list(["pasteque","banane","raisins"])
print(fruits)


# TODO: Add a new fruit to the end of the list
fruits = ["pasteque","banane","raisins"]

# Ajouter un nouveau fruit 
fruits.append("grenade")
print(fruits)

#ajouter plusieurs fruits d’un coup avec .extend()
fruits.extend(["orange", "kiwi", "pomme"])
print(fruits)

# TODO: Remove the second fruit from the list
# pour enlever un élément on utilise.pop après ce qu'on veut retirer : 0,1,2,3 etc

fruits.pop(1)
print(fruits)

# TODO: Sort the list alphabetically avec element.sort() et rien entre les parenthèses 

fruits.sort()
print(fruits)

# TODO: Create a new list with the first three fruits, on utilise le slicing [:]
first_three = fruits[0:3]
print(first_three)

# Print the original list and the new list
print(fruits)
print(first_three)