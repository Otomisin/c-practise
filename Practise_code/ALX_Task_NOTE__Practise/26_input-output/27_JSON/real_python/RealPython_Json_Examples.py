import json
import requests

response = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = json.loads(response.text)

# Map of userID to number of complete TODOS for that user
todos_by_user = {}
