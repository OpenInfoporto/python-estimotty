import requests


class Beacon:

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __repr__(self):
        return "<Beacon '%s'>" % self.id

class Supplicant:
    def __init__(self, username, password, endpoint=None):
        self.auth = (username, password)
        self.headers = dict(Accept='application/json')
        self.endpoint = endpoint or 'https://cloud.estimote.com/v1/'

    def get_beacons(self):
        resp = requests.get('%sbeacons' % self.endpoint,
                            auth=self.auth,
                            headers=self.headers)

        return resp.json()


class Estimotty:

    def __init__(self, username, password):
        self.s = Supplicant(username, password)

    def beacons(self):
        beacons = list()
        fetched = self.s.get_beacons()
        for b in fetched:
            beacons.append(Beacon(**b))

        return beacons

if __name__ == '__main__':
    e = Estimotty()

    beacons = e.beacons()
    print beacons
