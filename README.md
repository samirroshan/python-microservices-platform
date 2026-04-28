# Python Microservices Platform

Python-based microservices platform composed of multiple independent HTTP services that communicate over a Docker Compose network.

## Services

- **user-service**  
  Provides user data via HTTP endpoints such as `/users/{id}`.

- **product-service**  
  Provides product data via HTTP endpoints such as `/products/{id}`.

- **order-service**  
  Calls the user and product services and exposes order-related endpoints such as `/orders/demo`, returning a combined order JSON payload.

## Order Workflow

1. A client sends a request to the `order-service` endpoint `/orders/demo`.
2. `order-service` calls `user-service` to retrieve user information (for example user `1`).
3. `order-service` calls `product-service` to retrieve product information (for example product `101`).
4. `order-service` combines the user and product data into a single order object and returns it as JSON.

This models a simple synchronous orchestration pattern, where the order service coordinates other services to build a response. 

## Project Structure

```text
python-microservices-platform/
├── docker-compose.yml
└── services/
    ├── order-service/
    │   ├── app/
    │   │   └── main.py
    │   ├── Dockerfile
    │   └── requirements.txt
    ├── product-service/
    │   ├── app/
    │   │   └── main.py
    │   ├── Dockerfile
    │   └── requirements.txt
    └── user-service/
        ├── app/
        │   └── main.py
        ├── Dockerfile
        └── requirements.txt
```

## Technologies Used

- Python 3.11
- FastAPI
- Uvicorn
- httpx
- Docker
- Docker Compose
