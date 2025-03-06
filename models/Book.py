from pydantic import BaseModel, Field
from typing import ClassVar 
import itertools

class Book(BaseModel):
    id: int = Field(None, description="ID of the book, auto-generated")
    title: str
    author: str
    price: float
    description: str
    stockquantity: int


    _id_counter: ClassVar[itertools.count] = itertools.count(1)
    
    @classmethod
    def generate_id(cls) -> int:
        return next(cls._id_counter)

