from fastapi import FastAPI

app = FastAPI()

cars = [
    {"car_id": 1, "brand": "Toyota", "model": "Camry", "available": True},
    {"car_id": 2, "brand": "Honda", "model": "Civic", "available": False},
    {"car_id": 3, "brand": "Ford", "model": "Mustang", "available": True},
    {"car_id": 4, "brand": "Tesla", "model": "Model 3", "available": True}
]

@app.get("/cars")
def get_cars():
    return {"cars": cars}

@app.get("/health")
def get_health():
    return {"status": "ok"}
