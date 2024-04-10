from pydantic import BaseModel


class Laptop(BaseModel):
    id: int
    name: str
    description: str
    price: int

class Keyboard(BaseModel):
    id: int
    name: str
    description: str
    price: int

class Mouse(BaseModel):
    id: int
    name: str
    description: str
    price: int