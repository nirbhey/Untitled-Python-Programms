import requests
from lxml import etree
name = "foo"

url = 'https://recruitment.advarisk.com/tests/django'
client = requests.session()
tree = etree.HTML(client.get(url).content)
csrf = tree.xpath('//input[@name="csrf_token"]/@value')[0]
formData = dict(csrf_token=csrf, name=name)
headers = {'referer': url, 'content-type': 'application/x-www-form-urlencoded', 'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
r = client.post(url, data=formData, headers=headers)
strx = str(r.content)
print(strx[779:(len(strx)-66)])