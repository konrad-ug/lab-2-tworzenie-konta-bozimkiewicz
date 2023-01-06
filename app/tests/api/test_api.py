import unittest
import requests

class TestAPI(unittest.TestCase):
    url = "http://localhost:5000"
    body = {
            "imie": "Dariusz", 
            "nazwisko": "Januszewski", 
            "pesel": "99123456789"
        }

    def test_1_stworz_konto(self):
        response = requests.post(self.url + '/konta/stworz_konto', json=self.body)
        self.assertEqual(response.status_code, 201)

    def test_2_wyszukaj_konto(self):
        response = requests.get(self.url + f"/konta/konto/{self.body['pesel']}")
        response_json = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_json['imie'], self.body['imie'])
        self.assertEqual(response_json['nazwisko'], self.body['nazwisko'])
        self.assertEqual(response_json['saldo'], 0)

    def test_3_zaktualizuj_konto(self):
        new_body = {
            "imie": "Tomasz", 
            "nazwisko": "Nowak", 
            "pesel": "00123456789",
            "saldo": 500
        }
        response = requests.put(self.url + f"/konta/konto/{self.body['pesel']}", json=new_body)
        
        self.assertEqual(response.status_code, 200)

    def test_4_usun_konto(self):
        response = requests.delete(self.url + f"/konta/konto/{self.body['pesel']}")

        self.assertEqual(response.status_code, 202)

    def test_5_stworz_konto_o_istniejacym_peselu(self):
        new_body = {
            "imie": "Tomasz", 
            "nazwisko": "Nowak", 
            "pesel": "99123456789"
        }
        requests.post(self.url + '/konta/stworz_konto', json=self.body)
        response = requests.post(self.url + '/konta/stworz_konto', json=new_body)

        self.assertEqual(response.status_code, 400)