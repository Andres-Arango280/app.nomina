## Description web service
This is a web service built with Flask that manages employees and their payroll data, including information on accruals and deductions.

## Endpoints
- GET /

-- Displays the homepage.

-GET/POST /search_by_id

-- Searches for an employee by their ID number.
-- GET: Renders search_by_id.html.
-- POST: Renders employee.html with employee details or shows an error message.

- GET/POST /search_by_name

-- Searches for an employee by their first and last name.
-- GET: Renders search_by_name.html.
-- POST: Renders employee.html with employee details or shows an error message.

- GET/POST /consult_payroll_by_id

-- Consults an employee's payroll by their ID number.
-- GET: Renders consult_payroll_by_id.html.
-- POST: Renders payroll.html with employee details, accruals, and deductions or shows an error message.

- GET/POST /modify_employee

-- Modifies an existing employee's details.
-- GET: Renders modify_employee.html.
-- POST: Shows a success or error message and redirects to the homepage.

- GET/POST /insert_user

-- Inserts a new employee along with their accruals and deductions.
-- GET: Renders form.html.
-- POST: Shows a success message after inserting the data.

- GET/POST /manage_tables

-- Manages database tables for employees, accruals, and deductions.
-- GET: Renders manage_tables.html.
-- POST: Executes the selected action (create or delete tables) and shows a success or error message.

- GET/POST /delete_employee

-- Deletes an employee by their ID number.
-- GET: Renders delete_employee.html.
-- POST: Shows a success or error message and redirects to the homepage.

## Requirements
- Python 3.x
- Flask

## Installation

-Clone the repository: git clone https://github.com/Andres-Arango280/app.nomina.git
-Navigate to the project directory: cd app.nomina
-Install the dependencies: pip install -r requirements.txt
-Run the server: python app.py 