from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Item(BaseModel):
    name:str
    description: str = None
    price:float
    tex:float = None

@app.get("/")
async def read_root():
    return {"message":"Hello, World!"}
    
@app.post("/items/")
async def create_item(item: Item):
    return {"item_name":item.name, "item_price":item.price}
    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

        
