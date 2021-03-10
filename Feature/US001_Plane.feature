@tag
Feature: US_0001 Calculer la distance que peut parcourir mon avion
  En tant que Programmeur des vols chez ZamAir
  Je veux calculer la distance que peut parcourir mon avion
  Afin de savoir s'il pourra arriver à destination

  Scenario Outline: Realiser un vol de Paris a New York avec le modèle: Airbus A350
    Given Un avion avec <nb_passagers> passagers, un reservoir de <reservoir> L et un poids de <poids>
    Given Un vol au depart de "<ville_depart>" et à l arrivé de "<ville_arrivee>" soit un trajet de <distance> KM avec <nb_max_passagers> passagers
    When On affecte a l avion le nouveau vol
    Then La distance que peut parcourir l avion est superieur a la distance du vol
    Examples:
      | ville_depart | ville_arrivee | distance | nb_max_passagers | nb_passagers | reservoir | poids |
      | Paris CDG    | New York      | 6000     | 200              | 324          | 200000    | 280   |

  Scenario Outline: Realiser un vol de Paris a New York avec le modèle: Hawker-Siddeley.748
    Given Un avion avec <nb_passagers> passagers, un reservoir de <reservoir> L et un poids de <poids>
    Given Un vol au depart de "<ville_depart>" et à l arrivé de "<ville_arrivee>" soit un trajet de <distance> KM avec <nb_max_passagers> passagers
    When On affecte a l avion le nouveau vol
    Then L avion risque de s ecraser
    Examples:
      | ville_depart    | ville_arrivee | distance | nb_max_passagers | nb_passagers | reservoir | poids |
      | Paris           | New York      | 6000     | 200              | 48           | 4000      | 21    |

