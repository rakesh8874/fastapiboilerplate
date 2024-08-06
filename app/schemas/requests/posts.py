from pydantic import BaseModel, constr


class PostCreate(BaseModel):
    title: constr(min_length=1, max_length=100)
    content: constr(min_length=1, max_length=1000)
