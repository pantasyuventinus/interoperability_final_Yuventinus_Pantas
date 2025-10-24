from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas, database

router = APIRouter(prefix="/participants", tags=["Participants"])

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Get semua peserta
@router.get("/", response_model=list[schemas.Participant])
def get_participants(db: Session = Depends(get_db)):
    return db.query(models.Participant).all()


# Daftar peserta ke event
@router.post("/", response_model=schemas.Participant)
def register_participant(participant: schemas.ParticipantCreate, db: Session = Depends(get_db)):
    event = db.query(models.Event).filter(models.Event.id == participant.event_id).first()
    if not event:
        raise HTTPException(status_code=404, detail="Event tidak ditemukan")
    if len(event.participants) >= event.quota:
        raise HTTPException(status_code=400, detail="Kuota event sudah penuh")

    db_participant = models.Participant(**participant.dict())
    db.add(db_participant)
    db.commit()
    db.refresh(db_participant)
    return db_participant
