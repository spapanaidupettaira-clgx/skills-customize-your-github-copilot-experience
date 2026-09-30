import json
from urllib.request import urlopen


def fetch_todo(todo_id):
    url = f"https://jsonplaceholder.typicode.com/todos/{todo_id}"
    with urlopen(url) as response:
        response_text = response.read().decode("utf-8")

    # Convert the JSON response text into a Python dictionary.
    return json.loads(response_text)


def main():
    todo = fetch_todo(1)
    print("Response keys:", list(todo.keys()))


if __name__ == "__main__":
    main()