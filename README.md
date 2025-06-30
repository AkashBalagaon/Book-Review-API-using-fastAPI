#  Book Review Backend API

   This project is a Backend Technical Assessment for the Backend Engineer role at Predusk Technology.
   It includes API development, data modeling, caching integration, automated tests, and documentation.

#  Tech Stack

    Python with FastAPI

    PostgreSQL (can also use SQLite)

    SQLAlchemy ORM

    Uvicorn ASGI Server

    Redis (for caching)

    Pytest (for automated testing)

#  Project Structure

   book-review-api/
   │
   ├── app/
   │   ├── main.py              
   │   ├── models.py          
   │   ├── schemas.py           
   │   ├── database.py          
   │   ├── cache.py             
   │   └── routes/
   │       ├── books.py         
   │       └── reviews.py       
   │
   ├── tests/
   │   └── test_books.py       
   │ 
   ├── requirements.txt
   └── README.md

#  Setup Instructions
  
   1. Clone the Repo
      
      git clone https://github.com/AkashBalagaon/Book-Review-API-using-fastAPI
      cd book-review-api

   2. Create Virtual Environment & Install Dependencies

      python -m venv venv
      venv\Scripts\activate

      pip install -r requirements.txt

   3. Activate the Environment

      For Windows:
         .\venv\Scripts\activate

      For Mac/Linux:
         source venv/bin/activate

   4. Install Dependencies

     pip install -r requirements.txt

   5. Start the Server (on fixed port 8005)
      
      .\venv\Scripts\uvicorn.exe app.main:app --reload --port 8005

   6. Access API Documentation

      Open your browser and go to:
       http://127.0.0.1:8005/docs

#  API Endpoints

      Method	 Endpoint	            Description
      GET	    /books	               Get all books
      POST	    /books	               Add a new book
      GET	    /books/{id}/reviews	   Get reviews for a book
      POST	    /books/{id}/reviews	   Add a review to a book


#  Features Implemented

      RESTful API Design with proper HTTP status codes

      Data modeling using SQLAlchemy + Pydantic

      Redis caching with fallback if Redis is unavailable

      Automatic migrations

      Swagger/OpenAPI docs

      Automated Testing with pytest


#  Running Tests

    pytest

   This runs:

      Unit test for /books creation and retrieval

      Integration test simulating cache miss logic


#  Notes for Reviewer

         This project was built as part of a Backend Technical Assessment for Predusk Technology.
   I have walked through the entire process in my 5-minute live demo video and documented everything clearlyThank you for the opportunity!


#   Live Walkthrough Video

    This video demonstrates the working of the Book Review API, covering:
      - API endpoints
      - Code structure
      - Error handling
      - Caching with Redis
      - Testing

   # Watch Demo Video 
   
   https://drive.google.com/file/d/1eSHrvMJLMcF7kU51VG_FBkwiarUXxHmI/view?usp=drive_link