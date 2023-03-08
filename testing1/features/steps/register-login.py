from behave import *


@given(u'I am a new user')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I am a new user')


@when(u'I fill in a unique username in the username field')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I fill in a unique username in the username field')


@when(u'do the same for the email field')
def step_impl(context):
    raise NotImplementedError(u'STEP: When do the same for the email field')


@when(u'the password field')
def step_impl(context):
    raise NotImplementedError(u'STEP: When the password field')


@when(u'confirm the password')
def step_impl(context):
    raise NotImplementedError(u'STEP: When confirm the password')


@when(u'click the register button')
def step_impl(context):
    raise NotImplementedError(u'STEP: When click the register button')


@then(u'the account will be registered')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the account will be registered')