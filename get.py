import urllib.request
import shutil

url = ''

page = urllib.request.urlopen(url)
print(page)
f = open("#.html", "wb")
shutil.copyfileobj(page, f)
f.close()