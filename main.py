from fastapi import FastAPI
from app.routes import user_routes

app = FastAPI()

# Include routes from other modules
app.include_router(user_routes.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
