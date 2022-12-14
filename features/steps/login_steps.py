from behave import given, when, then


@given("I open login page")
def open_login_page(context):
    context.app.launch_page.login_with_existing_account()



@when("I login with email and password")
def login_with_email_and_password(context):
    context.app.login_page.login_with_email_and_password()


@then("I am on main page")
def verify_main_page_open(context):
    assert bool(context.app.main_page.verify_main_page_is_open())
