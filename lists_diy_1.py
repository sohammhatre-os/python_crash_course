## Lists Try it Yourself

# UNPACKING A LIST


names = ['Saakshee', 'Aadarsh', 'Dharmin', 'Shreyansha','Siddhi']

for name in names:
	print(f"{name}\n")



# GREETINGS

for name in names:
	print(f"Hi {name}, Welcome to the party \n")


# Your Own List

football_clubs = ['Liverpool', 'Manchester United', 'Manchester City', 'Arsenal','Chelsea']

for club in football_clubs:
 	print(f"I would love to own {club}")


## Program to make a list of football_clubs which is not Liverpool and replace them by Liverpool (List Comprehensions)
liverpool_list = ['Liverpool' for club in football_clubs if club != 'Liverpool']
print(liverpool_list)

## Replacing an item in a list
football_clubs[1]='FC Barcelona'

print(football_clubs)


## Adding an Item to a List (appends at last):
football_clubs.append('Bayern Munchen')
print(f"Item appended: {football_clubs}")


## Insert an item to a list, computationally expensive:
football_clubs.insert(0,'Young Guns FC')
print(f"Item inserted, Look how it has moved the list: {football_clubs}")

## Deleting an item from position with del function:
del football_clubs[0]
print(f"Item deleted, {football_clubs}")

## Deleting an item with the pop method, default will pop last element, arguement will pop element at that position 
print(f"You popped this club out: {football_clubs.pop(2)}, {football_clubs.pop()}")








