from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)   #  Important
    author = Column(String, nullable=False)  #  Important

    reviews = relationship("Review", back_populates="book", cascade="all, delete-orphan")

class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String, nullable=False)      # Important
    book_id = Column(Integer, ForeignKey("books.id"), nullable=False)  # Important

    book = relationship("Book", back_populates="reviews")
