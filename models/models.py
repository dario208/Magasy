from sqlmodel import SQLModel, Field, Relationship, Column, Index
from sqlalchemy import func
from typing import Optional, List
from datetime import datetime
from enum import Enum


# Enums
class RoleEnum(str, Enum):
    client = "client"
    administrator = "administrator"

class OrderStatusEnum(str, Enum):
    processing = "processing"
    shipped = "shipped"
    delivered = "delivered"

class PaymentStatusEnum(str, Enum):
    pending = "pending"
    completed = "completed"
    failed = "failed"


# Models
class User(SQLModel, table=True):
    __tablename__ = "users"
    __table_args__ = (Index("idx_user_email", "email", unique=True),)

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    email: str = Field(nullable=False)
    password: str
    role: RoleEnum
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    # Relationship
    orders: List["Order"] = Relationship(back_populates="user")
    cart: Optional["Cart"] = Relationship(back_populates="user")


class Category(SQLModel, table=True):
    __tablename__ = "categories"
    __table_args__ = (Index("idx_category_name", "name"),)

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    description: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    # Relationship
    products: List["Product"] = Relationship(back_populates="category")


class Product(SQLModel, table=True):
    __tablename__ = "products"
    __table_args__ = (Index("idx_product_name", "name"), Index("idx_product_category", "category_id"))

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    description: Optional[str] = None
    price: float
    stock_quantity: int
    category_id: int = Field(foreign_key="categories.id")
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    # Relationship
    category: Optional[Category] = Relationship(back_populates="products")
    cart_items: List["CartItem"] = Relationship(back_populates="product")
    order_details: List["OrderDetail"] = Relationship(back_populates="product")


class Cart(SQLModel, table=True):
    __tablename__ = "carts"

    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="users.id")
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    # Relationship
    user: Optional[User] = Relationship(back_populates="cart")
    cart_items: List["CartItem"] = Relationship(back_populates="cart")


class CartItem(SQLModel, table=True):
    __tablename__ = "cart_items"
    __table_args__ = (Index("idx_cart_product", "cart_id", "product_id"),)

    id: Optional[int] = Field(default=None, primary_key=True)
    cart_id: int = Field(foreign_key="carts.id")
    product_id: int = Field(foreign_key="products.id")
    quantity: int = Field(default=1)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    # Relationship
    cart: Optional[Cart] = Relationship(back_populates="cart_items")
    product: Optional[Product] = Relationship(back_populates="cart_items")


class Order(SQLModel, table=True):
    __tablename__ = "orders"

    id: Optional[int] = Field(default=None, primary_key=True)
    date: datetime = Field(default_factory=datetime.utcnow)
    user_id: int = Field(foreign_key="users.id")
    status: OrderStatusEnum
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    # Relationship
    user: Optional[User] = Relationship(back_populates="orders")
    order_details: List["OrderDetail"] = Relationship(back_populates="order")
    payments: List["Payment"] = Relationship(back_populates="order")


class OrderDetail(SQLModel, table=True):
    __tablename__ = "order_details"
    __table_args__ = (Index("idx_order_product", "order_id", "product_id"),)

    id: Optional[int] = Field(default=None, primary_key=True)
    order_id: int = Field(foreign_key="orders.id")
    product_id: int = Field(foreign_key="products.id")
    quantity: int
    unit_price: float
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    # Relationship
    order: Optional[Order] = Relationship(back_populates="order_details")
    product: Optional[Product] = Relationship(back_populates="order_details")


class Payment(SQLModel, table=True):
    __tablename__ = "payments"

    id: Optional[int] = Field(default=None, primary_key=True)
    amount: float
    date: datetime = Field(default_factory=datetime.utcnow)
    order_id: int = Field(foreign_key="orders.id")
    status: PaymentStatusEnum
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    # Relationship
    order: Optional[Order] = Relationship(back_populates="payments")
