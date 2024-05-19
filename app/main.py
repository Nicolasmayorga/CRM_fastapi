from fastapi import FastAPI
from app.core.config import settings

app = FastAPI(title=settings.PROJECT_NAME)

@app.get("/")
def read_root():
    return {"message": "Welcome to the CRM system"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
