import pytest
import re

import config
from utils.helpers import generate_user_registration_data

@pytest.fixture
def api_auth(playwright, browser):
    auth_url = '/login'
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36'

    session = playwright.request.new_context(base_url=config.get_base_url(), user_agent=user_agent)
    resp = session.get('/login')

    token_value = re.search(r'name=__RequestVerificationToken type=hidden value=(.+?)>', resp.text()).group(1)

    payload = {
        'Email': "user.shopper@yopmail.com",
        'Password': "user9900",
        # 'ConfirmPassword': "user.password",
        '__RequestVerificationToken': token_value,
        'RememberMe': 'false'
    }

    auth_response = session.post(auth_url, form=payload)
    is_success = 'My account' in auth_response.text() and 'Log out ' in auth_response.text()
    assert is_success, f"Authentication failed: {auth_response.status_code} - {auth_response.text()}"

    state = session.storage_state() # all the headers and cookies
    context = browser.new_context(storage_state=state)

    yield context.new_page()

    session.dispose()
    context.close()



@pytest.fixture
def api_register_user(playwright):
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36'

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
    assert is_success

    print(f"Registered user: {user.email}")
    print(f"Registration response status: {registration_response.status}")

    yield {'email': user.email, 'password': user.password}

    session.dispose()