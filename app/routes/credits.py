from fastapi import APIRouter, HTTPException, Depends, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from .. import models, schemas
from app.database import get_db

router = APIRouter()


@router.post("/credits", response_model=schemas.Credit, status_code=201)
def add_credit(credit: schemas.CreditCreate, db: Session = Depends(get_db)):
    existing = db.query(models.Credit).filter(models.Credit.token_id == credit.token_id).first()
    if existing:
        raise HTTPException(status_code=400, detail="Token ID already exists")
    new_credit = models.Credit(**credit.dict())
    db.add(new_credit)
    db.commit()
    db.refresh(new_credit)
    return new_credit


@router.get("/credits", response_model=List[schemas.Credit])
def get_all_credits(db: Session = Depends(get_db)):
    return db.query(models.Credit).all()


@router.get("/credits/{token_id}", response_model=schemas.Credit)
def get_credit_by_token_id(token_id: str, db: Session = Depends(get_db)):
    credit = db.query(models.Credit).filter(models.Credit.token_id == token_id).first()
    if not credit:
        raise HTTPException(status_code=404, detail="Credit not found")
    return credit

@router.get("/credits/search/{project_type}", response_model=List[schemas.Credit])
def search_credits_by_type(project_type: str, db: Session = Depends(get_db)):
    query = db.query(models.Credit).filter(
        models.Credit.project_type.ilike(f"%{project_type}%")
    )
    results = query.all()
    if not results:
        raise HTTPException(status_code=404, detail="Credit not found")
    return results
