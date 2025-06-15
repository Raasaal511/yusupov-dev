from datetime import datetime


from sqlalchemy import Integer, DateTime, ForeignKey, Table, Column
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.database import Base

post_tags = Table(
    "post_tags",
    Base.metadata,
    Column("post_id", Integer, ForeignKey("posts.id"), primary_key=True),
    Column("tag_id", Integer, ForeignKey("tags.id"), primary_key=True),
)


class Post(Base):
    __tablename__ = "posts"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column()
    content: Mapped[str] = mapped_column()
    category_id: Mapped[int] = mapped_column(Integer, ForeignKey('categories.id'))
    author_id: Mapped[int] = mapped_column(Integer, ForeignKey('admins.id'))
    playlist_id: Mapped[int] = mapped_column(Integer, ForeignKey("playlists.id"))
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))

    likes: Mapped[list["Like"]] =relationship(back_populates="post")
    comments: Mapped[list["Comment"]] = relationship(back_populates="post")
    views: Mapped[list["View"]] = relationship(back_populates="post")
    category: Mapped["Category"] = relationship(back_populates="posts")
    tags: Mapped[list["Tag"]] = relationship(secondary=post_tags, back_populates="posts")
    admin: Mapped["Admin"] = relationship(back_populates="posts")
    playlist: Mapped["Playlist"] = relationship(back_populates="posts")


class Playlist(Base):
    __tablename__ = "playlists"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column()
    author_id: Mapped[int] = mapped_column(Integer, ForeignKey("admins.id"))
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))

    posts: Mapped[list["Post"]] = relationship(back_populates="playlist")
    admin: Mapped["Admin"] = relationship(back_populates="playlists")


class Category(Base):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(unique=True, index=True)
    author_id: Mapped[int] = mapped_column(Integer, ForeignKey("admins.id"))
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))

    posts: Mapped[list["Post"]] = relationship(back_populates="category")
    subscriptions: Mapped[list["Subscription"]] = relationship(back_populates="category")
    admin: Mapped["Admin"] = relationship(back_populates="categories")


class Tag(Base):
    __tablename__ = "tags"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(unique=True, index=True)
    author_id: Mapped[int] = mapped_column(Integer, ForeignKey("admins.id"))
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))

    posts: Mapped[list["Post"]] = relationship(secondary=post_tags, back_populates="tags")
    admin: Mapped["Admin"] = relationship(back_populates="tags")
