from datetime import datetime
from enum import Enum as PyEnum

from sqlalchemy import (Integer,
                        DateTime,
                        ForeignKey,
                        UniqueConstraint,
                        Index,
                        CheckConstraint,
                        Enum)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.db.database import Base


class NotificationType(PyEnum):
    NEW_POST = "new_post"
    SUBSCRIPTION = "subscription"


class Subscription(Base):
    __tablename__ = "subscriptions"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"))
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))

    user: Mapped["User"] = relationship(back_populates="subscriptions")
    category: Mapped["Category"] = relationship(back_populates="subscriptions")

    __table_args__ = (
        UniqueConstraint(
            "user_id", "category_id",
            name="unique_user_category_subscribe"),
        Index("idx_user_category_subscribe",
                         "user_id", "category_id")
    )


class Like(Base):
    __tablename__ = "likes"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    post_id: Mapped[int] = mapped_column(ForeignKey("posts.id"))
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))

    user: Mapped["User"] = relationship(back_populates="likes")
    post: Mapped["Post"] = relationship(back_populates="likes")

    __table_args__ = (
        UniqueConstraint("user_id", "post_id", name="unique_user_post_like"),
        Index("idx_user_post_like", "user_id", "post_id")
    )


class Comment(Base):
    __tablename__ = "comments"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    content: Mapped[str] = mapped_column()
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=True)
    admin_id: Mapped[int] = mapped_column(ForeignKey("admins.id"), nullable=True)
    post_id: Mapped[int] = mapped_column(ForeignKey("posts.id"))
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))

    user: Mapped["User"] = relationship(back_populates="comments")
    admin: Mapped["Admin"] = relationship(back_populates="comments")
    post: Mapped["Post"] = relationship(back_populates="comments")

    __table_args__ = (
        CheckConstraint("user_id IS NOT NULL OR admin_id IS NOT NULL", name="author_check"),
        Index("idx_comment_author", "user_id", "admin_id", "post_id")
    )


class Notification(Base):
    __tablename__ = "notifications"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    message: Mapped[str] = mapped_column()
    notification_type: Mapped[NotificationType] = mapped_column(Enum(NotificationType, name="notification_type"))
    is_read: Mapped[bool] = mapped_column(default=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))

    user: Mapped["User"] = relationship(back_populates="notifications")


class View(Base):
    __tablename__ = "views"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))
    post_id: Mapped[int] = mapped_column(Integer, ForeignKey("posts.id"))
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))

    user: Mapped["User"] = relationship(back_populates="views")
    post: Mapped["Post"] = relationship(back_populates="views")

    __table_args__ = (
        UniqueConstraint('user_id', 'post_id', name='unique_user_post_view'),
        Index('idx_user_post_view', 'user_id', 'post_id'),
    )

