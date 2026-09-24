from sqlalchemy import Column,Integer,String,ForeignKey,Date,Enum,DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
import enum
from .database import Base

class RoleEnum(str,enum.Enum):
    admin = "admin"
    faculty = "faculty"
    student = "student"



class AttendanceStatus(str,enum.Enum):
    present = "present"
    absent = "absent"


class User(Base):
    __tablename__ = "users"

    id = Column(Integer,primary_key=True,index=True)
    name = Column(String,index=True)
    email = Column(String,unique=True,index=True)
    role = Column(Enum(RoleEnum),default=RoleEnum.student)
    section = Column(String,nullable=True)


class Subject(Base):
    __tablename__ = "subjects"

    id = Column(Integer,primary_key=True,index=True)
    name = Column(String,index=True)
    faculty_id = Column(Integer,ForeignKey("users.id"))

    faculty = relationship("User",foreign_keys=[faculty_id])


class AttendanceLog(Base):
    __tablename__ = "attendance_logs"

    id = Column(Integer,primary_key=True,index=True)
    student_id = Column(Integer,ForeignKey("users.id"))
    subject_id = Column(Integer,ForeignKey("subjects.id"))
    date = Column(Date,default=datetime.utcnow().date)
    status = Column(Enum(AttendanceStatus))
    recorded_by = Column(Integer,ForeignKey("users.id"))
    last_modified = Column(DateTime,default=datetime.utcnow,onupdate=datetime.utcnow)

    student = relationship("User",foreign_keys=[student_id])
    subject = relationship("Subject", foreign_keys=[subject_id])
    recorder = relationship("User",foreign_keys=[recorded_by])


