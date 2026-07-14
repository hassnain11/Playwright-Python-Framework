from faker import Faker
import random

fake = Faker()


class FakeData:

    @staticmethod
    def username():
        return f"qa_{fake.user_name()}{random.randint(100,999)}"

    @staticmethod
    def password():
        return "Test@12345"

    @staticmethod
    def employee_name():
        # Existing employee in OrangeHRM demo
        return "Paul Collings"

    @staticmethod
    def first_name():
        return fake.first_name()

    @staticmethod
    def last_name():
        return fake.last_name()

    @staticmethod
    def email():
        return fake.email()