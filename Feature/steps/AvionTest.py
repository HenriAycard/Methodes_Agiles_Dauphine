import unittest

from Avion import Avion
from Vol import Vol


class MyTestCase(unittest.TestCase):
    def setUp(self):
        # Vols
        self.paris_newyork = Vol("Paris CDG", "New York", 6000, 500)
        self.paris_hongkong = Vol("Paris CDG", "Hong Kong", 9620, 200)
        # Avions disponible
        self.airbus_a350 = Avion()
        self.hawker_siddley_748 = Avion(reservoir=4000, nb_passenger=48, poids=21)
        self.boeing_737_max = Avion(reservoir=150000, nb_passenger=120, poids=118)
        self.boeing_737_max_2 = Avion(reservoir=150000, nb_passenger=140, poids=118)

    def test_add_passenger(self):
        # Arrange
        self.airbus_a350.set_passenger(10)

        # Act
        self.airbus_a350.add_passenger(10)
        # Assert
        self.assertEqual(20, self.airbus_a350.get_passenger())

        # Act
        self.airbus_a350.add_passenger(15)
        # Assert
        self.assertEqual(35, self.airbus_a350.get_passenger())

    def test_calcul_consommer(self):
        # Arrange
        self.airbus_a350.set_passenger(150)
        self.airbus_a350.set_poids(118)
        self.airbus_a350.set_reservoir(10000)

        # Act
        self.airbus_a350.add_vol(self.paris_newyork)
        # Assert
        self.assertAlmostEqual(1330, self.airbus_a350.calcul_consommation(), places=0)

    def test_calcul_distance_avec_plusieurs_vols(self):
        # Arrange
        self.airbus_a350.set_passenger(150)
        self.airbus_a350.set_poids(118)
        self.airbus_a350.set_reservoir(150000)

        # Act
        self.airbus_a350.add_vol(self.paris_newyork)
        self.airbus_a350.add_vol(self.paris_hongkong)
        # Assert
        self.assertAlmostEqual(11278.195, self.airbus_a350.calcul_distance(), places=3)

    def test_crash_distance(self):
        # Arrange
        self.hawker_siddley_748.add_vol(self.paris_newyork)

        # Assert
        self.assertEqual(0, self.hawker_siddley_748.calcul_distance())

    def test_nb_passenger_autorise(self):
        # Arrange
        self.paris_newyork.add_avion(self.boeing_737_max)
        self.paris_newyork.add_avion(self.boeing_737_max_2)

        # Assert
        self.assertEqual(True, self.paris_newyork.is_max_passenger())

    def test_nb_passenger_autorise_depasse(self):
        # Arrange
        self.paris_hongkong.add_avion(self.boeing_737_max)
        self.paris_hongkong.add_avion(self.boeing_737_max_2)
        # Assert
        self.assertEqual(False, self.paris_hongkong.is_max_passenger())


if __name__ == '__main__':
    unittest.main()
