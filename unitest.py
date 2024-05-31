import unittest
import flask as Flask
from app import app

class TestApp(unittest.TestCase):
    
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome to the Payroll System', response.data)

    def test_search_by_id(self):
        response = self.app.post('/search_by_id', data=dict(idnumber='123456'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Employee Details', response.data)

    def test_search_by_name(self):
        response = self.app.post('/search_by_name', data=dict(firstname='John', surname='Doe'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Employee Details', response.data)

    def test_consult_payroll_by_id(self):
        response = self.app.post('/consult_payroll_by_id', data=dict(idnumber='123456'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Payroll Details', response.data)

    def test_modify_employee(self):
        response = self.app.post('/modify_employee', data=dict(idnumber='123456', firstname='John', surname='Doe', mail='john@example.com'))
        self.assertEqual(response.status_code, 302)  # Redirects after successful modification

    def test_insert_user(self):
        response = self.app.post('/insert_user', data=dict(firstname='John', surname='Doe', idnumber='123456', mail='john@example.com',
                                                            BasicSalary='1000000', WorkedDays='20', HolidayTimeWorked='5',
                                                            ExtraDaylightHoursWorked='2', ExtraNightHoursWorked='3',
                                                            HolidayExtraDaylightHoursWorked='1', HolidayExtraNightHoursWorked='2',
                                                            DaysOfDisability='0', LeaveDays='0',
                                                            HealthInsurancePercentage='2', PensionContributionPercentage='3',
                                                            PensionSolidarityFundContributionPercentage='1'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'User data inserted successfully!', response.data)

    def test_manage_tables(self):
        response = self.app.post('/manage_tables', data=dict(action='create_employees'))
        self.assertEqual(response.status_code, 302)  # Redirects after successful table management

    def test_delete_employee(self):
        response = self.app.post('/delete_employee', data=dict(idnumber='123456'))
        self.assertEqual(response.status_code, 302)  # Redirects after successful deletion

    def test_search_employee(self):
        response = self.app.post('/search_employee', data=dict(idnumber='123456'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Employee Details', response.data)


#fallan dos aproposito para confimar el funcionamiento de estas unitest#


if __name__ == '__main__':
    unittest.main()
