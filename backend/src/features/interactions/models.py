from datetime import datetime

import sqlalchemy
from sqlalchemy import Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.database import Base


class Subscription(Base):
    __tablename__ = "subscriptions"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"), nullable=True)
    playlist_id: Mapped[int] = mapped_column(ForeignKey("playlists.id"), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))

    __table_args__ = (
        sqlalchemy.UniqueConstraint(
            "user_id", "category_id", "playlist_id",
            name="unique_user_category_playlist_subscribe"),
        sqlalchemy.Index("idx_user_category_playlist_subscribe",
                         "user_id,", "category_id", "playlist_id")
    )


class Like(Base):
    __tablename__ = "likes"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    post_id: Mapped[int] = mapped_column(ForeignKey("categories.id"), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))

    __table_args__ = (
        sqlalchemy.UniqueConstraint("user_id", "post_id", name="unique_user_post_like"),
        sqlalchemy.Index("idx_user_post_like", "user_id,", "post_id")
    )


class Comment(Base):
    __tablename__ = "comments"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    content: Mapped[str] = mapped_column()
    user_id: Mapped[int]
    post_id: Mapped[int]
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))


class Notification(Base):
    __tablename__ = "notifications"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.od"))
    message: Mapped[str] = mapped_column()
    notification_type: Mapped[str] # Enum
    is_read: Mapped[bool] = mapped_column(default=False)
    email_sent: Mapped[bool] = mapped_column(default=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))


class View(Base):
    __tablename__ = "views"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))
    post_id: Mapped[int] = mapped_column(Integer, ForeignKey("posts.id"))
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))

    __table_args__ = (
        sqlalchemy.UniqueConstraint('user_id', 'post_id', name='unique_user_post_view'),
        sqlalchemy.Index('idx_user_post_view', 'user_id', 'post_id'),
    )

