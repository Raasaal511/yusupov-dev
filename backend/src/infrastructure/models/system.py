from datetime import datetime, timezone
from uuid import UUID, uuid4
from sqlalchemy import (
    ForeignKey,
    DateTime,
    Text,
    String,
    Boolean,
    Enum as SQLEnum,
    Uuid,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from enum import Enum as EnumType

from src.infrastructure.database import Base


class NotificationUserCategory(str, EnumType):
    NEW_POST = "new_post"
    COMMENT_REPLY = "comment_reply"
    COMMENT_LIKE = "comment_like"


class NotificationStatus(str, EnumType):
    UNREAD = "unread"
    READ = "read"
    ARCHIVED = "archived"
    DELETED = "deleted"


class NotificationAdminCategory(str, EnumType):
    NEW_COMMENT = "new_comment"
    NEW_SUBSCRIPTION = "new_subscription"
    SPAM_REPORT = "spam_report"
    SYSTEM = "system"


class Notification(Base):
    __tablename__ = "notifications"

    id: Mapped[UUID] = mapped_column(Uuid, primary_key=True, default=uuid4)
    user_id: Mapped[UUID] = mapped_column(ForeignKey("users.id"))
    category: Mapped[NotificationUserCategory] = mapped_column(
        SQLEnum(NotificationUserCategory)
    )
    status: Mapped[NotificationStatus] = mapped_column(SQLEnum(NotificationStatus))
    title: Mapped[str] = mapped_column(String(255))
    message: Mapped[str] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=datetime.now(timezone.utc)
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), onupdate=datetime.now(timezone.utc)
    )

    user: Mapped["User"] = relationship(back_populates="notifications")


class NotificationAdmin(Base):
    __tablename__ = "notification_admins"

    id: Mapped[UUID] = mapped_column(Uuid, primary_key=True, default=uuid4)
    admin_id: Mapped[UUID] = mapped_column(Uuid, ForeignKey("admins.id"))
    category: Mapped[NotificationAdminCategory] = mapped_column(
        SQLEnum(NotificationAdminCategory)
    )
    status: Mapped[NotificationStatus] = mapped_column(SQLEnum(NotificationStatus))
    title: Mapped[str] = mapped_column(String(255))
    message: Mapped[str] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=datetime.now(timezone.utc)
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), onupdate=datetime.now(timezone.utc)
    )

    admin: Mapped["Admin"] = relationship(back_populates="notifications")
