from fastapi import APIRouter, HTTPException
from models.Book import Book
import sqlite3
from typing import List, Dict

connection = sqlite3.connect('database/onlinestore.db')
connection.row_factory = sqlite3.Row
cursor = connection.cursor()

router = APIRouter()

# Route URL: http://127.0.0.1:8000/books/post
@router.post('/post')
async def new_book(bookdata: Book):
    bookdata.id = Book.generate_id()

    return {
        "message": "New book created!", 
        "bookInformation": bookdata.model_dump()
    }

@router.get('/all', response_model=List[Dict])
async def get_all_books():
    try:
        query = '''SELECT * FROM Books'''
        cursor.execute(query)

        books = [dict(row) for row in cursor.fetchall()]
        connection.close()

        return books
    
    except:
        raise HTTPException(status_code=404, detail="Item not found")  