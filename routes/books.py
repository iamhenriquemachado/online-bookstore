from fastapi import APIRouter, HTTPException
from models.Book import Book
import sqlite3
from typing import List, Dict
from helpers.validators import input_title_validation

router = APIRouter()

# Get all books in the database
@router.get('/all', response_model=List[Dict])
async def get_all_books():
    try:
        with sqlite3.connect('database/onlinestore.db') as database:
            database.row_factory = sqlite3.Row
            cursor = database.cursor()
            print("Fetching book all books in the database.")

            query = '''SELECT title, author, price FROM Books'''
            cursor.execute(query)

            books = cursor.fetchall()
            return [dict(book) for book in books]
    
    except:
        raise HTTPException(status_code=404, detail="Item not found") 

# Get books by ID 
@router.get('/{id}')
async def get_books_by_id(id: int):
    try:    
        with sqlite3.connect('database/onlinestore.db') as database:
            cursor = database.cursor()
            print(f"Fetching book ID: {id}")

            query = '''SELECT title, author, price FROM Books WHERE id = ?'''
            cursor.execute(query, (id,))  
            book = cursor.fetchone()

            if book is None:
                raise HTTPException(status_code=404, detail="Book not found")  

            print(f"Fetched book: {book}")

            
            return {"title": book[0], "author": book[1], "price": book[2]}
            
    except Exception as e:
        print(f"Error fetching book: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

# Insert a new book 
@router.post('/post')
async def new_book(bookdata: Book):
    bookdata.id = Book.generate_id()

    with sqlite3.connect('database/onlinestore.db') as database:
        try:
            cursor = database.cursor()
            # Check for duplicated records in the database 
            query_check_duplicated = """SELECT title from Books WHERE title = (?)"""
            cursor.execute(query_check_duplicated, (bookdata.title, ))
        
            if cursor.fetchone():
                raise HTTPException(status_code=409, detail="Book already exists.")
            
            validation_result = input_title_validation(bookdata.title)
            
            if validation_result != True: 
                raise HTTPException(status_code=422, detail=validation_result)

            query = """INSERT INTO Books(title, author, price, description, stockquantity) VALUES (?, ?, ?, ?, ?)"""
            cursor.execute(query,
                (bookdata.title, bookdata.author, bookdata.price, bookdata.description, bookdata.stockquantity))
            
            database.commit()

            return {
                "status": "sucess", 
                "message": "Book created successfully", 
                "data": {
                    "title": bookdata.title, 
                    "author": bookdata.author, 
                    "price": bookdata.price, 
                    "description": bookdata.description, 
                    "stockquantity": bookdata.stockquantity
                }

            }


        except sqlite3.Error as e:
            raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")