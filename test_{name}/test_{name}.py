import requests, json
import pytest

def status_code_test():
    rqst = requests.get("https://api.hh.ru:443/metro/4/?locale=EN")
    assert rqst.status_code == 200