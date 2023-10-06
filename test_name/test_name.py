import requests, json
import pytest

def test_status_code():
    rqst = requests.get("https://api.hh.ru:443/metro/4/?locale=EN")
    assert rqst.status_code == 200

def test_body_part():
    r = requests.get("https://api.hh.ru:443/metro/4/?locale=EN")
    assert r.json()["name"] == "Novosibirsk"


@pytest.mark.parametrize(("key", "value"),
                         [("name", "Novosibirsk"),
                          ("id", "4")])

def test_json(key, value):
    r = requests.get("https://api.hh.ru:443/metro/4/?locale=EN")
    assert r.json()[key] == value

