import requests

url = "http://127.0.0.1:8000/api/example?fn="

for i in range(0, 2000):
    req = requests.get(url + "@0:" + str(i))

    if req.status_code == 200:
        print(f"Port : {format(i)}")
        break
    print(f"C'est le port : {str(i)}")
