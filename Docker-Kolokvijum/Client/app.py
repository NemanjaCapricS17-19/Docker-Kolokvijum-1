import json
import http.client

conn = http.client.HTTPConnection("localhost:5000")
seed = json.dumps(
  {'ime': 'Nemanja',
  'prezime': 'Capric',
  'username': 'Capra',
  'smer': 'IT',
  'predmeti':
    [{'ime': 'Dizajn i razvoj web stranica', 'espb': 8},
     {'ime': 'Engleski 2', 'espb': 4}
    ]}
)
headers = {
  'Content-Type': 'application/json'
}
conn.request("POST", "/users", seed, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
