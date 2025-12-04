from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ImageDescriptionBase(BaseModel):
    title: str
    content: str
    tags: Optional[str] = None

class ImageDescriptionCreate(ImageDescriptionBase):
    pass

class ImageDescriptionUpdate(ImageDescriptionBase):
    title: Optional[str] = None
    content: Optional[str] = None

class ImageDescriptionOut(ImageDescriptionBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True