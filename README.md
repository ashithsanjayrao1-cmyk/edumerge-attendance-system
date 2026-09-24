# Edumerge Smart Attendance Prototype

## Overview
A full-stack prototype built for the Edumerge Pre-Drive Product Engineering Assignment. The application streamlines daily attendance recording for faculty and automates the identification of students with low attendance (defaulters) for administrators.

## Tech Stack
* **Backend:** FastAPI (Python), SQLAlchemy, SQLite
* **Frontend:** React, Vite, Axios
* **Architecture:** REST API with a decoupled client-server model.

## Core Features
1. **Faculty View:** Bulk attendance recording optimized for speed (defaults to 'Present').
2. **Admin View:** Real-time percentage calculation and automatic flagging of students below 75% attendance.
3. **Data Integrity:** API-level protection against duplicate daily logs.

## How to Run Locally
1. Clone the repository.
2. Start the FastAPI backend: `uvicorn app.main:app --reload`
3. Seed the dummy data: `python seed.py`
4. Start the React frontend: `cd frontend && npm run dev`
