from dataclasses import dataclass
from datetime import date

from faker import Faker


@dataclass
class RegisterUserData:
    first_name: str
    last_name: str
    date_of_birth_day: str
    date_of_birth_month: str
    date_of_birth_year: str
    email: str
    company_name: str
    password: str
    confirm_password: str


def generate_user_registration_data():
    f = Faker()
    birth_date = f.date_of_birth()
    password = f.password()

    return RegisterUserData(
        first_name=f.first_name(),
        last_name=f.last_name(),
        date_of_birth_day=str(birth_date.day),
        date_of_birth_month=str(birth_date.strftime("%B")),
        date_of_birth_year=str(birth_date.year),
        email=f.email(),
        company_name=f.company(),
        password=password,
        confirm_password=password,
    )
