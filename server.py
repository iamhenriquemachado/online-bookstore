from fastapi import FastAPI, APIRouter
from routes import books

app = FastAPI()
router = APIRouter()

# Test server
@app.get("/")
def server_running():
    return {"Message": "Server is running ✨"}

app.include_router(books.router, prefix="/books", tags=["books"])

# Start server
if __name__ == "__main__":
    import uvicorn 
    uvicorn.run("server:app", host="127.0.0.1", port=8000, reload=True) 


