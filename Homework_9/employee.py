from datetime import datetime, date

options = {
'M': 'Male',
'F': 'Female',
}

class Employee_Person:
    date_format = '%d.%m.%Y'

    def __init__(self, first_name, last_name, gender, phone_number, trial_passed, salary, join_date, leave_date = None):

        self.first_name = first_name
        self.last_name = last_name
        self._gender = None
        self.gender = gender
        self._phone_number = None
        self.phone_number = phone_number
        self.trial_passed = trial_passed.lower() == 'yes'
        self.salary = int(salary)

        self.join_date = datetime.strptime(join_date, self.date_format).date()
        if leave_date:
            self.leave_date = datetime.strptime(leave_date, self.date_format).date()
        else:
            self.leave_date = None

        self._email = None

        @property
        def email(self):
            if self._email:
                return self._email

            return f'{self.first_name.lower()}.{self.last_name.lower()}@company.com'

        @email.setter
        def email(self, value):
            if is_email(value) is False:
                raise ValueError('Invalid email')

            if self.is_email(value) is False:
                raise ValueError('Invalid email')

        # self._email = value

        @staticmethod
        def is_email(value):
            pass

        @property
        def gender(self):
            return self._gender

        @gender.setter
        def gender(self, value):
            if value not in options:
                raise ValueError('gender must be M or F')

            self._gender = value

            self.phone_number = phone_number

        @property
        def phone_number(self):
            return self._phone_number

        @gender.setter
        def phone_number(self, value):
            if self.is_phone_number(value):
                self._phone_number = value
            else:
                raise ValueError('Invalid phone number ')

        @staticmethod
        def is_phone_number(phone_number):
            pass

        def __repr__(self):
            return f'<Employee_Person {self.first_name} {self.last_name}>'

employee1 = Employee_Person('Davit', 'Tovmasyan', 'M', phone_number = '077 12 34 56', trial_passed = 'yes',
                            salary = 150000, join_date = '22.02.2018')
employee2 = Employee_Person('Tovmas', 'Davtyan', 'M', phone_number='077 12 34 56', trial_passed = 'no',
                            salary = 450000, join_date='11.01.2020', leave_date = '25.07.2020')
