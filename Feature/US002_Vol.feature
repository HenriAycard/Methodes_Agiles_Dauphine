@tag
Feature: US_0002 Verifier que le nombre de voyageurs sur un vol
  En tant que Programmeur des vols chez ZamAir
  Je veux vérifier le nombre de voyageur
  Afin de savoir qu'il ne dépasse pas la limite imposée

  Scenario Outline: Realiser 2 vols en respectant le nombre de voyageur autorisé à atterir sur le territoire (500 max)
    Given Un vol au depart de "<ville_depart>" et à l arrivé de "<ville_arrivee>" soit un trajet de <distance> KM avec <nb_max_passagers> passagers
    Given Des avions dont les informations sont
      | nb_passagers | reservoir | poids |
      | 324          | 200000    | 280   |
      | 120          | 100000    | 118   |
    When On affecte au vol les avions
    Then Le nombre de voyageurs est autorise

    Examples:
      | ville_depart | ville_arrivee | distance | nb_max_passagers |
      | Paris CDG    | Hong Kong     | 9620     | 500              |

  Scenario Outline: 3 vols dont la somme des passagers est supérieur à la limite imposée
    Given Un vol au depart de "<ville_depart>" et à l arrivé de "<ville_arrivee>" soit un trajet de <distance> KM avec <nb_max_passagers> passagers
    Given Des avions dont les informations sont
      | nb_passagers | reservoir | poids |
      | 324          | 200000    | 280   |
      | 120          | 100000    | 118   |
      | 140          | 150000    | 143   |
    When On affecte au vol les avions
    Then Le nombre de voyageurs n est plus autorise

    Examples:
      | ville_depart | ville_arrivee | distance | nb_max_passagers |
      | Paris CDG    | Hong Kong     | 9620     | 500              |