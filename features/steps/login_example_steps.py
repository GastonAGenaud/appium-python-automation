from behave import given, when, then


@when("The user input an name")
def user_input_an_name(context):
    context.app.example_page.user_input_name()