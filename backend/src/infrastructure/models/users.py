from datetime import datetime, timezone
from uuid import UUID, uuid4
from sqlalchemy import ForeignKey, DateTime, Text, String, Boolean, Enum as SQLEnum

from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.src.infrastructure.database import Base
from enum import Enum as EnumType

class SocialPlatform(str, EnumType):
    INSTAGRAM = "instagram"
    YOUTUBE = "youtube"
    TELEGRAM = "telegram"
    DISCORD = "discord"
    GITHUB = "github"
    GITLAB = "gitlab"


class Admin(Base):
    __tablename__ = "admins"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    username: Mapped[str] = mapped_column(String(255))
    email: Mapped[str] = mapped_column(String(255))
    password: Mapped[str] = mapped_column(String(255))
    first_name: Mapped[str] = mapped_column(String(255))
    last_name: Mapped[str] = mapped_column(String(255))
    photo_url: Mapped[str] = mapped_column(String(255))
    bio: Mapped[str] = mapped_column(Text)
    experience: Mapped[int] = mapped_column(String)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.now(timezone.utc))
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), onupdate=datetime.now(timezone.utc))
    last_login_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=True)

    posts: Mapped[list["Post"]] = relationship(back_populates="admin")
    comments: Mapped[list["Comment"]] = relationship(back_populates="admin")
    likes: Mapped[list["Like"]] = relationship(back_populates="admin")
    subscriptions: Mapped[list["Subscription"]] = relationship(back_populates="admin")
    saved_posts: Mapped[list["SavedPost"]] = relationship(back_populates="admin")
    social_links: Mapped[list["SocialLink"]] = relationship(back_populates="admin")


class User(Base):
    __tablename__ = "users"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    username: Mapped[str] = mapped_column(String(255))
    email: Mapped[str] = mapped_column(String(255))
    password: Mapped[str] = mapped_column(String(255))
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.now(timezone.utc))
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), onupdate=datetime.now(timezone.utc))

    subscriptions: Mapped[list["Subscription"]] = relationship(back_populates="subscriber")
    saved_posts: Mapped[list["SavedPost"]] = relationship(back_populates="user")
    comments: Mapped[list["Comment"]] = relationship(back_populates="user")
    likes: Mapped[list["Like"]] = relationship(back_populates="user")
    posts: Mapped[list["Post"]] = relationship(back_populates="user")

    subscribers: Mapped[list["Subscription"]] = relationship(back_populates="target")
    targets: Mapped[list["Subscription"]] = relationship(back_populates="subscriber")


class SocialLink(Base):
    __tablename__ = "social_links"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    user_id: Mapped[UUID] = mapped_column(UUID, ForeignKey("users.id"))
    platform: Mapped[SocialPlatform] = mapped_column(SQLEnum(SocialPlatform), nullable=False)
    url: Mapped[str] = mapped_column(String(255), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.now(timezone.utc))
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), onupdate=datetime.now(timezone.utc))

    admin: Mapped["Admin"] = relationship(back_populates="social_links")