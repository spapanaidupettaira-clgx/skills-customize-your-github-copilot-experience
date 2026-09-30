# 📘 Assignment: JSON API Explorer

## 🎯 Objective

Retrieve JSON data from a web API and use Python's standard library to turn the response into a Python dictionary. Display useful fields from the response in a clear format.

## 📝 Tasks

### 🛠️ Fetch and Parse a JSON Response

#### Description
Use the starter code to request a to-do item from the JSONPlaceholder API at `https://jsonplaceholder.typicode.com/todos/1`. Read the response text and convert it from JSON into a Python dictionary.

#### Requirements
Completed program should:

- Use `urllib.request.urlopen()` to send an HTTP request
- Read and decode the response as UTF-8 text
- Use `json.loads()` to convert the response text into a Python dictionary
- Print the dictionary's keys so you can inspect the returned data

### 🛠️ Display a Selected To-Do Item

#### Description
Update the program so the user can enter a to-do item ID from 1 to 200. Request that item from the API and display its title and whether it is completed.

#### Requirements
Completed program should:

- Ask the user for a to-do item ID and include it in the API URL
- Display the item's `title`
- Display `completed` as `Yes` or `No` instead of `True` or `False`
- Work for at least two different valid IDs