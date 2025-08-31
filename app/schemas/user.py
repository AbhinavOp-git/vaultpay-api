from pydantic import BaseModel, EmailStr

# Shared fields
class UserBase(BaseModel):
    username: str
    email: EmailStr

# When creating user
class UserCreate(UserBase):
    password: str

# When returning user (hide password)
class UserOut(UserBase):
    id: int

    class Config:
        from_attributes = True
