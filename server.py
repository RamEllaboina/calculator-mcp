import os
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI(title="Calculator API")

last_sum = None


class Numbers(BaseModel):
    a: float
    b: float


@app.post("/add")
def add_numbers(numbers: Numbers):
    global last_sum

    last_sum = numbers.a + numbers.b

    return {
        "sum": last_sum
    }


@app.get("/last-sum")
def get_last_sum():
    return {
        "last_sum": last_sum
    }


@app.get("/")
def home():
    return {
        "status": "Calculator API is running"
    }


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8001))

    uvicorn.run(
        app,
        host="0.0.0.0",
        port=port
    )