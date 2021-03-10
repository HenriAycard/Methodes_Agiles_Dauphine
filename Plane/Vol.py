class Vol(object):
    def __init__(self, ville_depart, ville_arrivee, distance, nb_max_passenger):
        self._ville_depart = ville_depart
        self._ville_arrivee = ville_arrivee
        self._distance = float(distance)
        self._nb_max_passenger = float(nb_max_passenger)
        self._lst_avion = []

    def set_avion(self, a):
        self._lst_avion = a

    def add_avion(self, a):
        self._lst_avion.append(a)

    def crash(self, dist):
        if self._distance > dist:
            return True
        return False

    def calcul_nb_passenger_atc(self):
        resultat = 0.0
        for a in self._lst_avion:
            resultat += a.get_passenger();
        return float(resultat)

    def is_max_passenger(self):
        if self._nb_max_passenger > self.calcul_nb_passenger_atc():
            return True
        return False