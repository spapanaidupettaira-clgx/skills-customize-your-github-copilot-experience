# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a simple REST API with FastAPI by creating endpoints, handling JSON data, and validating request payloads.

## 📝 Tasks

### 🛠️ Set Up the FastAPI Application

#### Description
Create a FastAPI app that serves a basic API and returns JSON responses for a small resource such as books, tasks, or students.

#### Requirements
Completed program should:

- Import `FastAPI` and create an app instance
- Define at least one root endpoint that returns a welcome message as JSON
- Run the app locally using Uvicorn or a similar ASGI server
- Show that the app responds correctly from the browser or a client tool

### 🛠️ Build CRUD Endpoints

#### Description
Expand the app to support creating and retrieving data through REST-style endpoints.

#### Requirements
Completed program should:

- Use an in-memory list or dictionary to store items
- Add a `GET /items` endpoint to return all items
- Add a `GET /items/{item_id}` endpoint to return one item by ID
- Add a `POST /items` endpoint to create a new item from JSON data
- Validate the incoming request body with a Pydantic model or equivalent checks
- Return clear JSON responses for successful and failed requests

### 🛠️ Add Error Handling and Validation

#### Description
Improve the API to handle invalid input and provide more useful feedback to clients.

#### Requirements
Completed program should:

- Validate required fields before storing data
- Return a helpful 404 error when an item is not found
- Return a validation error for invalid request data
- Keep the code organized with clear route functions and models
