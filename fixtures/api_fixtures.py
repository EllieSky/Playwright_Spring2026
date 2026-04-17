import pytest
import re

import config
from utils.helpers import generate_user_registration_data

@pytest.fixture
def api_auth(playwright, browser):
    auth_url = '/login'
    user_agent = config.get_user_agent()
    session = playwright.request.new_context(base_url=config.get_base_url(), user_agent=user_agent)
    resp = session.get(auth_url)

    token_value = re.search(r'name=__RequestVerificationToken type=hidden value=(.+?)>', resp.text()).group(1)

    payload = {
        'Email': 'user.shopper@yopmail.com',
        'Password': 'user9900',
        '__RequestVerificationToken': token_value,
        'RememberMe': 'false'
    }
    auth_response = session.post(auth_url, form=payload)
    is_success = 'My account' in auth_response.text() and 'Log out' in auth_response.text()
    assert is_success, "Failed to authenticate a user during test setup."

    state = session.storage_state()
    context = browser.new_context(storage_state=state, base_url=config.get_base_url())

    yield context.new_page()

    session.dispose()
    context.close()



@pytest.fixture
def api_register_user(playwright):
    user_agent = config.get_user_agent()

    session = playwright.request.new_context(base_url=config.get_base_url(), user_agent=user_agent)
    resp = session.get('/register')

    token_value = re.search(r'name=__RequestVerificationToken type=hidden value=(.+?)>', resp.text()).group(1)

    user = generate_user_registration_data()
    payload = {
        'Gender': 'M',
        'FirstName': user.first_name,
        'LastName': user.last_name,
        'DateOfBirthDay': user.birth_date.day,
        'DateOfBirthMonth': user.birth_date.month,
        'DateOfBirthYear': user.birth_date.year,
        'Email': user.email,
        'Company': user.company,
        'Password': user.password,
        'ConfirmPassword': user.password,
        '__RequestVerificationToken': token_value,
        'Newsletter': 'false'
    }

    registration_response = session.post("/register", form=payload)
    is_success = 'Your registration completed' in registration_response.text()
    assert is_success, "Failed to register a user during test setup."

    yield {'email': user.email, 'password': user.password}

    session.dispose()