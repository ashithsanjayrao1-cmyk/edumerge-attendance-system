from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import engine, Base
from .routers import attendance

Base.metadata.create_all(bind = engine)

app = FastAPI(title="Smart Attendance Management API")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(attendance.router)

@app.get("/")
def read_root():
    return{"message":"Smart Attendance API is running"}