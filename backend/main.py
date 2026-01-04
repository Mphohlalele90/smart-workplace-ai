from flask import Flask, jsonify

app = Flask(__name__)

# ---------------------------
# 1️⃣ Fictitious data
# ---------------------------
employees = [
    {"employee_id": "E001", "first_name": "Thabo", "last_name": "Radebe", "role": "Software Engineer", "department": "Tech", "employment_type": "Full-Time"},
    {"employee_id": "E002", "first_name": "Lerato", "last_name": "Mofokeng", "role": "Data Analyst", "department": "Analytics", "employment_type": "Full-Time"},
    {"employee_id": "E003", "first_name": "Jenny", "last_name": "Van Tonder", "role": "HR Specialist", "department": "HR", "employment_type": "Part-Time"},
    {"employee_id": "E004", "first_name": "Mike", "last_name": "Mdlalose", "role": "Project Manager", "department": "Operations", "employment_type": "Full-Time"},
]

projects = [
    {"project_id": "P001", "project_name": "AI Chatbot", "deadline": "2026-02-28", "priority_level": 1},
    {"project_id": "P002", "project_name": "Website Redesign", "deadline": "2026-03-15", "priority_level": 2},
]

work_logs = [
    {"log_id": 1, "employee_id": "E001", "project_id": "P001", "work_date": "2026-01-01", "hours_worked": 8, "overtime": False},
    {"log_id": 2, "employee_id": "E002", "project_id": "P001", "work_date": "2026-01-01", "hours_worked": 6, "overtime": False},
    {"log_id": 3, "employee_id": "E003", "project_id": "P002", "work_date": "2026-01-02", "hours_worked": 4, "overtime": False},
]

# ---------------------------
# 2️⃣ Routes
# ---------------------------

@app.route("/")
def home():
    return {"message": "Smart Workplace API is running!"}

# Route for employees
@app.route("/employees", methods=["GET"])
def get_employees():
    return jsonify(employees)

# Route for projects
@app.route("/projects", methods=["GET"])
def get_projects():
    return jsonify(projects)

# Route for work logs
@app.route("/work_logs", methods=["GET"])
def get_work_logs():
    return jsonify(work_logs)

# ---------------------------
# 3️⃣ Run the server
# ---------------------------
if __name__ == "__main__":
    app.run(debug=True)
