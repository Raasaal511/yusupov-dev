from datetime import datetime


from sqlalchemy import DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.database import Base


class Admin(Base):
    __tablename__ = "admins"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    email: Mapped[str] = mapped_column(nique=True, index=True)
    photo_url: Mapped[str] = mapped_column(nullable=True)
    first_name: Mapped[str] = mapped_column()
    last_name: Mapped[str] = mapped_column()
    bio: Mapped[str] = mapped_column(nullable=True)
    experience: Mapped[str] = mapped_column(nullable=True)
    password_hash: Mapped[str] = mapped_column()
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))

    social_links: Mapped[list["SocialLink"]] = relationship(back_populates="admin", cascade="all")


class SocialLink(Base):
    __tablename__ = "social_links"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    admin_id: Mapped[int] = mapped_column(ForeignKey("admins.id"))
    platform: Mapped[str] = mapped_column()
    url: Mapped[str] = mapped_column()
    is_public: Mapped[bool] = mapped_column(default=True)

    admin: Mapped["Admin"] = relationship(back_populates="social_links")
