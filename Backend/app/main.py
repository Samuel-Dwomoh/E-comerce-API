from fastapi import FastAPI
from routers import auth, cart, categories, orders, product, reviews, users

app = FastAPI()

app.include_router(auth.router)
app.include_router(categories.router)
app.include_router(cart.router)
app.include_router(orders.router)
app.include_router(product.router)
app.include_router(reviews.router)
app.include_router(users.router)


@app.get("/")
def home():
    return{"Project Status": "Running.."}