import datetime
from dataclasses import dataclass
from faker import Faker


@dataclass
class RegisterUserData:
    first_name: str
    last_name: str
    birth_date: datetime.date
    email: str
    company: str
    phone: str
    password: str


def generate_user_registration_data():
    f = Faker()
    return RegisterUserData(
        first_name=f.first_name_female(),
        last_name = f.last_name(),
        birth_date = f.date_of_birth(maximum_age=99),
        email = f.free_email(),
        company = f.company(),
        phone = f.phone_number(),
        password = f.password(8)
    )

@dataclass
class AddressData:
    street: str
    city: str
    zip: str


def generate_address_data():
    f = Faker()
    return AddressData(
        street = f.street_address(),
        city = f.city(),
        zip = f.zipcode()
    )
