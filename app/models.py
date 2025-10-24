from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    date = Column(Date, nullable=False)
    location = Column(String(100), nullable=False)
    quota = Column(Integer, nullable=False)

    # Relasi: satu event bisa punya banyak peserta
    participants = relationship("Participant", back_populates="event")


class Participant(Base):
    __tablename__ = "participants"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    event_id = Column(Integer, ForeignKey("events.id"))

    event = relationship("Event", back_populates="participants")
