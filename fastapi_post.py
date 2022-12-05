import json
import requests


r = requests.post("http://127.0.0.1:8000/items/", data=json.dumps({"item_id": "1234", "item_name": "foo"}))
print(r.json())
