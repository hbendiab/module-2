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

#Exercice 2 : tuple 


# TODO: Create a tuple with your favorite colors
favorite_colors1 = ("orange","rouge","beige","marron")


favorite_colors2 = ("blue", "yellow", "purple")

# TODO: Try to modify one of the colors (this should raise an error)


# TODO: Find the index of a specific color




# TODO: Create a new tuple by concatenating two existing tuples

new_tuple = favorite_colors1 + favorite_colors2 
print(new_tuple)

# Print the results of each operation



#exercice 3 : Dictionary 

person = {
    "name": "Hanine",
    "age": 26,
    "city": "Paris"
}

print(person)

person["occupation"] = "Etudiante"
print(person)

# TODO: Update the person's age

person["age"] = 27
print(person)


del person["city"]
print(person)


# TODO: Print all keys, then all values
print("clés :", person.keys())
print("valeurs :", person.values())

print("Clés :")
for key in person.keys():
    print(key)

print("valeurs:")
for values in person.values():
    print(values)


# TODO: Check if a specific key exists in the dictionary

if "name" in person : 
    print("La clé 'name'existe.")
else:
    print("La clé 'name' n'existe pas.")

# Print the final dictionary

print("Dictionnaire final :", person)


#Exercice 4 : 
# TODO: Create two sets of numbers

# TODO: Find the union of the two sets

# TODO: Find the intersection of the two sets

# TODO: Find the difference between the first and second set

# TODO: Add a new element to one of the sets

# TODO: Remove an element from one of the sets

# Print the results of each operation



## Exercise 5: Nested Data Structures
# TODO: Create a list of dictionaries representing books (title, author, year)

books = [
{"title": "L'Etranger", "author": "Albert Camus", "year": 1942},
{"title": "1984", "author": "George Orwell", "year": 1949},
{"title": "Le Petit Prince", "author": "Antoine de Saint-Exupéry", "year": 1943}
]
print(books)

   
for book in books: 
    print(f"{book["title"]} - {book["author"]} ({book["year"]})")

# TODO: Add a new book to the list

person["occupation"] = "Etudiante"
print(person)

books.append({"title": "Aurevoir", "author": "Benjamin Button", "year": 2045})
print(books)

print("Dictionnaire final :", books)

# TODO: Sort the list of books by year = sorted 

sorted_books = sorted(books, key=lambda x: x["year"])
for book in sorted_books: 
    print(f"{book['year']} - {book['title']} — {book['author']}")


# TODO: Create a dictionary where keys are authors and values are lists of their books
astro = { 
    "hanine bendiab" :["cancer", "balance", "scorpion"],
    "thomas cochet" :["cancer", "balance", "vierge"],
    "rea preci" : ["verseau","sagittaire"] 
    }
print(astro)

# TODO: Print all books by a specific author

author = "George Orwell"

print(f"Livres de {author} :")
for book in books[author]:
    print("-", book)

# Print the final nested data structure