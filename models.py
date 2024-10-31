from sqlalchemy import Column, Integer, String, ForeignKey, DATE
from sqlalchemy.orm import relationship

from database import Base

class DBAuthor(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), unique=True)
    bio = Column(String(255))


class DBBook(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title   = Column(String(255))
    summary = Column(String(255))
    publication_date = Column(DATE)
    author_id = Column(Integer, ForeignKey("authors.id"))
    author = relationship(DBAuthor)
