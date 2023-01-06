import unittest
import requests

class TestAPI(unittest.TestCase):
    url = "http://localhost:5000"
    body = {
            "imie": "Dariusz", 
            "nazwisko": "Januszewski", 
            "pesel": "99123456789"
        }

    def test_stworz_konto(self):
        response = requests.post(self.url + '/konta/stworz_konto', json=self.body)
        self.assertEqual(response.status_code, 201)

    def test_wyszukaj_konto(self):
        response = requests.get(self.url + f"/konta/konto/{self.body['pesel']}")
        response_json = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_json['imie'], self.body['imie'])
        self.assertEqual(response_json['nazwisko'], self.body['nazwisko'])
        self.assertEqual(response_json['saldo'], 0)
