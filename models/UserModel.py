from pydantic import BaseModel


class UserBody(BaseModel):
    email: str
    password: str
    name: str
    noOfProject: int
