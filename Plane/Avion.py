class Avion(object):
    def __init__(self, reservoir=0.0, nb_passenger=0.0, poids=0.0):
        self._reservoir = float(reservoir)
        self._nb_passenger = float(nb_passenger)
        self._poids = float(poids)
        self._vol = []

    def set_passenger(self, nb):
        self._nb_passenger = float(nb)

    def set_reservoir(self, reservoir):
        self._reservoir = float(reservoir)

    def set_poids(self, poids):
        self._poids = float(poids)

    def get_passenger(self):
        return self._nb_passenger

    def get_reservoir(self):
        return self._reservoir

    def get_poids(self):
        return self._poids

    def add_vol(self, v):
        self._vol.append(v)

    def add_passenger(self, nb):
        self._nb_passenger += nb

    def calcul_consommation(self):
        return (self._nb_passenger * 0.1 + self._poids) * 10

    def calcul_distance(self):
        dist = (float(self._reservoir) / float(self.calcul_consommation())) * 100
        for v in self._vol:
            if (v.crash(dist)):
                return 0
        return dist