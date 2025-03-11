from fastapi import APIRouter, HTTPException
from models.Book import Book
import sqlite3
from typing import List, Dict
from helpers.validators import input_title_validation
from helpers.database import fetch_books, get_db_connection, insert_book, update_book
import logging

router = APIRouter()

# Setup logger
logger = logging.getLogger("uvicorn")

# Get all books in the database
@router.get('/all', response_model=List[Dict])
async def get_all_books():
    try:
            query = '''SELECT title, author, price FROM Books'''
            books = fetch_books(query)
            return [dict(book) for book in books]
    except Exception as e: 
        logger.error(f"Error fetching books: {str(e)}")
        raise HTTPException(status_code=404, detail="Item not found") 

# Get books by ID 
@router.get('/{id}')
async def get_books_by_id(id: int):
    try:    
            query = '''SELECT title, author, price FROM Books WHERE id = ?'''
            books = fetch_books(query, (id, ))

            if not books:
                raise HTTPException(status_code=404, detail="Book not found")  

            book = books[0]            
            return {"title": book["title"], "author": book["author"], "price": book["price"]}
            
    except Exception as e:
        logger.error(f"Error fetching book by ID: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

# Insert a new book 
@router.post('/post')
async def new_book(bookdata: Book):
    bookdata.id = Book.generate_id()

    query_check_duplicated = """SELECT title from Books WHERE title = (?)"""
    books = fetch_books(query_check_duplicated, (bookdata.title, ))

    if books:
        raise HTTPException(status_code=409, detail="Book already exists.")
    
    validation_result = input_title_validation(bookdata.title)
    
    if validation_result != True: 
        raise HTTPException(status_code=422, detail=validation_result)
    
    try: 

        query = """INSERT INTO Books(title, author, price, description, stockquantity) VALUES (?, ?, ?, ?, ?)"""
        book_id = insert_book(query, (bookdata.title, bookdata.author, bookdata.price, bookdata.description, bookdata.stockquantity))


        return {
            "status": "sucess", 
            "message": "Book created successfully", 
            "data": {
                 "id": book_id, 
                "title": bookdata.title, 
                "author": bookdata.author, 
                "price": bookdata.price, 
                "description": bookdata.description, 
                "stockquantity": bookdata.stockquantity
            }

        }


    except sqlite3.Error as e:
            logger.error(f"Database error: {str(e)}")
            raise HTTPException(status_code=500, detail="Database error")
    

# Update books 
@router.put("update/{id}")
async def update_books_by_id(bookdata: Book):
     query = """UPDATE Books SET title = (?), price =  (?), description = (?), stockquantity = (?) WHERE id ?"""
     book_id = update_book(query, (bookdata.title, bookdata.author, bookdata.price, bookdata.description, bookdata.stockquantity))
     
     return {
        "status": "sucess", 
        "message": "Book updated successfully", 
        "data": {
             "id": book_id, 
            "title": bookdata.title, 
            "author": bookdata.author, 
            "price": bookdata.price, 
            "description": bookdata.description, 
            "stockquantity": bookdata.stockquantity
        }

    }