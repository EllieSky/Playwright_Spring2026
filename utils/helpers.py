from dataclasses import dataclass
from faker import Faker
from datetime import date

fake = Faker()


@dataclass
class RegisterUserData:
    first_name: str
    last_name: str
    email: str
    company: str
    password: str
    birth_date: date


def generate_user_registration_data() -> RegisterUserData:
    return RegisterUserData(
        first_name=fake.first_name_female(),
        last_name=fake.last_name(),
        email=fake.free_email(),
        company=fake.company(),
        password=fake.password(length=8),
        birth_date=fake.date_of_birth(minimum_age=18, maximum_age=65),
    )