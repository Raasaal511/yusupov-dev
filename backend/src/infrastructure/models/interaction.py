from datetime import datetime, timezone
from uuid import UUID, uuid4
from sqlalchemy import ForeignKey, DateTime, Text, String, Boolean, Uuid
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.src.infrastructure.database import Base


class Like(Base):
    __tablename__ = "likes"

    id: Mapped[UUID] = mapped_column(Uuid, primary_key=True, default=uuid4)
    user_id: Mapped[UUID] = mapped_column(ForeignKey("users.id"))
    post_id: Mapped[UUID] = mapped_column(ForeignKey("posts.id"))
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=datetime.now(timezone.utc)
    )

    post: Mapped["Post"] = relationship(back_populates="likes")
    user: Mapped["User"] = relationship(back_populates="likes")


class Comment(Base):
    __tablename__ = "comments"

    id: Mapped[UUID] = mapped_column(Uuid, primary_key=True, default=uuid4)
    user_id: Mapped[UUID] = mapped_column(ForeignKey("users.id"))
    post_id: Mapped[UUID] = mapped_column(ForeignKey("posts.id"))
    admin_id: Mapped[UUID] = mapped_column(ForeignKey("admins.id"))
    parent_comment_id: Mapped[UUID] = mapped_column(
        ForeignKey("comments.id"), nullable=True
    )
    content: Mapped[str] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=datetime.now(timezone.utc)
    )

    post: Mapped["Post"] = relationship(back_populates="comments")
    user: Mapped["User"] = relationship(back_populates="comments")
    admin: Mapped["Admin"] = relationship(back_populates="comments")
    parent_comment: Mapped["Comment"] = relationship(back_populates="child_comments")
    child_comments: Mapped[list["Comment"]] = relationship(
        back_populates="parent_comment"
    )


class Subscription(Base):
    __tablename__ = "subscriptions"

    id: Mapped[UUID] = mapped_column(Uuid, primary_key=True, default=uuid4)
    subscriber_id: Mapped[UUID] = mapped_column(UUID, ForeignKey("users.id"))
    target_id: Mapped[UUID] = mapped_column(UUID, ForeignKey("users.id"))
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=datetime.now(timezone.utc)
    )
    subscriber: Mapped["User"] = relationship(back_populates="subscriptions")
    target: Mapped["User"] = relationship(back_populates="subscribers")


class SavedPost(Base):
    __tablename__ = "saved_posts"

    id: Mapped[UUID] = mapped_column(Uuid, primary_key=True, default=uuid4)
    user_id: Mapped[UUID] = mapped_column(ForeignKey("users.id"))
    post_id: Mapped[UUID] = mapped_column(ForeignKey("posts.id"))
    folder_name: Mapped[str] = mapped_column(String(255))
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=datetime.now(timezone.utc)
    )

    post: Mapped["Post"] = relationship(back_populates="saved_posts")
    user: Mapped["User"] = relationship(back_populates="saved_posts")
