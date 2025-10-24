from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas, database

router = APIRouter(prefix="/events", tags=["Events"])

# Dapatkan koneksi database
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Get semua event
@router.get("/", response_model=list[schemas.Event])
def get_events(db: Session = Depends(get_db)):
    events = db.query(models.Event).all()
    return events


# Tambah event baru
@router.post("/", response_model=schemas.Event)
def create_event(event: schemas.EventCreate, db: Session = Depends(get_db)):
    db_event = models.Event(**event.dict())
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event


# Hapus event
@router.delete("/{event_id}")
def delete_event(event_id: int, db: Session = Depends(get_db)):
    event = db.query(models.Event).filter(models.Event.id == event_id).first()
    if not event:
        raise HTTPException(status_code=404, detail="Event tidak ditemukan")
    db.delete(event)
    db.commit()
    return {"message": "Event berhasil dihapus"}
