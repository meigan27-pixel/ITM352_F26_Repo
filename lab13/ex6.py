import requests
from bs4 import BeautifulSoup

url = "https://www.hicentral.com/hawaii-mortgage-rates.php"

response = requests.get(url)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

# Find the mortgage-rate table
table = soup.find("table")

# Extract rows
rows = table.find_all("tr")

for row in rows[1:]:  # Skip header row
    cells = row.find_all("td")

    if cells:
        bank_name = cells[0].get_text(strip=True)

        rates = [cell.get_text(strip=True) for cell in cells[1:]]

        print(bank_name, rates)