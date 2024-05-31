import sys
sys.path.append("src")

import controller.usercontroller as usercontroller
from flask import Flask, request, render_template, redirect, url_for, flash
from model.Payroll_Logic import Accruals, Deductions, Employee

app = Flask(__name__)
app.secret_key = 'melos'


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search_by_id', methods=['GET', 'POST'])
def search_by_id():
    if request.method == 'POST':
        idnumber = request.form['idnumber']
        try:
            employee = usercontroller.SearchById(idnumber)
            if employee:
                return render_template('employee.html', employee=employee)
            else:
                flash("Employee not found")
                return redirect(url_for('index'))
        except Exception as e:
            flash(f"Error: {str(e)}")
            return redirect(url_for('index'))
    return render_template('search_by_id.html')

@app.route('/search_by_name', methods=['GET', 'POST'])
def search_by_name():
    if request.method == 'POST':
        firstname = request.form['firstname']
        surname = request.form['surname']
        try:
            employee = usercontroller.SearchByNameAndSurname(firstname, surname)
            return render_template('employee.html', employee=employee)
        except Exception as e:
            flash(f"Error: {str(e)}")
            return redirect(url_for('index'))
    return render_template('search_by_name.html')

@app.route('/consult_payroll_by_id', methods=['GET', 'POST'])
def consult_payroll_by_id():
    if request.method == 'POST':
        idnumber = request.form['idnumber']
        try:
            employee, accruals, deductions = usercontroller.SearchInAllTablesByID(idnumber)
            return render_template('payroll.html', employee=employee, accruals=accruals, deductions=deductions)
        except Exception as e:
            flash(f"Error: {str(e)}")
            return redirect(url_for('index'))
    return render_template('consult_payroll_by_id.html')

@app.route('/modify_employee', methods=['GET', 'POST'])
def modify_employee():
    if request.method == 'POST':
        idnumber = request.form['idnumber']
        firstname = request.form['firstname']
        surname = request.form['surname']
        mail = request.form['mail']
        employee = Employee(firstname, surname, idnumber, mail)
        try:
            usercontroller.Update(employee)
            flash("Employee updated successfully")
            return redirect(url_for('index'))
        except Exception as e:
            flash(f"Error: {str(e)}")
            return redirect(url_for('index'))
    return render_template('modify_employee.html')

## si ingresa a inser user##
@app.route('/insert_user', methods=['GET', 'POST'])
def insert_user():
    if request.method == 'POST':
        # Employee details
        firstname = request.form['firstname']
        surname = request.form['surname']
        idnumber = request.form['idnumber']
        mail = request.form['mail']
        
        # Accruals details
        BasicSalary = float(request.form['BasicSalary'])
        WorkedDays = int(request.form['WorkedDays'])
        HolidayTimeWorked = int(request.form['HolidayTimeWorked'])
        ExtraDaylightHoursWorked = int(request.form['ExtraDaylightHoursWorked'])
        ExtraNightHoursWorked = int(request.form['ExtraNightHoursWorked'])
        HolidayExtraDaylightHoursWorked = int(request.form['HolidayExtraDaylightHoursWorked'])
        HolidayExtraNightHoursWorked = int(request.form['HolidayExtraNightHoursWorked'])
        DaysOfDisability = int(request.form['DaysOfDisability'])
        LeaveDays = int(request.form['LeaveDays'])
        
        # Deductions details
        HealthInsurancePercentage = float(request.form['HealthInsurancePercentage'])
        PensionContributionPercentage = float(request.form['PensionContributionPercentage'])
        PensionSolidarityFundContributionPercentage = float(request.form['PensionSolidarityFundContributionPercentage'])
        
        # Create objects
        employee = Employee(firstname, surname, idnumber, mail)
        accruals = Accruals(idnumber, BasicSalary, WorkedDays, HolidayTimeWorked, ExtraDaylightHoursWorked, ExtraNightHoursWorked, HolidayExtraDaylightHoursWorked, HolidayExtraNightHoursWorked, DaysOfDisability, LeaveDays)
        deductions = Deductions(idnumber, accruals, HealthInsurancePercentage, PensionContributionPercentage, PensionSolidarityFundContributionPercentage)
        
        # Use UserControl to save to database
        usercontroller.GetCursor()
        usercontroller.Insert(employee)
        usercontroller.InsertAccruals(accruals)
        usercontroller.InsertDeductions(deductions)
        
        return "User data inserted successfully!"
    return render_template('form.html')

@app.route('/manage_tables', methods=['GET', 'POST'])
def manage_tables():
    if request.method == 'POST':
        action = request.form['action']
        try:
            if action == 'create_employees':
                usercontroller.CreateTable()
            elif action == 'create_accruals':
                usercontroller.CreateAccrualsTable()
            elif action == 'create_deductions':
                usercontroller.CreateTableDeductions()
            elif action == 'delete_employees':
                usercontroller.DeleteTable()
            elif action == 'delete_accruals':
                usercontroller.DeleteTableAccruals()
            elif action == 'delete_deductions':
                usercontroller.DeleteTableDeductions()
            flash(f"Action {action} executed successfully")
            return redirect(url_for('index'))
        except Exception as e:
            flash(f"Error: {str(e)}")
            return redirect(url_for('index'))
    return render_template('manage_tables.html')

@app.route('/delete_employee', methods=['GET', 'POST'])
def delete_employee():
    if request.method == 'POST':
        idnumber = request.form['idnumber']
        try:
            employee = Employee("", "", idnumber, "")
            usercontroller.DeleteById(employee)
            flash("Employee deleted successfully")
            return redirect(url_for('index'))
        except Exception as e:
            flash(f"Error: {str(e)}")
            return redirect(url_for('index'))
    return render_template('delete_employee.html')

#luego de eligir el menu principal



## buscar empleado enla base de datos
@app.route('/search_employee', methods=['GET', 'POST'])
def search_employee():
    if request.method == 'POST':
        idnumber = request.form['idnumber']
        try:
            employee = usercontroller.SearchById(idnumber)
            if employee:
                return render_template('employee.html', employee=employee)
            else:
                flash("Employee not found", 'error')
                return redirect(url_for('index'))
        except Exception as e:
            flash(str(e), 'error')
            return redirect(url_for('index'))
    return render_template('search_employee.html')





if __name__ == '__main__':
    app.run(debug=True)


