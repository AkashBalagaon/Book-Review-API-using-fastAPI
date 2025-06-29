from pydantic import BaseModel
from typing import List

#    *****Review Schemas*****

class ReviewCreate(BaseModel):
    content: str

class Review(BaseModel):
    id: int
    content: str

    class Config:
        orm_mode = True  # Use this if you're using Pydantic v1

#    *****Book Schemas*****
class BookCreate(BaseModel):
    title: str
    author: str

class Book(BaseModel):
    id: int
    title: str
    author: str
    reviews: List[Review] = []

    class Config:
        from_attributes = True  #  This is for Pydantic v2
