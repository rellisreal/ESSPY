from fastapi import FastAPI
from api.model.base import Item
from api.model.target import Target
from api.modules.http.ping import Ping
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}



@app.post("/items/")
async def create_item(item: Item) -> Item:
    return item

@app.get("/items/")
async def read_items() -> list[Item]:
    return [
        Item(name="Portal Gun", price=42.0),
        Item(name="Plumbus", price=32.0),
    ]
    
    
@app.post("/pingTarget", response_model=Target) #Change this to new class for ping output
async def create_item(target: Target) -> Target:
    ping_runner = Ping(target=target)
    if target.ipv4 is not None:
        result = ping_runner.ping_ipv4()
    elif target.ipv6 is not None: 
        result = ping_runner.ping_ipv6()
    elif target.hostName is not None: 
        result = ping_runner.ping_host_name()
    return result

