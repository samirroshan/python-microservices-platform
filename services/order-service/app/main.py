from fastapi import FastAPI, HTTPException
import httpx

app = FastAPI()

USER_SERVICE_URL = "http://user-service:8000"
PRODUCT_SERVICE_URL = "http://product-service:8000"

@app.get("/")
def root():
    return {"message": "order-service is running"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/orders/demo")
async def create_demo_order():
    with httpx.Client(timeout=5.0) as client:
        user_resp = client.get("http://user-service:8000/users/1")
        product_resp = client.get("http://product-service:8000/products/101")
       
    if user_resp.status_code != 200:
        raise HTTPException(status_code=502, detail="User service error")

    if product_resp.status_code != 200:
        raise HTTPException(status_code=502, detail="Product service error")
    user = user_resp.json()
    product = product_resp.json()
    return {
        "order_id": 5001,
        "user": user,
        "product": product,
        "status": "created",
    }
