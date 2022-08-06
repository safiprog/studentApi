from ctypes import addressof
from mimetypes import init
from typing import Union
from typing_extensions import Self
from unicodedata import name

from fastapi import FastAPI

app = FastAPI()
class student:
    def __init__(self,name,age,address):
        
      self.name=name
      self.age=age
      self.address=address
    def allDetail(self):
        detail={"name":self.name}
        detail["age"]=self.age
        detail["address"]=self.address
        return detail
        

safi=student("safi hamza",22,"dharavi")

@app.get("/")
def read_root():
    return {"Hello": "World"}
@app.get("/detail")
def getDetail():
    return safi.allDetail()

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
