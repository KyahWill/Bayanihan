import requests
import re

url = "https://maps.app.goo.gl/g7o15ag4qZLqVxzy6"
session = requests.Session()  # so connections are recycled
resp = session.head(url, allow_redirects=True)
nurl = resp.url
print(nurl)
temp = re.findall('([0-9]?[0-9]?[0-9]\.[0-9]*)', nurl, re.DOTALL)

print(temp)