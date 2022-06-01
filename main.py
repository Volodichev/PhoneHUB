from typing import Optional, List
from schemas import Book, Author

from fastapi import FastAPI, Query, Path, Body

app = FastAPI()

# ALT+Shift + Enter

@app.get("/")
def read_root():
    return {"Hello": "World"}


# http://127.0.0.1:8000/items/123?q=321
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


@app.get('/user/{pk}/items/{item}/')
def get_user_item(pk: int, item: Optional[str] = None):
    return {"user": pk, "item": item}

@app.post('/author')
def create_author(author: Author = Body(..., embed=True)):
    return {"author": author}

@app.post('/book', response_model=Book, response_model_exclude_unset=True) #Все свойства по-умолчанию исключены
def create_book(item: Book, author: Author, quantity: int = Body(...)): #Body - добавляет в тело запроса
    return {"item": item, "author": author}

@app.get('/book')
def get_book(q: List[str] = Query(["test1","test2"], description='Searching book', deprecated=True)):
    return q

@app.get('/book/{pk}')
def get_single_book(pk: int = Path(..., gt=1, le=20), pages: int = Query(None, gt=2, le=500)): # gt - Мин значение, le - Макс или равно значение
    return {"pk":pk}