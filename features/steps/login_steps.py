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


@given("The user input an name")
def user_input_an_name(context):
    context.app.login_page.user_input_name()


@then("Valid that the title of the home page is visible")
def verify_user_input_visible(context):
    assert bool(context.app.main_page.valid_title_home())


@then("Valid that the texts of the home page is visible")
def verify_texts_visible(context):
    assert bool(context.app.main_page.valid_title_home())
    assert bool(context.app.main_page.valid_secondary_title_text())
    assert bool(context.app.main_page.valid_introductory_message())


@when("Select the Update State 1 button")
def select_update_state_one(context):
    context.app.main_page.select_update_state_one()


@when("Select the Update State 2 button")
def select_update_state_two(context):
    context.app.main_page.select_update_state_two()


@when("Select the Open Modal button")
def select_open_modal(context):
    context.app.main_page.select_open_modal()


@when("Select the Close Modal button")
def select_close_modal(context):
    context.app.main_page.select_close_modal()


@when("Select the Go to DetailScreen button")
def select_go_to_detailScreen(context):
    context.app.main_page.select_go_to_detailScreen()


@when("Select the Pedidos section")
def select_pedidos_section(context):
    context.app.main_page.select_pedidos_section()


@when("Select the Camera section")
def select_camera_section(context):
    context.app.main_page.select_camera_section()


@when("click on the option while using the app")
def click_the_option_while_using_app(context):
    context.app.main_page.select_while_using_the_app()


@then("valid that the camera section is opened")
def valid_the_camera_section(context):
    assert bool(context.app.main_page.valid_capturar_foto())


@when("Click on the option Don't Allow")
def click_the_option_dont_allow(context):
    context.app.main_page.select_dont_allow()


@then("Valid if the camera section is not open")
def valid_the_camera_section(context):
    assert bool(context.app.main_page.valid_no_permision_message())


@when("Select the details section")
def select_details_section(context):
    context.app.main_page.select_details_section()


@then("I validate the section titles")
def valid_titles_section(context):
    assert bool(context.app.main_page.valid_flatlist_from_API_title())

