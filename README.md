# 🎓 Academic Progress Tracker and Resource Recommender

A Python-based application to help students track their academic performance, identify weak subjects, and get personalized learning resources based on their scores and attendance.

---

## 📌 Features

- 📋 Input student details including subject-wise marks and overall attendance.
- 📊 Automatically calculates percentage scores and overall academic performance.
- 🔍 Identifies weak subjects (below threshold).
- 📈 Displays performance using bar charts.
- 💡 Provides subject-wise resource recommendations based on performance.
- 💾 Stores data in CSV files for reuse and record-keeping.

---

## 📂 Dataset Description

- `users.csv`  
  Contains student progress data with the following columns:
  - Student Name
  - Subject
  - Score (%)
  - Attendance (%)
  - Overall (%)
  - Weak Subject (Yes/No)

- `resources.csv`  
  Contains resource recommendations with the following columns:
  - Subject
  - Condition (e.g., `score<33 & attendance<75`)
  - Recommendation (text with links or advice)

---

## 🧠 Technologies Used

- **Python**
- **Pandas** - for data manipulation
- **NumPy** - for calculations
- **Matplotlib** - for graphs
- **OOP (Object-Oriented Programming)** - for structured and modular code

---

## ⚙️ How It Works

1. **Start the application** by running `academictracker.py`.
2. **Enter your details** when prompted – name, subjects, marks, and attendance.
3. The system:
   - Calculates subject-wise and overall performance.
   - Stores your data in `users.csv`.
   - Displays your performance table and graph.
   - Checks conditions in `resources.csv` and recommends resources.
4. **To import this project into another file**, just:
   ```python
   from academictracker import AcademicTracker

   tracker = AcademicTracker()
   tracker.input_student_data()
   tracker.calculate_progress()
   tracker.data_saving()
   tracker.show_graph()
   tracker.recommendation()

