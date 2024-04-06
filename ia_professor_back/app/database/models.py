from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from app.database.base import Base


class UserModel(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True,
        autoincrement=True)
    username = Column(String, unique=True, index=True,
        nullable=False)
    email = Column(String, unique=True, index=True,
        nullable=False)
    password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)
    is_staff = Column(Boolean, default=False)
    is_verified = Column(Boolean, default=False)
    products = relationship("Product", back_populates="owner")

class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True, index=True,
        autoincrement=True)
    name = Column(String, unique=False, index=True,
        nullable=False)
    products = relationship("Product", back_populates="category")
    slug = Column(String, unique=True, index=True,)

class Product(Base):
