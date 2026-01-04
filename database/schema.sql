-- Smart Workplace AI
-- Privacy-first database schema
-- All data is fictitious

CREATE TABLE employees (
  employee_id VARCHAR(10) PRIMARY KEY,
  first_name VARCHAR(50),
  last_name VARCHAR(50),
  role VARCHAR(100),
  department VARCHAR(100),
  employment_type VARCHAR(50),
  start_date DATE,
  is_active BOOLEAN
);

CREATE TABLE projects (
  project_id VARCHAR(10) PRIMARY KEY,
  project_name VARCHAR(100),
  deadline DATE,
  priority_level INT
);

CREATE TABLE work_logs (
  log_id INT PRIMARY KEY AUTO_INCREMENT,
  employee_id VARCHAR(10),
  project_id VARCHAR(10),
  work_date DATE,
  hours_worked DECIMAL(4,2),
  overtime BOOLEAN,
  FOREIGN KEY (employee_id) REFERENCES employees(employee_id),
  FOREIGN KEY (project_id) REFERENCES projects(project_id)
);
