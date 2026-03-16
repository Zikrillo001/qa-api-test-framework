from pydantic import BaseModel


class LoginResponseSchema(BaseModel):
    accessToken: str
    refreshToken: str
    id: int
    username: str
    email: str