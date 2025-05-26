from datetime import datetime
from enum import Enum as PyEnum

from sqlalchemy import DateTime, ForeignKey, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.db.database import Base


class AdminNotificationType(PyEnum):
    SUBSCRIPTION = "subscription"
    LIKE = "like"
    COMMENT = "comment"


class Admin(Base):
    __tablename__ = "admins"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    email: Mapped[str] = mapped_column(unique=True, index=True)
    photo_url: Mapped[str] = mapped_column(nullable=True)
    first_name: Mapped[str] = mapped_column()
    last_name: Mapped[str] = mapped_column()
    bio: Mapped[str] = mapped_column(nullable=True)
    experience: Mapped[str] = mapped_column(nullable=True)
    password_hash: Mapped[str] = mapped_column()
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))

    social_links: Mapped[list["SocialLink"]] = relationship(back_populates="admin")
    posts: Mapped[list["Post"]] = relationship(back_populates="admin")
    playlists: Mapped[list["Playlist"]] = relationship(back_populates="admin")
    comments: Mapped[list["Comment"]] = relationship(back_populates="admin")
    categories: Mapped[list["Category"]] = relationship(back_populates="admin")
    tags: Mapped[list["Tag"]] = relationship(back_populates="admin")
    notifications: Mapped[list["AdminNotification"]] = relationship(back_populates="admin")


class AdminNotification(Base):
    __tablename__ = "admin_notifications"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    admin_id: Mapped[int] = mapped_column(ForeignKey("admins.id"))
    message: Mapped[str] = mapped_column()
    notification_type: Mapped[AdminNotificationType] = mapped_column(Enum(AdminNotificationType))
    related_id: Mapped[int] = mapped_column(nullable=True)
    is_read: Mapped[bool] = mapped_column(default=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))

    admin: Mapped["Admin"] = relationship(back_populates="notifications")


class SocialLink(Base):
    __tablename__ = "social_links"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    admin_id: Mapped[int] = mapped_column(ForeignKey("admins.id"))
    platform: Mapped[str] = mapped_column()
    url: Mapped[str] = mapped_column()
    is_public: Mapped[bool] = mapped_column(default=True)

    admin: Mapped["Admin"] = relationship(back_populates="social_links")
