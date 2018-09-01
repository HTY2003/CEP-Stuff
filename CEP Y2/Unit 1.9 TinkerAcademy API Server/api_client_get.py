import urllib.request

def access_key(server):
    request = urllib.request.Request(server, method="GET")
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))

access_key("http://localhost:8080")

