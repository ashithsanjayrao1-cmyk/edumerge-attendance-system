from pydantic import BaseModel
from typing import Optional,List
from datetime import date,datetime
from .models import RoleEnum,AttendanceStatus

class UserBase(BaseModel):
    name: str
    email:str
    role: RoleEnum
    secttion: Optional[str] = None

class UserCreate(UserBase):
    pass

class UserResponse(UserBase):
    id: int

    class Config:
        from_attributes = True


class AttendanceUpdate(BaseModel):
    student_id: int
    subject_id: int
    status: AttendanceStatus
    recorded_by: int

class AttendanceUpdate(BaseModel):
    status: AttendanceStatus
    recorded_by: int

class AttendanceResponse(BaseModel):
    id: int
    student_id: int
    subject_id: int
    date: date
    status: AttendanceStatus
    recorded_by: int
    last_modified: datetime

    class Config:
        from_attributes =True
        
    