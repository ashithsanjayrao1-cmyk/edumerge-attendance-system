from fastapi import APIRouter, Depends, HTTPException,status
from sqlalchemy.orm import Session
from typing import List
from datetime import datetime
from .. import models, schemas, database

router = APIRouter(
    prefix="/attendance",
    tags=["Attendance"]
)


@router.post("/", response_model=List[schemas.AttendanceResponse])
def record_bulk_attendance(attendance_data: List[schemas.AttendanceCreate], db: Session = Depends(database.get_db)):

    db_logs = []
    for record in attendance_data:
        
        existing = db.query(models.AttendanceLog).filter(
            models.AttendanceLog.student_id == record.student_id,
            models.AttendanceLog.subject_id == record.subject_id,
            models.AttendanceLog.date == datetime.utcnow().date() 
        ).first()

        if existing:
            continue 
            
        new_log = models.AttendanceLog(
            student_id=record.student_id,
            subject_id=record.subject_id,
            status=record.status,
            recorded_by=record.recorded_by
        )
        db.add(new_log)
        db_logs.append(new_log)
        
    db.commit()
    for log in db_logs:
        db.refresh(log)
    return db_logs


@router.put("/{log_id}", response_model=schemas.AttendanceResponse)
def correct_attendance(log_id: int, update_data: schemas.AttendanceUpdate, db: Session = Depends(database.get_db)):
    db_log = db.query(models.AttendanceLog).filter(models.AttendanceLog.id == log_id).first()
    if not db_log:
        raise HTTPException(status_code=404, detail="Attendance record not found")
    
    db_log.status = update_data.status
    db_log.recorded_by = update_data.recorded_by
    
    db.commit()
    db.refresh(db_log)
    return db_log


@router.get("/student/{student_id}", response_model=List[schemas.AttendanceResponse])
def get_student_history(student_id: int, db: Session = Depends(database.get_db)):
    logs = db.query(models.AttendanceLog).filter(models.AttendanceLog.student_id == student_id).all()
    return logs


@router.get("/students", response_model=List[schemas.UserResponse])
def get_all_students(db: Session = Depends(database.get_db)):
    return db.query(models.User).filter(models.User.role == models.RoleEnum.student).all()