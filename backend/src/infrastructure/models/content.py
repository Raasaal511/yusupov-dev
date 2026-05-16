from datetime import datetime, timezone
from uuid import UUID, uuid4
from enum import Enum as EnumType
from sqlalchemy import (
    Integer,
    DateTime,
    ForeignKey,
    Table,
    Column,
    Text,
    Enum as SQLEnum,
    Uuid,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.src.infrastructure.database import Base


class PostStatus(str, EnumType):
    DRAFT = "draft"
    PUBLISHED = "published"
    ARCHIVED = "archived"
    DELETED = "deleted"


post_tags = Table(
    "post_tags",
    Base.metadata,
    Column("post_id", Uuid, ForeignKey("posts.id"), primary_key=True),
    Column("tag_id", Uuid, ForeignKey("tags.id"), primary_key=True),
)

playlist_posts = Table(
    "playlist_posts",
    Base.metadata,
    Column("playlist_id", Uuid, ForeignKey("playlists.id"), primary_key=True),
    Column("post_id", Uuid, ForeignKey("posts.id"), primary_key=True),
)


class Post(Base):
    __tablename__ = "posts"

    id: Mapped[UUID] = mapped_column(Uuid, primary_key=True, default=uuid4)
    category_id: Mapped[UUID] = mapped_column(ForeignKey("categories.id"))
    admin_id: Mapped[UUID] = mapped_column(ForeignKey("admins.id"))
    name: Mapped[str] = mapped_column(index=True, unique=True)
    content: Mapped[str] = mapped_column(Text)
    slug: Mapped[str] = mapped_column(index=True, unique=True)
    cover_image_url: Mapped[str] = mapped_column()
    status: Mapped[PostStatus] = mapped_column(
        SQLEnum(PostStatus), default=PostStatus.DRAFT
    )
    published_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=True
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=lambda: datetime.now(timezone.utc)
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
    )

    comments: Mapped[list["Comment"]] = relationship(back_populates="post")
    likes: Mapped[list["Like"]] = relationship(back_populates="post")
    category: Mapped["Category"] = relationship(back_populates="posts")
    admin: Mapped["Admin"] = relationship(back_populates="posts")
    tags: Mapped[list["Tag"]] = relationship(
        secondary=post_tags, back_populates="posts"
    )
    playlists: Mapped[list["Playlist"]] = relationship(
        secondary=playlist_posts, back_populates="posts"
    )
    saved_posts: Mapped[list["SavedPost"]] = relationship(back_populates="post")


class Playlist(Base):
    __tablename__ = "playlists"

    id: Mapped[UUID] = mapped_column(Uuid, primary_key=True, default=uuid4)
    title: Mapped[str] = mapped_column()
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=lambda: datetime.now(timezone.utc)
    )

    posts: Mapped[list["Post"]] = relationship(
        secondary=playlist_posts, back_populates="playlists"
    )


class Category(Base):
    __tablename__ = "categories"

    id: Mapped[UUID] = mapped_column(Uuid, primary_key=True, default=uuid4)
    name: Mapped[str] = mapped_column(unique=True, index=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=lambda: datetime.now(timezone.utc)
    )

    posts: Mapped[list["Post"]] = relationship(back_populates="category")


class Tag(Base):
    __tablename__ = "tags"

    id: Mapped[UUID] = mapped_column(Uuid, primary_key=True, default=uuid4)
    name: Mapped[str] = mapped_column(unique=True, index=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=lambda: datetime.now(timezone.utc)
    )

    posts: Mapped[list["Post"]] = relationship(
        secondary=post_tags, back_populates="tags"
    )
