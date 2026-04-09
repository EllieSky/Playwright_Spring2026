from dataclasses import dataclass
from datetime import date

from faker import Faker


@dataclass
class UserRegistrationData:
     first_name: str
     last_name: str
     birth_date: date
     email: str
     company: str
     password: str


 def generate_user_registration_data() -> UserRegistrationData:
     fake = Faker()
     return UserRegistrationData(
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        birth_date=fake.date_of_birth(minimum_age=18, maximum_age=80),
        email=fake.email(),
        company=fake.company(),
        password=fake.password(length=12),
    )
