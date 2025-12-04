# app/models/image_description.py
from sqlalchemy import Column, Integer, String, Text
from app.models import Base, TimestampMixin

class ImageDescription(Base, TimestampMixin):
    __tablename__ = "image_descriptions"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), index=True, nullable=False)
    content = Column(Text, nullable=False)          # основное описание
    tags = Column(String, nullable=True)            # например: "cyberpunk,cat,neon"
    author_id = Column(Integer, nullable=False)     # FK на User (можно добавить позже)