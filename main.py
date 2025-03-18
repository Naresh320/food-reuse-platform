from fastapi import FastAPI
from routers import items, users

app = FastAPI(title="Food Reuse Platform")

# Include the routers
app.include_router(items.router)
app.include_router(users.router)

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the Food Reuse Platform!"}

