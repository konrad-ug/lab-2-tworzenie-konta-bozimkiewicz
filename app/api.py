from flask import Flask, request, jsonify
from app.RejestrKont import RejestrKont
from app.Konto import Konto

app = Flask(__name__)

@app.route("/konta/stworz_konto", methods=['POST'])
def stworz_konto():
  dane = request.get_json()
  print(f"Request o stworzenie konta z danymi: {dane}")

  if RejestrKont.wyszukaj_konto_osobiste(dane["pesel"]):
    return jsonify('Konto o takim peselu już istnieje!'), 400
  
  konto = Konto(dane["imie"], dane["nazwisko"], dane["pesel"])
  RejestrKont.dodaj_konto(konto)
  return jsonify("Konto stworzone"), 201

@app.route("/konta/ile_kont", methods=['GET'])
def ile_kont():
  return f"Ilość kont w rejestrze {RejestrKont.zwroc_ilosc_kont()}", 200

@app.route("/konta/konto/<pesel>", methods=['GET'])
def wyszukaj_konto_z_peselem(pesel):
  konto = RejestrKont.wyszukaj_konto_osobiste(pesel)
  return jsonify(imie=konto.imie, nazwisko=konto.nazwisko, pesel=konto.pesel, saldo=konto.saldo), 200

@app.route("/konta/konto/<pesel>", methods=['PUT'])
def aktualizuj_konto(pesel):
  dane = request.get_json()
  konto = RejestrKont.wyszukaj_konto_osobiste(pesel)

  konto.imie = dane['imie'] if 'imie' else konto.imie
  konto.nazwisko = dane['nazwisko'] if 'nazwisko' in dane else konto.nazwisko
  konto.pesel = dane['pesel'] if 'pesel' in dane else konto.pesel
  konto.saldo = dane['saldo'] if 'saldo' in dane else konto.saldo

  return jsonify(f'Konto o peselu: <{pesel}> zaktualizowano pomyślnie!'), 200

@app.route("/konta/konto/<pesel>", methods=['DELETE'])
def usun_konto(pesel):
  RejestrKont.usun_konto_osobiste(pesel)

  return jsonify(f"Usunięto konto o peselu: <{pesel}>"), 202
