from behave import given, when, then
from hamcrest import assert_that, equal_to, greater_than
from Vol import Vol
from Avion import Avion


@given('Un vol au depart de "{ville_depart}" et à l arrivé de "{ville_arrivee}" soit un trajet de {distance} KM avec {nb_max_passagers} passagers')
def step_given_vol(context, ville_depart, ville_arrivee, distance, nb_max_passagers):
    context.vol = Vol(ville_depart, ville_arrivee, distance, nb_max_passagers)


@given('Un avion avec {nb_passagers} passagers, un reservoir de {reservoir} L et un poids de {poids}')
def step_given_avion(context, nb_passagers, reservoir, poids):
    context.avion = Avion(float(reservoir), float(nb_passagers), float(poids))


@when('On affecte a l avion le nouveau vol')
def step_update_avion(context):
    context.avion.add_vol(context.vol)


@then('La distance que peut parcourir l avion est superieur a la distance du vol')
def step_then_distance(context):
    assert_that(context.avion.calcul_distance(), greater_than(0))


@then('L avion risque de s ecraser')
def step_then_distance(context):
    assert_that(context.avion.calcul_distance(), equal_to(0))
