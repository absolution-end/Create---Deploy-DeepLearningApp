import requests

resp = requests.post("http://localhost:5000/predict", files = {'file':open('boom.png','rb')})

print(resp.text)