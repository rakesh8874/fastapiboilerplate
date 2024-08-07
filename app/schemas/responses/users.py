from pydantic import UUID4, BaseModel, Field


class UserResponse(BaseModel):
    id: UUID4 = Field(...)
    email: str = Field(...)

    class Config:
        orm_mode = True
