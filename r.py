items = ["Milk", "Bread", "Eggs", "Fruit", "Vegetables", "Meat", "Fish", "Cheese", "Yogurt", "Cookies"]
prices = [2.5, 1.0, 0.5, 1.5, 2.0, 3.0, 4.0, 2.5, 1.0, 1.5,50,40]


def shopping_list():
  """Generates and prints a shopping list."""
  print("Here is your shopping list:")
  for item, price in zip(items, prices):
    print(f"{item}: ${price}")


def search_shopping_list(search_item):
  """Searches the shopping list for an item."""
  found = False
  for item, price in zip(items, prices):
    if item.lower() == search_item.lower():
      found = True
      break
  if found:
    print("Found the item:", item, "Price:", price)
  else:
    print("The item was not found.")


def add_item(item):
  """Adds an item to the shopping list."""
  item_as_string = str(item)
  items.append(item_as_string)


def remove_item(item):
  """Removes an item from the shopping list."""
  items.remove(item)


def edit_item(item, new_item):
  """Edits an item on the shopping list."""
  index = items.index(item)
  items[index] = new_item



def clear_shopping_list():
  """Clears the shopping list."""
  items.clear()


def sort_shopping_list():
  """Sorts the shopping list alphabetically."""
  items.sort()


def check_remaining_budget():
  """Checks the remaining budget."""
  global budget
  total_cost = 0
  for price in prices:
    total_cost += price
  remaining_budget = budget - total_cost
  print("The remaining budget is:", remaining_budget)


def main():
  """Main function."""
  global budget
  budget = 100
  while True:
    print("1,Add Item to Shopping List")
    print("2,Remove Item from Shopping List")
    print("3,View Shopping List")
    print("4,Clear Shopping List")
    print("5,Search Item")
    print("6,Sort Shopping List")
    print("7,Check Remaining Budget")
    print("8,Edit Item")
    print("9,Exit")
    action = input("Enter your choice: ")
    if action == "1":
      item = input("Enter the item you want to add: ")
      add_item(item)
    elif action == "2":
      item = input("Enter the item you want to remove: ")
      remove_item(item)
    elif action == "3":
      shopping_list()
    elif action == "4":
      clear_shopping_list()
    elif action == "5":
      item = input("Enter the item you want to search for: ")
      search_shopping_list(item)
    elif action == "6":
      sort_shopping_list()
    elif action == "7":
      check_remaining_budget()
    elif action == "8":
      item = input("Enter the item you want to edit: ")
      new_item = input("Enter the new item name: ")
      edit_item(item, new_item)
    elif action == "9":
      break


if __name__ == "__main__":
  main()
# dfsdf