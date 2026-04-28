from fastapi import FastAPI, HTTPException

app = FastAPI()

PRODUCTS = {
    101: {"id": 101, "name": "Keyboard", "price": 49.99},
    102: {"id": 102, "name": "Mouse", "price" : 19.99},
}

@app.get("/")
def root():
    return {"message": "product-service is running"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/products/{product_id}")
def get_product(product_id: int):
    product = PRODUCTS.get(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product
