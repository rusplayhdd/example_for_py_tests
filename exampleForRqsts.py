import requests
import json

# and certainly we need to choose the method
# we also can use headers and body in requests (in JSON format) like this:  
r = requests.get("https://api.hh.ru:443/metro/4/?locale=EN"#, 
                 #headers={"name" : "value"}, json{"string": "value"}
                 )

r_json = json.dumps(r.json(), indent=2#, ensure_ascii=False 
                    # (it's nassesary if we've got a russian abc)
                    )

if r.status_code == 200:
    print("all good")
elif r.status_code >= 400:
    print("the page dosn't find!")
else:
    print("the code isn't 200")


if r.status_code == 200:
    print(r_json)
else: 
    print("Not found, Something wrong!!!")