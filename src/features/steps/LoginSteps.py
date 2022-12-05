from behave import *
from functions.Functions import Functions
from pages.LoginPage import Login
import time

use_step_matcher("re")

Login = Login()


@given("Start application in default device")
def step_impl(context):
    """
    :param device: is device that you will run the test
    :type context: behave.runner.Context
    """
    desired_caps = Functions.get_capabilities(context)
    Functions.get_driver(context, capabilities=desired_caps)


@given('Application start with device (.)')
def step_impl(context, device):
    """
    :param device: is device that you will run the test
    :type context: behave.runner.Context
    """
    desired_caps = Functions.get_capabilities(context, test_device=device)
    Functions.get_driver(context, capabilities=desired_caps)


@then("Close application")
def step_impl(context):
    Functions.close_application(context)


@when("I set (.) and (.) in Login Page")
def step_impl(context, arg1, arg2):
    Login.set_players()


@step("wait (.) seconds")
def step_impl(context, times):
    time.sleep(int(times))