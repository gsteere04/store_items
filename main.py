import json
from fastapi import FastAPI, HTTPException
from models import Item

file_path = "store_items.json"
with open(file_path, "r") as json_file:
    data = json.load(json_file)

app = FastAPI()
# item_data is a temporary varible used to get access to the json data.  Only used here.
items = [Item(**item_data) for item_data in data]

# Very self explanatory, just returns the items list.
@app.get("/items")
async def get_items() -> list[Item]:
    return items


#This one just appends a new Item to the items list.  Nothing special really.
@app.post("/items")
async def add_item(item: Item) -> None:
    global items # I opted to use the global statement in all the functions below just to make things easier.  If I hadn't, a new instance of "items" would be made and thats not ideal.
    items.append(item)
    
# I made a for loop to loop through the items list to find the user inputed id.
# Once it found the id, it would update that specific item in the list.
# I opted for a for loop because my original method was using indexing, but indexing only works 
# if the number of items remained the same wihtout adding or removing items from the list.
    
@app.put("/items/{id}")
async def update_item(id: int, updated_item: Item) -> Item:
    global items

    for i in range(len(items)):
        if items[i].id == id:
            items[i] = updated_item
            break
    return updated_item

# I made a for loop to loop through the items list to find the user inputed id.  
# Once it found the id, it would delete it from the list.
# The loop is pretty much the same thing as the update list above.
@app.delete("/items/{id}") 
async def delete_item(id: int) -> dict:
    global items
    for i in range(len(items)):
        if items[i].id == id:
            del items[i]
            break
    return {"message": "Item has been removed."}

