from pydantic import BaseModel


class UserResponseSchema(BaseModel):
    id: int
    firstName: str
    lastName: str
    age: int | float
    email: str