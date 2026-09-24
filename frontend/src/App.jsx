import { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [view, setView] = useState('faculty'); // 'faculty' or 'admin'
  const [students, setStudents] = useState([]);
  const [attendance, setAttendance] = useState({});
  const [message, setMessage] = useState('');
  const [report, setReport] = useState([]);

  const API_BASE = 'http://127.0.0.1:8000';

  useEffect(() => {
    fetchStudents();
  }, []);

  const fetchStudents = () => {
    axios.get(`${API_BASE}/attendance/students`)
      .then(res => {
        setStudents(res.data);
        const initialAttendance = {};
        res.data.forEach(student => {
          initialAttendance[student.id] = 'present';
        });
        setAttendance(initialAttendance);
      })
      .catch(err => console.error(err));
  };

  const fetchReport = () => {
    axios.get(`${API_BASE}/attendance/report`)
      .then(res => setReport(res.data))
      .catch(err => console.error(err));
  };

  const handleStatusChange = (studentId, status) => {
    setAttendance({ ...attendance, [studentId]: status });
  };

  const submitAttendance = () => {
    const payload = Object.keys(attendance).map(studentId => ({
      student_id: parseInt(studentId, 10),
      subject_id: 1, 
      status: attendance[studentId],
      recorded_by: 1 
    }));

    axios.post(`${API_BASE}/attendance/`, payload)
      .then(res => {
        setMessage('✅ Attendance recorded successfully!');
        setTimeout(() => setMessage(''), 3000);
      })
      .catch(err => setMessage('❌ Error saving attendance.'));
  };

  return (
    <div className="container">
      <header style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
        <div>
          <h1>Smart Attendance Portal</h1>
          <h2>{view === 'faculty' ? 'BCA-A | Python Web Development' : 'Admin Low Attendance Report'}</h2>
        </div>
        <div>
          <button 
            onClick={() => { setView('faculty'); fetchStudents(); }}
            style={{ marginRight: '10px', padding: '8px', cursor: 'pointer' }}>
            Faculty Entry
          </button>
          <button 
            onClick={() => { setView('admin'); fetchReport(); }}
            style={{ padding: '8px', cursor: 'pointer' }}>
            Admin Report
          </button>
        </div>
      </header>
      
      {message && <div className="alert">{message}</div>}

   
      {view === 'faculty' && (
        <>
          <div className="student-list">
            {students.map(student => (
              <div key={student.id} className="student-card">
                <span className="student-name">{student.name}</span>
                <div className="toggle">
                  <label className={attendance[student.id] === 'present' ? 'active-present' : ''}>
                    <input 
                      type="radio" 
                      value="present"
                      checked={attendance[student.id] === 'present'}
                      onChange={() => handleStatusChange(student.id, 'present')}
                    /> Present
                  </label>
                  <label className={attendance[student.id] === 'absent' ? 'active-absent' : ''}>
                    <input 
                      type="radio" 
                      value="absent"
                      checked={attendance[student.id] === 'absent'}
                      onChange={() => handleStatusChange(student.id, 'absent')}
                    /> Absent
                  </label>
                </div>
              </div>
            ))}
          </div>
          <button onClick={submitAttendance} className="submit-btn">Submit Today's Attendance</button>
        </>
      )}

      {view === 'admin' && (
        <div className="report-list">
          <table style={{ width: '100%', textAlign: 'left', borderCollapse: 'collapse' }}>
            <thead>
              <tr style={{ borderBottom: '2px solid #ddd' }}>
                <th>Name</th>
                <th>Classes Held</th>
                <th>Attendance %</th>
                <th>Status</th>
              </tr>
            </thead>
            <tbody>
              {report.map(row => (
                <tr key={row.id} style={{ borderBottom: '1px solid #eee', padding: '10px' }}>
                  <td style={{ padding: '10px 0' }}>{row.name}</td>
                  <td>{row.total_classes}</td>
                  <td>{row.percentage}%</td>
                  <td>
                    {row.percentage < 75 && row.total_classes > 0 ? (
                      <span style={{ color: 'red', fontWeight: 'bold' }}>Defaulter</span>
                    ) : (
                      <span style={{ color: 'green' }}>Good</span>
                    )}
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
}

export default App;