from behave import *
from agile.filiale import *
from agile.boss import *

@given("une filiale Louis Vuitton")
def step_impl(context):
    context.boss = Boss("Bernard Arnault", "LVMH")
    context.filiale = Subsidiary("LVMH", "Louis Vuitton", context.boss)
    assert context.filiale is not None

@when("demande la maison mere")
def step_impl(context):
    context.result = context.filiale.maison_mere()

@then("la maison mere")
def step_impl(context):
    assert context.result == "la maison mere de Louis Vuitton est LVMH"

@given("une entreprise {filiale} de {mere}")
def step_impl(context, filiale, mere):
    context.boss = Boss(filiale, mere)
    context.filiale = Subsidiary(mere, filiale, context.boss)
    assert context.filiale is not None

@then("retourner la maison mere {mere}")
def step_impl(context, mere):
    assert context.result == mere


