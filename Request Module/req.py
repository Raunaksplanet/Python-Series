#!/usr/bin/python3

import requests
import webbrowser

session = requests.Session()

url = "http://localhost/PHP_LoginForm/index.php"

# name=sdf&pass=sdf

data = {
	"name":"raunak",
	"pass":"admin"
}

session.post(url,data=data)

r = session.get("http://localhost/PHP_LoginForm/index.php")

file = open("file.html","wb")
file.write(r.content)
file.close()

webbrowser.open("file.html")