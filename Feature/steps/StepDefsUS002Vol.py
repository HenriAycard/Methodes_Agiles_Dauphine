from behave import given, when, then
from hamcrest import assert_that, equal_to
from Vol import Vol
from Avion import Avion


@given('Des avions dont les informations sont')
def step_given_avion(context):
    context.lst_avion = []
    for row in context.table:
        context.lst_avion.append(Avion(float(row['reservoir']), float(row['nb_passagers']), float(row['poids'])))


@when('On affecte au vol les avions')
def step_set_vol(context):
    context.vol.set_avion(context.lst_avion)


@then('Le nombre de voyageurs est autorise')
def step_then_distance(context):
    assert_that(context.vol.is_max_passenger(), equal_to(True))


@then('Le nombre de voyageurs n est plus autorise')
def step_then_distance(context):
    assert_that(context.vol.is_max_passenger(), equal_to(False))