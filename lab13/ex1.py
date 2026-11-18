#scrape data from city of chicago's data portal
#print anyline with a <title> tag in it

import ssl
import urllib.request

ssl._create_default_https_context = ssl._create_unverified_context
url = 'https://data.cityofchicago.org/Historic-Preservation/Landmark-Districts/zidz-sdfj/about_data'

print("retrieving", url)
response = urllib.request.urlopen(url)

for line in response:
    line = line.decode("utf-8").strip()
    if '<title>' in line:
        print(line)