from pydantic import UUID4, BaseModel, Field


class UserResponse(BaseModel):
    user_id: UUID4 = Field(...)
    email: str = Field(...)

    class Config:
        orm_mode = True
