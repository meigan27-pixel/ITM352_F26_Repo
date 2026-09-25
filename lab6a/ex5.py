#testing use of assertion

def celciusToFahrenheit(celcius):
    assert celcius >= -273.15, "Temperature cannot be below absolute zero"
    fahrenheit = (celcius * 9/5) + 32
    return fahrenheit

print(celciusToFahrenheit(0))   #should print 32.0
print(celciusToFahrenheit(100)) #should print 212.0
print(celciusToFahrenheit(-300))  # This will raise an AssertionError   