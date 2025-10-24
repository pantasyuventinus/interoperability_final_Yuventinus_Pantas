from app.database import Base, engine
from app import models

Base.metadata.create_all(bind=engine)  # ini akan membuat tabel saat FastAPI dijalankan

from fastapi import FastAPI
from app.routes import event, participant
from app import models, database

# Buat database jika belum ada
models.Base.metadata.create_all(bind=database.engine)

# Inisialisasi FastAPI
app = FastAPI(
    title="Campus Event Registration Platform",
    description="API untuk melihat dan mendaftar event kampus",
    version="1.0.0"
)

# Tambahkan routes
app.include_router(event.router)
app.include_router(participant.router)


# Root endpoint (halaman utama)
@app.get("/")
def home():
    return {"message": "Selamat datang di Campus Event Registration API!"}
