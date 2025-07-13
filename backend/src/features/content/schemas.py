from pydantic import BaseModel


class PostBase(BaseModel):
    id: int
    title: str
    content: str
    category_id: int
    author_id: int
    tags: None = None
    playlist_id: int | None = None


class PostCreate(BaseModel):
    title: str
    content: str
    category_id: int


class PostUpdate(BaseModel):
    title: str
    content: str
    category_id: int
    playlist_id: int
    tags: list[int]


class PlaylistBase(BaseModel):
    id: int
    title: str


class PlaylistCreate(PlaylistBase):
    pass


class CategoryBase(BaseModel):
    id: int
    name: str


class CategoryCreate(BaseModel):
    name: str


class TagBase(BaseModel):
    id: int
    name: str
    author_id: int


class TagCreate(TagBase):
    pass