class Item:
    # This method that creates a new Item instance.
    def __init__(self, item_id, item_name, item_price):
        self.item_id = item_id
        self.item_name = item_name
        self.item_price = item_price

class itemManager:
    # This method that creates a new Item manager instance.
    def __init__(self, items):
        # store the list of items in a dict
        self.items = items
# display all available products
    def display_items(self):
        print("Available Products:")
        # loop over all the items in the list and print details
        for item in self.items:
            print(f"ID: {item['id']}, Name: {item['name']}, Price: {item['price']}")
# add items to the list
    def add_item(self, item_name, item_price):
         # create a new ID based on the current number of items.
        new_id = str(len(self.items) + 1)
        # Append the new item as a dict to the items list.
        self.items.append({"id": new_id, "name": item_name, "price": item_price})
        print("Item added successfully!")

  # Method to update an existing item's name or price.
    def update_item(self, item_id, item_name=None, item_price=None):
        for item in self.items:
            if item['id'] == item_id:
                if item:
                    item['name'] = item_name
                if item_price is not None:
                    item['price'] = item_price
                print("item updated successfully!")
                return
        print("item not found.")
    # Method to remove an item from the list.
    def remove_item(self, item_id):
        try:
            # loop through the items
            for item in self.items:
                # remove the item from the list if it matches the item id
                if item['id'] == item_id:
                    self.items.remove(item)
                    print("Item deleted successfully!")
                    return
            print("Item not found.")
        except Exception as e:
            # Handle any exceptions that occur during removal.
            print(f"Error removing item: {e}")
# Method to retrieve a specific item based on its id
    def get_item(self, item_id):
        # loop through the items
        for item in self.items:
            if item['id'] == item_id:
                return item
        print("Item not found.")
        return None