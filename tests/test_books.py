from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

#    *****Unit Test 1: Add Book*****

def test_add_book():
    response = client.post("/books", json={
        "title": "Test Book",
        "author": "Tester"
    })
    assert response.status_code == 201
    assert response.json()["title"] == "Test Book"

#     *****Unit Test 2: Get All Books*****

def test_get_books():
    response = client.get("/books")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

#      *****Integration Test: Cache-Miss Path*****
def test_cache_miss_then_hit():
    # I. Add a new book
    book = client.post("/books", json={
        "title": "Cache Test Book",
        "author": "Cache Author"
    }).json()

    book_id = book["id"]

    # II. Add a review for this book
    client.post(f"/books/{book_id}/reviews", json={
        "reviewer": "Akash",
        "rating": 5,
        "comment": "Great!"
    })

    # III. First fetch
    res_1 = client.get(f"/books/{book_id}/reviews")
    assert res_1.status_code == 200
    assert any(review["rating"] == 5 for review in res_1.json())

    # IV. Second fetch
    res_2 = client.get(f"/books/{book_id}/reviews")
    assert res_2.status_code == 200
