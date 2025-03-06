from models.Book import BookModel
from fastapi import APIRouter, HTTPException

router = APIRouter()

# Route URL: http://127.0.0.1:8000/books/post
@router.post('/post')
async def new_book(bookdata: BookModel):
    bookdata.id = BookModel.generate_id()

    return {
        "message": "New book created!", 
        "bookInformation": bookdata.model_dump()
    }

@router.post('/getbooks')
async def get_all_books():
    try:
        return {
            "bookInformation": bookdata.model_dump()
            }
    except:
        raise HTTPException(status_code=404, detail="Item not found")