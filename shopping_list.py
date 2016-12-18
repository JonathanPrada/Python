#TODO: Need to add delete option
#TODO: Need to add send functionality
#TODO: Need to validate input

#make a list to hold onto our items
shopping_list = []

#print out instructions on how to use the app
def show_help():
  print("What should we pick up at the store?")
  print("""
Enter 'DONE' to stop adding to the list.
Enter 'HELP' to show this again.
Enter 'SHOW' to show the shopping list.
""")

#Show the items in the list
def show_list():
    print("Here are the current items listed: ")
    for item in shopping_list:
      print(item)
      
#add new items to our list
def add_item():
    shopping_list.append(new_item)
    print("Added {}. The list has now {} items.".format(new_item, len(shopping_list)))

show_help()

while True:
  #ask for new items
  new_item = input("> ")

  #be able to quit the app
  if new_item == 'DONE':
    break
  elif new_item == 'HELP':
    show_help()
    continue
  elif new_item == 'SHOW':
    show_list()
    continue
  else:
    add_item()

#print out the list
print("Here's your list:")
for item in shopping_list:
    print(item)
  
