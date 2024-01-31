from behave import given, when, then


@given('I open the application')
def step_open_app(context):
    context.app.login_state = context.app.login_page.login_successfully()


@when("I enter my user and password")
def step_enter_user_and_password(context):
    context.app.login_page.login_successfully()


@then(u'I should see the successful login')
def step_check_successful_login(context):
    assert context.app.login_page.is_logged_in(), "The login was unsuccessful"
