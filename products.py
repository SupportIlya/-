# app/routers/descriptions.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db
from app.models.image_description import ImageDescriptionCreate, ImageDescriptionUpdate, ImageDescriptionOut
from app.repositories.descriptions import (
    get_description_by_id,
    create_description,
    update_description,
)

router = APIRouter(prefix="/descriptions", tags=["image descriptions"])

@router.get("/{desc_id}", response_model=ImageDescriptionOut)
async def get_description(desc_id: int, session: AsyncSession = Depends(get_db)):
    desc = await get_description_by_id(session, desc_id)
    if not desc:
        raise HTTPException(status_code=404, detail="Описание не найдено")
    return desc

@router.post("/", response_model=ImageDescriptionOut)
async def create_description_endpoint(
    desc_in: ImageDescriptionCreate,
    session: AsyncSession = Depends(get_db)
):
    desc = await create_description(session, desc_in)
    return desc

@router.put("/{desc_id}", response_model=ImageDescriptionOut)
async def update_description_endpoint(
    desc_id: int,
    desc_in: ImageDescriptionUpdate,
    session: AsyncSession = Depends(get_db)
):
    desc = await get_description_by_id(session, desc_id)
    if not desc:
        raise HTTPException(status_code=404, detail="Описание не найдено")
    updated = await update_description(session, desc, desc_in)
    return updated