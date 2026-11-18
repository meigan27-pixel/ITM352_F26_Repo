#scrape names of itm faculty and grad students
import urllib.request
from bs4 import BeautifulSoup

url = 'https://shidler.hawaii.edu/itm/people'
print("retrieving", url)

itm_page = urllib.request.urlopen(url)
itm_names = []

soup = BeautifulSoup(itm_page, 'html.parser')

#find all faculty which are in h2 tags with class="title"
faculty = soup.find_all('h2', class_='title')

for person in faculty:
    itm_names.append(person.text())
    print("faculty:", person.text())

print("total faculty:", len(faculty))