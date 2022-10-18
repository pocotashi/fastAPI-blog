from lib2to3.pytree import Base
from typing import Optional, List, Dict
from fastapi import APIRouter, Query, Body, Path
from pydantic import BaseModel

router = APIRouter(
    prefix="/blog",
    tags=['blog']
)


class Image(BaseModel):
    url: str
    alias: str


class BlogModel(BaseModel):
    title: str
    content: str
    published: Optional[bool]
    num_of_comments: int
    tags: List[str] = []
    metaData: Dict[str, str] = {'key': 'value'}
    image: Optional[Image] = None


@router.post('/new/{id}')
def create_blog(blog: BlogModel, id: int, version: int = 1):
    return {
        'id': id,
        'data': blog,
        'version': version
    }


@router.post('/new/{id}/comment/{comment_id}')
def create_comment(
    blog: BlogModel,
    id: int,
    comment_title: int = Query(None,
                               title="Title of comment",
                               description="Some describe",
                               alias='comment Title',
                               deprecated=True
                               ),
    content: str = Body(...,
                        regex='^[a-z\s]*$',
                        min_length=10,
                        max_length=50
                        ),
    v: Optional[List[str]] = Query(None),
    comment_id: int = Path(None, gt=5, le=10)
):
    return {
        'blog': blog,
        'id': id,
        'comment_title': comment_title,
        'comment_id': comment_id,
        'content': content,
        'version': v
    }
