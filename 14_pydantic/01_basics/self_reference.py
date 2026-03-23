from typing import List, Optional
from pydantic import BaseModel

class Comment(BaseModel):
    id: int
    content: str
    replies: Optional[List["Comment"]] = None

Comment.model_rebuild()

comment = Comment(id=1, content="Hello", replies=[
    Comment(id=2, content="World"),
    Comment(id=3, content="Goodbye")
    ])

print(comment)