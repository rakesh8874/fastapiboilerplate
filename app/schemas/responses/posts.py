from pydantic import BaseModel, Field


class PostResponse(BaseModel):
    title: str = Field(..., description="Post name")
    content: str = Field(..., description="Post Content")

    class Config:
        orm_mode = True
