from behave import *
from agile.country import *


@given("un pays France")
def step_impl(context):
    context.country = Country()
    assert context.country is not None


@when("je set une population et une surface")
def step_impl(context):
    context.country.set_population_and_surface(67390000, 543904)
    context.result = 67390000 / 543904


@then(" j obtiens la densité")
def step_impl(context):
    assert context.result == context.country.calculate_density()
