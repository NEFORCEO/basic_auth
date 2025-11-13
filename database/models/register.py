from database.database.db import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer


class Register(Base):
    
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String, index=True) 
    password: Mapped[str] = mapped_column(String, index=True)