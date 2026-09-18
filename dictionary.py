#example of dictionary

countryCapitals = {
    "USA": {"capital": "Washington, D.C.", "population": 331002651},
    "France": {"capital": "Paris", "population": 68042591},
    "Japan": {"capital": "Tokyo", "population": 125836021},
}

print("country capitals:", countryCapitals)

#access value by using key
print("Capital of USA:", countryCapitals["USA"])
print("Capital of France:", countryCapitals["France"])
print("Capital of Japan:", countryCapitals["Japan"])

countryCapitals["Germany"] = {"capital": "Berlin", "population": 83783922}
print("Capital of Germany:", countryCapitals["Germany"])
print("Population of Germany:", countryCapitals["Germany"])

print("Germany" in countryCapitals)
print("Spain" not in countryCapitals)

