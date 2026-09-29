from fastapi import FastAPI

app = FastAPI(title="Simple API")


@app.get("/")
def read_root():
    return {"message": "Welcome to the API!"}


# TODO: Add your items list, models, and API routes here
