from pydantic import BaseModel


class ProductResponseSchema(BaseModel):
    id: int
    title: str
    price: int | float
