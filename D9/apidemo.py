import requests

response = requests.get("https://fakestoreapi.com/products/")
mydata = response.json()

for i in mydata:
    print("name is", i['title'],"Price is",i['price'])