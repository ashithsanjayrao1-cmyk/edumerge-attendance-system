from pydantic import BaseModel
from typing import Optional, List
from datetime import date, datetime

# --- User Schemas ---
class UserBase(BaseModel):
    name: str
    email: str
    role: str
    section: Optional[str] = None

class UserCreate(UserBase):
    pass

class UserResponse(UserBase):
    id: int

    class Config:
        from_attributes = True

# --- Attendance Schemas ---
class AttendanceCreate(BaseModel):
    student_id: int
    subject_id: int
    status: str  
    recorded_by: int 

class AttendanceUpdate(BaseModel):
    status: str
    recorded_by: int

class AttendanceResponse(BaseModel):
    id: int
    student_id: int
    subject_id: int
    date: date
    status: str
    recorded_by: int
    last_modified: datetime

    class Config:
        from_attributes = True