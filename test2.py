import requests

r = requests.get("https://jsonplaceholder.typicode.com/posts")

new = r.json()

for obj in new:
    if obj["title"][0] == "a":
        print(obj["title"])
        print("UESSSSSSS******************")
