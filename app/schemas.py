from pydantic import BaseModel
from datetime import date

# ========================
# User Schemas
# ========================

class UserBase(BaseModel):
    name: str
    email: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int

    class Config:
        from_attributes = True


# ========================
# Participant Schemas
# ========================

class ParticipantBase(BaseModel):
    name: str
    email: str

class ParticipantCreate(ParticipantBase):
    event_id: int

class Participant(ParticipantBase):
    id: int
    event_id: int

    class Config:
        from_attributes = True


# ========================
# Event Schemas
# ========================

class EventBase(BaseModel):
    title: str
    date: date
    location: str
    quota: int

class EventCreate(EventBase):
    pass

class Event(EventBase):
    id: int
    participants: list[Participant] = []

    class Config:
        from_attributes = True
