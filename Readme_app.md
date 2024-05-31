## autores 
-BRAHIAN ANDRES OSORIO ARANGO
-Jarrison Andres Lopez Roldan


## Web service description
This is a web service built with Flask that manages employees and their payroll data, including information about accruals and deductions.

## Facility

-Clone the repository: git clone https://github.com/Andres-Arango280/app.nomina.git
-create a database in neon.cosole and add

PGDATABASE = "Enter database name"
PGUSER = "Enter the DB user"
PGPASSWORD = "Enter password"
PGHOST = "Enter the DNS address or IP address of the server"
PGPORT = 5432 # Default is 5432,

Once this is created, add to the file located in the src folder which contains a model folder with the SecretConfig file, there you must add the database configuration so that it works similar to the previous data along with the pgport

-Once this is done you can run the app.py from your terminal
using the cd command along with the address in which you placed the repository folder
-To start, the first thing you must do is create the tables from the main menu of the website, create the 3 tables
corresponding(Accruals,Deductions,Empoyee)
-then you can start creating users which are inserted into the previously created and connected database
-you can insert, update and delete any employee from the menu options

-Navigate to the project directory: cd app.nomina
-Install the dependencies: pip install -r requirements.txt
-Run the server: python app.py

## Requirements
- Python 3.x
- flask
- psycopg2
-sys

## EXECUTION UNITEST
-You can execute this file from your terminal with the command cd and the address of the file depending on where you have it,     for   example cd C:\Users\Usuario\Desktop\app.nomina\unitest.py

## Endpoints
- GET /

-- Shows the home page.

-GET/POST /search_by_id

- Search for an employee by their ID number.
-- GET: Represents search_by_id.html.
-- POST: Represents the Employee.html file with the employee details or displays an error message.

- GET/POST /search_by_name

- Search for an employee by first and last name.
-- GET: Represents search_by_name.html.
-- POST: Represents the Employee.html file with the employee details or displays an error message.

- GET/POST /consult_payroll_by_id

-- Consult an employee's payroll by their ID number.
-- GET: Represents query_payroll_by_id.html.
-- POST: Presents payroll.html with employee details, accruals and deductions or displays an error message.

- GET/POST /modify_employee

-- Modify the data of an existing employee.
-- GET: Represents modify_employee.html.
-- POST: Display a success or error message and redirect to the home page.

- GET/POST /insert_user

-- Insert a new employee along with his accruals and deductions.
-- GET: Represents form.html.
-- POST: Displays a success message after inserting data.

- GET/POST /manage_tables

- Management of database tables for employees, accruals and deductions.
-- GET: Represents Manage_tables.html.
-- POST: Executes the selected action (create or delete tables) and displays a success or error message.

- GET/POST /delete_employee

- Delete an employee by her ID number.
-- GET: Represents delete_employee.html.
-- POST: Display a success or error message and redirect to the home page.

