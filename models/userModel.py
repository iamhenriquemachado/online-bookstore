from pydantic import BaseModel
from datetime import datetime

class User(BaseModel):
    id: str
    username: str
    email: str
    password: str
    fullname: str
    role: int
    created_at: datetime
    updated_at: datetime
    status: int