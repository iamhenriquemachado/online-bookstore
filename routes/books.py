from models.bookModel import BookModel
from fastapi import APIRouter

router = APIRouter()

# Route: http://127.0.0.1:8000/books/post
# Create a new book
@router.post('/post')
def new_book(bookdata: BookModel):
    bookdata.id = BookModel.generate_id()

    return {
        "message": "New book created!", 
        "bookInformation": bookdata.model_dump()
    }


