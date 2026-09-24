import { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [students, setStudents] = useState([]);
  const [attendance, setAttendance] = useState({});
  const [message, setMessage] = useState('');

  const API_BASE = 'http://127.0.0.1:8000';

  useEffect(() => {

    axios.get(`${API_BASE}/attendance/students`)
      .then(res => {
        setStudents(res.data);
    
        const initialAttendance = {};
        res.data.forEach(student => {
          initialAttendance[student.id] = 'present';
        });
        setAttendance(initialAttendance);
      })
      .catch(err => console.error("Error fetching students:", err));
  }, []);

  const handleStatusChange = (studentId, status) => {
    setAttendance({
      ...attendance,
      [studentId]: status
    });
  };

  const submitAttendance = () => {
 
   
    const payload = Object.keys(attendance).map(studentId => ({
      student_id: parseInt(studentId),
      subject_id: 1, 
      status: attendance[studentId],
      recorded_by: 1 
    }));

    console.log("Sending payload:", payload);

    axios.post(`${API_BASE}/attendance/`, payload)
      .then(res => {
        setMessage('✅ Attendance recorded successfully!');
        setTimeout(() => setMessage(''), 3000);
      })
      .catch(err => {
        const errorDetail = err.response?.data?.detail;
        console.error("FastAPI Error:", errorDetail);

        setMessage(`❌ Error: ${JSON.stringify(errorDetail)}`);
      });
  };

  return (
    <div className="container">
      <header>
        <h1>Smart Attendance Portal</h1>
        <h2>BCA-A | Python Web Development | Prof. Sharma</h2>
      </header>
      
      {message && <div className="alert">{message}</div>}

      <div className="student-list">
        {students.map(student => (
          <div key={student.id} className="student-card">
            <span className="student-name">{student.name} </span>
            <div className="toggle">
              <label className={attendance[student.id] === 'present' ? 'active-present' : ''}>
                <input 
                  type="radio" 
                  name={`student-${student.id}`} 
                  value="present"
                  checked={attendance[student.id] === 'present'}
                  onChange={() => handleStatusChange(student.id, 'present')}
                /> Present
              </label>
              <label className={attendance[student.id] === 'absent' ? 'active-absent' : ''}>
                <input 
                  type="radio" 
                  name={`student-${student.id}`} 
                  value="absent"
                  checked={attendance[student.id] === 'absent'}
                  onChange={() => handleStatusChange(student.id, 'absent')}
                /> Absent
              </label>
            </div>
          </div>
        ))}
      </div>
      
      <button onClick={submitAttendance} className="submit-btn">
        Submit Today's Attendance
      </button>
    </div>
  );
}

export default App;